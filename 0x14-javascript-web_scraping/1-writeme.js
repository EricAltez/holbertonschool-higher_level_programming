#!/usr/bin/node
/* cript that writes a string to a file */

const fileName = process.argv[2];
const text = process.argv[3];
const fs = require('fs');
fs.writeFile(fileName, text, (error) => {
  error && console.log(error);
});
