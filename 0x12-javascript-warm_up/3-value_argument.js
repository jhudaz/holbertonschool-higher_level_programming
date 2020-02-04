#!/usr/bin/node
const data = process.argv[2];
if (data !== undefined) {
  console.log(data);
} else {
  console.log('No argument');
}
