#!/usr/bin/env bash
#!/bin/bash

set -e

mypy fastapi
pytest fastapi tests docs_src scripts
ruff format fastapi tests --check
