#!/usr/bin/node
const fs = require('fs');
const args = process.argv.slice(2);

try {
  const data = fs.readFileSync(args[0], 'utf-8');
  console.log(data);
} catch (e) {
  console.error(e);
}
