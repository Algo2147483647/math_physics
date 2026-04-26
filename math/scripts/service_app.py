from __future__ import annotations

import argparse

from flask import Flask, jsonify, request
from flask_cors import CORS

from concept_lookup_core import lookup_concept
from graph_store import (
    add_child_in_json,
    add_parent_in_json,
    create_node_in_json,
    delete_node_in_json,
    get_node_in_json,
    list_nodes_in_json,
    remove_child_in_json,
    remove_parent_in_json,
    rename_node_in_json,
    update_node_in_json,
)
from graph_validate_core import repair_math_json, validate_math_json
from markdown_export import build_markdown_from_graph_json
from markdown_import import build_graph_json_from_markdown_folder, diff_markdown_vs_json


app = Flask(__name__)
CORS(app)


def import_markdown(**params):
    return build_graph_json_from_markdown_folder(**params)


def export_markdown(**params):
    return build_markdown_from_graph_json(**params)


def validate_graph(**params):
    return validate_math_json(**params)


def repair_graph(**params):
    return repair_math_json(**params)


def diff_graph(**params):
    return diff_markdown_vs_json(**params)


def rename_concept(**params):
    return rename_node_in_json(**params)


FUNCTIONS = {
    "import_markdown": import_markdown,
    "export_markdown": export_markdown,
    "validate_graph": validate_graph,
    "repair_graph": repair_graph,
    "diff_graph": diff_graph,
    "rename_concept": rename_concept,
    "lookup_concept": lookup_concept,
    "list_nodes_in_json": list_nodes_in_json,
    "get_node_in_json": get_node_in_json,
    "create_node_in_json": create_node_in_json,
    "update_node_in_json": update_node_in_json,
    "delete_node_in_json": delete_node_in_json,
    "add_child_in_json": add_child_in_json,
    "add_parent_in_json": add_parent_in_json,
    "remove_child_in_json": remove_child_in_json,
    "remove_parent_in_json": remove_parent_in_json,
}


def get_param(source, key, default=None, required=False):
    value = source.get(key, default)
    if required and value is None:
        raise ValueError(f"Missing required parameter: '{key}'")
    return value


@app.errorhandler(Exception)
def handle_exception(error):
    return jsonify({"status": "error", "message": str(error)}), 500


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "math-tools"}), 200


@app.route("/functions", methods=["GET"])
def list_functions():
    return jsonify({"status": "success", "data": sorted(FUNCTIONS)}), 200


@app.route("/function", methods=["POST"])
def service_function():
    function_name = "<unknown>"
    try:
        payload = request.get_json(silent=True) or {}
        function_name = get_param(payload, "function", required=True)
        params = get_param(payload, "params", default={})

        if function_name not in FUNCTIONS:
            raise ValueError(f"Function '{function_name}' is not defined or not callable.")
        if not isinstance(params, dict):
            raise ValueError("Parameter 'params' must be a JSON object.")

        response = FUNCTIONS[function_name](**params)
        return jsonify({"status": "success", "data": response}), 200
    except ValueError as error:
        return jsonify({"status": "error", "message": str(error)}), 400
    except TypeError as error:
        return (
            jsonify(
                {
                    "status": "error",
                    "message": f"Invalid parameters for function '{function_name}': {error}",
                }
            ),
            400,
        )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the local Flask service for math tools.")
    parser.add_argument("--host", default="127.0.0.1", help="Host to bind.")
    parser.add_argument("--port", type=int, default=5000, help="Port to bind.")
    parser.add_argument("--debug", action="store_true", help="Enable Flask debug mode.")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    app.run(host=args.host, port=args.port, debug=args.debug)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
