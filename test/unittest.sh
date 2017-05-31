#!/bin/bash
SCRIPT_DIR=$(cd $(dirname $0);pwd)
find $SCRIPT_DIR -name unittestMain.py | xargs -L 1 python

