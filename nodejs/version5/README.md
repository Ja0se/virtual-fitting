### profile, up, bottom, dress, clear 기능 추가

ㅇ db에 color랑 파일 이름 넣는거 추가

이후 추천 시스템 작성할것

ㅇ profile : 누끼 제거 및 profile DB에 좌표 작성

ㅇ up : 로직을 활용하여 피팅 -> 이미지에 따른 사이즈문제로인해 크롭티는 불가능할듯

ㅇ down : up과 같은 방식으로 이미지를 늘려서 사용 -> 반바지에 대한 해답 필요(아마 추가로 태그를 생성해야할듯)

ㅇ dress : 비율을 활용해서 피팅 -> 치마같은 경우도 태그를 달아서 좌표조정하는 역할을 해주면 될듯하다.

ㅇ submit : 이미지 등록시 filename을 주요키로 db작성 color 추출 db저장 / 누끼제거 이미지 response -> 휴대폰 로컬 저장하면 됨

wear : 입고 있는 옷 last update -> 현재 입고있는 옷의 정보를 가지는 전역 변수나 json을 가지고 있어야 할듯하다.
