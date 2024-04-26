#!/usr/bin/env bash

set -e
set -x

mypy fastapi
ruff format fastapi tests --check
