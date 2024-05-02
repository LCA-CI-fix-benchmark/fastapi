#!/usr/bin/env bash

set -e
#!/bin/bash

set -x
export PYTHONPATH=./docs_src
coverage run -m pytest tests ${@}