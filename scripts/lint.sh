#set -e
set -x

mypy fastapi
black fastapi tests docs_src scripts
black --check fastapi testsin/env bash

set -e
set -x

mypy fastapi
ruff fastapi tests docs_src scripts
ruff format fastapi tests --check
