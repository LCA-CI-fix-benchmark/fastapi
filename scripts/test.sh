#!/usr/bin/env bash

set -e
set -x

export PYTHONPATH=./fastapi:./tests
coverage run -m pytest fastapi tests ${@}