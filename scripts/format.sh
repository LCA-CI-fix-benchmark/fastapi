#set -x

ruff format fastapi tests docs_src scripts --fixn/sh -e
set -x

ruff fastapi tests docs_src scripts --fix
ruff format fastapi tests docs_src scripts
