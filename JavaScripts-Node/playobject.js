const person = {
    name: "Max",
    age: 29,
    greet: function () {
        console.log("Hi, I am " + this.name);
    }
};

person.greet();

// reference type
const hobbies = ['Sports','Cooking'];

// for (let hobby of hobbies){
//     console.log(hobby);
// }

// console.log(hobbies.map(hobby =>  'Hobby: ' + hobby ));

// console.log(hobbies);

hobbies.push('Programming'); // the reference of this array is not changed. that's why it could add item.
// console.log(hobbies)

const copiedArray = hobbies.slice();

// spread operator and rest opeartor

// spread array, pull the items out and put into the new array 
const copiedArray1 = [...hobbies];
//  it could be new object as well. 
const copiedPerson = {...person};

//console.log(copiedArray);
console.log(copiedArray1);


// rest operator is essential the opposite to the spread operator
const toArray = (arg1, arg2, arg3) => {
    return [arg1, arg2, arg3];
};

// merge multiple arguments into an array
const toArray1 = (...args) => {
 return args;
};

console.log(toArray(1, 2, 3));
console.log(toArray1(1, 2, 3, 4));


/* Destructring */

const printName = (personData) => {
    console.log(personData.name);
}
printName(person);

// destructre syntax, add curly braces, it'll pull out the name property
const printName1 = ({ name }) => {
    console.log(name);
};

printName1(person);

// for object, we can do like this
const {name, age} = person;
console.log(name, age);

// for array
const [hobby1, hobby2] = hobbies;
console.log(hobby1, hobby2)


