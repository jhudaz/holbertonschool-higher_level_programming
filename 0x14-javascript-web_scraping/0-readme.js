#!/usr/bin/node
const fs = require("fs");
const args = process.argv.slice(2);

data = fs.readFile(args[0], "utf-8", (err, data) => {
  if (err) console.error(err);
  else console.log(data);
});
