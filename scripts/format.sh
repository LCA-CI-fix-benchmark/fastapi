#!/b# Format the code using ruff tool for FastAPI, tests, documentation source, and scripts directories
ruff format fastapi tests docs_src scriptsn/sh -e
set -x

ruff fastapi tests docs_src scripts --fix
ruff format fastapi tests docs_src scripts
