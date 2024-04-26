import typing
- Add the missing import statement for typing.
            },
            "/b": {
                "get": {
                    "responses": {
                        "500": {
                            "description": "Error",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/Error"}
                                }
                            },
                        },
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        },
                    },
                    "summary": "B",
                    "operationId": "b_b_get",
                }
            },
        },
        "components": {
            "schemas": {
                "Error": {
                    "title": "Error",
                    "required": ["status", "title"],
                    "type": "object",
                    "properties": {
                        "status": {"title": "Status", "type": "string"},
                        "title": {"title": "Title", "type": "string"},
                    },
                },
                "JsonApiError": {
                    "title": "JsonApiError",
                    "required": ["errors"],
                    "type": "object",
                    "properties": {
                        "errors": {
                            "title": "Errors",
                            "type": "array",
                            "items": {"$ref": "#/components/schemas/Error"},
                        }
                    },
                },
            }
        },
    }
