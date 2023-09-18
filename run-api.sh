#!/usr/bin/env sh

# abort on errors
set -e

# Activate virtuals envs
cd api
source apivenv/bin/activate
uvicorn api:app
