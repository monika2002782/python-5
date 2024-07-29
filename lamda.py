##lamda
gift=lambda person:print("abinisha",person)
gift("watch")



x=lambda a,b:a*b
print(x(4,7))

def myfun(n):
  return lambda a:a*n
m=myfun(2)
print(m(11))
print(m(45))

##lamda examples using (mapping & splitering)
data=[1,2,3,4,5,6,7,8,9]
result1=map(lambda x:x*2,data)
print(list(result1))
print(result1)
result2=filter(lambda x:x%2==0,data)
print(list(result2))
print(result2)



# for i in range(1,11):
# #     print(i,"*","7","=",i*7)
# #  '''
# # name=lambda find:print("moni",find)
# # name("watch")
# # x=lambda a,b:a*b
# # print(x(4,7))

