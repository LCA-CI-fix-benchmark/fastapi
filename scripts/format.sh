#!/bin/sh -e
set -x

black fastapi tests scripts --fix
black fastapi tests scripts