#!/usr/bin/node
// imports an array
const list = require('./100-data').list;
const NewList = list.map(function (item, index) {
  return item * index;
});

console.log(list);
console.log(NewList);
