#!/usr/bin/env bash

set -e
#!/usr/bin/env bash

set -x

mypy fastapi
ruff fastapi tests docs_src scripts
ruff format fastapi tests --check