from fun import *

a = {3500: 72, 3000: 72, 2000: 72, 1000: 72}
a = list_or_dict(a)
print(a)


# a = [5000,3000,3000,2000,2000,1000,1000,500,500,500]
def caiqie3(li, max_number=6000):
    aa = li[:]
    s = 0  # 所需数量
    h = []
    b = []
    while len(aa):
        b.append(max_number)
        s = s + 1
        # k = 1
        while sorted(b)[-1] >= sorted(aa)[-1]:
            # 循环从b内获取最小值
            min_num = sorted(b)[-1]
            print("b内最小值{}".format(min_num))
            # 在a内组合出最合适的组合
            for k in zuhe(aa, min_num)[::-1]:

                h.append(k)
                print("a内最佳组合{}".format(k))
                # 剔除a内的组合
                for i in k:
                    aa.remove(i)
                    print("从a内弹出{}".format(i))
                b.remove(min_num)
                if max_number - sum(k):
                    b.append(max_number - sum(k))
                break
            break

    return s, h, b

a = [6,4,2,1,1]
b = [5,2,2,1]
for i in a:
    for j in b:
        if i == j:
            a.remove(i)
            b.remove(j)
print(a)
print(b)

def caiqie4(a,max_num):
    pass

