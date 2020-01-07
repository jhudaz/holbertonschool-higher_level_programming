#!/bin/bash
#akes in a URL and displays all HTTP methods the server will accept.
curl -siX OPTIONS  $1 | grep "Allow" | cut -d " " -f1 --complement
