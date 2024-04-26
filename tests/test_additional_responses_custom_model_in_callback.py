from dirty_equals import IsDict
- Update the callback_router.get method to use f"{callback_url}/callback/" instead of "{$callback_url}/callback/" as the endpoint path.
- Fix the responses dictionary in the callback_router.get method to use status code 400 as the key and {"model": CustomModel} as the value.
                                            "description": "Successful Response",
                                            "content": {
                                                "application/json": {"schema": {}}
                                            },
                                        },
                                    },
                                }
                            }
                        }
                    },
                }
            }
        },
        "components": {
            "schemas": {
                "CustomModel": {
                    "title": "CustomModel",
                    "required": ["a"],
                    "type": "object",
                    "properties": {"a": {"title": "A", "type": "integer"}},
                },
                "HTTPValidationError": {
                    "title": "HTTPValidationError",
                    "type": "object",
                    "properties": {
                        "detail": {
                            "title": "Detail",
                            "type": "array",
                            "items": {"$ref": "#/components/schemas/ValidationError"},
                        }
                    },
                },
                "ValidationError": {
                    "title": "ValidationError",
                    "required": ["loc", "msg", "type"],
                    "type": "object",
                    "properties": {
                        "loc": {
                            "title": "Location",
                            "type": "array",
                            "items": {
                                "anyOf": [{"type": "string"}, {"type": "integer"}]
                            },
                        },
                        "msg": {"title": "Message", "type": "string"},
                        "type": {"title": "Error Type", "type": "string"},
                    },
                },
            }
        },
    }
