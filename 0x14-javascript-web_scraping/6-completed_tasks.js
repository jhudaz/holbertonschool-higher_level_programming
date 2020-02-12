#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
const url = args[0];

const options = {
  url: url,
  method: 'GET'
};

request(options, (err, res, body) => {
  if (err) console.log(err);
  if (res) {
    const response = JSON.parse(body);
    const ids = [...new Set(response.map(value => value.userId))];
    const dict = {};
    ids.map(id => {
      let count = 0;
      response.map(value => {
        if (id === value.userId && value.completed) count++;
      });
      dict[id] = count;
    });
    console.log(dict);
  }
});
