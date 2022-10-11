'''
# 1. 빨간색  22
# 2. 주황색  29
# 3. 노란색  15
# 4. 연두색  37
# 5. 초록색  73
# 6. 카키색  57
# 7. 갈색    51
# 8. 검은색  1
# 9. 회색    22
# 10. 분홍색 27
# 11. 보라색 88
# 12. 파란색 55
# 13. 하늘색 15
# 14. 남색   24
# 15. 베이지색  5 
# 16. 아이보리색  3
# 0. 흰색  1
# 색 리턴해주는 함수
'''
def Colorfull(output):
  if 16 <=output[0] and output[0]<= 255 and 0 <=output[1] and output[1]<= 15 and 0 <=output[2] and output[2]<= 15:
    return 1
  elif 61 <=output[0] and output[0]<= 255 and 16 <=output[1] and output[1]<= 30 and 0 <=output[2] and output[2]<= 15:
    return 1
  elif 121 <=output[0] and output[0]<= 255 and 31 <=output[1] and output[1]<= 45 and 0 <=output[2] and output[2]<= 15:
    return 1
  elif 181 <=output[0] and output[0]<= 255 and 46 <=output[1] and output[1]<= 60 and 0 <=output[2] and output[2]<= 15:
    return 1
  elif 241 <=output[0] and output[0]<= 255 and 61 <=output[1] and output[1]<= 75 and 0 <=output[2] and output[2]<= 15:
    return 1
  elif 16 <=output[0] and output[0]<= 30 and 0 <=output[1] and output[1]<= 15 and 16 <=output[2] and output[2]<= 30:
    return 1
  elif 61 <=output[0] and output[0]<= 255 and 0 <=output[1] and output[1]<= 15 and 16 <=output[2] and output[2]<= 30:
    return 1
  elif 31 <=output[0] and output[0]<= 255 and 16 <=output[1] and output[1]<= 30 and 16 <=output[2] and output[2]<= 30:
    return 1
  elif 91 <=output[0] and output[0]<= 255 and 31 <=output[1] and output[1]<= 45 and 16 <=output[2] and output[2]<= 30:
    return 1
  elif 136 <=output[0] and output[0]<= 255 and 46 <=output[1] and output[1]<= 60 and 16 <=output[2] and output[2]<= 30:
    return 1
  elif 196 <=output[0] and output[0]<= 210 and 61 <=output[1] and output[1]<= 90 and 16 <=output[2] and output[2]<= 30:
    return 1
  elif 211 <=output[0] and output[0]<= 225 and 61 <=output[1] and output[1]<= 75 and 16 <=output[2] and output[2]<= 30:
    return 1
  elif 226 <=output[0] and output[0]<= 255 and 61 <=output[1] and output[1]<= 90 and 16 <=output[2] and output[2]<= 30:
    return 1
  elif 91 <=output[0] and output[0]<= 255 and 1 <=output[1] and output[1]<= 15 and 31 <=output[2] and output[2]<= 45:
    return 1
  elif 106 <=output[0] and output[0]<= 255 and 16 <=output[1] and output[1]<= 30 and 31 <=output[2] and output[2]<= 45:
    return 1
  elif 136 <=output[0] and output[0]<= 255 and 31 <=output[1] and output[1]<= 45 and 31 <=output[2] and output[2]<= 45:
    return 1
  elif 181 <=output[0] and output[0]<= 255 and 1 <=output[1] and output[1]<= 30 and 46 <=output[2] and output[2]<= 60:
    return 1
  elif 151 <=output[0] and output[0]<= 255 and 31 <=output[1] and output[1]<= 45 and 46 <=output[2] and output[2]<= 60:
    return 1
  elif 196 <=output[0] and output[0]<= 255 and 46 <=output[1] and output[1]<= 60 and 46 <=output[2] and output[2]<= 60:
    return 1
  elif 211 <=output[0] and output[0]<= 255 and 61 <=output[1] and output[1]<= 90 and 46 <=output[2] and output[2]<= 60:
    return 1
  elif 181 <=output[0] and output[0]<= 255 and 0 <=output[1] and output[1]<= 75 and 61 <=output[2] and output[2]<= 75:
    return 1
  elif 196 <=output[0] and output[0]<= 255 and 76 <=output[1] and output[1]<= 90 and 61 <=output[2] and output[2]<= 75:
    return 1
  elif 181 <=output[0] and output[0]<= 195 and 61 <=output[1] and output[1]<= 135 and 0 <=output[2] and output[2]<= 15:
    return 2
  elif 196 <=output[0] and output[0]<= 210 and 61 <=output[1] and output[1]<= 150 and 0 <=output[2] and output[2]<= 15:
    return 2
  elif 211 <=output[0] and output[0]<= 225 and 61 <=output[1] and output[1]<= 165 and 0 <=output[2] and output[2]<= 15:
    return 2
  elif 226 <=output[0] and output[0]<= 240 and 61 <=output[1] and output[1]<= 180 and 0 <=output[2] and output[2]<= 15:
    return 2
  elif 241 <=output[0] and output[0]<= 255 and 76 <=output[1] and output[1]<= 180 and 0 <=output[2] and output[2]<= 15:
    return 2
  elif 181 <=output[0] and output[0]<= 195 and 61 <=output[1] and output[1]<= 150 and 16 <=output[2] and output[2]<= 30:
    return 2
  elif 196 <=output[0] and output[0]<= 210 and 91 <=output[1] and output[1]<= 150 and 16 <=output[2] and output[2]<= 30:
    return 2
  elif 211 <=output[0] and output[0]<= 225 and 76 <=output[1] and output[1]<= 165 and 16 <=output[2] and output[2]<= 30:
    return 2
  elif 226 <=output[0] and output[0]<= 255 and 91 <=output[1] and output[1]<= 165 and 16 <=output[2] and output[2]<= 30:
    return 2
  elif 166 <=output[0] and output[0]<= 255 and 46 <=output[1] and output[1]<= 90 and 31 <=output[2] and output[2]<= 45:
    return 2
  elif 181 <=output[0] and output[0]<= 255 and 91 <=output[1] and output[1]<= 105 and 31 <=output[2] and output[2]<= 45:
    return 2
  elif 196 <=output[0] and output[0]<= 255 and 106 <=output[1] and output[1]<= 135 and 31 <=output[2] and output[2]<= 45:
    return 2
  elif 211 <=output[0] and output[0]<= 255 and 136 <=output[1] and output[1]<= 180 and 31 <=output[2] and output[2]<= 45:
    return 2
  elif 211 <=output[0] and output[0]<= 255 and 91 <=output[1] and output[1]<= 180 and 46 <=output[2] and output[2]<= 60:
    return 2
  elif 196 <=output[0] and output[0]<= 255 and 91 <=output[1] and output[1]<= 120 and 61 <=output[2] and output[2]<= 75:
    return 2
  elif 211 <=output[0] and output[0]<= 255 and 136 <=output[1] and output[1]<= 180 and 61 <=output[2] and output[2]<= 75:
    return 2
  elif 196 <=output[0] and output[0]<= 255 and 106 <=output[1] and output[1]<= 165 and 76 <=output[2] and output[2]<= 90:
    return 2
  elif 211 <=output[0] and output[0]<= 255 and 166 <=output[1] and output[1]<= 195 and 76 <=output[2] and output[2]<= 105:
    return 2
  elif 196 <=output[0] and output[0]<= 255 and 151 <=output[1] and output[1]<= 165 and 91 <=output[2] and output[2]<= 105:
    return 2
  elif 196 <=output[0] and output[0]<= 255 and 136 <=output[1] and output[1]<= 180 and 106 <=output[2] and output[2]<= 120:
    return 2
  elif 211 <=output[0] and output[0]<= 255 and 181 <=output[1] and output[1]<= 195 and 106 <=output[2] and output[2]<= 120:
    return 2
  elif 196 <=output[0] and output[0]<= 255 and 151 <=output[1] and output[1]<= 165 and 121 <=output[2] and output[2]<= 135:
    return 2
  elif 211 <=output[0] and output[0]<= 255 and 166 <=output[1] and output[1]<= 195 and 121 <=output[2] and output[2]<= 135:
    return 2
  elif 226 <=output[0] and output[0]<= 255 and 151 <=output[1] and output[1]<= 195 and 136 <=output[2] and output[2]<= 150:
    return 2
  elif 241 <=output[0] and output[0]<= 255 and 196 <=output[1] and output[1]<= 210 and 136 <=output[2] and output[2]<= 150:
    return 2
  elif 211 <=output[0] and output[0]<= 255 and 151 <=output[1] and output[1]<= 195 and 151 <=output[2] and output[2]<= 165:
    return 2
  elif 211 <=output[0] and output[0]<= 255 and 181 <=output[1] and output[1]<= 195 and 166 <=output[2] and output[2]<= 180:
    return 2
  elif 241 <=output[0] and output[0]<= 255 and 211 <=output[1] and output[1]<= 225 and 166 <=output[2] and output[2]<= 180:
    return 2
  elif 226 <=output[0] and output[0]<= 255 and 196 <=output[1] and output[1]<= 210 and 151 <=output[2] and output[2]<= 195:
    return 2
  elif 181 <=output[0] and output[0]<= 195 and 136 <=output[1] and output[1]<= 240 and 0 <=output[2] and output[2]<= 15:
    return 3
  elif 196 <=output[0] and output[0]<= 210 and 151 <=output[1] and output[1]<= 180 and 0 <=output[2] and output[2]<= 15:
    return 3
  elif 211 <=output[0] and output[0]<= 225 and 166 <=output[1] and output[1]<= 180 and 0 <=output[2] and output[2]<= 15:
    return 3
  elif 196 <=output[0] and output[0]<= 255 and 181 <=output[1] and output[1]<= 255 and 0 <=output[2] and output[2]<= 15:
    return 3
  elif 181 <=output[0] and output[0]<= 210 and 151 <=output[1] and output[1]<= 240 and 16 <=output[2] and output[2]<= 30:
    return 3
  elif 211 <=output[0] and output[0]<= 255 and 166 <=output[1] and output[1]<= 255 and 16 <=output[2] and output[2]<= 30:
    return 3
  elif 211 <=output[0] and output[0]<= 255 and 181 <=output[1] and output[1]<= 255 and 31 <=output[2] and output[2]<= 60:
    return 3
  elif 211 <=output[0] and output[0]<= 255 and 181 <=output[1] and output[1]<= 210 and 61 <=output[2] and output[2]<= 75:
    return 3
  elif 226 <=output[0] and output[0]<= 255 and 211 <=output[1] and output[1]<= 255 and 61 <=output[2] and output[2]<= 75:
    return 3
  elif 211 <=output[0] and output[0]<= 255 and 196 <=output[1] and output[1]<= 255 and 76 <=output[2] and output[2]<= 90:
    return 3
  elif 211 <=output[0] and output[0]<= 255 and 196 <=output[1] and output[1]<= 255 and 91 <=output[2] and output[2]<= 135:
    return 3
  elif 211 <=output[0] and output[0]<= 255 and 211 <=output[1] and output[1]<= 225 and 136 <=output[2] and output[2]<= 150:
    return 3
  elif 226 <=output[0] and output[0]<= 255 and 226 <=output[1] and output[1]<= 255 and 136 <=output[2] and output[2]<= 150:
    return 3
  elif 226 <=output[0] and output[0]<= 255 and 211 <=output[1] and output[1]<= 255 and 151 <=output[2] and output[2]<= 165:
    return 3
  elif 226 <=output[0] and output[0]<= 255 and 226 <=output[1] and output[1]<= 255 and 166 <=output[2] and output[2]<= 195:
    return 3
  elif 0 <=output[0] and output[0]<= 45 and 181 <=output[1] and output[1]<= 255 and 0 <=output[2] and output[2]<= 15:
    return 4
  elif 46 <=output[0] and output[0]<= 60 and 196 <=output[1] and output[1]<= 255 and 0 <=output[2] and output[2]<= 15:
    return 4
  elif 0 <=output[0] and output[0]<= 60 and 181 <=output[1] and output[1]<= 210 and 16 <=output[2] and output[2]<= 30:
    return 4
  elif 0 <=output[0] and output[0]<= 165 and 211 <=output[1] and output[1]<= 225 and 16 <=output[2] and output[2]<= 30:
    return 4
  elif 0 <=output[0] and output[0]<= 180 and 226 <=output[1] and output[1]<= 240 and 16 <=output[2] and output[2]<= 30:
    return 4
  elif 0 <=output[0] and output[0]<= 210 and 241 <=output[1] and output[1]<= 255 and 16 <=output[2] and output[2]<= 30:
    return 4
  elif 106 <=output[0] and output[0]<= 150 and 166 <=output[1] and output[1]<= 180 and 31 <=output[2] and output[2]<= 60:
    return 4
  elif 61 <=output[0] and output[0]<= 165 and 181 <=output[1] and output[1]<= 195 and 31 <=output[2] and output[2]<= 45:
    return 4
  elif 76 <=output[0] and output[0]<= 165 and 181 <=output[1] and output[1]<= 195 and 46 <=output[2] and output[2]<= 60:
    return 4
  elif 91 <=output[0] and output[0]<= 165 and 166 <=output[1] and output[1]<= 180 and 61 <=output[2] and output[2]<= 75:
    return 4
  elif 0 <=output[0] and output[0]<= 165 and 181 <=output[1] and output[1]<= 195 and 61 <=output[2] and output[2]<= 75:
    return 4
  elif 0 <=output[0] and output[0]<= 195 and 196 <=output[1] and output[1]<= 225 and 61 <=output[2] and output[2]<= 75:
    return 4
  elif 0 <=output[0] and output[0]<= 225 and 226 <=output[1] and output[1]<= 255 and 61 <=output[2] and output[2]<= 75:
    return 4
  elif 106 <=output[0] and output[0]<= 180 and 181 <=output[1] and output[1]<= 195 and 76 <=output[2] and output[2]<= 105:
    return 4
  elif 61 <=output[0] and output[0]<= 195 and 196 <=output[1] and output[1]<= 210 and 76 <=output[2] and output[2]<= 90:
    return 4
  elif 0 <=output[0] and output[0]<= 210 and 211 <=output[1] and output[1]<= 255 and 76 <=output[2] and output[2]<= 90:
    return 4
  elif 0 <=output[0] and output[0]<= 180 and 196 <=output[1] and output[1]<= 255 and 91 <=output[2] and output[2]<= 105:
    return 4
  elif 121 <=output[0] and output[0]<= 165 and 181 <=output[1] and output[1]<= 195 and 106 <=output[2] and output[2]<= 120:
    return 4
  elif 121 <=output[0] and output[0]<= 210 and 196 <=output[1] and output[1]<= 210 and 106 <=output[2] and output[2]<= 120:
    return 4
  elif 91 <=output[0] and output[0]<= 210 and 211 <=output[1] and output[1]<= 225 and 106 <=output[2] and output[2]<= 120:
    return 4
  elif 0 <=output[0] and output[0]<= 210 and 226 <=output[1] and output[1]<= 255 and 106 <=output[2] and output[2]<= 120:
    return 4
  elif 106 <=output[0] and output[0]<= 150 and 166 <=output[1] and output[1]<= 180 and 121 <=output[2] and output[2]<= 135:
    return 4
  elif 106 <=output[0] and output[0]<= 165 and 181 <=output[1] and output[1]<= 195 and 121 <=output[2] and output[2]<= 135:
    return 4
  elif 0 <=output[0] and output[0]<= 210 and 196 <=output[1] and output[1]<= 255 and 121 <=output[2] and output[2]<= 135:
    return 4
  elif 166 <=output[0] and output[0]<= 180 and 181 <=output[1] and output[1]<= 195 and 136 <=output[2] and output[2]<= 150:
    return 4
  elif 166 <=output[0] and output[0]<= 195 and 196 <=output[1] and output[1]<= 210 and 136 <=output[2] and output[2]<= 150:
    return 4
  elif 151 <=output[0] and output[0]<= 210 and 211 <=output[1] and output[1]<= 225 and 136 <=output[2] and output[2]<= 150:
    return 4
  elif 136 <=output[0] and output[0]<= 225 and 226 <=output[1] and output[1]<= 255 and 136 <=output[2] and output[2]<= 150:
    return 4
  elif 136 <=output[0] and output[0]<= 180 and 196 <=output[1] and output[1]<= 210 and 151 <=output[2] and output[2]<= 165:
    return 4
  elif 136 <=output[0] and output[0]<= 225 and 211 <=output[1] and output[1]<= 240 and 151 <=output[2] and output[2]<= 165:
    return 4
  elif 121 <=output[0] and output[0]<= 225 and 241 <=output[1] and output[1]<= 255 and 151 <=output[2] and output[2]<= 165:
    return 4
  elif 151 <=output[0] and output[0]<= 210 and 211 <=output[1] and output[1]<= 225 and 166 <=output[2] and output[2]<= 195:
    return 4
  elif 136 <=output[0] and output[0]<= 225 and 226 <=output[1] and output[1]<= 255 and 166 <=output[2] and output[2]<= 180:
    return 4
  elif 151 <=output[0] and output[0]<= 225 and 226 <=output[1] and output[1]<= 255 and 181 <=output[2] and output[2]<= 210:
    return 4
  elif 181 <=output[0] and output[0]<= 210 and 211 <=output[1] and output[1]<= 225 and 196 <=output[2] and output[2]<= 210:
    return 4
  elif 181 <=output[0] and output[0]<= 210 and 226 <=output[1] and output[1]<= 240 and 211 <=output[2] and output[2]<= 225:
    return 4
  elif 166 <=output[0] and output[0]<= 210 and 241 <=output[1] and output[1]<= 255 and 211 <=output[2] and output[2]<= 225:
    return 4
  elif 0 <=output[0] and output[0]<= 15 and 16 <=output[1] and output[1]<= 180 and 0 <=output[2] and output[2]<= 15:
    return 5
  elif 16 <=output[0] and output[0]<= 30 and 31 <=output[1] and output[1]<= 180 and 0 <=output[2] and output[2]<= 15:
    return 5
  elif 31 <=output[0] and output[0]<= 45 and 46 <=output[1] and output[1]<= 180 and 0 <=output[2] and output[2]<= 15:
    return 5
  elif 46 <=output[0] and output[0]<= 60 and 61 <=output[1] and output[1]<= 195 and 0 <=output[2] and output[2]<= 15:
    return 5
  elif 61 <=output[0] and output[0]<= 75 and 91 <=output[1] and output[1]<= 180 and 0 <=output[2] and output[2]<= 15:
    return 5
  elif 76 <=output[0] and output[0]<= 90 and 106 <=output[1] and output[1]<= 180 and 0 <=output[2] and output[2]<= 15:
    return 5
  elif 91 <=output[0] and output[0]<= 105 and 121 <=output[1] and output[1]<= 180 and 0 <=output[2] and output[2]<= 15:
    return 5
  elif 106 <=output[0] and output[0]<= 120 and 151 <=output[1] and output[1]<= 180 and 0 <=output[2] and output[2]<= 15:
    return 5
  elif 121 <=output[0] and output[0]<= 135 and 166 <=output[1] and output[1]<= 180 and 0 <=output[2] and output[2]<= 15:
    return 5
  elif 61 <=output[0] and output[0]<= 180 and 181 <=output[1] and output[1]<= 255 and 0 <=output[2] and output[2]<= 15:
    return 5
  elif 181 <=output[0] and output[0]<= 195 and 241 <=output[1] and output[1]<= 255 and 0 <=output[2] and output[2]<= 15:
    return 5
  elif 0 <=output[0] and output[0]<= 45 and 31 <=output[1] and output[1]<= 180 and 16 <=output[2] and output[2]<= 30:
    return 5
  elif 46 <=output[0] and output[0]<= 60 and 46 <=output[1] and output[1]<= 180 and 16 <=output[2] and output[2]<= 30:
    return 5
  elif 61 <=output[0] and output[0]<= 90 and 61 <=output[1] and output[1]<= 210 and 16 <=output[2] and output[2]<= 30:
    return 5
  elif 91 <=output[0] and output[0]<= 120 and 91 <=output[1] and output[1]<= 210 and 16 <=output[2] and output[2]<= 30:
    return 5
  elif 121 <=output[0] and output[0]<= 150 and 106 <=output[1] and output[1]<= 210 and 16 <=output[2] and output[2]<= 30:
    return 5
  elif 151 <=output[0] and output[0]<= 165 and 121 <=output[1] and output[1]<= 210 and 16 <=output[2] and output[2]<= 30:
    return 5
  elif 166 <=output[0] and output[0]<= 180 and 136 <=output[1] and output[1]<= 225 and 16 <=output[2] and output[2]<= 30:
    return 5
  elif 0 <=output[0] and output[0]<= 15 and 31 <=output[1] and output[1]<= 45 and 31 <=output[2] and output[2]<= 45:
    return 5
  elif 0 <=output[0] and output[0]<= 45 and 46 <=output[1] and output[1]<= 60 and 31 <=output[2] and output[2]<= 45:
    return 5
  elif 0 <=output[0] and output[0]<= 60 and 61 <=output[1] and output[1]<= 90 and 31 <=output[2] and output[2]<= 45:
    return 5
  elif 0 <=output[0] and output[0]<= 75 and 91 <=output[1] and output[1]<= 105 and 31 <=output[2] and output[2]<= 45:
    return 5
  elif 0 <=output[0] and output[0]<= 90 and 106 <=output[1] and output[1]<= 135 and 31 <=output[2] and output[2]<= 45:
    return 5
  elif 0 <=output[0] and output[0]<= 105 and 136 <=output[1] and output[1]<= 150 and 31 <=output[2] and output[2]<= 45:
    return 5
  elif 0 <=output[0] and output[0]<= 135 and 151 <=output[1] and output[1]<= 165 and 31 <=output[2] and output[2]<= 75:
    return 5
  elif 0 <=output[0] and output[0]<= 105 and 166 <=output[1] and output[1]<= 180 and 31 <=output[2] and output[2]<= 60:
    return 5
  elif 0 <=output[0] and output[0]<= 60 and 181 <=output[1] and output[1]<= 195 and 31 <=output[2] and output[2]<= 45:
    return 5
  elif 0 <=output[0] and output[0]<= 60 and 46 <=output[1] and output[1]<= 60 and 46 <=output[2] and output[2]<= 60:
    return 5
  elif 0 <=output[0] and output[0]<= 75 and 61 <=output[1] and output[1]<= 75 and 46 <=output[2] and output[2]<= 60:
    return 5
  elif 0 <=output[0] and output[0]<= 90 and 76 <=output[1] and output[1]<= 120 and 46 <=output[2] and output[2]<= 60:
    return 5
  elif 0 <=output[0] and output[0]<= 120 and 121 <=output[1] and output[1]<= 150 and 46 <=output[2] and output[2]<= 75:
    return 5
  elif 0 <=output[0] and output[0]<= 75 and 181 <=output[1] and output[1]<= 195 and 46 <=output[2] and output[2]<= 60:
    return 5
  elif 0 <=output[0] and output[0]<= 60 and 61 <=output[1] and output[1]<= 75 and 61 <=output[2] and output[2]<= 75:
    return 5
  elif 0 <=output[0] and output[0]<= 90 and 76 <=output[1] and output[1]<= 105 and 61 <=output[2] and output[2]<= 75:
    return 5
  elif 0 <=output[0] and output[0]<= 105 and 106 <=output[1] and output[1]<= 120 and 61 <=output[2] and output[2]<= 75:
    return 5
  elif 0 <=output[0] and output[0]<= 90 and 166 <=output[1] and output[1]<= 180 and 61 <=output[2] and output[2]<= 75:
    return 5
  elif 0 <=output[0] and output[0]<= 60 and 76 <=output[1] and output[1]<= 90 and 76 <=output[2] and output[2]<= 90:
    return 5
  elif 0 <=output[0] and output[0]<= 90 and 91 <=output[1] and output[1]<= 105 and 76 <=output[2] and output[2]<= 90:
    return 5
  elif 0 <=output[0] and output[0]<= 120 and 106 <=output[1] and output[1]<= 120 and 76 <=output[2] and output[2]<= 90:
    return 5
  elif 0 <=output[0] and output[0]<= 135 and 121 <=output[1] and output[1]<= 135 and 76 <=output[2] and output[2]<= 90:
    return 5
  elif 0 <=output[0] and output[0]<= 150 and 136 <=output[1] and output[1]<= 150 and 76 <=output[2] and output[2]<= 90:
    return 5
  elif 0 <=output[0] and output[0]<= 165 and 151 <=output[1] and output[1]<= 180 and 76 <=output[2] and output[2]<= 90:
    return 5
  elif 0 <=output[0] and output[0]<= 105 and 181 <=output[1] and output[1]<= 195 and 76 <=output[2] and output[2]<= 105:
    return 5
  elif 0 <=output[0] and output[0]<= 60 and 196 <=output[1] and output[1]<= 210 and 76 <=output[2] and output[2]<= 90:
    return 5
  elif 0 <=output[0] and output[0]<= 75 and 91 <=output[1] and output[1]<= 105 and 91 <=output[2] and output[2]<= 105:
    return 5
  elif 0 <=output[0] and output[0]<= 105 and 106 <=output[1] and output[1]<= 135 and 91 <=output[2] and output[2]<= 105:
    return 5
  elif 0 <=output[0] and output[0]<= 120 and 136 <=output[1] and output[1]<= 150 and 91 <=output[2] and output[2]<= 105:
    return 5
  elif 0 <=output[0] and output[0]<= 135 and 151 <=output[1] and output[1]<= 165 and 91 <=output[2] and output[2]<= 105:
    return 5
  elif 0 <=output[0] and output[0]<= 150 and 166 <=output[1] and output[1]<= 180 and 91 <=output[2] and output[2]<= 105:
    return 5
  elif 0 <=output[0] and output[0]<= 75 and 106 <=output[1] and output[1]<= 120 and 106 <=output[2] and output[2]<= 120:
    return 5
  elif 0 <=output[0] and output[0]<= 90 and 121 <=output[1] and output[1]<= 135 and 106 <=output[2] and output[2]<= 120:
    return 5
  elif 0 <=output[0] and output[0]<= 105 and 136 <=output[1] and output[1]<= 150 and 106 <=output[2] and output[2]<= 120:
    return 5
  elif 0 <=output[0] and output[0]<= 135 and 151 <=output[1] and output[1]<= 180 and 106 <=output[2] and output[2]<= 120:
    return 5
  elif 0 <=output[0] and output[0]<= 120 and 181 <=output[1] and output[1]<= 210 and 106 <=output[2] and output[2]<= 120:
    return 5
  elif 0 <=output[0] and output[0]<= 90 and 211 <=output[1] and output[1]<= 225 and 106 <=output[2] and output[2]<= 120:
    return 5
  elif 0 <=output[0] and output[0]<= 90 and 106 <=output[1] and output[1]<= 135 and 121 <=output[2] and output[2]<= 135:
    return 5
  elif 0 <=output[0] and output[0]<= 105 and 136 <=output[1] and output[1]<= 195 and 121 <=output[2] and output[2]<= 135:
    return 5
  elif 0 <=output[0] and output[0]<= 105 and 136 <=output[1] and output[1]<= 150 and 136 <=output[2] and output[2]<= 150:
    return 5
  elif 0 <=output[0] and output[0]<= 150 and 151 <=output[1] and output[1]<= 165 and 136 <=output[2] and output[2]<= 150:
    return 5
  elif 0 <=output[0] and output[0]<= 165 and 166 <=output[1] and output[1]<= 210 and 136 <=output[2] and output[2]<= 150:
    return 5
  elif 0 <=output[0] and output[0]<= 150 and 211 <=output[1] and output[1]<= 255 and 136 <=output[2] and output[2]<= 150:
    return 5
  elif 0 <=output[0] and output[0]<= 135 and 226 <=output[1] and output[1]<= 255 and 136 <=output[2] and output[2]<= 150:
    return 5
  elif 0 <=output[0] and output[0]<= 120 and 151 <=output[1] and output[1]<= 165 and 151 <=output[2] and output[2]<= 165:
    return 5
  elif 0 <=output[0] and output[0]<= 165 and 166 <=output[1] and output[1]<= 180 and 151 <=output[2] and output[2]<= 165:
    return 5
  elif 0 <=output[0] and output[0]<= 180 and 181 <=output[1] and output[1]<= 195 and 151 <=output[2] and output[2]<= 180:
    return 5
  elif 0 <=output[0] and output[0]<= 135 and 196 <=output[1] and output[1]<= 240 and 151 <=output[2] and output[2]<= 165:
    return 5
  elif 0 <=output[0] and output[0]<= 120 and 241 <=output[1] and output[1]<= 255 and 151 <=output[2] and output[2]<= 165:
    return 5
  elif 0 <=output[0] and output[0]<= 150 and 166 <=output[1] and output[1]<= 180 and 166 <=output[2] and output[2]<= 180:
    return 5
  elif 0 <=output[0] and output[0]<= 195 and 196 <=output[1] and output[1]<= 210 and 166 <=output[2] and output[2]<= 195:
    return 5
  elif 0 <=output[0] and output[0]<= 150 and 211 <=output[1] and output[1]<= 225 and 166 <=output[2] and output[2]<= 195:
    return 5
  elif 0 <=output[0] and output[0]<= 135 and 226 <=output[1] and output[1]<= 255 and 166 <=output[2] and output[2]<= 180:
    return 5
  elif 0 <=output[0] and output[0]<= 180 and 211 <=output[1] and output[1]<= 225 and 196 <=output[2] and output[2]<= 210:
    return 5
  elif 0 <=output[0] and output[0]<= 150 and 226 <=output[1] and output[1]<= 255 and 196 <=output[2] and output[2]<= 210:
    return 5
  elif 31 <=output[0] and output[0]<= 45 and 31 <=output[1] and output[1]<= 45 and 0 <=output[2] and output[2]<= 15:
    return 6
  elif 46 <=output[0] and output[0]<= 60 and 46 <=output[1] and output[1]<= 60 and 0 <=output[2] and output[2]<= 15:
    return 6
  elif 61 <=output[0] and output[0]<= 75 and 46 <=output[1] and output[1]<= 90 and 0 <=output[2] and output[2]<= 15:
    return 6
  elif 76 <=output[0] and output[0]<= 90 and 61 <=output[1] and output[1]<= 105 and 0 <=output[2] and output[2]<= 15:
    return 6
  elif 91 <=output[0] and output[0]<= 105 and 76 <=output[1] and output[1]<= 120 and 0 <=output[2] and output[2]<= 15:
    return 6
  elif 106 <=output[0] and output[0]<= 120 and 91 <=output[1] and output[1]<= 150 and 0 <=output[2] and output[2]<= 15:
    return 6
  elif 121 <=output[0] and output[0]<= 135 and 91 <=output[1] and output[1]<= 165 and 0 <=output[2] and output[2]<= 15:
    return 6
  elif 136 <=output[0] and output[0]<= 150 and 106 <=output[1] and output[1]<= 180 and 0 <=output[2] and output[2]<= 15:
    return 6
  elif 151 <=output[0] and output[0]<= 165 and 121 <=output[1] and output[1]<= 180 and 0 <=output[2] and output[2]<= 15:
    return 6
  elif 166 <=output[0] and output[0]<= 180 and 136 <=output[1] and output[1]<= 180 and 0 <=output[2] and output[2]<= 15:
    return 6
  elif 46 <=output[0] and output[0]<= 60 and 46 <=output[1] and output[1]<= 60 and 31 <=output[2] and output[2]<= 45:
    return 6
  elif 61 <=output[0] and output[0]<= 90 and 61 <=output[1] and output[1]<= 75 and 31 <=output[2] and output[2]<= 45:
    return 6
  elif 166 <=output[0] and output[0]<= 210 and 181 <=output[1] and output[1]<= 195 and 31 <=output[2] and output[2]<= 45:
    return 6
  elif 76 <=output[0] and output[0]<= 135 and 91 <=output[1] and output[1]<= 105 and 31 <=output[2] and output[2]<= 45:
    return 6
  elif 61 <=output[0] and output[0]<= 105 and 76 <=output[1] and output[1]<= 90 and 31 <=output[2] and output[2]<= 45:
    return 6
  elif 91 <=output[0] and output[0]<= 150 and 106 <=output[1] and output[1]<= 120 and 31 <=output[2] and output[2]<= 60:
    return 6
  elif 91 <=output[0] and output[0]<= 165 and 121 <=output[1] and output[1]<= 135 and 31 <=output[2] and output[2]<= 45:
    return 6
  elif 106 <=output[0] and output[0]<= 210 and 136 <=output[1] and output[1]<= 150 and 31 <=output[2] and output[2]<= 45:
    return 6
  elif 136 <=output[0] and output[0]<= 210 and 151 <=output[1] and output[1]<= 165 and 31 <=output[2] and output[2]<= 75:
    return 6
  elif 151 <=output[0] and output[0]<= 210 and 166 <=output[1] and output[1]<= 180 and 31 <=output[2] and output[2]<= 60:
    return 6
  elif 91 <=output[0] and output[0]<= 120 and 76 <=output[1] and output[1]<= 90 and 46 <=output[2] and output[2]<= 60:
    return 6
  elif 91 <=output[0] and output[0]<= 135 and 91 <=output[1] and output[1]<= 105 and 46 <=output[2] and output[2]<= 75:
    return 6
  elif 121 <=output[0] and output[0]<= 165 and 121 <=output[1] and output[1]<= 135 and 46 <=output[2] and output[2]<= 60:
    return 6
  elif 121 <=output[0] and output[0]<= 210 and 136 <=output[1] and output[1]<= 150 and 46 <=output[2] and output[2]<= 75:
    return 6
  elif 166 <=output[0] and output[0]<= 210 and 181 <=output[1] and output[1]<= 195 and 46 <=output[2] and output[2]<= 60:
    return 6
  elif 106 <=output[0] and output[0]<= 165 and 106 <=output[1] and output[1]<= 120 and 61 <=output[2] and output[2]<= 75:
    return 6
  elif 121 <=output[0] and output[0]<= 180 and 121 <=output[1] and output[1]<= 135 and 61 <=output[2] and output[2]<= 75:
    return 6
  elif 166 <=output[0] and output[0]<= 210 and 166 <=output[1] and output[1]<= 195 and 61 <=output[2] and output[2]<= 75:
    return 6
  elif 196 <=output[0] and output[0]<= 210 and 196 <=output[1] and output[1]<= 210 and 61 <=output[2] and output[2]<= 90:
    return 6
  elif 196 <=output[0] and output[0]<= 225 and 211 <=output[1] and output[1]<= 225 and 61 <=output[2] and output[2]<= 75:
    return 6
  elif 121 <=output[0] and output[0]<= 135 and 106 <=output[1] and output[1]<= 120 and 76 <=output[2] and output[2]<= 90:
    return 6
  elif 136 <=output[0] and output[0]<= 165 and 121 <=output[1] and output[1]<= 135 and 76 <=output[2] and output[2]<= 90:
    return 6
  elif 151 <=output[0] and output[0]<= 165 and 136 <=output[1] and output[1]<= 150 and 76 <=output[2] and output[2]<= 90:
    return 6
  elif 166 <=output[0] and output[0]<= 195 and 151 <=output[1] and output[1]<= 165 and 76 <=output[2] and output[2]<= 90:
    return 6
  elif 166 <=output[0] and output[0]<= 210 and 166 <=output[1] and output[1]<= 180 and 76 <=output[2] and output[2]<= 90:
    return 6
  elif 181 <=output[0] and output[0]<= 210 and 181 <=output[1] and output[1]<= 195 and 76 <=output[2] and output[2]<= 90:
    return 6
  elif 106 <=output[0] and output[0]<= 120 and 106 <=output[1] and output[1]<= 120 and 91 <=output[2] and output[2]<= 105:
    return 6
  elif 106 <=output[0] and output[0]<= 135 and 121 <=output[1] and output[1]<= 135 and 91 <=output[2] and output[2]<= 105:
    return 6
  elif 121 <=output[0] and output[0]<= 180 and 136 <=output[1] and output[1]<= 150 and 91 <=output[2] and output[2]<= 105:
    return 6
  elif 136 <=output[0] and output[0]<= 195 and 151 <=output[1] and output[1]<= 165 and 91 <=output[2] and output[2]<= 105:
    return 6
  elif 151 <=output[0] and output[0]<= 210 and 166 <=output[1] and output[1]<= 180 and 91 <=output[2] and output[2]<= 105:
    return 6
  elif 181 <=output[0] and output[0]<= 210 and 181 <=output[1] and output[1]<= 255 and 91 <=output[2] and output[2]<= 105:
    return 6
  elif 106 <=output[0] and output[0]<= 165 and 136 <=output[1] and output[1]<= 150 and 106 <=output[2] and output[2]<= 120:
    return 6
  elif 136 <=output[0] and output[0]<= 195 and 151 <=output[1] and output[1]<= 180 and 106 <=output[2] and output[2]<= 120:
    return 6
  elif 166 <=output[0] and output[0]<= 210 and 181 <=output[1] and output[1]<= 195 and 106 <=output[2] and output[2]<= 135:
    return 6
  elif 106 <=output[0] and output[0]<= 195 and 151 <=output[1] and output[1]<= 165 and 121 <=output[2] and output[2]<= 135:
    return 6
  elif 151 <=output[0] and output[0]<= 210 and 166 <=output[1] and output[1]<= 180 and 121 <=output[2] and output[2]<= 135:
    return 6
  elif 151 <=output[0] and output[0]<= 165 and 151 <=output[1] and output[1]<= 165 and 136 <=output[2] and output[2]<= 150:
    return 6
  elif 166 <=output[0] and output[0]<= 180 and 166 <=output[1] and output[1]<= 180 and 136 <=output[2] and output[2]<= 165:
    return 6
  elif 181 <=output[0] and output[0]<= 210 and 181 <=output[1] and output[1]<= 195 and 136 <=output[2] and output[2]<= 150:
    return 6
  elif 196 <=output[0] and output[0]<= 210 and 196 <=output[1] and output[1]<= 210 and 136 <=output[2] and output[2]<= 150:
    return 6
  elif 166 <=output[0] and output[0]<= 195 and 166 <=output[1] and output[1]<= 180 and 151 <=output[2] and output[2]<= 165:
    return 6
  elif 181 <=output[0] and output[0]<= 210 and 181 <=output[1] and output[1]<= 210 and 151 <=output[2] and output[2]<= 165:
    return 6
  elif 181 <=output[0] and output[0]<= 195 and 181 <=output[1] and output[1]<= 195 and 166 <=output[2] and output[2]<= 180:
    return 6
  elif 196 <=output[0] and output[0]<= 210 and 196 <=output[1] and output[1]<= 210 and 166 <=output[2] and output[2]<= 180:
    return 6
  elif 211 <=output[0] and output[0]<= 225 and 211 <=output[1] and output[1]<= 225 and 166 <=output[2] and output[2]<= 195:
    return 6
  elif 196 <=output[0] and output[0]<= 210 and 196 <=output[1] and output[1]<= 210 and 181 <=output[2] and output[2]<= 195:
    return 6
  elif 16 <=output[0] and output[0]<= 60 and 16 <=output[1] and output[1]<= 30 and 0 <=output[2] and output[2]<= 15:
    return 7
  elif 46 <=output[0] and output[0]<= 120 and 31 <=output[1] and output[1]<= 45 and 0 <=output[2] and output[2]<= 15:
    return 7
  elif 76 <=output[0] and output[0]<= 180 and 46 <=output[1] and output[1]<= 60 and 0 <=output[2] and output[2]<= 15:
    return 7
  elif 91 <=output[0] and output[0]<= 180 and 61 <=output[1] and output[1]<= 75 and 0 <=output[2] and output[2]<= 15:
    return 7
  elif 106 <=output[0] and output[0]<= 180 and 76 <=output[1] and output[1]<= 90 and 0 <=output[2] and output[2]<= 15:
    return 7
  elif 136 <=output[0] and output[0]<= 180 and 91 <=output[1] and output[1]<= 105 and 0 <=output[2] and output[2]<= 15:
    return 7
  elif 151 <=output[0] and output[0]<= 180 and 106 <=output[1] and output[1]<= 120 and 0 <=output[2] and output[2]<= 15:
    return 7
  elif 166 <=output[0] and output[0]<= 180 and 121 <=output[1] and output[1]<= 135 and 0 <=output[2] and output[2]<= 15:
    return 7
  elif 46 <=output[0] and output[0]<= 90 and 31 <=output[1] and output[1]<= 45 and 16 <=output[2] and output[2]<= 30:
    return 7
  elif 61 <=output[0] and output[0]<= 135 and 46 <=output[1] and output[1]<= 60 and 16 <=output[2] and output[2]<= 30:
    return 7
  elif 91 <=output[0] and output[0]<= 180 and 61 <=output[1] and output[1]<= 90 and 16 <=output[2] and output[2]<= 30:
    return 7
  elif 121 <=output[0] and output[0]<= 180 and 91 <=output[1] and output[1]<= 105 and 16 <=output[2] and output[2]<= 30:
    return 7
  elif 151 <=output[0] and output[0]<= 180 and 106 <=output[1] and output[1]<= 120 and 16 <=output[2] and output[2]<= 30:
    return 7
  elif 166 <=output[0] and output[0]<= 180 and 121 <=output[1] and output[1]<= 135 and 16 <=output[2] and output[2]<= 30:
    return 7
  elif 151 <=output[0] and output[0]<= 195 and 106 <=output[1] and output[1]<= 120 and 31 <=output[2] and output[2]<= 45:
    return 7
  elif 76 <=output[0] and output[0]<= 90 and 0 <=output[1] and output[1]<= 15 and 31 <=output[2] and output[2]<= 45:
    return 7
  elif 61 <=output[0] and output[0]<= 105 and 16 <=output[1] and output[1]<= 30 and 31 <=output[2] and output[2]<= 45:
    return 7
  elif 46 <=output[0] and output[0]<= 135 and 31 <=output[1] and output[1]<= 45 and 31 <=output[2] and output[2]<= 45:
    return 7
  elif 61 <=output[0] and output[0]<= 165 and 46 <=output[1] and output[1]<= 60 and 31 <=output[2] and output[2]<= 45:
    return 7
  elif 91 <=output[0] and output[0]<= 165 and 61 <=output[1] and output[1]<= 75 and 31 <=output[2] and output[2]<= 45:
    return 7
  elif 106 <=output[0] and output[0]<= 165 and 76 <=output[1] and output[1]<= 90 and 31 <=output[2] and output[2]<= 45:
    return 7
  elif 136 <=output[0] and output[0]<= 180 and 91 <=output[1] and output[1]<= 105 and 31 <=output[2] and output[2]<= 45:
    return 7
  elif 166 <=output[0] and output[0]<= 195 and 121 <=output[1] and output[1]<= 135 and 31 <=output[2] and output[2]<= 45:
    return 7
  elif 76 <=output[0] and output[0]<= 150 and 31 <=output[1] and output[1]<= 45 and 46 <=output[2] and output[2]<= 60:
    return 7
  elif 61 <=output[0] and output[0]<= 195 and 46 <=output[1] and output[1]<= 60 and 46 <=output[2] and output[2]<= 60:
    return 7
  elif 76 <=output[0] and output[0]<= 210 and 61 <=output[1] and output[1]<= 75 and 46 <=output[2] and output[2]<= 60:
    return 7
  elif 121 <=output[0] and output[0]<= 210 and 76 <=output[1] and output[1]<= 90 and 46 <=output[2] and output[2]<= 60:
    return 7
  elif 136 <=output[0] and output[0]<= 210 and 91 <=output[1] and output[1]<= 105 and 46 <=output[2] and output[2]<= 60:
    return 7
  elif 151 <=output[0] and output[0]<= 210 and 106 <=output[1] and output[1]<= 120 and 46 <=output[2] and output[2]<= 60:
    return 7
  elif 166 <=output[0] and output[0]<= 210 and 121 <=output[1] and output[1]<= 135 and 46 <=output[2] and output[2]<= 60:
    return 7
  elif 61 <=output[0] and output[0]<= 180 and 61 <=output[1] and output[1]<= 75 and 61 <=output[2] and output[2]<= 75:
    return 7
  elif 91 <=output[0] and output[0]<= 195 and 76 <=output[1] and output[1]<= 90 and 61 <=output[2] and output[2]<= 75:
    return 7
  elif 136 <=output[0] and output[0]<= 195 and 91 <=output[1] and output[1]<= 105 and 61 <=output[2] and output[2]<= 75:
    return 7
  elif 166 <=output[0] and output[0]<= 195 and 106 <=output[1] and output[1]<= 120 and 61 <=output[2] and output[2]<= 75:
    return 7
  elif 181 <=output[0] and output[0]<= 210 and 121 <=output[1] and output[1]<= 135 and 61 <=output[2] and output[2]<= 75:
    return 7
  elif 136 <=output[0] and output[0]<= 180 and 91 <=output[1] and output[1]<= 105 and 76 <=output[2] and output[2]<= 90:
    return 7
  elif 136 <=output[0] and output[0]<= 195 and 106 <=output[1] and output[1]<= 120 and 76 <=output[2] and output[2]<= 90:
    return 7
  elif 166 <=output[0] and output[0]<= 195 and 121 <=output[1] and output[1]<= 150 and 76 <=output[2] and output[2]<= 90:
    return 7
  elif 106 <=output[0] and output[0]<= 135 and 91 <=output[1] and output[1]<= 105 and 91 <=output[2] and output[2]<= 105:
    return 7
  elif 121 <=output[0] and output[0]<= 180 and 106 <=output[1] and output[1]<= 120 and 91 <=output[2] and output[2]<= 105:
    return 7
  elif 136 <=output[0] and output[0]<= 180 and 121 <=output[1] and output[1]<= 135 and 91 <=output[2] and output[2]<= 105:
    return 7
  elif 166 <=output[0] and output[0]<= 195 and 136 <=output[1] and output[1]<= 150 and 106 <=output[2] and output[2]<= 120:
    return 7
  elif 166 <=output[0] and output[0]<= 195 and 151 <=output[1] and output[1]<= 165 and 136 <=output[2] and output[2]<= 150:
    return 7
  elif 181 <=output[0] and output[0]<= 195 and 166 <=output[1] and output[1]<= 180 and 136 <=output[2] and output[2]<= 150:
    return 7
  elif 166 <=output[0] and output[0]<= 210 and 151 <=output[1] and output[1]<= 165 and 151 <=output[2] and output[2]<= 165:
    return 7
  elif 196 <=output[0] and output[0]<= 210 and 166 <=output[1] and output[1]<= 180 and 151 <=output[2] and output[2]<= 165:
    return 7
  elif 181 <=output[0] and output[0]<= 210 and 166 <=output[1] and output[1]<= 180 and 166 <=output[2] and output[2]<= 180:
    return 7
  elif 196 <=output[0] and output[0]<= 210 and 181 <=output[1] and output[1]<= 195 and 166 <=output[2] and output[2]<= 180:
    return 7
  elif 196 <=output[0] and output[0]<= 210 and 181 <=output[1] and output[1]<= 195 and 181 <=output[2] and output[2]<= 195:
    return 7
  elif 211 <=output[0] and output[0]<= 225 and 196 <=output[1] and output[1]<= 210 and 181 <=output[2] and output[2]<= 195:
    return 7
  elif 211 <=output[0] and output[0]<= 225 and 196 <=output[1] and output[1]<= 210 and 196 <=output[2] and output[2]<= 210:
    return 7
  elif 0 <=output[0] and output[0]<= 15 and 0 <=output[1] and output[1]<= 15 and 0 <=output[2] and output[2]<= 15:
    return 8
  elif 16 <=output[0] and output[0]<= 30 and 16 <=output[1] and output[1]<= 30 and 16 <=output[2] and output[2]<= 30:
    return 9
  elif 16 <=output[0] and output[0]<= 45 and 31 <=output[1] and output[1]<= 45 and 31 <=output[2] and output[2]<= 45:
    return 9
  elif 61 <=output[0] and output[0]<= 105 and 76 <=output[1] and output[1]<= 90 and 76 <=output[2] and output[2]<= 90:
    return 9
  elif 91 <=output[0] and output[0]<= 135 and 91 <=output[1] and output[1]<= 105 and 76 <=output[2] and output[2]<= 90:
    return 9
  elif 76 <=output[0] and output[0]<= 105 and 91 <=output[1] and output[1]<= 105 and 91 <=output[2] and output[2]<= 105:
    return 9
  elif 76 <=output[0] and output[0]<= 120 and 91 <=output[1] and output[1]<= 105 and 106 <=output[2] and output[2]<= 120:
    return 9
  elif 76 <=output[0] and output[0]<= 135 and 106 <=output[1] and output[1]<= 120 and 106 <=output[2] and output[2]<= 120:
    return 9
  elif 91 <=output[0] and output[0]<= 150 and 121 <=output[1] and output[1]<= 135 and 106 <=output[2] and output[2]<= 120:
    return 9
  elif 91 <=output[0] and output[0]<= 150 and 106 <=output[1] and output[1]<= 120 and 121 <=output[2] and output[2]<= 135:
    return 9
  elif 91 <=output[0] and output[0]<= 165 and 121 <=output[1] and output[1]<= 135 and 121 <=output[2] and output[2]<= 135:
    return 9
  elif 106 <=output[0] and output[0]<= 180 and 136 <=output[1] and output[1]<= 150 and 121 <=output[2] and output[2]<= 135:
    return 9
  elif 91 <=output[0] and output[0]<= 120 and 106 <=output[1] and output[1]<= 120 and 136 <=output[2] and output[2]<= 150:
    return 9
  elif 106 <=output[0] and output[0]<= 150 and 121 <=output[1] and output[1]<= 135 and 136 <=output[2] and output[2]<= 150:
    return 9
  elif 106 <=output[0] and output[0]<= 165 and 136 <=output[1] and output[1]<= 150 and 136 <=output[2] and output[2]<= 150:
    return 9
  elif 106 <=output[0] and output[0]<= 120 and 121 <=output[1] and output[1]<= 135 and 151 <=output[2] and output[2]<= 165:
    return 9
  elif 106 <=output[0] and output[0]<= 150 and 136 <=output[1] and output[1]<= 150 and 151 <=output[2] and output[2]<= 165:
    return 9
  elif 121 <=output[0] and output[0]<= 165 and 151 <=output[1] and output[1]<= 165 and 151 <=output[2] and output[2]<= 165:
    return 9
  elif 136 <=output[0] and output[0]<= 165 and 151 <=output[1] and output[1]<= 165 and 166 <=output[2] and output[2]<= 195:
    return 9
  elif 151 <=output[0] and output[0]<= 180 and 166 <=output[1] and output[1]<= 180 and 166 <=output[2] and output[2]<= 180:
    return 9
  elif 136 <=output[0] and output[0]<= 180 and 166 <=output[1] and output[1]<= 180 and 181 <=output[2] and output[2]<= 195:
    return 9
  elif 166 <=output[0] and output[0]<= 195 and 181 <=output[1] and output[1]<= 195 and 181 <=output[2] and output[2]<= 210:
    return 9
  elif 181 <=output[0] and output[0]<= 210 and 196 <=output[1] and output[1]<= 210 and 196 <=output[2] and output[2]<= 225:
    return 9
  elif 181 <=output[0] and output[0]<= 210 and 196 <=output[1] and output[1]<= 210 and 196 <=output[2] and output[2]<= 225:
    return 9
  elif 166 <=output[0] and output[0]<= 255 and 0 <=output[1] and output[1]<= 90 and 76 <=output[2] and output[2]<= 90:
    return 10
  elif 181 <=output[0] and output[0]<= 255 and 91 <=output[1] and output[1]<= 105 and 76 <=output[2] and output[2]<= 90:
    return 10
  elif 166 <=output[0] and output[0]<= 255 and 0 <=output[1] and output[1]<= 30 and 91 <=output[2] and output[2]<= 105:
    return 10
  elif 181 <=output[0] and output[0]<= 255 and 31 <=output[1] and output[1]<= 150 and 91 <=output[2] and output[2]<= 105:
    return 10
  elif 166 <=output[0] and output[0]<= 255 and 0 <=output[1] and output[1]<= 15 and 106 <=output[2] and output[2]<= 120:
    return 10
  elif 181 <=output[0] and output[0]<= 255 and 16 <=output[1] and output[1]<= 135 and 106 <=output[2] and output[2]<= 120:
    return 10
  elif 181 <=output[0] and output[0]<= 255 and 0 <=output[1] and output[1]<= 150 and 121 <=output[2] and output[2]<= 135:
    return 10
  elif 181 <=output[0] and output[0]<= 255 and 0 <=output[1] and output[1]<= 30 and 136 <=output[2] and output[2]<= 150:
    return 10
  elif 196 <=output[0] and output[0]<= 255 and 31 <=output[1] and output[1]<= 90 and 136 <=output[2] and output[2]<= 150:
    return 10
  elif 181 <=output[0] and output[0]<= 255 and 91 <=output[1] and output[1]<= 135 and 136 <=output[2] and output[2]<= 150:
    return 10
  elif 166 <=output[0] and output[0]<= 255 and 136 <=output[1] and output[1]<= 150 and 136 <=output[2] and output[2]<= 150:
    return 10
  elif 181 <=output[0] and output[0]<= 255 and 0 <=output[1] and output[1]<= 45 and 151 <=output[2] and output[2]<= 165:
    return 10
  elif 196 <=output[0] and output[0]<= 255 and 46 <=output[1] and output[1]<= 150 and 151 <=output[2] and output[2]<= 165:
    return 10
  elif 196 <=output[0] and output[0]<= 255 and 0 <=output[1] and output[1]<= 90 and 166 <=output[2] and output[2]<= 180:
    return 10
  elif 211 <=output[0] and output[0]<= 255 and 91 <=output[1] and output[1]<= 180 and 166 <=output[2] and output[2]<= 180:
    return 10
  elif 196 <=output[0] and output[0]<= 255 and 0 <=output[1] and output[1]<= 60 and 181 <=output[2] and output[2]<= 210:
    return 10
  elif 211 <=output[0] and output[0]<= 255 and 61 <=output[1] and output[1]<= 195 and 181 <=output[2] and output[2]<= 210:
    return 10
  elif 226 <=output[0] and output[0]<= 240 and 196 <=output[1] and output[1]<= 210 and 196 <=output[2] and output[2]<= 210:
    return 10
  elif 196 <=output[0] and output[0]<= 255 and 0 <=output[1] and output[1]<= 30 and 211 <=output[2] and output[2]<= 225:
    return 10
  elif 211 <=output[0] and output[0]<= 255 and 31 <=output[1] and output[1]<= 90 and 211 <=output[2] and output[2]<= 225:
    return 10
  elif 226 <=output[0] and output[0]<= 255 and 91 <=output[1] and output[1]<= 210 and 211 <=output[2] and output[2]<= 225:
    return 10
  elif 211 <=output[0] and output[0]<= 255 and 0 <=output[1] and output[1]<= 60 and 226 <=output[2] and output[2]<= 240:
    return 10
  elif 226 <=output[0] and output[0]<= 255 and 61 <=output[1] and output[1]<= 150 and 226 <=output[2] and output[2]<= 240:
    return 10
  elif 241 <=output[0] and output[0]<= 255 and 151 <=output[1] and output[1]<= 210 and 226 <=output[2] and output[2]<= 240:
    return 10
  elif 211 <=output[0] and output[0]<= 255 and 0 <=output[1] and output[1]<= 45 and 241 <=output[2] and output[2]<= 255:
    return 10
  elif 226 <=output[0] and output[0]<= 255 and 46 <=output[1] and output[1]<= 165 and 241 <=output[2] and output[2]<= 255:
    return 10
  elif 241 <=output[0] and output[0]<= 255 and 166 <=output[1] and output[1]<= 210 and 241 <=output[2] and output[2]<= 255:
    return 10
  elif 31 <=output[0] and output[0]<= 60 and 0 <=output[1] and output[1]<= 15 and 16 <=output[2] and output[2]<= 30:
    return 11
  elif 16 <=output[0] and output[0]<= 75 and 0 <=output[1] and output[1]<= 15 and 31 <=output[2] and output[2]<= 45:
    return 11
  elif 16 <=output[0] and output[0]<= 60 and 16 <=output[1] and output[1]<= 30 and 31 <=output[2] and output[2]<= 45:
    return 11
  elif 61 <=output[0] and output[0]<= 180 and 0 <=output[1] and output[1]<= 30 and 46 <=output[2] and output[2]<= 60:
    return 11
  elif 46 <=output[0] and output[0]<= 180 and 0 <=output[1] and output[1]<= 15 and 61 <=output[2] and output[2]<= 75:
    return 11
  elif 61 <=output[0] and output[0]<= 180 and 16 <=output[1] and output[1]<= 30 and 61 <=output[2] and output[2]<= 75:
    return 11
  elif 76 <=output[0] and output[0]<= 180 and 31 <=output[1] and output[1]<= 60 and 61 <=output[2] and output[2]<= 75:
    return 11
  elif 31 <=output[0] and output[0]<= 165 and 0 <=output[1] and output[1]<= 30 and 76 <=output[2] and output[2]<= 90:
    return 11
  elif 46 <=output[0] and output[0]<= 165 and 31 <=output[1] and output[1]<= 45 and 76 <=output[2] and output[2]<= 90:
    return 11
  elif 61 <=output[0] and output[0]<= 165 and 46 <=output[1] and output[1]<= 60 and 76 <=output[2] and output[2]<= 90:
    return 11
  elif 76 <=output[0] and output[0]<= 165 and 61 <=output[1] and output[1]<= 75 and 76 <=output[2] and output[2]<= 90:
    return 11
  elif 106 <=output[0] and output[0]<= 165 and 76 <=output[1] and output[1]<= 90 and 76 <=output[2] and output[2]<= 90:
    return 11
  elif 31 <=output[0] and output[0]<= 165 and 0 <=output[1] and output[1]<= 30 and 91 <=output[2] and output[2]<= 105:
    return 11
  elif 46 <=output[0] and output[0]<= 180 and 31 <=output[1] and output[1]<= 45 and 91 <=output[2] and output[2]<= 105:
    return 11
  elif 61 <=output[0] and output[0]<= 180 and 46 <=output[1] and output[1]<= 60 and 91 <=output[2] and output[2]<= 105:
    return 11
  elif 76 <=output[0] and output[0]<= 180 and 61 <=output[1] and output[1]<= 90 and 91 <=output[2] and output[2]<= 105:
    return 11
  elif 136 <=output[0] and output[0]<= 180 and 91 <=output[1] and output[1]<= 105 and 91 <=output[2] and output[2]<= 105:
    return 11
  elif 31 <=output[0] and output[0]<= 165 and 0 <=output[1] and output[1]<= 15 and 106 <=output[2] and output[2]<= 120:
    return 11
  elif 46 <=output[0] and output[0]<= 180 and 16 <=output[1] and output[1]<= 45 and 106 <=output[2] and output[2]<= 120:
    return 11
  elif 61 <=output[0] and output[0]<= 180 and 46 <=output[1] and output[1]<= 90 and 106 <=output[2] and output[2]<= 120:
    return 11
  elif 121 <=output[0] and output[0]<= 180 and 91 <=output[1] and output[1]<= 105 and 106 <=output[2] and output[2]<= 120:
    return 11
  elif 136 <=output[0] and output[0]<= 180 and 106 <=output[1] and output[1]<= 120 and 106 <=output[2] and output[2]<= 120:
    return 11
  elif 151 <=output[0] and output[0]<= 180 and 121 <=output[1] and output[1]<= 135 and 106 <=output[2] and output[2]<= 120:
    return 11
  elif 46 <=output[0] and output[0]<= 180 and 0 <=output[1] and output[1]<= 60 and 121 <=output[2] and output[2]<= 135:
    return 11
  elif 61 <=output[0] and output[0]<= 180 and 61 <=output[1] and output[1]<= 90 and 121 <=output[2] and output[2]<= 135:
    return 11
  elif 76 <=output[0] and output[0]<= 180 and 91 <=output[1] and output[1]<= 105 and 121 <=output[2] and output[2]<= 135:
    return 11
  elif 151 <=output[0] and output[0]<= 180 and 106 <=output[1] and output[1]<= 120 and 121 <=output[2] and output[2]<= 135:
    return 11
  elif 166 <=output[0] and output[0]<= 180 and 121 <=output[1] and output[1]<= 135 and 121 <=output[2] and output[2]<= 135:
    return 11
  elif 61 <=output[0] and output[0]<= 180 and 0 <=output[1] and output[1]<= 30 and 136 <=output[2] and output[2]<= 150:
    return 11
  elif 61 <=output[0] and output[0]<= 195 and 31 <=output[1] and output[1]<= 60 and 136 <=output[2] and output[2]<= 150:
    return 11
  elif 76 <=output[0] and output[0]<= 195 and 61 <=output[1] and output[1]<= 75 and 136 <=output[2] and output[2]<= 165:
    return 11
  elif 91 <=output[0] and output[0]<= 195 and 76 <=output[1] and output[1]<= 90 and 136 <=output[2] and output[2]<= 180:
    return 11
  elif 106 <=output[0] and output[0]<= 180 and 91 <=output[1] and output[1]<= 105 and 136 <=output[2] and output[2]<= 150:
    return 11
  elif 121 <=output[0] and output[0]<= 180 and 106 <=output[1] and output[1]<= 120 and 136 <=output[2] and output[2]<= 150:
    return 11
  elif 121 <=output[0] and output[0]<= 135 and 151 <=output[1] and output[1]<= 180 and 136 <=output[2] and output[2]<= 150:
    return 11
  elif 61 <=output[0] and output[0]<= 180 and 0 <=output[1] and output[1]<= 45 and 151 <=output[2] and output[2]<= 165:
    return 11
  elif 61 <=output[0] and output[0]<= 195 and 46 <=output[1] and output[1]<= 60 and 151 <=output[2] and output[2]<= 165:
    return 11
  elif 106 <=output[0] and output[0]<= 195 and 91 <=output[1] and output[1]<= 105 and 151 <=output[2] and output[2]<= 165:
    return 11
  elif 121 <=output[0] and output[0]<= 195 and 106 <=output[1] and output[1]<= 135 and 151 <=output[2] and output[2]<= 165:
    return 11
  elif 151 <=output[0] and output[0]<= 195 and 136 <=output[1] and output[1]<= 150 and 151 <=output[2] and output[2]<= 165:
    return 11
  elif 61 <=output[0] and output[0]<= 195 and 0 <=output[1] and output[1]<= 45 and 166 <=output[2] and output[2]<= 195:
    return 11
  elif 76 <=output[0] and output[0]<= 195 and 46 <=output[1] and output[1]<= 75 and 166 <=output[2] and output[2]<= 180:
    return 11
  elif 91 <=output[0] and output[0]<= 210 and 91 <=output[1] and output[1]<= 105 and 166 <=output[2] and output[2]<= 180:
    return 11
  elif 106 <=output[0] and output[0]<= 210 and 106 <=output[1] and output[1]<= 120 and 166 <=output[2] and output[2]<= 180:
    return 11
  elif 121 <=output[0] and output[0]<= 210 and 121 <=output[1] and output[1]<= 135 and 166 <=output[2] and output[2]<= 180:
    return 11
  elif 136 <=output[0] and output[0]<= 210 and 136 <=output[1] and output[1]<= 150 and 166 <=output[2] and output[2]<= 180:
    return 11
  elif 166 <=output[0] and output[0]<= 210 and 151 <=output[1] and output[1]<= 165 and 166 <=output[2] and output[2]<= 195:
    return 11
  elif 61 <=output[0] and output[0]<= 195 and 0 <=output[1] and output[1]<= 45 and 181 <=output[2] and output[2]<= 195:
    return 11
  elif 76 <=output[0] and output[0]<= 195 and 46 <=output[1] and output[1]<= 60 and 181 <=output[2] and output[2]<= 195:
    return 11
  elif 76 <=output[0] and output[0]<= 210 and 61 <=output[1] and output[1]<= 75 and 181 <=output[2] and output[2]<= 195:
    return 11
  elif 91 <=output[0] and output[0]<= 210 and 76 <=output[1] and output[1]<= 90 and 181 <=output[2] and output[2]<= 195:
    return 11
  elif 106 <=output[0] and output[0]<= 210 and 91 <=output[1] and output[1]<= 105 and 181 <=output[2] and output[2]<= 195:
    return 11
  elif 121 <=output[0] and output[0]<= 210 and 106 <=output[1] and output[1]<= 120 and 181 <=output[2] and output[2]<= 210:
    return 11
  elif 136 <=output[0] and output[0]<= 210 and 121 <=output[1] and output[1]<= 150 and 181 <=output[2] and output[2]<= 195:
    return 11
  elif 181 <=output[0] and output[0]<= 195 and 166 <=output[1] and output[1]<= 180 and 181 <=output[2] and output[2]<= 195:
    return 11
  elif 76 <=output[0] and output[0]<= 195 and 0 <=output[1] and output[1]<= 45 and 196 <=output[2] and output[2]<= 210:
    return 11
  elif 91 <=output[0] and output[0]<= 195 and 46 <=output[1] and output[1]<= 60 and 196 <=output[2] and output[2]<= 210:
    return 11
  elif 91 <=output[0] and output[0]<= 210 and 61 <=output[1] and output[1]<= 75 and 196 <=output[2] and output[2]<= 210:
    return 11
  elif 106 <=output[0] and output[0]<= 210 and 76 <=output[1] and output[1]<= 105 and 196 <=output[2] and output[2]<= 210:
    return 11
  elif 136 <=output[0] and output[0]<= 210 and 121 <=output[1] and output[1]<= 135 and 196 <=output[2] and output[2]<= 210:
    return 11
  elif 151 <=output[0] and output[0]<= 210 and 136 <=output[1] and output[1]<= 165 and 196 <=output[2] and output[2]<= 210:
    return 11
  elif 181 <=output[0] and output[0]<= 210 and 166 <=output[1] and output[1]<= 180 and 196 <=output[2] and output[2]<= 210:
    return 11
  elif 196 <=output[0] and output[0]<= 210 and 181 <=output[1] and output[1]<= 195 and 196 <=output[2] and output[2]<= 210:
    return 11
  elif 76 <=output[0] and output[0]<= 195 and 0 <=output[1] and output[1]<= 30 and 211 <=output[2] and output[2]<= 225:
    return 11
  elif 91 <=output[0] and output[0]<= 210 and 31 <=output[1] and output[1]<= 60 and 211 <=output[2] and output[2]<= 225:
    return 11
  elif 106 <=output[0] and output[0]<= 210 and 61 <=output[1] and output[1]<= 90 and 211 <=output[2] and output[2]<= 225:
    return 11
  elif 121 <=output[0] and output[0]<= 225 and 91 <=output[1] and output[1]<= 120 and 211 <=output[2] and output[2]<= 225:
    return 11
  elif 136 <=output[0] and output[0]<= 225 and 121 <=output[1] and output[1]<= 135 and 211 <=output[2] and output[2]<= 225:
    return 11
  elif 151 <=output[0] and output[0]<= 225 and 136 <=output[1] and output[1]<= 150 and 211 <=output[2] and output[2]<= 225:
    return 11
  elif 166 <=output[0] and output[0]<= 225 and 151 <=output[1] and output[1]<= 180 and 211 <=output[2] and output[2]<= 225:
    return 11
  elif 181 <=output[0] and output[0]<= 225 and 181 <=output[1] and output[1]<= 195 and 211 <=output[2] and output[2]<= 225:
    return 11
  elif 211 <=output[0] and output[0]<= 225 and 196 <=output[1] and output[1]<= 210 and 211 <=output[2] and output[2]<= 225:
    return 11
  elif 76 <=output[0] and output[0]<= 210 and 0 <=output[1] and output[1]<= 15 and 226 <=output[2] and output[2]<= 240:
    return 11
  elif 91 <=output[0] and output[0]<= 210 and 16 <=output[1] and output[1]<= 60 and 226 <=output[2] and output[2]<= 240:
    return 11
  elif 106 <=output[0] and output[0]<= 225 and 61 <=output[1] and output[1]<= 75 and 226 <=output[2] and output[2]<= 240:
    return 11
  elif 121 <=output[0] and output[0]<= 225 and 76 <=output[1] and output[1]<= 105 and 226 <=output[2] and output[2]<= 240:
    return 11
  elif 136 <=output[0] and output[0]<= 225 and 106 <=output[1] and output[1]<= 120 and 226 <=output[2] and output[2]<= 240:
    return 11
  elif 151 <=output[0] and output[0]<= 225 and 121 <=output[1] and output[1]<= 150 and 226 <=output[2] and output[2]<= 240:
    return 11
  elif 166 <=output[0] and output[0]<= 240 and 166 <=output[1] and output[1]<= 180 and 226 <=output[2] and output[2]<= 240:
    return 11
  elif 196 <=output[0] and output[0]<= 240 and 181 <=output[1] and output[1]<= 195 and 226 <=output[2] and output[2]<= 255:
    return 11
  elif 91 <=output[0] and output[0]<= 210 and 0 <=output[1] and output[1]<= 30 and 241 <=output[2] and output[2]<= 255:
    return 11
  elif 106 <=output[0] and output[0]<= 210 and 31 <=output[1] and output[1]<= 45 and 241 <=output[2] and output[2]<= 255:
    return 11
  elif 121 <=output[0] and output[0]<= 225 and 46 <=output[1] and output[1]<= 90 and 241 <=output[2] and output[2]<= 255:
    return 11
  elif 136 <=output[0] and output[0]<= 225 and 91 <=output[1] and output[1]<= 105 and 241 <=output[2] and output[2]<= 255:
    return 11
  elif 151 <=output[0] and output[0]<= 225 and 106 <=output[1] and output[1]<= 150 and 241 <=output[2] and output[2]<= 255:
    return 11
  elif 166 <=output[0] and output[0]<= 225 and 151 <=output[1] and output[1]<= 165 and 241 <=output[2] and output[2]<= 255:
    return 11
  elif 181 <=output[0] and output[0]<= 240 and 166 <=output[1] and output[1]<= 180 and 241 <=output[2] and output[2]<= 255:
    return 11
  elif 211 <=output[0] and output[0]<= 240 and 196 <=output[1] and output[1]<= 210 and 241 <=output[2] and output[2]<= 255:
    return 11
  elif 0 <=output[0] and output[0]<= 15 and 0 <=output[1] and output[1]<= 30 and 16 <=output[2] and output[2]<= 30:
    return 12
  elif 0 <=output[0] and output[0]<= 30 and 46 <=output[1] and output[1]<= 60 and 136 <=output[2] and output[2]<= 150:
    return 12
  elif 0 <=output[0] and output[0]<= 45 and 61 <=output[1] and output[1]<= 90 and 136 <=output[2] and output[2]<= 150:
    return 12
  elif 0 <=output[0] and output[0]<= 105 and 91 <=output[1] and output[1]<= 105 and 136 <=output[2] and output[2]<= 165:
    return 12
  elif 0 <=output[0] and output[0]<= 90 and 106 <=output[1] and output[1]<= 120 and 136 <=output[2] and output[2]<= 150:
    return 12
  elif 0 <=output[0] and output[0]<= 75 and 121 <=output[1] and output[1]<= 135 and 136 <=output[2] and output[2]<= 150:
    return 12
  elif 0 <=output[0] and output[0]<= 60 and 0 <=output[1] and output[1]<= 60 and 151 <=output[2] and output[2]<= 165:
    return 12
  elif 0 <=output[0] and output[0]<= 75 and 61 <=output[1] and output[1]<= 75 and 151 <=output[2] and output[2]<= 165:
    return 12
  elif 0 <=output[0] and output[0]<= 90 and 76 <=output[1] and output[1]<= 90 and 151 <=output[2] and output[2]<= 165:
    return 12
  elif 0 <=output[0] and output[0]<= 120 and 106 <=output[1] and output[1]<= 120 and 151 <=output[2] and output[2]<= 165:
    return 12
  elif 0 <=output[0] and output[0]<= 105 and 121 <=output[1] and output[1]<= 135 and 151 <=output[2] and output[2]<= 165:
    return 12
  elif 0 <=output[0] and output[0]<= 120 and 136 <=output[1] and output[1]<= 150 and 151 <=output[2] and output[2]<= 165:
    return 12
  elif 0 <=output[0] and output[0]<= 60 and 0 <=output[1] and output[1]<= 45 and 166 <=output[2] and output[2]<= 195:
    return 12
  elif 0 <=output[0] and output[0]<= 75 and 46 <=output[1] and output[1]<= 75 and 166 <=output[2] and output[2]<= 195:
    return 12
  elif 0 <=output[0] and output[0]<= 90 and 76 <=output[1] and output[1]<= 105 and 166 <=output[2] and output[2]<= 180:
    return 12
  elif 0 <=output[0] and output[0]<= 105 and 106 <=output[1] and output[1]<= 120 and 166 <=output[2] and output[2]<= 180:
    return 12
  elif 0 <=output[0] and output[0]<= 120 and 121 <=output[1] and output[1]<= 135 and 166 <=output[2] and output[2]<= 180:
    return 12
  elif 0 <=output[0] and output[0]<= 135 and 136 <=output[1] and output[1]<= 165 and 166 <=output[2] and output[2]<= 180:
    return 12
  elif 0 <=output[0] and output[0]<= 60 and 0 <=output[1] and output[1]<= 45 and 181 <=output[2] and output[2]<= 195:
    return 12
  elif 0 <=output[0] and output[0]<= 75 and 46 <=output[1] and output[1]<= 75 and 181 <=output[2] and output[2]<= 195:
    return 12
  elif 0 <=output[0] and output[0]<= 90 and 76 <=output[1] and output[1]<= 90 and 181 <=output[2] and output[2]<= 195:
    return 12
  elif 0 <=output[0] and output[0]<= 105 and 91 <=output[1] and output[1]<= 105 and 181 <=output[2] and output[2]<= 195:
    return 12
  elif 0 <=output[0] and output[0]<= 120 and 106 <=output[1] and output[1]<= 120 and 181 <=output[2] and output[2]<= 210:
    return 12
  elif 0 <=output[0] and output[0]<= 135 and 121 <=output[1] and output[1]<= 150 and 181 <=output[2] and output[2]<= 195:
    return 12
  elif 0 <=output[0] and output[0]<= 75 and 0 <=output[1] and output[1]<= 45 and 196 <=output[2] and output[2]<= 210:
    return 12
  elif 0 <=output[0] and output[0]<= 90 and 46 <=output[1] and output[1]<= 75 and 196 <=output[2] and output[2]<= 210:
    return 12
  elif 0 <=output[0] and output[0]<= 105 and 76 <=output[1] and output[1]<= 105 and 196 <=output[2] and output[2]<= 210:
    return 12
  elif 0 <=output[0] and output[0]<= 135 and 121 <=output[1] and output[1]<= 135 and 196 <=output[2] and output[2]<= 225:
    return 12
  elif 0 <=output[0] and output[0]<= 150 and 136 <=output[1] and output[1]<= 165 and 196 <=output[2] and output[2]<= 210:
    return 12
  elif 121 <=output[0] and output[0]<= 180 and 166 <=output[1] and output[1]<= 180 and 196 <=output[2] and output[2]<= 210:
    return 12
  elif 0 <=output[0] and output[0]<= 75 and 0 <=output[1] and output[1]<= 30 and 211 <=output[2] and output[2]<= 225:
    return 12
  elif 0 <=output[0] and output[0]<= 90 and 31 <=output[1] and output[1]<= 60 and 211 <=output[2] and output[2]<= 225:
    return 12
  elif 0 <=output[0] and output[0]<= 105 and 61 <=output[1] and output[1]<= 90 and 211 <=output[2] and output[2]<= 225:
    return 12
  elif 0 <=output[0] and output[0]<= 120 and 91 <=output[1] and output[1]<= 120 and 211 <=output[2] and output[2]<= 225:
    return 12
  elif 0 <=output[0] and output[0]<= 150 and 136 <=output[1] and output[1]<= 150 and 211 <=output[2] and output[2]<= 225:
    return 12
  elif 0 <=output[0] and output[0]<= 165 and 151 <=output[1] and output[1]<= 165 and 211 <=output[2] and output[2]<= 255:
    return 12
  elif 106 <=output[0] and output[0]<= 165 and 166 <=output[1] and output[1]<= 180 and 211 <=output[2] and output[2]<= 225:
    return 12
  elif 151 <=output[0] and output[0]<= 180 and 181 <=output[1] and output[1]<= 195 and 211 <=output[2] and output[2]<= 225:
    return 12
  elif 0 <=output[0] and output[0]<= 75 and 0 <=output[1] and output[1]<= 15 and 226 <=output[2] and output[2]<= 240:
    return 12
  elif 0 <=output[0] and output[0]<= 90 and 16 <=output[1] and output[1]<= 60 and 226 <=output[2] and output[2]<= 240:
    return 12
  elif 0 <=output[0] and output[0]<= 105 and 61 <=output[1] and output[1]<= 75 and 226 <=output[2] and output[2]<= 240:
    return 12
  elif 0 <=output[0] and output[0]<= 120 and 76 <=output[1] and output[1]<= 105 and 226 <=output[2] and output[2]<= 240:
    return 12
  elif 0 <=output[0] and output[0]<= 135 and 106 <=output[1] and output[1]<= 120 and 226 <=output[2] and output[2]<= 240:
    return 12
  elif 0 <=output[0] and output[0]<= 150 and 121 <=output[1] and output[1]<= 150 and 226 <=output[2] and output[2]<= 240:
    return 12
  elif 76 <=output[0] and output[0]<= 165 and 166 <=output[1] and output[1]<= 180 and 226 <=output[2] and output[2]<= 240:
    return 12
  elif 106 <=output[0] and output[0]<= 195 and 181 <=output[1] and output[1]<= 195 and 226 <=output[2] and output[2]<= 240:
    return 12
  elif 151 <=output[0] and output[0]<= 240 and 196 <=output[1] and output[1]<= 210 and 226 <=output[2] and output[2]<= 240:
    return 12
  elif 0 <=output[0] and output[0]<= 90 and 0 <=output[1] and output[1]<= 30 and 241 <=output[2] and output[2]<= 255:
    return 12
  elif 0 <=output[0] and output[0]<= 105 and 31 <=output[1] and output[1]<= 45 and 241 <=output[2] and output[2]<= 255:
    return 12
  elif 0 <=output[0] and output[0]<= 120 and 46 <=output[1] and output[1]<= 90 and 241 <=output[2] and output[2]<= 255:
    return 12
  elif 0 <=output[0] and output[0]<= 135 and 91 <=output[1] and output[1]<= 105 and 241 <=output[2] and output[2]<= 255:
    return 12
  elif 0 <=output[0] and output[0]<= 150 and 106 <=output[1] and output[1]<= 150 and 241 <=output[2] and output[2]<= 255:
    return 12
  elif 76 <=output[0] and output[0]<= 180 and 166 <=output[1] and output[1]<= 180 and 241 <=output[2] and output[2]<= 255:
    return 12
  elif 136 <=output[0] and output[0]<= 195 and 181 <=output[1] and output[1]<= 195 and 241 <=output[2] and output[2]<= 255:
    return 12
  elif 136 <=output[0] and output[0]<= 210 and 196 <=output[1] and output[1]<= 210 and 241 <=output[2] and output[2]<= 255:
    return 12
  elif 76 <=output[0] and output[0]<= 105 and 121 <=output[1] and output[1]<= 135 and 136 <=output[2] and output[2]<= 150:
    return 13
  elif 0 <=output[0] and output[0]<= 135 and 151 <=output[1] and output[1]<= 180 and 181 <=output[2] and output[2]<= 195:
    return 13
  elif 0 <=output[0] and output[0]<= 165 and 181 <=output[1] and output[1]<= 195 and 181 <=output[2] and output[2]<= 210:
    return 13
  elif 0 <=output[0] and output[0]<= 120 and 166 <=output[1] and output[1]<= 180 and 196 <=output[2] and output[2]<= 210:
    return 13
  elif 0 <=output[0] and output[0]<= 180 and 196 <=output[1] and output[1]<= 210 and 196 <=output[2] and output[2]<= 225:
    return 13
  elif 0 <=output[0] and output[0]<= 105 and 166 <=output[1] and output[1]<= 180 and 211 <=output[2] and output[2]<= 225:
    return 13
  elif 0 <=output[0] and output[0]<= 150 and 181 <=output[1] and output[1]<= 195 and 211 <=output[2] and output[2]<= 225:
    return 13
  elif 0 <=output[0] and output[0]<= 210 and 211 <=output[1] and output[1]<= 225 and 211 <=output[2] and output[2]<= 225:
    return 13
  elif 0 <=output[0] and output[0]<= 180 and 226 <=output[1] and output[1]<= 240 and 211 <=output[2] and output[2]<= 225:
    return 13
  elif 0 <=output[0] and output[0]<= 165 and 241 <=output[1] and output[1]<= 255 and 211 <=output[2] and output[2]<= 225:
    return 13
  elif 0 <=output[0] and output[0]<= 75 and 166 <=output[1] and output[1]<= 180 and 226 <=output[2] and output[2]<= 255:
    return 13
  elif 0 <=output[0] and output[0]<= 105 and 181 <=output[1] and output[1]<= 195 and 226 <=output[2] and output[2]<= 240:
    return 13
  elif 0 <=output[0] and output[0]<= 150 and 196 <=output[1] and output[1]<= 210 and 226 <=output[2] and output[2]<= 240:
    return 13
  elif 0 <=output[0] and output[0]<= 210 and 211 <=output[1] and output[1]<= 255 and 226 <=output[2] and output[2]<= 255:
    return 13
  elif 0 <=output[0] and output[0]<= 135 and 181 <=output[1] and output[1]<= 210 and 241 <=output[2] and output[2]<= 255:
    return 13
  elif 0 <=output[0] and output[0]<= 15 and 0 <=output[1] and output[1]<= 30 and 31 <=output[2] and output[2]<= 45:
    return 14
  elif 0 <=output[0] and output[0]<= 60 and 0 <=output[1] and output[1]<= 30 and 46 <=output[2] and output[2]<= 60:
    return 14
  elif 0 <=output[0] and output[0]<= 75 and 31 <=output[1] and output[1]<= 45 and 46 <=output[2] and output[2]<= 60:
    return 14
  elif 0 <=output[0] and output[0]<= 45 and 0 <=output[1] and output[1]<= 15 and 61 <=output[2] and output[2]<= 75:
    return 14
  elif 0 <=output[0] and output[0]<= 60 and 16 <=output[1] and output[1]<= 30 and 61 <=output[2] and output[2]<= 75:
    return 14
  elif 0 <=output[0] and output[0]<= 75 and 31 <=output[1] and output[1]<= 60 and 61 <=output[2] and output[2]<= 75:
    return 14
  elif 0 <=output[0] and output[0]<= 30 and 0 <=output[1] and output[1]<= 30 and 76 <=output[2] and output[2]<= 105:
    return 14
  elif 0 <=output[0] and output[0]<= 45 and 31 <=output[1] and output[1]<= 45 and 76 <=output[2] and output[2]<= 105:
    return 14
  elif 0 <=output[0] and output[0]<= 60 and 46 <=output[1] and output[1]<= 60 and 76 <=output[2] and output[2]<= 105:
    return 14
  elif 0 <=output[0] and output[0]<= 75 and 61 <=output[1] and output[1]<= 75 and 76 <=output[2] and output[2]<= 90:
    return 14
  elif 0 <=output[0] and output[0]<= 30 and 0 <=output[1] and output[1]<= 30 and 91 <=output[2] and output[2]<= 105:
    return 14
  elif 0 <=output[0] and output[0]<= 45 and 31 <=output[1] and output[1]<= 45 and 91 <=output[2] and output[2]<= 105:
    return 14
  elif 0 <=output[0] and output[0]<= 60 and 46 <=output[1] and output[1]<= 60 and 91 <=output[2] and output[2]<= 105:
    return 14
  elif 0 <=output[0] and output[0]<= 75 and 61 <=output[1] and output[1]<= 90 and 91 <=output[2] and output[2]<= 105:
    return 14
  elif 0 <=output[0] and output[0]<= 30 and 0 <=output[1] and output[1]<= 15 and 106 <=output[2] and output[2]<= 120:
    return 14
  elif 0 <=output[0] and output[0]<= 45 and 16 <=output[1] and output[1]<= 45 and 106 <=output[2] and output[2]<= 120:
    return 14
  elif 0 <=output[0] and output[0]<= 60 and 46 <=output[1] and output[1]<= 90 and 106 <=output[2] and output[2]<= 120:
    return 14
  elif 0 <=output[0] and output[0]<= 75 and 91 <=output[1] and output[1]<= 105 and 106 <=output[2] and output[2]<= 135:
    return 14
  elif 0 <=output[0] and output[0]<= 45 and 0 <=output[1] and output[1]<= 60 and 121 <=output[2] and output[2]<= 135:
    return 14
  elif 0 <=output[0] and output[0]<= 60 and 61 <=output[1] and output[1]<= 90 and 121 <=output[2] and output[2]<= 135:
    return 14
  elif 0 <=output[0] and output[0]<= 60 and 0 <=output[1] and output[1]<= 45 and 136 <=output[2] and output[2]<= 150:
    return 14
  elif 31 <=output[0] and output[0]<= 60 and 46 <=output[1] and output[1]<= 60 and 136 <=output[2] and output[2]<= 150:
    return 14
  elif 46 <=output[0] and output[0]<= 75 and 61 <=output[1] and output[1]<= 75 and 136 <=output[2] and output[2]<= 150:
    return 14
  elif 46 <=output[0] and output[0]<= 90 and 76 <=output[1] and output[1]<= 90 and 136 <=output[2] and output[2]<= 150:
    return 14
  elif 196 <=output[0] and output[0]<= 225 and 151 <=output[1] and output[1]<= 180 and 136 <=output[2] and output[2]<= 150:
    return 15
  elif 211 <=output[0] and output[0]<= 225 and 181 <=output[1] and output[1]<= 195 and 136 <=output[2] and output[2]<= 150:
    return 15
  elif 211 <=output[0] and output[0]<= 240 and 196 <=output[1] and output[1]<= 210 and 136 <=output[2] and output[2]<= 150:
    return 15
  elif 211 <=output[0] and output[0]<= 225 and 196 <=output[1] and output[1]<= 210 and 151 <=output[2] and output[2]<= 180:
    return 15
  elif 226 <=output[0] and output[0]<= 240 and 211 <=output[1] and output[1]<= 225 and 166 <=output[2] and output[2]<= 180:
    return 15
  elif 226 <=output[0] and output[0]<= 240 and 211 <=output[1] and output[1]<= 225 and 166 <=output[2] and output[2]<= 180:
    return 15
  elif 211 <=output[0] and output[0]<= 255 and 211 <=output[1] and output[1]<= 255 and 196 <=output[2] and output[2]<= 240:
    return 16
  elif 211 <=output[0] and output[0]<= 255 and 211 <=output[1] and output[1]<= 240 and 241 <=output[2] and output[2]<= 255:
    return 16
  elif 211 <=output[0] and output[0]<= 225 and 241 <=output[1] and output[1]<= 255 and 241 <=output[2] and output[2]<= 255:
    return 16

  return 0