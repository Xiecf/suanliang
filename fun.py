# coding=utf-8
def baohan(a, b):
    """
    判断a内是否包含b内的所有元素
    :param a: list
    :param b: list
    :return: 0/1
    """
    import copy

    c = copy.deepcopy(a)
    k = 1
    for i in b:
        if i in c:
            c.remove(i)
        else:
            k = 0
            break
    return k


def zuhe(a, max_number=6000):
    """
    获取列表中所有元素的不大于指定值的任意组合,并去除超出元素数量的子集
    :param a: list
    :param max_number: 组合的和的最大值
    :return: list,组合方式
    """

    from itertools import combinations_with_replacement

    # print("\t开始对{}进行不大于{}的组合:".format(a, max_number))

    aa = list(set(a))[:]
    # print("\t去重后：{}".format(a))
    b = []
    o = int(max_number / min(aa)) + 1
    for i in range(1, o):
        b = b + list(combinations_with_replacement(aa, i))
    # 删除列表中元素大于指定值的元素
    k = 0
    while k < len(b):
        if sum(b[k]) > max_number or not baohan(a,b[k]):
            del b[k]
        else:
            k += 1
    # 删除非子集的组合
    # bb = b[:]
    # for i in bb:
    #     if not baohan(a,list(i)):
    #         b.remove(i)


    # 将组合排序
    # print("\t组合结果共计{}种为：\n{}。".format(len(b), b))
    return sorted(b, key=lambda x: sum(x))


def caiqie(all_size, standard_size=6000):
    """
    铝料裁切,
    :param all_size: list,所有裁切尺寸
    :param standard_size: int,标准料长
    :return: list,元素为每根料的裁切方式
    """
    s = zuhe(all_size, standard_size)
    x = []
    for i in s[::-1]:
        while baohan(all_size, i):
            x.append(i)
            for j in i:
                all_size.remove(j)
    print("\t共需长度为{}的型材{}根，截断方式如下：\n\t\t{}.".format(standard_size, len(x), x))
    liaotou = []
    for i in x:
        if standard_size - sum(i):
            liaotou.append(standard_size - sum(i))
    print(
        "\t剩余料头{}根,总长度为{}米,尺寸为:\n\t\t{}.".format(
            len(liaotou), sum(liaotou) / 1000, liaotou
        )
    )
    print("\t出材率：{:.0%}。".format(1 - sum(liaotou) / standard_size / len(x)))
    return x


def glass(fenge, style, row=60, column=60, glue_seam=15):
    """
    由分格尺寸及幕墙样式，获取玻璃尺寸。
    未考虑飞边及边龙骨！
    :param fenge: ((自左向右宽度),(自上而下高度))
    :param style: 00全隐，01横隐竖明，10横明竖隐，11全明
    :param row: 横梁迎面宽度，默认60mm
    :param column: 立柱迎面宽度，默认60mm
    :param glue_seam: 隐框幕墙胶缝宽度，默认15mm
    :return: 玻璃尺寸
    """
    a = []
    g = ()
    for i in fenge[0]:
        for j in fenge[1]:
            if style == 0:
                # 全隐
                g = (i - glue_seam, j - glue_seam)
            elif style == 1:
                # 横隐竖明
                g = (i - column + 30, j - glue_seam)
            elif style == 10:
                # 横明竖隐
                g = (i - glue_seam, j - row + 30)
            elif style == 11:
                # 全明
                g = (i - column + 30, j - row + 30)
            else:
                pass
            a.append(g)
            if g[0] >= 2400 and g[1] >= 2400:
                print("{}超过标准尺寸！".format(g))
    return a


def fukuang(glass_format):
    """
    由玻璃尺寸获取副框尺寸汇总
    未考虑飞边！！！！
    :param glass_format: 玻璃尺寸dict
    :return: list
    """

    a = []
    if isinstance(glass_format, dict):
        for i in glass_format:
            for j in range(glass_format[i]):
                a.append(i[0])
                a.append(i[1])
    elif isinstance(glass_format, list):
        for i in glass_format:
            a.append(i[0])
            a.append(i[0])
            a.append(i[1])
            a.append(i[1])
    a.sort()

    return a


def list_or_dict(a):
    s = []
    if isinstance(a, dict):
        s = []
        for i in a.keys():
            for j in range(a[i]):
                s.append(i)
    elif isinstance(a, list):
        s = {}
        for i in a:
            if i in s.keys():
                s[i] += 1
            else:
                s[i] = 1

    return s


def caiqie2(all_size, max_size=6000, min_size=0):
    all_size.sort(reverse=True)
    x = []

    liaotou = []
    while len(all_size):
        b = max_size
        i = 0
        s = []
        while b >= min_size and i < len(all_size):
            c = b - all_size[i]
            if c >= min_size:
                s.append(all_size[i])
                b = c
            i += 1
        for i in s:
            all_size.remove(i)
        x.append(s)
        if sum(s) <= max_size:
            liaotou.append(max_size - sum(s))

    print(
        "共需长度为{}的型材{}根，裁切方式如下:\n\t{}\n剩余料头{}个，尺寸如下：\n\t{}\n\t出材率：{:.0%}。".format(
            max_size,
            len(x),
            x,
            len(liaotou),
            liaotou,
            1 - sum(liaotou) / max_size / len(x),
        )
    )
    return x, liaotou


if __name__ == "__main__":
    fenge = ((750, 1500, 810, 810), (1000, 1150, 1150))  # 窗户中到中分格,(宽，高)
    a = glass(fenge, 11)
    print(a)
    fukuang(a)
