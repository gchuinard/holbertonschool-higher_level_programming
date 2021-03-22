#!/usr/bin/node

function factoriel (nbr) {
  if (isNaN(nbr) || nbr <= 0) {
    return (1);
  }
  return nbr * factoriel(nbr - 1);
}

console.log(factoriel(parseInt(process.argv[2])));
