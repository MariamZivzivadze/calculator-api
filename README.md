# Calculator API

A small REST API built with Flask that performs basic arithmetic. Built as
a hands-on exercise covering Flask routing, REST API design, input
validation, and automated testing with pytest.

## Endpoints

All arithmetic endpoints accept `POST` requests with a JSON body containing
two numbers, `a` and `b`.

| Method | Route        | Description          |
|--------|--------------|-----------------------|
| GET    | `/`          | Health check          |
| POST   | `/add`       | Returns a + b         |
| POST   | `/subtract`  | Returns a - b         |
| POST   | `/multiply`  | Returns a * b         |
| POST   | `/divide`    | Returns a / b         |

### Example request

```bash
curl -X POST http://127.0.0.1:5000/add \
  -H "Content-Type: application/json" \
  -d '{"a": 4, "b": 5}'
```

### Example response

```json
{
  "a": 4.0,
  "b": 5.0,
  "operation": "add",
  "result": 9.0
}
```

### Error handling

- Missing `a` or `b` → `400 Bad Request`
- Non-numeric input → `400 Bad Request`
- Division by zero → `400 Bad Request`

## Running locally

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

The server runs at `http://127.0.0.1:5000`.

## Running tests

```bash
pip install pytest
python -m pytest test_app.py -v
```

9 tests cover all four operations, plus edge cases (divide by zero,
missing fields, invalid types, missing JSON body).

## What this project demonstrates

- Flask routing and JSON request/response handling
- REST API design (correct HTTP methods, meaningful status codes)
- Input validation
- Unit testing with pytest and the Flask test client
