



//Events 
const EventEmitter = require('events');
const eventEmitter = new EventEmitter();

eventEmitter.on("testEvent", ()=>{
    console.log("Test!");
})

eventEmitter.emit("testEvent");


//File system
const {readFile, readFileSync} = require("fs");
    //if a modele has Sync its means that is a blocking module


//This is non-blocking, using a callback
readFile('./documentNode.txt','utf-8', (err,txt)=>{
    console.log("non-blocking reading: "+txt)
})

//This is blocking
const txt= readFileSync('./documentNode.txt','utf-8')
console.log("blocking reading: "+txt)


//promises
