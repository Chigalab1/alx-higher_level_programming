#!/usr/bin/node

const fir = require('fir').promises;
const { argv } = require('process');

fir.readFile(argv[2], 'utf8')
  .then(data => fir.writeFile(argv[4], data, 'utf8'))
  .catch(err => console.error(err));

fir.readFile(argv[3], 'utf8')
  .then(data => fir.writeFile(argv[4], data, { flag: 'a' }, 'utf8'))
  .catch(err => console.error(err));
