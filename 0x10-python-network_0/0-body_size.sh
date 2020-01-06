#!/bin/bash
#content length in a header
curl -sI $1 | grep "Content-Length" | cut -d ":" -f2
