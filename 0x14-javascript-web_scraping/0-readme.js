#!/usr/bin/node
/* Script that reads and prints the content of a file */

const fs = require('fs');
const filename = process.argv[2];
fs.readFile(filename, 'utf8', (error, data) => {
	if (error) {
		console.log(error);
		return;
	}
	console.log(data)
});
