# opencv_study2.py

# AI가 영상분석을 하는데 먼저 전처리한다.
# 전처리는 크기 변경, 흑백 변환, 노이즈 제거, 강조 처리 등 (흑백변환: 분석을 용이하게 하기 위함, 밝음 어두움이라는 두 가지 기준으로!)

import cv2
# img = cv2.imread("opencv_study/images/surfer.png")

# 변경 이후에 show
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# cv2.imshow("surfer", gray)
# print(gray.shape) # (166, 304, 3)
# print( gray[100][100])
# cv2.waitKey(0)

# 크기 변경 하기

# cv2.resize( 대상, (가로, 세로) )
# small = cv2.resize( img, (152, 83) )
# cv2.imshow("size", small)
# print( small.shape )
# cv2.waitKey(0)

# 이미지 뒤집기 (반전)
# flip = cv2.flip(img , 1)
# # 1 - 좌우 반전, 0 - 상하반전, -1 - 상하좌우반전
# cv2.imshow("flip", flip)
# cv2.waitKey(0)

# 블러 처리 - 이미지를 흐리게 만드는 것
# 노이즈 감소의 목적
# blur = cv2.GaussianBlur( img, (5,5), 0 )
# # (5,5)의 값을 크게 주면 더 흐려진다.

# cv2.imshow("blur", blur)
# cv2.waitKey(0)

# 경계 - threshold
# gray = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY)
# _, thresh = cv2.threshold(
#     gray, 50, 255, cv2.THRESH_BINARY
# )
# _, thresh_rev = cv2.threshold(
#     gray, 127, 255, cv2.THRESH_BINARY_INV   
# )

# cv2.imshow("gray", gray)
# cv2.imshow("bin", thresh)
# cv2.imshow("inv",thresh_rev)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 사진의 크기는 가로길이 320으로 비율 유지해서 변경하고 흑백 변환하고, 멍멍이가 잘 보일 수 있도록 경계설정하여
# dog_result.png로 저장하기

dog = cv2.imread("opencv_study/images/dog.png")
# cv2.imshow("dog", dog)
# print(dog.shape) # (1512, 2016, 3)
# # print( gray[100][100])
# # cv2.waitKey(0)
# dog_gray = cv2.cvtColor(dog, cv2.COLOR_BGR2GRAY)
# print(dog_gray)
# cv2.waitKey(0)

# cv2.resize( 대상, (가로, 세로) )
dog_resize = cv2.resize( dog, (320, 150) )
cv2.imshow("size", dog_resize)
print( dog_resize.shape )
cv2.waitKey(0)
