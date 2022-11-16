const URL = "http://localhost:9999";

$(document).ready(function (event) {
  $('#wear').on('click', function(){
    $.ajax({
      url:`${URL}/wear`,
      method:"POST",
      data : {
        filename:'14.jpg',
        species:'dress',
        last : '2022-11-16'
      },
      success: async function(res){
      },
      error:function(){
        alert('서버 연결 상태가 원활하지 않습니다.');
      }
    })
  })

  $('#submit').on('click', function(){
    $.ajax({
      url:`${URL}/submit`,
      method:"POST",
      data : {
        filename:'14.jpg',
        data: document.getElementById('dressimg').src,
        species : 'dress'
      },
      success: async function(res){
        console.log(res)
      },
      error:function(){
        alert('서버 연결 상태가 원활하지 않습니다.');
      }
    })
  })

  $('#clear').off().on('click', function() {
    $.ajax({
      url: `${URL}/clear`,
      method: "POST",
      success: async function (res) {
        console.log('success');
        var imgsrc = "data:image/jpg;base64," + res;
        document.getElementById('img2').src = imgsrc;
      },
      error: function () {
        alert("서버 연결 상태가 원할하지 않습니다.");
      },
    });
  })

  $('#dress').off().on('click', function() {
    $.ajax({
      url: `${URL}/dress`,
      method: "POST",
      data : { 
        dress : document.getElementById('dressimg').src
      },
      success: async function (res) {
        console.log('success');
        var imgsrc = "data:image/jpg;base64," + res;
        document.getElementById('img2').src = imgsrc;
      },
      error: function () {
        alert("서버 연결 상태가 원할하지 않습니다.");
      },
    });
  })

  $('#bottom').off().on('click', function() {
    $.ajax({
      url: `${URL}/bottom`,
      method: "POST",
      data : { 
        bottom : document.getElementById('bottomimg').src
      },
      success: async function (res) {
        console.log('success');
        var imgsrc = "data:image/jpg;base64," + res;
        document.getElementById('img2').src = imgsrc;
      },
      error: function () {
        alert("서버 연결 상태가 원할하지 않습니다.");
      },
    });
  })

  $('#up').off().on('click', function() {
    $.ajax({
      url: `${URL}/up`,
      method: "POST",
      data : { 
        up : document.getElementById('upimg').src
      },
      success: async function (res) {
        console.log('success');
        var imgsrc = "data:image/jpg;base64," + res;
        document.getElementById('img2').src = imgsrc;
      },
      error: function () {
        alert("서버 연결 상태가 원할하지 않습니다.");
      },
    });
  })

  $('#test').off().on('click', function() {
    $.ajax({
      url: `${URL}/test`,
      method: "POST",
      data : { data : document.getElementById('img').src},
      success: async function (res) {
        console.log('success');
        var imgsrc = "data:image/jpg;base64," + res;
        //btoa(String.fromCharCode.apply(null, new Uint8Array(res)));
        document.getElementById('img2').src = imgsrc;
      },
      error: function () {
        alert("서버 연결 상태가 원할하지 않습니다.");
      },
    });
  })

});
