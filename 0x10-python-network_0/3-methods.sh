#!/bin/bash
# Displays all HTTP method
ALLOWED=$(curl -sI "$1" | grep "Allow") && echo "${ALLOWED##*: }"
