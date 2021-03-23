#!/usr/bin/node

exports.converter = (base) => {
  const setBase = (nbr) => {
    return (nbr.toString(base));
  };
  return (setBase);
};
