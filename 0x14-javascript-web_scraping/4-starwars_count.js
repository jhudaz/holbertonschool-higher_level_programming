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
    const results = response.results;
    let count = 0;
    results.map(data => {
      data.characters.map(chars =>
        chars.search('people/18') !== -1 ? (count += 1) : (count += 0)
      );
    });
    console.log(count);
  }
});
