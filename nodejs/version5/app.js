const express = require("express");
const bodyParser = require("body-parser");
const fs = require("fs");
const spawn = require("child_process").spawn;
const mysql = require('mysql');
const dbconfig = require('./database.js');
const { send } = require("process");
const connection = mysql.createConnection(dbconfig);

const app = express();
const PORT = 9999;

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ limit: "1gb", extended: false }));

app.post("/recommend",(req,res)=>{
  res.header("Access-Control-Allow-Origin", "*");
  let ret=fs.readFileSync('recommend.txt')
  ret=ret.toString();
  ret=JSON.parse(ret);
  let Json={
    "recommend1":null,
    "recommend2":null,
    "recommend3":null,
    "recommend4":null
  }
  Json=JSON.stringify(Json);
  Json=JSON.parse(Json);
  console.log(ret);
  if((ret.up==null &&ret.bottom==null)||(ret.up!=null&&ret.bottom!=null)){
    console.log('recommend rand bottom and up');
    let sql=`select * from hand.up order by rand() limit 2`;
    connection.query(sql,(error,rows)=>{
      if(error)throw error;  
      let first=rows[0];
      let second=rows[1];
      Json.recommend1=first.filename;
      Json.recommend3=second.filename;
      let result=spawn('python',['recommend_up.py',first.color.toString()]);
      result.stdout.on('data',function(data){
        data=data.toString();
        let sql1=`select * from hand.down where `+data;
        connection.query(sql1,(error,row)=>{
          if(error)throw error;
          Json.recommend2=row[0].filename;
          let result2=spawn('python',['recommend_up.py',second.color.toString()]);
          result2.stdout.on('data',function(data){
          data=data.toString();
          sql1=`select * from hand.down where `+data;
            connection.query(sql1,(error,row)=>{
              if(error)throw error;
              Json.recommend4=row[0].filename;
              res.send(Json);
            })
          })
        })
      })
    })
  }
  else if(ret.up==null &&ret.bottom!=null){
    console.log('recommend rand up');
    Json.recommend2=ret.bottom;
    Json.recommend4=ret.bottom;
    let sql=`select * from hand.down where filename='`+ret.bottom.toString()+`'`;
    connection.query(sql,(error,rows)=>{
      if(error)throw error;
      let result = spawn('python',['recommend_bottom.py',rows[0].color.toString()]);
      result.stdout.on('data',function(data){
        let sql2=`select * from hand.up where `+data.toString();
        connection.query(sql2,(error,row)=>{
          Json.recommend1=row[0].filename;
          Json.recommend3=row[1].filename;
          res.send(Json);
        })
      })
    })
  }
  else{
    console.log('recommend rand bottom');
    Json.recommend1=ret.up;
    Json.recommend3=ret.up;
    let sql=`select * from hand.up where filename='`+ret.up.toString()+`'`;
    connection.query(sql,(error,rows)=>{
      if(error)throw error;
      let result = spawn('python',['recommend_up_2.py',rows[0].color.toString()]);
      result.stdout.on('data',function(data){
        let sql2=`select * from hand.down where `+data.toString();
        connection.query(sql2,(error,row)=>{
          Json.recommend2=row[0].filename;
          Json.recommend4=row[1].filename;
          res.send(Json);
        })
      })
    })
  }
})

app.post("/start",(req,res)=>{
  res.header("Access-Control-Allow-Origin", "*");
  data=fs.readFileSync('profile.txt')
  fs.writeFile('fit.txt', data, (err) => err && console.error(err));
  data=data.toString()
  let Json={
    "up":null,
    "bottom":null
  }
  Json=JSON.stringify(Json);
  // wirte할때 서버가 재시작 되버림 ;;; -> 고쳐줭
  fs.writeFile('recommend.txt', Json, (err) => err && console.error(err));
  console.log('json clear')
  res.send(data);
})

// 굳이 DB에 착용 날짜를 넣을 필요가 없는걸?
// app.post("/wear",(req,res)=>{
//   res.header("Access-Control-Allow-Origin", "*");
//   let sql=`update hand.`+req.body.upspecies.toString();
//   sql=sql+` set last = '`+req.body.uplast.toString();
//   sql=sql+ `' where filename = '`+req.body.upfilename.toString()+`'`;
//   console.log(sql)
//   connection.query(sql,(error,rows)=>{
//     if(error)throw error;  
//     console.log('success update');
//     res.send('success');
//   })
// })

app.post("/submit",(req,res)=>{
  res.header("Access-Control-Allow-Origin", "*");
  let tmp = req.body.data;
  tmp = tmp.toString();
  tmp = tmp.replace(/^data:image\/[a-z]+;base64,/, "");
  fs.writeFile('test.txt', tmp, (err) => err && console.error(err));
  let result=spawn('python',['initimage.py']);
  result.stdout.on('data',function(data){
    data=data.toString()
    data =data.replace(/\s/g,'');
    let ins=`'`+req.body.filename.toString()+`','`+data;
    ins =ins.replace(/\r/g,'');
    ins=ins+`',NULL)`
    
    let sql=`insert into hand.`+req.body.species.toString()+`(filename,color,last) values(`+ins;
    
    console.log(sql)
    connection.query(sql,(error,rows)=>{
      data=fs.readFileSync('test.txt');
      data=data.toString()
      if(error)throw error;  
      console.log('success init');
      res.send(data);
    })
  })
})

app.post("/clear",(req,res)=>{
  res.header("Access-Control-Allow-Origin", "*");
  data=fs.readFileSync('profile.txt')
  fs.writeFile('fit.txt', data, (err) => err && console.error(err));
  data=data.toString()
  let Json={
    "up":null,
    "bottom":null
  }
  Json=JSON.stringify(Json);
  fs.writeFile('recommend.txt', Json, (err) => err && console.error(err));
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

    let result4 = spawn('python',['dress.py',tmp4.upwidth,tmp4.neck,tmp4.neckx,tmp4.bottom]);
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

  let ret=fs.readFileSync('recommend.txt')
  ret=ret.toString();
  ret=JSON.parse(ret);
  ret.bottom=req.body.filename;
  console.log('now ret =',ret);
  ret=JSON.stringify(ret);
  fs.writeFile('recommend.txt', ret, (err) => err && console.error(err));
  
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
  let ret=fs.readFileSync('recommend.txt')
  ret=ret.toString();
  ret=JSON.parse(ret);
  ret.up=req.body.filename;

  console.log(ret);

  ret=JSON.stringify(ret);
  fs.writeFile('recommend.txt', ret, (err) => err && console.error(err));
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
  
  console.log('프로필 등록');

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

