#!/bin/sh -e
set

ruff fastapi tests docs_src scripts --fix
ruff format fastapi tests docs_src scripts
