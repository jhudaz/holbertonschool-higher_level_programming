#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, res, body) => {
  if (err) console.log(err);
  if (res) {
    const response = JSON.parse(body);
    const dict = {};
    response.map(value => {
      if (value.completed) { dict[value.userId] = 0; }
    });
    response.map(value => {
      if (value.completed) dict[value.userId] += 1;
    });
    console.log(dict);
  }
});
