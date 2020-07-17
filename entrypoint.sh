#!/bin/bash
SERVICE=$1

exec uvicorn --proxy-headers --host 0.0.0.0 fiction.app:app
