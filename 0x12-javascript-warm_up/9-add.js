#!/usr/bin/node
function add (a, b) {
  const ap = parseInt(process.argv[2]);
  const bp = parseInt(process.argv[3]);
  console.log(ap + bp);
}

add(process.argv[2], process.argv[3]);
