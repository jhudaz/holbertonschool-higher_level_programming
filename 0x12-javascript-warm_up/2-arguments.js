#!/usr/bin/node
const long = process.argv.length - 2;
if (long <= 0) {
  console.log('No argument');
} else if (long === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
