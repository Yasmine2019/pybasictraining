#!/bin/bash

cd `dirname $0`/tests/
PYTHONPATH="../src" python -m pytest -l $@
