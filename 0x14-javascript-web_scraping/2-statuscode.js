#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
const url = args[0];

request
  .get(url)
  .on('response', response => console.log(`code: ${response.statusCode}`));
