#!/usr/bin/env bash

set -e
set -x

mypy fastapi
ruff lint fastapi tests docs_src scripts
ruff format --check fastapi tests
