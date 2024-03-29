### 데이터프레임 고급 인덱싱
### loc

import pandas as pd
import numpy as np

# loc : 라벨값 기반의 2차원 인덱싱
# iloc : 순서를 나타내는 정수 기반의 2차원 인덱싱
# at: 라벨값 기반의 2차원 인덱싱 (한개의 스칼라 값만 찾는다)
# iat : 순서를 나타내는 정수 기반의 2차원 인덱싱 (한개의 스칼라 값만 찾는다)

## loc 인덱서
# df.loc[행 인덱싱값]
# df.loc[행 인덱싱값, 열 인덱싱값]

# 인덱스데이터
# 인덱스데이터 슬라이스
# 인덱스데이터 리스트
# 같은 행 인덱스를 가지는 불리언 시리즈 (행 인덱싱의 경우)
# 또는 위의 값들을 반환하는 함수

df = pd.DataFrame(np.arange(10, 22).reshape(3, 4),
                  index = ['a', 'b', 'c'],
                  columns = ['A', 'B', 'C', 'D'])

# 인덱싱값을 하나만 받는 경우
df.loc['a']

# 인덱스데이터의 슬라이스
df.loc['b' : 'c']
df['b' : 'c']

# 인덱스데이터의 리스트
df.loc[['b', 'c']]
# df[["b", "c"]]  # KeyError

# 데이터베이스와 같은 인덱스를 가지는 불리언 시리즈도 행을 선택하는 인덱싱값
df.A > 15
df.loc[df.A > 15]


# 인덱스 대신 인덱스 값을 반환하는 함수를 사용할 수도 있다.
# 다음 함수는 A열의 값이 12보다 큰 행만 선택
def select_rows(df):
    return df.A > 15

select_rows(df)
df.loc[select_rows(df)]

# loc 인덱서가 없는 경우에 사용했던 라벨 인덱싱이나 라벨 리스트 인덱싱은 불가능
# df.loc["A"]         # KeyError
# df.loc[["A", "B"]]  # KeyError

# 원래 (행) 인덱스값이 정수인 경우에는 슬라이싱도 라벨 슬라이싱 방식을 따르게 된다.
# 즉, 슬라이스의 마지막 값이 포함된다.
df2 = pd.DataFrame(np.arange(10, 26).reshape(4, 4),
                   columns = ['A', 'B', 'C', 'D'])

df2.loc[1 : 2]


## 인덱싱값을 행과 열 모두 받는 경우
# 인덱싱값을 행과 열 모두 받으려면 df.loc[행 인덱스, 열 인덱스]와 같은 형태로 사용한다.
# 행 인덱스 라벨값이 a,
# 열 인덱스 라벨값이 A인 위치의 값을 구하는 것은 다음과 같다.
df.loc['a', 'A']

# 인덱싱값으로 라벨 데이터의 슬라이싱 또는 리스트를 사용
df.loc['b':, 'A']
df.loc['a', :]
df.loc[['a', 'b'], ['B', 'D']]

# 행 인덱스가 같은 불리언 시리즈나 이러한 불리언 시리즈를 반환하는 함수도 행의 인덱싱값이 될 수 있다
df.loc[df.A > 10, ['C', 'D']]



### iloc 인덱서
# iloc 인덱서는 loc 인덱서와 반대로 라벨이 아니라
# 순서를 나타내는 정수(integer) 인덱스만 받는다.
# 다른 사항은 loc 인덱서와 같다.
df.iloc[0, 1]         # 첫번째 열, 두번째 행
df.iloc[:2, 2]        # 첫번째 두번째 열, 세번째 행
df.iloc[0, -2:]       # 첫번째 열, 세번째 행부터 마지막행
df.iloc[2:3, 1:3]     # 두번째 열, 두번째 세번째 행


# loc 인덱서와 마찬가지로 인덱스가 하나만 들어가면 행을 선택한다.
df.iloc[-1]
df.iloc[-1] * 2


### at, iat 인덱서
# at, iat 인덱서는 loc, iloc 인덱서와 비슷하지만 하나의 스칼라 값을 뽑을 때만 사용한다.
# 빠른 인덱싱 속도가 요구되는 경우에 사용한다.
%timeit df.loc["a", "A"]
%timeit df.at["a", "A"]
%timeit df.iloc[0, 0]
%timeit df.iat[0, 0]