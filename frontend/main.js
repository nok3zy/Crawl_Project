import router from "./router";
import express from "express";
import axios from "axios"
import bodyParser from "body-parser"


// const schedule = require("node-schedule");
// const job = schedule.scheduleJob("30 * * * * *",function(){
//     console.log("here")
//     });


const app = express()

app.use("/static", express.static("static"));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.set("view engine","pug");

app.listen(4000,()=>{
    console.log("listen on 4000");
});


app.use("/",router);

