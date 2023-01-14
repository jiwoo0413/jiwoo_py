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
a = "Hello, World!"
b = 'Hello, World!'
# c='jiwoo's python ->''사이에 '가 있어서 오류남
c='jiwoo\'s python' #\백슬래쉬는 그 오류를 방지->\는 문자를 그대로 사용할 때 사용
d='Hello, \nWorld!'
e="""Hello,


World""" #"""은 다른 줄바꿈같은 이스케이프 문자를 쓰지 않아도 스스로 인식해서 출력
f= a+b 
g="Hello, World"
h= "I eat %d apples." %3 # -> "I eat " + str(3) + " apples."...보다 간단하게 씀
number = 10
day = "three"
i= "I eat %d apples. so I was sick for %s days." %(number, day) #%d는 정수 %s는 문자열 %f는 실수
j="I am {}.".format("jiwoo") #{}안에 .format으로 jiwoo 넣음
k="%10s" %"hi"
l=",".join("abcd") #abcd 사이에 ,를 넣어서 출력
m=",".join(["a","b","c"])
o=["홍지우", "유채린", "김은지", "이은혜"] #리스트 만들기

print(a)
print(type(a))
print('\n')

print(a * 2) #a를 두번 출력해라
print(a+c) #a와 c를 더해서 출력해라
print(a.count('l')) #함수 a에서 l의 개수를 출력
print(a.find('l')) #함수 a에서 l의 인덱스 번호(0부터 시작해서 처음 l의 자리) 출력 없으면 -1 출력됨
print(a.index('l')) #함수 a에서 l의 인덱스를 출력 없으면 에러
print(a.upper()) #함수 a를 대문자로 출력
print(a.lower()) #함수 a를 소문자로 출력
print(a.replace("Hello", "Hi")) #Hello를 Hi로 바꿔서 출력
print(a.split( )) #띄어쓰기 기준으로 잘라서 출력 '도 잘라서 출력 ()안에 있는 문자를 기준으로 자름
print('\n')

print(b)
print(type(b))
print('\n')

print(c)
print(type(c))
print('\n')

print(d)
print(type(d))
print('\n')

print(e)
print(type(e))
print('\n')

print(f)
print(type(f))
print('\n')

print(g[0]) #배열
print(g[-2]) #뒤에서 두번째
print(g[0:4:2]) #0이상 4미만 2간격 0자리를 비우면 무조건 처음부터 시작 4자리를 비우면 끝까지
print(g[::-1]) #반대로 출력됨
print(type(g[0]))
print('\n')

print(h)
print(type(h))
print('\n') 

print(i)
print(type(i))
print('\n')

print(j)
print(type(j))
print('\n')

print(k)
print(type(k))
print('\n')

print(l)
print(type(l))
print('\n')

print(m)
print(type(m))
print('\n')

print(o[1])
print(type(o))
print('\n')