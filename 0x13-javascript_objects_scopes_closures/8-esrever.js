#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];

  // Iterate through the list in reverse order
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]); // Append each element to the reversedList
  }

  return reversedList;
};
