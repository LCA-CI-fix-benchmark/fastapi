#!/usr/bin/env bash
#!/bin/bash

set -e

export PYTHONPATH=./docs_src
coverage run -m pytest tests "${@}"

deactivate
