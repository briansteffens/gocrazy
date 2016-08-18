var mongojs = require('mongojs');
var db = mongojs('gocrazy', ['stuff', 'things']);

function random(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min)) + min;
}

function randomLetter() {
  return String.fromCharCode(random(0, 26) + 97);
}

function randomString(len) {
  var ret = '';
  for (var i = 0; i < len; i++) {
    ret += randomLetter();
  }
  return ret;
}

for (var i = 0; i < 10000; i++) {
  db.stuff.save({
    stuff: randomString(64),
    things: randomString(64),
    nonsense: randomString(64),
    important: randomString(64)
  }, function(err, list) {
    if (err) {
      console.log('Error: ' + err);
    }
  });

  if (i % 100 == 0) {
    console.log(i);
  }
}
