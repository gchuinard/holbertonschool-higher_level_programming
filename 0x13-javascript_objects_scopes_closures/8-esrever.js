#!/usr/bin/node

exports.esrever = (list) => {
  const len = (list.length - 1) / 2;
  let beg = 0;
  let end = list.length - 1;
  let tmp;

  while (beg < len) {
    tmp = list[beg];
    list[beg] = list[end];
    list[end] = tmp;
    beg++;
    end--;
  }
  return (list);
};
