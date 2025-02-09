from flask import Flask, request, jsonify
from flask_cors import CORS
from build_graph import build_graph_json_from_markdown_folder
from typora import open_typora

app = Flask(__name__)
CORS(app)  # Restrict domains in production


# Utility function to validate and retrieve JSON or query parameters
def get_param(source, key, default=None, required=False):
    value = source.get(key, default)
    if required and value is None:
        raise ValueError(f"Missing required parameter: '{key}'")
    return value


# Common error handler
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/function', methods=['POST'])
def service_function():
    try:
        # Retrieve function name and parameters from request
        function_name = get_param(request.json, 'function', required=True)
        params = get_param(request.json, 'params', required=True)

        # Dynamically resolve the function
        if function_name in globals() and callable(globals()[function_name]):
            function = globals()[function_name]
        else:
            raise ValueError(f"Function '{function_name}' is not defined or not callable.")

        # Call the function with the provided parameters
        response = function(**params)
        return jsonify({"status": "success", "data": response}), 200
    except ValueError as e:
        return jsonify({"status": "error", "message": str(e)}), 400
    except TypeError as e:
        return jsonify({"status": "error", "message": f"Invalid parameters for function '{function_name}': {e}"}), 400


if __name__ == '__main__':
    app.run(port=5000)
