#!/usr/bin/env bash
set -e
set -x

mypy fastapi
black fastapi tests docs_src scripts
black format fastapi tests --check
