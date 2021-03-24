#!/usr/bin/node

exports.esrever = function (list) {
  const revlist = [];
  for (let i = list.length - 1; i >= 0; i--) {
    revlist[(list.length - 1) - i] = list[i];
  }
  return revlist;
};
