#!/usr/bin/node
/* Prints the title of a Star Wars movie for given character */

const axios = require('axios').default;
axios.get(process.argv[2])
  .then(function (response) {
    let num = 0;
    for (const x in response.data.results) {
      for (const y in response.data.results[x].characters) {
        const id = response.data.results[x].characters[y].split('/')[5];
        if (id === '18') {
          num = num + 1;
        }
      }
    }
    console.log(num);
  })
  .catch(function (error) {
    error = '0';
    console.log(error);
  });
