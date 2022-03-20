

//Events 
const EventEmitter = require('events');
const eventEmitter = new EventEmitter();

eventEmitter.on("testEvent", ()=>{
    console.log("Test!");
})

eventEmitter.emit("testEvent");


//File system
var {readFile, readFileSync} = require("fs");
    //if a modele has Sync its means that is a blocking module


//This is non-blocking, using a callback
readFile('./documentNode.txt','utf-8', (err,txt)=>{
    console.log("non-blocking reading: "+txt)
})

//This is blocking
const txt= readFileSync('./documentNode.txt','utf-8')
console.log("blocking reading: "+txt)


//promises
var {readFile} = require("fs").promises;


async function read(){
    const file = await readFile('./documentNode.txt','utf-8');
    console.log("async promise reading: "+file);
}
read()

//modules
var module = require("./myModule")
console.log(module);
module.testFunction(" TEST! MODULE");