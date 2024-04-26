#!/usr/bin/env bash

set -e
set -x

mypy fastapi
#!/bin/bash
# Run linting for codebase
ruff lint fastapi tests docs_src scripts
# Check code formatting
ruff format fastapi tests --check
