#!/usr/bin/node

exports.converter = (base) => {
  function setBase (nbr) {
    return (nbr.toString(base));
  }
  return (setBase);
};
