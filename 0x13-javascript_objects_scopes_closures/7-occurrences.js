#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach((i) => (i === searchElement && count++));
  return (count);
};
