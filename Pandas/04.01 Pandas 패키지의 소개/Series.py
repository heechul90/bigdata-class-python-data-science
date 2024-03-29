### 시리즈 클래스¶
import pandas as pd
import numpy as np

## 시리즈 클래스는 NumPy에서 제공하는 1차원 배열과 비슷하지만
## 각 데이터의 의미를 표시하는 인덱스(index)를 붙일 수 있다.
## 데이터 자체는 값(value)라고 한다.

# 시리즈 = 값(value) + 인덱스(index)
s = pd.Series([9904312, 3448737, 2890451, 2466052],
              index=["서울", "부산", "인천", "대구"])
s


# 인덱스를 지정하지 않고 시리즈를 만들면 시리즈의 인덱스는 0부터 시작하는 정수값이 된다.
pd.Series(range(10, 14))


# 시리즈의 인덱스는 index 속성으로 접근할 수 있다.
# 시리즈의 값은 1차원 배열이며 values 속성으로 접근할 수 있다.
s.index
s.values

# name 속성을 이용하여 시리즈 데이터에 이름을 붙일 수 있다.
# index.name 속성으로 시리즈의 인덱스에도 이름을 붙일 수 있다.

s.name = "인구"
s.index.name = "도시"
s


## 시리즈 연산
## NumPy 배열처럼 시리즈도 벡터화 연산을 할 수 있다.
## 다만 연산은 시리즈의 값에만 적용되며 인덱스 값은 변하지 않는다.
s / 1000000



## 시리즈 인덱싱¶
## 시리즈는 NumPy 배열에서 가능한 인덱스 방법 이외에도
## 인덱스 라벨을 이용한 인덱싱도 할 수 있다.
## 배열 인덱싱이나 인덱스 라벨을 이용한 슬라이싱(slicing)도 가능하다.
s[1], s["부산"]
s[3], s["대구"]

# 배열 인덱싱을 하면 자료의 순서를 바꾸거나 특정한 자료만 선택할 수 있다.
s[[0, 3, 1]]
s[["서울", "대구", "부산"]]
s[(250e4 < s) & (s < 500e4)]

# 문자열 라벨을 이용한 슬라이싱을 하는 경우에는
# 콜론(:) 기호 뒤에 오는 인덱스에 해당하는 값도 결과에 포함되므로 주의
s[1:3]
s["부산":"대구"]

# 만약 라벨 값이 영문 문자열인 경우에는
# 마치 속성인것처럼 점(.)을 이용하여 접근할 수도 있다.
s0 = pd.Series(range(3), index=["a", "b", "c"])
s0

s0.a
s0.b



## 시리즈와 딕셔너리 자료형
## 딕셔너리 자료형에서 제공하는 in 연산도 가능하고
## items 메서드를 사용하면 for 루프를 통해
## 각 원소의 키(key)와 값(value)을 접근할 수도 있다.

"서울" in s
"대전" in s

for k, v in s.items():
    print("%s = %d" % (k, v))

# 딕셔너리 객체에서 시리즈를 만들 수도 있다.
s2 = pd.Series({"서울": 9631482, "부산": 3393191, "인천": 2632035, "대전": 1490158})
s2

# 딕셔너리의 원소는 순서를 가지지 않으므로 시리즈의 데이터도 순서가 보장되지 않는다.
# 만약 순서를 정하고 싶다면 인덱스를 리스트로 지정해야 한다.
s2 = pd.Series({"서울": 9631482, "부산": 3393191, "인천": 2632035, "대전": 1490158},
               index=["부산", "서울", "인천", "대전"])
s2



## 인덱스 기반 연산¶
## 두 시리즈에 대해 연산을 하는 경우 인덱스가 같은 데이터에 대해서만 차이를 구한다.
ds = s - s2
ds

s.values - s2.values

ds.notnull()
ds[ds.notnull()]

# 인구 증가율(%)
rs = (s - s2) / s2 * 100
rs = rs[rs.notnull()]
rs



## 데이터의 갱신, 추가, 삭제¶
## 인덱싱을 이용하면 딕셔너리처럼 데이터를 갱신(update)하거나 추가(add)할 수 있다.
rs["부산"] = 1.63
rs

rs["대구"] = 1.41
rs

# 데이터를 삭제할 때도 딕셔너리처럼 del 명령을 사용
del rs["서울"]
rs