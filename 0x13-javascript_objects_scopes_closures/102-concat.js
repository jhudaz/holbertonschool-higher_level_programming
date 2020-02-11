#!/usr/bin/node
const fs = require('fs');
const args = process.argv.slice(2);

console.log(args);

function concat (file1, appendFile) {
  fs.readFile(appendFile, (err, data) => {
    if (err) throw err;

    fs.appendFile(file1, data, err => {
      if (err) throw err;
    });
  });
}
const file = args[2];
let appendFile1 = args[0];
concat(file, appendFile1);
appendFile1 = args[1];
concat(file, appendFile1);
