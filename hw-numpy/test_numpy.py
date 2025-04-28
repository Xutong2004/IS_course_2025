导入numpy库并命名为np
从numpy_tasks导入*

#np.__version__ - Numpy 的版本号应高于 2.0

def 测试1():

    断言等间隔(-1.2, 2.4, 7)的结果与数组(-1.2, -0.6, 0., 0.6, 1.2, 1.8, 2.4)相同。
def test2():
    断言 cyclic123_array(4) 等于 np.array([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])

def test3():
    断言前3个奇数（first_n_odd_number(3)）与数组[1, 3, 5]接近。

def test4():
    断言 zeros_array_with_border(4) 等于 np.array([[1., 1., 1., 1.],
                                                             [1., 0., 0., 1.]
                                                             [1., 0., 0., 1.]
                                                             [1., 1., 1., 1.]]))
def test5():



    断言 chess_board(3) 等于 np.array([[1., 0., 1.],
                                                 [0., 1., 0.]
                                                 [1., 0., 1.]]))

def test6():
    断言 matrix_with_sum_index(3) 等于 np.array([[0, 1, 2],
                                                           [1, 2, 3]
                                                           [2, 3, 4]]))
def test7():
    断言 np.allclose(cos_sin_as_two_rows(0, 1, 0.25), np.array([[1.        , 0.96891242, 0.87758256, 0.73168887],
                                                                  [0.        , 0.24740396, 0.47942554, 0.68163876]]))

def test8():


    np.random.seed(42)
    A = np.random.rand(3, 5)
    平均值, 行和, 列和 = 计算平均值行和列和(A)
    断言 np.abs(mean - 0.49456456164468965) < 1e-12
    断言 rows_sum 等于数组 [0.55111913, 1.97870777, 2.43061273, 1.41211261, 1.04591619]。
    断言 columns_sum 等于数组 [2.81192549, 2.38944187, 2.21710107]。

def test9():


    np.random.seed(42)
    A = np.random.rand(5, 5)
    断言 np.allclose(sort_array_by_column(A, 1), np.array([[0.15599452, 0.05808361, 0.86617615, 0.60111501, 0.70807258],
                                                             [0.61185289, 0.13949386, 0.29214465, 0.36636184, 0.45606998]
                                                             [0.18340451, 0.30424224, 0.52475643, 0.43194502, 0.29122914]
                                                             [0.37454012, 0.95071431, 0.73199394, 0.59865848, 0.15601864]
                                                             [0.02058449, 0.96990985, 0.83244264, 0.21233911, 0.18182497]

def test10():


    f1 = lambda x: (x**2 + 3) / (x - 2)
    断言 np.allclose(compute_integral(3, 4, f1, 0.001, method='rectangular'), 10.352030263919616, rtol=0.01)
    断言 np.allclose(compute_integral(3, 4, f1, 0.001, method="trapezoidal"), 10.352030263919616, rtol=0.01)
    断言 np.allclose(compute_integral(3, 4, f1, 0.001, method="simpson"), 10.352030263919616, rtol=0.001)

    f2 = lambda x: np.cos(x)**3
    断言 np.allclose(compute_integral(0, np.pi/2, f2, 0.001, method="rectangular"), 2/3, rtol=0.01)
    断言 np.allclose(compute_integral(0, np.pi/2, f2, 0.001, method="trapezoidal"), 2/3, rtol=0.01)
    断言 np.allclose输入：(计算积分(0, np.pi/2, f2, 0.001, method="simpson"), 2/3, rtol=0.001)
