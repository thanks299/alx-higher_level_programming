#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  // Iterate through the list
  for (let i = 0; i < list.length; i++) {
    // Check if the current element is equal to the searchElement
    if (list[i] === searchElement) {
      count++;
    }
  }

  return count;
};
