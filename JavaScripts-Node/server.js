const http = require('http');
const fs = require("fs");
const _ = require('lodash');

// import { createServer } from 'http';

const server = http.createServer((req, res) => {
    
    //lodash
    const num = _.random(0, 20);
    console.log(num);

    const greet = _.once(() => {
        console.log('hello');
    });

    //console.log('request made');
    // console.log(req);
    //console.log(req.url, req.method);

    // set header content type
    /*
    res.setHeader('Content-Type', "text/plain");

    res.write('Hello nodejs');

    res.end();

    res.setHeader('Content-Type', "text/html")
    res.write('<head><link rel='stylesheet' href="#"></head>')
    res.write('<p>hello again</p>');
    res.end(); */

    res.setHeader('Content-Type', 'text/html');

    let path = './views/';

    // Question: what's the difference between setHeader and writeHeader

    switch (req.url) {
        case '/':
            path += 'index.html';
            res.statusCode = 200;
            break;
        case '/about':
            path += 'about.html';
            res.statusCode = 200;
            break;
        case '/about-me':
            path += 'about.html';
            //res.writeHead(301, {'Location':'/about'}); this writeHead works

            // only set Location doesn't work, we'll need to add the statusCode, so it could redirect 
            res.setHeader('Location', '/about');
            res.statusCode = 301;
            res.end();
            break;
        default:
            res.statusCode = 404;
            path += '404.html'
            break;
    }

    fs.readFile(path, (err, data) => {
        if (err) {
            console.log(err);
        } else {
            res.write(data);
            res.end();
        }
        // if we got simple date to return, we can just use "res.end(data)""
    });

});

server.listen(3000, 'localhost', () => {
    console.log('listening for requests on port 3000');
});


// Base Routing -> req.url
// Status Code
// Status code describe the type of response sent to browser

// 200-ok, 301-Resource moved, 404- Page not found, 500-internal server error

/****
 * Status code
 * 100 Range - information response
 * 200 Range - success code
 * 300 Range - codes for redirects
 * 400 Range - user or client error codes
 * 500 Range - server error codes
 */


// Redirect


// npm - additional package for extra feature which is not in node core, such as some framework
// npm - node package management

// nodemon - you don't have to restart the server every time
// install package globally
// npm install -g nodemon
// -g: global install flag
// run server as "nodemon server.js"

// package.js: track any package we installed locally to our project and other things such as project details
// and any kind of project specific scripts.

// if you want to use 3rd party package, you should create a package JSON file. 
// npm init: it will init a package JSON file
// whatever 3rd party package we install for our project, it'll create a "node_modules" folder under the project

// type "npn install", will look into the package.json file and look for the dependencies for you and install all packages.


// install "express" framework.
// what is express? helps monitor routing easily
// npm install express



// view Engines - inject dynamic data
// we use EJS as view engine