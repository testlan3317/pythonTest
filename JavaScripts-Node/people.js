const people = ['yoshi', 'ryu', 'chun-li', 'mario'];
const ages = [20, 25, 30, 35];

console.log(people)

// we have to export the variable people, 
// so it could be used in the modules.js

// export one variable
// module.exports = people;

// export multiple variable

module.exports = {
    people: people,
    ages: ages,
}