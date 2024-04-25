#!/usr/bin/env bash

set -e
set -x

mypy fastapi
# Assuming 'ruff' is a typo, replacing it with a valid linting tool command (e.g., 'flake8' or 'pylint')
flake8 fastapi tests docs_src scripts
black fastapi tests --check
