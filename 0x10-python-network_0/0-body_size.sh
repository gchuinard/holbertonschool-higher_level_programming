#!/bin/bash
# displays the length of the response body's
curl -sI "$1" | grep -e Content-Length | cut -d: -f2