### profile, up, bottom, dress, clear 기능 추가

ㅇ db hand.up, hand.down, hand.dress, hand.profile 네가지 스키마 정의

ㅇ 추천 시스템 : test 누르면 추천 적용된 이미지가 뜹니다.  / 실제로는 피팅화면 접속시, 상의 또는 하의 선택시 해당 api가 제공되야한다.

ㅇ profile : 누끼 제거 및 profile DB에 좌표 작성

ㅇ up : 로직을 활용하여 피팅

ㅇ down : up과 같은 방식으로 이미지를 늘려서 사용

ㅇ dress : 비율을 활용해서 피팅

ㅇ submit : 이미지 등록시 filename을 주요키로 db작성 color 추출 db저장 / 누끼제거 이미지 response -> 휴대폰 로컬 저장하면 됨

ㅇ wear : 입고 있는 옷 last update / DB에 last필요 없음 로컬에만 들고있으면 될듯하다.

app.js -> nodejs

database.js -> db 내용

index.js -> script

index.css / index.html -> test web page

bottom,dress,up -> make fitting image

Extract_Color.py / Color.py / initimage.py -> 색상 추출

Make_Image.py -> unet을 활용한 이미지 추출

pose.py / pofile.py / initprofile.py -> 프로필 생성, openpose를 활용해서 db에 좌표 저장 및 이미지 버퍼파일 생성

recommend_up.py -> 초기 이미지 이미지 두개 추천위한 py

recommend_bottom.py -> 상의에 맞는 하의 추천

recommend_up_2.py -> 하의에 맞는 상의 추천

test2.py -> base64 image 생성 파일

test.py -> test파일

up_bottom.csv -> 선호도 기반 데이터 파일
