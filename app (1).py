"""
Calculator REST API
--------------------
A small Flask API demonstrating core backend concepts:
- Routing (Module 3)
- REST design: proper HTTP methods, status codes, JSON in/out (Module 5)
- Input validation and error handling (Module 5/6)

Run locally:
    python app.py

Then hit it with curl (see README.md for full examples):
    curl -X POST http://127.0.0.1:5000/add -H "Content-Type: application/json" -d '{"a": 4, "b": 5}'
"""

from flask import Flask, request, jsonify

app = Flask(__name__)


def get_operands():
    """
    Pulls 'a' and 'b' out of the incoming JSON body and validates them.
    Returns (a, b, None) on success, or (None, None, error_response) on failure.

    This is a small example of input validation -- never trust that the
    client sent what you expect.
    """
    data = request.get_json(silent=True)

    if not data:
        return None, None, (jsonify({"error": "Request body must be JSON"}), 400)

    if "a" not in data or "b" not in data:
        return None, None, (jsonify({"error": "Both 'a' and 'b' are required"}), 400)

    try:
        a = float(data["a"])
        b = float(data["b"])
    except (TypeError, ValueError):
        return None, None, (jsonify({"error": "'a' and 'b' must be numbers"}), 400)

    return a, b, None


@app.route("/", methods=["GET"])
def index():
    """Simple health check / landing route."""
    return jsonify({
        "message": "Calculator API is running",
        "endpoints": ["/add", "/subtract", "/multiply", "/divide"]
    })


@app.route("/add", methods=["POST"])
def add():
    a, b, error = get_operands()
    if error:
        return error
    return jsonify({"a": a, "b": b, "operation": "add", "result": a + b}), 200


@app.route("/subtract", methods=["POST"])
def subtract():
    a, b, error = get_operands()
    if error:
        return error
    return jsonify({"a": a, "b": b, "operation": "subtract", "result": a - b}), 200


@app.route("/multiply", methods=["POST"])
def multiply():
    a, b, error = get_operands()
    if error:
        return error
    return jsonify({"a": a, "b": b, "operation": "multiply", "result": a * b}), 200


@app.route("/divide", methods=["POST"])
def divide():
    a, b, error = get_operands()
    if error:
        return error

    # This is the interesting edge case interviewers like to probe on.
    if b == 0:
        return jsonify({"error": "Cannot divide by zero"}), 400

    return jsonify({"a": a, "b": b, "operation": "divide", "result": a / b}), 200


if __name__ == "__main__":
    app.run(debug=True)
