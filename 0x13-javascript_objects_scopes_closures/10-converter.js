#!/usr/bin/node

exports.converter = function (base) {
  if (base <= 1) {
    return;
  }

  exports.converter = function (num) {
    if (num >= base) {
      exports.converter(parseInt(num / base));
    }
    process.stdout.write((num % base).toString());
  };
};
