#!/usr#!/bin/bash
# Run linting for the project
ruff lint fastapi tests docs_src scripts

# Check and format code using linter rules
ruff format fastapi tests --checkin/env bash

set -e
set -x

mypy fastapi
ruff fastapi tests docs_src scripts
ruff format fastapi tests --check
