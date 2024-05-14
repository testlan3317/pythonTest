const xyz = require('./people');

// const { people } = require('./people')
// console.log(people, ages)   // in this case only people got extracted
// extract both
// const { people, ages } = require('./people')

console.log(xyz.people, xyz.ages);

// os is built in module
const os = require('os');

// console.log(os);
console.log(os.platform(), os.homedir());

