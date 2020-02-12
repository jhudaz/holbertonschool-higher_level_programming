#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
const url = args[0];

request(url, (err, res, body) => {
  if (err) console.log(err);
  if (res) {
    const response = JSON.parse(body);
    const dict = {};
    response.map(value => (dict[value.userId] = 0));
    response.map(value => {
      if (value.completed) { dict[value.userId] += 1; }
    });
    console.log(dict);
  }
});
