import typing
- Update the responses dictionary in the app.get method to use status code 422 as the key and {"description": "Error", "content": {"application/vnd.api+json": {"schema": {"$ref": "#/components/schemas/JsonApiError"}}}} as the value.
