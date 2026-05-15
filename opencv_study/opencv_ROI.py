# opencv_ROI.py

# Region of Interest - 관심 영역: 영상이나 이미지에서 특정 영역만 분석하기 위함
# 특정영역을 잘라내는 방법은 numpy 배열 자르기(slicing)

import cv2

point = [] # 두 좌표 저장용

# 마우스 클릭 함수
def mouse_pos(event, x, y, flag, param ):
    global point

    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"x : {x}, y: {y}")
        point.append({"x" : x, "y" : y }) # 마우스 클릭 좌표 값 저장

        cv2.circle(
            img , (x,y), 5, (0,255,150), -1
        )

        # 좌표 클릭을 2번 했다면
        if len(point) == 2:
            p1 = point[0]
            p2 = point[1]
            cv2.rectangle( img, (p1["x"], p1["y"]),
                          (p2["x"], p2["y"]), (255, 0, 0), 2)
            # ROI
            roi = img[
                min(p1["y"], p2["y"]) : max(p1["y"], p2["y"]),
                min(p1["x"], p2["x"]) : max(p1["x"], p2["x"])
            ]
            cv2.imshow("roi",roi)

img = cv2.imread("opencv_study/images/door.png")

cv2.namedWindow("image")
cv2.setMouseCallback("image", mouse_pos)

# roi = img[200:642, 165:337] # img[y1:y2, x1:x2]

while True:
    cv2.imshow("image", img)
    # cv2.imshow("roi", roi)

    k = cv2.waitKey(1)
    if k == 27: break # ESC 키값은 27
    if k == ord('r'): # 알파벳 'r'키 누르면 좌표 초기화!
        img = cv2.imread("opencv_study/images/door.png")
        point=[]

cv2.destroyAllWindows()