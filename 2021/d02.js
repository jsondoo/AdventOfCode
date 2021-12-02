// run with `cat input.txt | node d02.js`
const lines = require('fs').readFileSync(0).toString().split(/\s+/).filter((t) => t.length > 0)
const commands = []
for (let i = 0; i < lines.length; i += 2) {
  commands.push([lines[i], parseInt(lines[i+1])]);
}

function p1() {
  let [h, d] = [0, 0];
  commands.forEach(function(command) {
    const dir = command[0]
    const x = command[1]
    switch (dir) {
      case "forward":
        h += x;
        break;
      case "down":
        d += x;
        break;
      case "up":
        d -= x;
        break;
    }
  });
  return h * d;
}

function p2() {
  let [h, d, a] = [0, 0, 0];
  commands.forEach(function(command) {
    const dir = command[0]
    const x = command[1]
    switch (dir) {
      case "forward":
        h += x;
        d += a * x;
        break;
      case "down":
        a += x;
        break;
      case "up":
        a -= x;
        break;
    }
  });
  return h * d;
}

console.log(p1())
console.log(p2())