#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
const id = args[0];

const options = {
  url: `https://swapi.co/api/films/${id}`,
  method: 'GET'
};

request(options, (err, res, body) => {
  if (err) console.log(err);
  if (res) {
    const response = JSON.parse(body);
    const characters = response.characters;
    characters.map(char => {
      request(char, (err, res, body) => {
        if (err) console.log(err);
        if (res) {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      }
      );
    });
  }
});
