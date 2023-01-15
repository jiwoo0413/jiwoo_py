# print("Hello, World!")

# #숫자 자료형
# a=1
# b=2.23
# c = 1.13e10 #e는 지수표현
# d=a*b
# e=a/b #나누기
# f=a//b #몫
# g=a**b #제곱

# print(a)
# print(type(a))

# print(b)
# print(type(b))

# print(c)
# print(type(c))

# print(d)
# print(type(d))

# print(e)
# print(type(e))

# print(f)
# print(type(f))

# print(g)
# print(type(g))





#문자열 자료형
# a = "Hello, World!"
# b = 'Hello, World!'
# # c='jiwoo's python ->''사이에 '가 있어서 오류남
# c='jiwoo\'s python' #\백슬래쉬는 그 오류를 방지->\는 문자를 그대로 사용할 때 사용
# d='Hello, \nWorld!'
# e="""Hello,


# World""" #"""은 다른 줄바꿈같은 이스케이프 문자를 쓰지 않아도 스스로 인식해서 출력
# f= a+b 
# g="Hello, World"
# h= "I eat %d apples." %3 # -> "I eat " + str(3) + " apples."...보다 간단하게 씀
# number = 10
# day = "three"
# i= "I eat %d apples. so I was sick for %s days." %(number, day) #%d는 정수 %s는 문자열 %f는 실수
# j="I am {}.".format("jiwoo") #{}안에 .format으로 jiwoo 넣음
# k="%10s" %"hi"
# l=",".join("abcd") #abcd 사이에 ,를 넣어서 출력
# m=",".join(["a","b","c"])
# o=["홍지우", "유채린", "김은지", "이은혜"] #리스트 만들기

# print(a)
# print(type(a))
# print('\n')

# print(a * 2) #a를 두번 출력해라
# print(a+c) #a와 c를 더해서 출력해라
# print(a.count('l')) #함수 a에서 l의 개수를 출력
# print(a.find('l')) #함수 a에서 l의 인덱스 번호(0부터 시작해서 처음 l의 자리) 출력 없으면 -1 출력됨
# print(a.index('l')) #함수 a에서 l의 인덱스를 출력 없으면 에러
# print(a.upper()) #함수 a를 대문자로 출력
# print(a.lower()) #함수 a를 소문자로 출력
# print(a.replace("Hello", "Hi")) #Hello를 Hi로 바꿔서 출력
# print(a.split( )) #띄어쓰기 기준으로 잘라서 출력 '도 잘라서 출력 ()안에 있는 문자를 기준으로 자름
# print('\n')

# print(b)
# print(type(b))
# print('\n')

# print(c)
# print(type(c))
# print('\n')

# print(d)
# print(type(d))
# print('\n')

# print(e)
# print(type(e))
# print('\n')

# print(f)
# print(type(f))
# print('\n')

# print(g[0]) #배열
# print(g[-2]) #뒤에서 두번째
# print(g[0:4:2]) #0이상 4미만 2간격 0자리를 비우면 무조건 처음부터 시작 4자리를 비우면 끝까지
# print(g[::-1]) #반대로 출력됨
# print(type(g[0]))
# print('\n')

# print(h)
# print(type(h))
# print('\n') 

# print(i)
# print(type(i))
# print('\n')

# print(j)
# print(type(j))
# print('\n')

# print(k)
# print(type(k))
# print('\n')

# print(l)
# print(type(l))
# print('\n')

# print(m)
# print(type(m))
# print('\n')

# print(o[1])
# del o[0] #o리스트의 0번째(홍지우) 삭제
# print(o)
# o.append("jiwoo") #o리스트의 맨 마지막에 jiwoo 추가 
# print(o)
# o.sort() #영어 먼저 알파벳 순서로 한글은 가나다 순서로 정렬 숫자는 123순서로 저열 
# print(o)
# o.pop()
# print(o)
# print(o.pop) ######왜 안됨??
# print(o)
# print(type(o))
# o.extend([2,3]) #2,3을 추가
# print(o)
# print('\n')




#나머지 자료형
#튜플-()로 열고 닫음 리스트와 다르게 고정된 길이와 값들
t1=(1,2,'a', 'b')
t2=(3,4)
#del t1[0] 안됨 값을 변경할 수 없다.
print(t1)
print(t1+t2)
print(t2*3)
print("\n")


#딕셔너리-사전(연관배열, 해시)-키(name)와 value(jiwoo)로 이루어짐
dic = {'name': 'jiwoo', 'age': 22}
print(dic['name'], dic['age'])
a={1:'a'}
a['name'] ="익명" #a딕셔너리에 name 추가
print(a)
del a['name'] #a딕셔너리 안에 있는 'name' 삭제
print(a)
print('\n')

b={1:'a', 1:'b'} #마지막 1만 남음 키가 겹치면 안됨 value는 겹쳐도 된다
print(b)
print('\n')

c={1:'홍지우', 2:'유채린', 3:'김은지'} #반복문에 많이 쓰이는 방법
print(c.keys())
print(c.values())
print(c.items()) 
print('\n')
for k in c.keys():
    print(k)
for k in c.values():
    print(k)
for k in c.items():
    print(k)
print('\n')

for k, v in c.items():
    print("키는: " + str(k))
    print("value는: " + v)
print('\n')
#c.clear() #딕셔너리 비우기
print(c)
print('\n')

print(c.get(3)) #3이 비었지만 get을 쓰면 오류가 나지 않고 비어있는 None이 출력
#print(c[3]) #위 print(a.get(3))과는 다르게 오류가 남
print(c.get(4,'jiwoo')) #4가 없지만 get으로 추가하고 jiwoo를 넣어서 출력
print('\n')

print(4 in c) #4가 c에 있다면 True 없다면 False가 출력
print(1 in c)