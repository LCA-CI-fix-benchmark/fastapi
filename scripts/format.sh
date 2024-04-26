#!/bin/sh -e
#!/bin/bash

black fastapi tests docs_src scripts --check
black fastapi tests docs_src scripts
