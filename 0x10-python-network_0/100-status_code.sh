#!/bin/bash
# only status code
curl -sLw "%{response_code}" "$1" -o /dev/null
