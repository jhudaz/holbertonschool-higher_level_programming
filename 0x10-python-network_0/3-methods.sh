#!/bin/bash
#akes in a URL and displays all HTTP methods the server will accept.
curl -sIX OPTIONS $1| grep "Allow" | cut -d ":" -f2
