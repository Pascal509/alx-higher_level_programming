#!/usr/bin/node

exports.nbOccurences = function (list, searchEle) {
  let count = 0;
  for (let j = 0; j < list.length; j++) {
    if (list[j] === searchEle) {
      count++;
    }
  }
  return count;
};
