// var name = "max";
// var age = 29;
// var hasHobbies = true;


const name = 'Max';
let age = 29;               // new way to declare variable
const hasHobbies = true;

age = 30;

console.log(name);

// new syntax to define function
// arrow function syntax
const summarizeUser = (userName, userAge, userHashHobby) => {
    return (
        'Name is ' +  userName + ", age is " + userAge + 
        ' and the user has hobbies: ' + userHashHobby
        );
}

/* old way to create function
normal way to define a function
function summarizeUser(userName, userAge, userHashHobby) {
    return (
        'Name is ' +  userName + ", age is " + userAge + 
        ' and the user has hobbies: ' + userHashHobby
        );
}

annoymous definition of function
const summarizeUser = function (userName, userAge, userHashHobby){
    return (
        'Name is ' +  userName + ", age is " + userAge + 
        ' and the user has hobbies: ' + userHashHobby
        );
}
*/

/* 
const add = (a,b) => {
    return a + b;
}
 if you only get one return statement inside the function as above, you can write this way
*/

const add = (a,b) => a + b;

const addOne = (a) => a + 1;

// since you only have 1 argument, you can write as this, const addOne = a => a + 1;

// function with no arguments.
const addRandom = () => 1 + 2;

console.log(summarizeUser(name, age, hasHobbies))

console.log(add(1,2));
console.log(addOne(1));
console.log(addRandom());

