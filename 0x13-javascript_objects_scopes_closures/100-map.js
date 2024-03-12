#!/usr/bin/node
// map

const list = require('./100-data.js').list;

console.log(list.map((item, index) => item * index));
