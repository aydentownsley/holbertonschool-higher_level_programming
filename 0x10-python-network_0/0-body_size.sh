#!/bin/bash
# gets content size
curl -sw "%{size_download}\n" "$1" -o /dev/null
