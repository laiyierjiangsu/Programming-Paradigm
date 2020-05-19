from functools import reduce
func = lambda s: s*2
l = map(func,[1,2,3,4,5])
print(list(l))

plus = lambda x,y : (x or 0 ) + (y+ 0)
l = map(plus,[1,2,3],[4,5,6])
print(list(l))

l = reduce(plus,[2,3])
print(l)

mode2 = lambda x: x % 2
l = filter(mode2, [1,2,3,4,5,6])
print(list(l))

# 替换条件控制语句
pr = lambda s: s
print_num = lambda x : (x == 1 and pr("one"))\
            or (x == 2 and pr("two"))\
            or (x == 3 and pr("three"))
print(print_num(1) )

#替换for循环
square = lambda x: x*x
#for x in [1,2,3]: square(x)
l = map(square,[1,2,3])
print_num(list(l))

# 替换while循环: 通过递归来实现while循环
def monadic_print(x):
    print(x)
    return x

echo_FP = lambda: monadic_print(input("FP -- "))=='quit' or echo_FP()
echo_FP()