#!/usr/bin/node
const number = Number(Math.trunc(process.argv[2]));
if (number) {
  for (let i = 0; i < number; i++) {
    let letter = '';
    for (let j = 0; j < number; j++) {
      letter += 'X';
    }
    console.log(letter);
  }
} else {
  console.log('Missing size');
}
