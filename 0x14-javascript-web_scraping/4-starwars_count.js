#!/usr/bin/node
/* Prints the title of a Star Wars movie for given character */

const axios = require('axios').default;
const characterx = 'https://swapi-api.hbtn.io/api/people/18/';
if (process.argv.length >= 3) {
  axios.get(process.argv[2])
    .then(function (response) {
      let num = 0;
      for (const x in response.data.results) {
        if (response.data.results[x].characters.includes(characterx)) {
          num = num + 1;
        }
      }
      console.log(num);
    })
    .catch(function (error) {
      error = '0';
      console.log(error);
    });
}
