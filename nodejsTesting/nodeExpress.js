const express = require('express');

const app = express();

var {readFile} = require("fs");
const { send } = require('process');

app.get('/',(request,response)=>{

    readFile('./home.html','utf-8',(err,html)=>{
        if(err){
            response.status(500).send("Sorry, we are in maintenance")
        }

        response.send(html);
    })
    
});

app.listen(process.env.PORT || 3000 ,()=>{
    console.log("APP AVALAIBLE in port 3000 ")
})