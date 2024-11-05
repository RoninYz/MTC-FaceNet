import numpy as np
from collections import Counter
from fractions import Fraction

f = [
    [1, 5, 255, 255, 100, 200, 255, 200],
    [1, 7, 254, 255, 100, 10, 10, 9],
    [3, 7, 10, 100, 100, 2, 9, 6],
    [3, 6, 10, 10, 9, 2, 8, 2],
    [2, 1, 8, 8, 9, 3, 4, 2],
    [1, 0, 7, 8, 8, 3, 2, 1],
    [1, 1, 8, 8, 7, 2, 2, 1],
    [2, 3, 9, 8, 7, 2, 2, 0]
]

if __name__ == "__main__":
    fn = np.array(f)
    N = fn.size
    flat_fn = fn.ravel()  # 将二维数组展平为一维数组
    freq = Counter(flat_fn)  # 统计每个数字出现的频次

    # 按照数字从小到大排序
    sorted_freq = dict(sorted(freq.items()))
    val = []
    ori_list = []
    for k, v in sorted_freq.items():
        ori_list.append(k)
        val.append(Fraction(v, N))
    L = len(val)

    ori_dict = {}
    for i in range(len(ori_list)):
        ori_dict[i] = ori_list[i]

    # print(ori_dict)
    # 计算前缀和
    prefix_sum = []
    current_sum = Fraction(0, 1)
    for num in val:
        current_sum += num
        prefix_sum.append(current_sum)

    R = []
    for num in prefix_sum:
        temp = num * 14
        # 将 temp 转换为浮点数并四舍五入取整
        rounded_temp = round(float(temp))
        R.append(rounded_temp)

    Now_dic = {}
    for i in range(len(R)):
        Now_dic[ori_dict[i]] = ori_dict[R[i]]

    for i in range(fn.shape[0]):
        for j in range(fn.shape[1]):
            fn[i][j] = Now_dic[fn[i][j]]



