// streams
// start using data, before it has finished loading

const fs = require('fs');

const readStream = fs.createReadStream('./docs/blog3.txt', {encoding: 'utf-8'});

const writeStream = fs.createWriteStream('./docs/blog4.txt');

// readStream.on('data', (chunk) =>{   // listened on the 'data' event on this stream.
//     console.log('----- New CHUNK -----');
//     //console.log(chunk.toString());
//     console.log(chunk);
//     writeStream.write('\nNEW CHUNK\n');
//     writeStream.write(chunk);
// });

// piping
// read from readStream and pipe to writeStram
readStream.pipe(writeStream);