// Global object

const { clearInterval } = require("timers");

console.log(global);

global.setTimeout( () => {
    console.log('in the timeout');
    clearInterval(int);
}, 3000);

const int = setInterval(() =>{
    console.log('in the interval');
}, 1000);

console.log(__dirname); // get the current absolute path for the current folder
console.log(__filename);// get the current absolute path for the current file

// console.log(document.querySelector); // we'll get error, because document is in the window object.




