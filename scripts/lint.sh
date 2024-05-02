#!/usr/bin/env bash

set -e
set -x

mypy fastapi
flake8 fastapi tests scripts
flake8 --check fastapi tests