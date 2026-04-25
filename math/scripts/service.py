from __future__ import annotations

import argparse

from flask import Flask, jsonify, request
from flask_cors import CORS

from build_graph_from_markdown import build_graph_json_from_markdown_folder
from build_markdown_from_graph import add_kid_for_graph, build_markdown_from_graph_json
from compare_concepts import compare_concepts
from find_references import find_references
from lookup_concept import lookup_concept
from typora import open_typora
from validate_math_json import validate_math_json


app = Flask(__name__)
CORS(app)

FUNCTIONS = {
    "build_graph_json_from_markdown_folder": build_graph_json_from_markdown_folder,
    "build_markdown_from_graph_json": build_markdown_from_graph_json,
    "add_kid_for_graph": add_kid_for_graph,
    "open_typora": open_typora,
    "lookup_concept": lookup_concept,
    "compare_concepts": compare_concepts,
    "find_references": find_references,
    "validate_math_json": validate_math_json,
}


def get_param(source, key, default=None, required=False):
    value = source.get(key, default)
    if required and value is None:
        raise ValueError(f"Missing required parameter: '{key}'")
    return value


@app.errorhandler(Exception)
def handle_exception(error):
    return jsonify({"status": "error", "message": str(error)}), 500


@app.route("/function", methods=["POST"])
def service_function():
    function_name = "<unknown>"
    try:
        payload = request.get_json(silent=True) or {}
        function_name = get_param(payload, "function", required=True)
        params = get_param(payload, "params", required=True)

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


if __name__ == "__main__":
    args = build_parser().parse_args()
    app.run(host=args.host, port=args.port, debug=args.debug)
