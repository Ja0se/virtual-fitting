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

app.post("/clear",(req,res)=>{
  res.header("Access-Control-Allow-Origin", "*");
  data=fs.readFileSync('profile.txt')
  data=data.toString()
  res.send(data)
})

app.post("/dress",(req,res)=>{
  res.header("Access-Control-Allow-Origin", "*");
  let tmp4 = req.body.dress;
  tmp4=tmp4.toString();
  tmp4 = tmp4.replace(/^data:image\/[a-z]+;base64,/, "");
  fs.writeFile('dress.txt', tmp4, (err) => err && console.error(err));
  let sql4=`SELECT * FROM hand.profile`;
  connection.query(sql4,(error,rows)=>{
    if(error)throw error;
    tmp4=rows[0];

    let result4 = spawn('python',['dress.py',tmp4.upwidth,tmp4.neck,tmp4.neckx]);
    console.log('dress fitting start');
    //이미지 합치는 py실행
    result4.stdout.on('data',function(data){
      console.log('dress fitting send');
      data=fs.readFileSync('fit.txt')
      data=data.toString()
      res.send(data)
    })
  })
})

app.post("/bottom",(req,res)=>{
  res.header("Access-Control-Allow-Origin", "*");
  let tmp3 = req.body.bottom;
  tmp3=tmp3.toString();
  tmp3 = tmp3.replace(/^data:image\/[a-z]+;base64,/, "");
  fs.writeFile('bottom.txt', tmp3, (err) => err && console.error(err));
  let sql3=`SELECT * FROM hand.profile`;
  connection.query(sql3,(error,rows)=>{
    if(error)throw error;
    tmp3=rows[0];

    let result3 = spawn('python',['bottom.py',tmp3.pelvis,tmp3.pelvisx,tmp3.bottomwidth,tmp3.bottom]);
    console.log('bottom fitting start');
    //이미지 합치는 py실행
    result3.stdout.on('data',function(data){
      console.log('bottom fitting send');
      data=fs.readFileSync('fit.txt')
      data=data.toString()
      res.send(data)
    })
  })
})

app.post("/up",(req,res)=>{
  res.header("Access-Control-Allow-Origin", "*");
  let tmp2 = req.body.up;
  tmp2=tmp2.toString();
  tmp2 = tmp2.replace(/^data:image\/[a-z]+;base64,/, "");
  fs.writeFile('up.txt', tmp2, (err) => err && console.error(err));
  let sql2=`SELECT * FROM hand.profile`;
  connection.query(sql2,(error,rows)=>{
    if(error)throw error;
    tmp2=rows[0];

    let result2 = spawn('python',['up.py',tmp2.neck,tmp2.neckx,tmp2.upwidth,tmp2.pelvis]);
    console.log('up fitting start');
    //이미지 합치는 py실행
    result2.stdout.on('data',function(data){
      console.log('up fitting send');
      data=fs.readFileSync('fit.txt')
      data=data.toString()
      res.send(data)
    })
  })
})

app.post("/test", (req, res) => {
  res.header("Access-Control-Allow-Origin", "*");
  let tmp = req.body.data;
  tmp=tmp.toString();
  tmp = tmp.replace(/^data:image\/[a-z]+;base64,/, "");
  fs.writeFile('profile.txt', tmp, (err) => err && console.error(err));
  //console.log('tmp : '+tmp)
  let result = spawn('python',['initprofile.py']);
  
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
    sql=`INSERT INTO hand.profile(neck,neckx,upwidth,pelvis,pelvisx,bottomwidth,bottom) VALUES `+data;
    connection.query(sql,(error,rows)=>{
      if(error)throw error;
      console.log('insert profile');
    })
    data=fs.readFileSync('profile.txt')
    data=data.toString()
    res.send(data)
  })

});

app.listen(PORT, () => {
  console.log(`✅ Listening Server htttp://localhost:${PORT}`);
});

