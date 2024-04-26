#!/bin/sh -e
set -x

ruff format fastapi tests docs_src scripts --fix
