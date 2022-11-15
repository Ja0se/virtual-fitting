const express = require("express");
const bodyParser = require("body-parser");
const fs = require("fs");
const spawn = require("child_process").spawn;
const mysql = require('mysql');
const dbconfig = require('./database.js');
const connection = mysql.createConnection(dbconfig);

const app = express();
const PORT = 9999;

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ limit: "1gb", extended: false }));

app.post("/test", (req, res) => {
  res.header("Access-Control-Allow-Origin", "*");
  let tmp = req.body.data;
  tmp=tmp.toString();
  tmp = tmp.replace(/^data:image\/[a-z]+;base64,/, "");
  fs.writeFile('test.txt', tmp, (err) => err && console.error(err));
  //console.log('tmp : '+tmp)
  let result = spawn('python',['test.py']);
  
  console.log('hello');

  result.stdout.on('data',function(data){
    console.log('send response')
    data=data.toString();
    // point 좌표 sql 실행
    let sql=`TRUNCATE TABLE hand.profile`;
    connection.query(sql,(error,rows)=>{
      if(error)throw error;
      console.log('Delete profile');
    })
    console.log(data)
    sql=`INSERT INTO hand.profile(neck,neckx,upwidth,pelvis,pelvisx,bottomwidth) VALUES `+data;
    connection.query(sql,(error,rows)=>{
      if(error)throw error;
      console.log('insert profile');
    })
    data=fs.readFileSync('test.txt')
    data=data.toString()
    res.send(data)
  })

});

app.listen(PORT, () => {
  console.log(`✅ Listening Server htttp://localhost:${PORT}`);
});

