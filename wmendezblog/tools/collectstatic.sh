#!/bin/bash

# Automatic collect static

# Change to project dir
cd ..

# Copy static files to STATIC_ROOT
./manage.py collectstatic --noinput --link
