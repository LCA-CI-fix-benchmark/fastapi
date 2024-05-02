#!/usr/bin/env bash

set -e
set -x

mypy fastapi
flake8 fastapi tests docs_src scripts
flake8 format fastapi tests --check