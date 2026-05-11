# opencv_study1.py

# open source Computer vision lib
# 컴퓨터 비전 - 비전AI

# 이미지 - 사람이다, 파랑색이다, 하늘색이다.
#         고양이다. 멍멍이다.
# 컴퓨터는 픽셀 숫자들의 모음으로 보고 있다.

# opencv로 이미지나 영상을 불러오기
# yolo에게 전달하여 객체 탐지
# 탐지 결과를 토대로 이미지나 영상에 opencv로 표시하기
# opencv - BGR(blue green red)
# arr = np.array ( [[0, 50, 100], [150, 200, 255] ])
# 영상 - opencv 열기 -> 프레임 한장 열기 -> 이미지 처리 -> 다음 프레임 읽기 -> 이미지 처리
# 앞으로 할 것
# 이미지 필터 , 객체 외곽선 찾기
# 움직임 감지, 영상 저장, 객체 탐지 결과 시각화

# 이미지 numpy 배열이다.
# 영상은 이미지 여러 장이다.
# 프레임 하나는 이미지 한 장이다. fps( frame per second)
# opencv는 배열을 읽고 변경하고, 분석하고 그려주고, 저장

import cv2
import numpy as np

img = cv2.imread("opencv_study/images/cat.png")

cv2.imshow("image", img)

print( type(img) )
print( img.shape ) # 세로(행), 가로(열), 색상값 - 3은 rgb
# 색상정보 - 1은 흑백, 4는 투명도 포함 (BGRA, RGBA)
# (183, 275, 1) - 픽셀 하나에 숫자 1개
# (183, 275, 3) - 픽셀 하나에 숫자 3개 ( B, G, R )
# (183, 275, 4) - 픽셀 하나에 숫자 4개 ( B, G, R, A )
#               A는 알파 (투명도 - 0 (투명) ~ 255(불투명) )

# print( img[100][100])
copy_img = img.copy() # 원본 데이터를 변경하지말고 복사본으로 

copy_img[100:200 , 100:200] = [0,0,255]
cv2.imshow("image", img)
# 이미지 저장 .imwrite("저장할 파일명", 저장객체)
cv2.imwrite("opencv_study/images/copy_cat.png", copy_img)
cv2.waitKey(0)

# # 실습문제. (134, 229, 127) RGB 색상값, Cat 이미지 정중앙에 위 RGB 색상으로 가로 세로 50 픽셀 채우기
# copy_img2 = img.copy()
# # print(copy_img2.shape) # (세로픽셀수, 가로픽셀수, 채널수) (480, 640, 3)
# h, w = copy_img2.shape[:2] # 앞에 두 개만 가져온다는 슬라이싱! 
# cy, cx = h // 2, w // 2 # 정수형이므로 소수점 버려야 함! "//"

# copy_img2[cy-25:cy+25, cx-25:cx+25] = [127, 229, 134] # 50픽셀씩 주라 했으니!
# cv2.imwrite("opencv_study/images/copy_cat2.png", copy_img2)
# cv2.waitKey(0)

"""
강사님 풀이
h, w= copy_img2.shape[:2]

cx = w // 2 
cy = h // 2

cv2.rectangle(
    copy_img2,
    (cx-25, cy-25),
    (cx+25, cy+25),
    (127,229,134),
    -1
)
cv2.imshow("cat", copy_img)
cv2.waitKey(0)
"""

cut = copy_img[20:120, 130:230]
cv2.imwrite('opencv_study/images/cut_cat.png', cut)
cv2.imshow("cut",cut)
cv2.waitKey(0)