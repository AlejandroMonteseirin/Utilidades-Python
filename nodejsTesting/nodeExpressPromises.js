const express = require('express');

const app = express();

var {readFile} = require("fs").promises;
const { send } = require('process');

app.get('/',async (request,response)=>{

    response.send(await readFile('./home.html','utf-8'));
    
    
});

app.listen(process.env.PORT || 3000 ,()=>{
    console.log("APP AVALAIBLE in port 3000 using promises")
})