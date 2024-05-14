const fs = require('fs');

// reading files
fs.readFile('./docs/blog1.txt', (err, data) => {
    if (err){
        console.log(err);
    }
    console.log(data.toString());
});

console.log('last line');

// writing files
fs.writeFile('./docs/blog1.txt', 'hello world', ()=> {
    console.log('file was written');
});


// directories
if(!fs.existsSync('./assets')){
    fs.mkdir('./assets', (err) =>{
        if(err){
            console.log(err);
        }
        console.log('folder created');
    });
} else {
    fs.rmdir('./assets', (err)=>{
        if(err){
            console.log(err);
        }
        console.log('folder deleted');
    });
}


// delete files
// unlink - used to delete file
if(fs.existsSync('./docs/deleteme.txt')){
    fs.unlink('./docs/deleteme.txt', (err)=>{
        if(err){
            console.log(err);
        }
        console.log('file deleted');
    });
}

// above are asynchornized functions(writeFile, readFile, unlink, mkdir, rmdir)

// streams
// start using data, before it has finished loading
