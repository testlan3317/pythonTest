const express = require('express');
const morgan = require('morgan');
const mongoose = require('mongoose');
const Blog = require('./models/blog')

// express app
const app = express();

// connect to mongoDB, note-tuts is the collections we create
const dbURI = 'mongodb+srv://jforstudy247:46vgDGbD9aYau3f7@cluster0.pmbwztx.mongodb.net/note-tuts?retryWrites=true&w=majority';


// we'll need mongoose to manage it. (mongoose, Models & Schemas)
 mongoose.connect(dbURI)
         .then((result) => {
            console.log('connected to db');
            app.listen(3000);     // after it's connected to db, then start listen on 3000
         })
         .catch((err) => console.log(err));

// register view engine
app.set('view engine', 'ejs'); //let it know ejs will be used to create our template
                               // default ejs will look for the views folder, 
                               // but you can use "set" to set another location. app.set('views', 'myviews');



// listen for request
// app.listen(3000)

/*
// using next(), otherwise, it'll hang
app.use((req, res, next) =>{
    console.log('New request made: ');
    console.log('host: ', req.hostname);
    console.log('path: ', req.path);
    console.log('method: ', req.method);
    next();
});
*/

// we need to define what files should be public (or allow user client to access)
// we can use it with static middleware. 

app.use(express.static('public')); // in this case, if you put css inside the folder, it'll be accessible.

app.use(express.urlencoded( { extended: true})); // this middleware to accept post data.

app.use(morgan('dev'));
app.use((req, res, next) => {
  res.locals.path = req.path;
  next();
});

// mongoose and mongo sandbox routes
app.get('/add-blog', (req, res) =>{
    const blog = new Blog({
        title: 'new blog 2',
        snippet: 'about my new blog',
        body: 'more about my new blog'
    });

    blog.save()
        .then((result) =>{
            res.send(result);
        })
        .catch((err) =>{
            console.log(err);
        })
});

app.get('/all-blogs', (req, res) => {
    Blog.find()
        .then((result) => {
            res.send(result);
        })
        .catch((err) =>{
            console.log(err);
        });
})

app.get('/single-blog', (req, res) => {
    Blog.findById('65a2f70a6f5180170e7f9855')
    .then((result) =>{
        res.send(result);
    })
    .catch((err) =>{
        console.log(err);
    })
})


app.get('/', (req, res) => {

    // res.send('<p>Home Page</p>');  // it'll automatically set the header, and it'll indicate the statusCode automatically
    // res.sendFile('./views/index.html', {root: __dirname});
    
    // use render function to call view engine
    // res.render('index');

    // when render, we can pass the data to the ejs page. 

    /*
    const blogs = [
        {title: 'Yoshi finds eggs', snippet: 'Lorem ipsum dolor sit amet consectetur'},
        {title: 'mario finds stars', snippet: 'Lorem ipsum dolor sit amet consectetur'},
        {title: 'How to defeat browser', snippet: 'Lorem ipsum dolor sit amet consectetur'},
    ]

    res.render('index', {title: 'Home', blogs: blogs}); // we can just pass "blogs" since both key-value are same
    */
    res.redirect('/blogs');
});


app.get('/blogs/create', (req, res) => {
  
    res.render('create', { title: 'Create a new blog' })

});

app.get('/about', (req, res) => {

    // res.send('<p>About Page</p>');  
     // res.sendFile('./views/about.html', {root: __dirname});

    res.render('about', {title: 'About'});
    
});

// using next(), otherwise, it'll hang
/*
app.use((req, res, next) =>{
    console.log('in the next middleware');
    next();
});
*/


// redirect
app.get('/about-us', (req, res) => {
 
    res.redirect('/about');

});

// handle post request

  
app.get('/blogs', (req, res) => {
    Blog.find().sort({ createdAt: -1 })
      .then(result => {
        res.render('index', { blogs: result, title: 'All blogs' });
      }).catch(err => {
        console.log(err);
      });
});

app.post('/blogs', (req, res) => {
    // console.log(req.body);
    const blog = new Blog(req.body);
  
    blog.save()
      .then((result) => {
        res.redirect('/blogs');
      })
      .catch((err) => {
        console.log(err);
      });
  });

// :id is parameter
// looks like the order matter, the detection of the path is based on the level, if 1st level match, then it'll dig into it. so it'll search for /blogs/, if this /blogs/:id is before /blogs/create, then the app'll crash.
app.get('/blogs/:id', (req, res) =>{
    const id = req.params.id;
    //console.log(id);
    Blog.findById(id)
        .then(result => {
            res.render('details', {blog: result, title:'Blog Details'})
        }).catch(err =>{
            console.log(err);
        })
})

app.delete('/blogs/:id', (req, res) => {
    const id = req.params.id;
    
    Blog.findByIdAndDelete(id)
      .then(result => {
        res.json({ redirect: '/blogs' });
      })
      .catch(err => {
        console.log(err);
        res.status(404).render('404', {title: 'Blog not found 404'});
      });
  });


// 404
// use(): to create middleware and fire middleware functions in express
// it's basically tell use this function for every single request if the code reach here. 
// technically, the code load them all, if one match, it's routing. if not, it'll go to the here which is very end.
app.use((req, res) => {
//    res.status(404).sendFile('./views/404.html', {root: __dirname}); // we have to manually add 404 code to indicate it's an 404 error 
                                                                    // otherwise, it just return the 404 page without error code.
        
    res.status(404).render('404', {title: '404'});
});



// EJS Template
// EJS Templates are processed through the EJS view engine on the server (server side rendering)

// partials (or called partial templates): parts of templates can be re-used in different views.


// 3rd party middleware - morgan


// request Types

// GET, POST, DELETE, PUT
