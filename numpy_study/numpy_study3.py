# numpy_study3.py

import numpy as np

# 배열에서 원하는 위치 데이터 가져오기
print("배열에서 원하는 위치 데이터 가져오기")
arr = np.random.randint(0, 50, 12)
print(arr)

print("\n 슬라이싱")
# 슬라이싱
print( arr[3:0] )
print( arr[:4]) # :4 -> 0번 인덱스부터 3번까지
                # :2 -> 2번 인덱스부터 끝까지

print( arr[::2] ) # ::2 -> 2칸씩
print( arr[::-1] ) # 역방향으로 출력

arr2 = np.random.randint( 0, 50, (3,4))
print( arr2 )
print( arr2[1] )
print( arr2[: , 2])
print( arr2[0:1, 1:3])

print("\n fancy indexing : 원하는 위치만 고르기")
# fancy indexing : 원하는 위치만 고르기
print( arr[[0, 4, 7]]) # [ [ 인덱스, 인덱스 ] ] 원하는 인덱스 번호 넣기

print( arr2[[0,2]] ) # 2차원 배열에서는 행을 선택
print( arr2[ [0,2] , [1,3] ]) # 0,1 (arr[0][1]) 과 2,3 (arr[2][3])

# boolean indexing
print("\n boolean indexing")
print( arr > 30 )
print( arr[ arr > 30] ) # 조건식에 맞는 데이터만 뽑아 내기
print( arr[arr % 2 == 1])

print( arr2[ arr2 > 15])

print("\n 학생 5명의 6과목 성적 임의, 80점 이상 출력")
# 학생 5명의 6과목 성적을 배열로 저장하세요 ( 성적은 50~100 사이 임의값)
# 학생 5명 성적이 저장된 배열에서 성적이 80점 이상만 출력하시오.
scores = np.random.randint(50, 100, (5,6))
print( scores [scores >= 80] )
print("80점 이상 해당 인덱스 출력")
pos = np.argwhere(scores >= 80)
print( pos )

# 흑백 사진에서 밝은 영역이 어디인지 찾아서 표시하시오.
# 어두운 영역 - 0, 밝은 영역 - 255
print("\n 흑백 사진에서 밝은 영역이 어디인지")
img = np.array([
    [],
    [],
    [],
    []

])