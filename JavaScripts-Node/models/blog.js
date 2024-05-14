const mongoose = require('mongoose');

const Schema = mongoose.Schema;

const blogSchema = new Schema({
    title: { type: String, required: true},    // fields
    snippet: {type: String, required: true},
    body: {type: String, required: true}
}, {timestamps: true});

// schema is to define the structure of the document. 
// the model is based on this schema. it's the interface we use to interacte with the mongoDB

const Blog = mongoose.model('Blog', blogSchema)

module.exports = Blog;


