#!/usr/bin/env bash
set -e
set -x

mypy fastapi
run fastapi tests docs_src scripts
run format fastapi tests --check
