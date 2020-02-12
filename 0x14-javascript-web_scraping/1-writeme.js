#!/usr/bin/node
const fs = require('fs');
const args = process.argv.slice(2);
const file = args[0];
const data = args[1];

fs.writeFile(file, data, (err) => {
  if (err) console.log(err);
});
