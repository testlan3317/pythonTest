const fetchData = callback => {
    setTimeout(() => {
        callback('Done!');
    }, 1500);
}

// Asynchronous code, it doesn't finish immediately.
setTimeout(() =>{
    console.log('Timer is done!')
    fetchData(text => {
        console.log(text);
    })
}, 2000);

// below is synchronous code
console.log('hello!');
console.log('Hi!');
// it'll read the synchronous code fast and exec,while asychronous code was read. then exec async code

// promises
const fetchData1 = () => {
    const promise = new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve('Done!');
        }, 1500);
    });
    return promise;
};
setTimeout(() =>{
    console.log('Timer is done!')
    fetchData1().then(text => {
        console.log(text);
        return fetchData1();
    })
    .then(text2 => {
        console.log(text2);
    });
}, 2000);


// backticks  you can use backticks (`)
// `Another way of writing strings`
// console.log(`My name is ${name} and I am ${age} years old.`);
