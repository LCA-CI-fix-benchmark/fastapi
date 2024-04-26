import pytest
- Update the responses dictionary in the app.get method to use a valid status code (e.g., "400") instead of "hello" to avoid raising a ValueError.

client = TestClient(app)


def test_openapi_schema():
    with pytest.raises(ValueError):
        client.get("/openapi.json")
