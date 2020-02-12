#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const args = process.argv.slice(2);
const url = args[0];
const file = args[1];

const options = {
  url: url,
  method: 'GET'
};

request(options, (err, res, body) => {
  if (err) console.log(err);
  if (res) {
    fs.writeFile(file, body, (err) => {
      if (err) console.log(err);
    });
  }
});
