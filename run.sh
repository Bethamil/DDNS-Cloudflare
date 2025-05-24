#!/bin/sh

# Only needed for cron to use docker env's
. /app/env.sh

/usr/local/bin/python3 /app/app.py
