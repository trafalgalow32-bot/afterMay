# pandas_study2.py

import pandas as pd

df = pd.read_csv('pandas_fruit.csv') # csv 파일 메모장으로 열어서 인코딩 "utf-8"로 바꿔서 저장해줘야!
print(df)
print( df.head(3))
print('데이터 구조', df.info())
print('데이터 정보', df.info())
print(df.describe())

print("\n 어떤 과일이 있냐? ")
print(df['fruit'])

print(" 사과만 찾아보자 ")
print( df[df['fruit'] == "사과"] )

print(" 바나나를 찾는다? ")
print( df[df['fruit'] == "바나나"])

print(" 판매 수량이 10개 이상인 과일 찾기")
print( df[df['sale'] >= 10])

print(" 판매 수량이 10개 이상이고 금액이 8만원 이상 찾기")
print( df[
           (df['sale'] >= 10)
           & (df['price'] >= 80000)
       ]
    )

print(" 과일 이름에 '박'이 포함된 것 찾기")
print( df[
            df['fruit']
                .str
                    .contains("박")
       ]
    )

print(" 가격 높은순으로 정렬")
print( df.sort_values('price', ascending=False )
       )
print(
    df.sort_values(by=['fruit','sale'], ascending=[True,False])
)

print(" 집계 함수 사용해보기")
print(" 과일별 판매량 ")
print(
    df.groupby('fruit')['sale'].sum()
)

# 문제 1. 과일별 평균 판매금액
print("\n 문제 1. 과일별 평균 판매금액")
print(round(df.groupby('fruit')['sale'].mean()),2)

print(" 판매량의 총합과 평균, 금액의 최대, 최소 구하기")
print(
    df.groupby('fruit').agg({
        'sale': ['sum', 'mean'],
        'price' : ['max','min']
    })
)

print("과일 개당 가격은?")
df['un_price'] = df['price'] / df['sale']
print(df)

print(" 각 과일들 몇 번 기록 되었나")
print(
    df['fruit'].value_counts()
)

import matplotlib.pyplot as plt

# 문제2. 과일별 판매량을 그래프로 그리시오.
result = df.groupby('fruit')['sale'].sum()

result.plot(kind='bar')
plt.show()

# csv 파일 저장
df.to_csv('pandas_study2.csv', index=False, encoding='utf-8')