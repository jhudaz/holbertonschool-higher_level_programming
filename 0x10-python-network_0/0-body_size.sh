#!/bin/bash
#content length in a header
curl -sI "http://74ce65162028.38.hbtn-cod.io:5000/" | grep "Content-Length" | cut -d ":" -f2
