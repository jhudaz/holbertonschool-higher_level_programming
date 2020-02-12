#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
const url = args[0];
request(url, (err, res, body) => {
  if (err) console.log(err);
  if (res) {
    const response = JSON.parse(body);
    const ids = [...new Set(response.map(value => value.userId))];
    const dict = {};
    ids.map(id => {
      let count = 0;
      response.map(value => id === value.userId && value.completed ? (count++) : (count + 0));
      dict[id] = count;
    });
    console.log(dict);
  }
});
