const URL = "http://localhost:9999";

$(document).ready(function () {
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
});

$(document).ready(function () {
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
});

$(document).ready(function () {
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
});

$(document).ready(function () {
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
});


$(document).ready(function () {
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
