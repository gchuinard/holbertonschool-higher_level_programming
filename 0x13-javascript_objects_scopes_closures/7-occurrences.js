#!/usr/bin/node

exports.nbOccurences = (list, searchElement) => {
  let count = 0;

  list.forEach((elem) => {
    if (searchElement === elem) {
      count++;
    }
  });
  return (count);
};
