#!/bin/bash
#displays the length of the response body's
curl -sI "$1" | grep Length | cut -d ' ' -f2
