导入numpy库并命名为np

def uniform_intervals(a, b, n):


    """1. 创建numpy数组 - 将区间从a到b均匀分割成n个段。"""
    返回 np.linspace(a, b, n)

定义一个名为cyclic123_array的函数，参数为n：
    """2. 生成长度为3n的numpy数组，填充循环数字1, 2, 3, 1, 2, 3, 1..."""
    返回 np.tile([1, 2, 3], n)

def first_n_odd_number(n):
    """3. 创建前 n 个奇数的数组"""
    返回 np.arange(1, 2*n+1, 2)

def zeros_array_with_border(n):
    return np.zeros((n+2, n+2))
    返回 np.zeros((n+2, n+2))
    返回 np.zeros((n+2, n+2))
    """4. 创建一个 n x n 大小的数组，边缘由 1 组成，内部为 0。"""
    arr = np.zeros((n, n))
    arr[[0, -1], :] = 1  # 第一行和最后一行
    arr[:, [0, -1]] = 1  # 第一列和最后一列
    返回 arr

定义一个国际象棋棋盘函数 chess_board(n):
    """5. 创建一个 n x n 的数组，包含棋盘上的0和1"""
    board = np.zeros((n, n))
    board[::2, ::2] = 1  # 偶数行的偶数格子
    board[1::2, 1::2] = 1  # 奇数行中的奇数格
    返回棋盘

def matrix_with_sum_index(n):


    """6. 创建一个 n × n 的矩阵，其中 (i,j) 元素等于 i+j."""
    rows = np.arange(n).reshape(-1, 1)
    cols = np.arange(n).reshape(1, -1)
    返回行数 + 列数

定义 cos 和 sin 为两行(a, b, dx):
    """7. 在区间 [a, b) 上以步长 dx 计算 cos(x) 和 sin(x)，
    然后将两个数字数组合并为一个字符串数组。 "''"
    x = np.arange(a, b, dx)
    cos_x = np.cos(x)
    sin_x = np.sin(x)
    返回 np.vstack([cos_x, sin_x])

def compute_mean_rowssum_columnssum(A):
    行和的平均值
    列和的平均值
    总和的平均值
    返回行平均值、列平均值、总平均值
    行和的平均值
    列和的平均值
    总和的平均值
    返回行平均值、列平均值、总平均值
    """8. 对于numpy数组A，计算所有元素的平均值、行和和列和。"""
    mean = np.mean(A)
    行和 = np.sum(A, axis=1)
    列和 = np.sum(A, axis=0)
    返回均值，列和，行和

def sort_array_by_column(A, j):


    """9. 按照j列升序对numpy数组A的行进行排序。"""
    返回 A[np.argsort(A[:, j])]

def compute_integral(a, b, f, dx, method):
    计算积分的函数
    a: 积分下限
    b: 积分上限
    f: 被积函数
    dx: 自变量的增量
    method: 积分方法，例如 'trapezoidal'（梯形法）或 ' Simpsons'（辛普森法）
    返回: 积分结果

    计算积分的函数
    a: 积分下限
    b: 积分上限
    f: 被积函数
    dx: 自变量的增量
    方法: 积分方法，例如 'trapezoidal'（梯形法）或 'Simpsons'（辛普森法）
    返回: 积分结果

    """10. 使用3种方法计算函数f在区间[a, b]上的定积分，步长为dx：  
    method == 'rectangular' - 方法为矩形法   
    method == 'trapezoidal' - 方法为梯形法   
    方法为辛普森法  
    '"""
    n_intervals = int((b - a) / dx)
    x = np.linspace(a, b, n_intervals + 1)
    
    if method == '矩形':

        x_mid = x[:-1]  # 左端点
        return np.sum(f(x_mid)) * dx

    elif method == 'trapezoidal':
        y = f(x)
        return (y[0] + 2 * np.sum(y[1:-1]) + y[-1]) * dx / 2

    elif method == 'simpson':
        if n_intervals % 2 == 1:  # 需要偶数个区间 → 奇数个点
            x = np.linspace(a, b, n_intervals + 2)
            dx = (b - a) / (n_intervals + 1)
        
        y = f(x)
        return dx / 3 * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])

    否则:
        抛出 ValueError("未知的方法。使用 '矩形', '梯形' 或 '辛普森'。")
