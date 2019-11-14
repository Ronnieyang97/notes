# .机器人的运动范围
# 题目：地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
# 但是不能进入行坐标和列坐标的数位之和大于k的格子。请问该机器人能够达到多少个格子？

def farest(m, n, k):  # 获取棋盘的大小，和k的大小
    m, n = str(m), str(n)
    x, y = '', ''
    loc_m, loc_n = 0, 0
    while k > 0 and loc_m < len(m) and loc_n < len(n):
        if int(m[loc_m]) + int(n[loc_n]) > k:
            if m[loc_m] > n[loc_n]:
                m = m[:loc_m] + str(int(m[loc_m])-1) + m[loc_m+1:]
            else:
                n = n[:loc_n] + str(int(n[loc_n])-1) + n[loc_n+1:]
            continue
        else:
            x += m[loc_m]
            y += n[loc_n]
            k -= (int(m[loc_m]) + int(n[loc_n]))
            loc_m += 1
            loc_n += 1
    x, y = int(x), int(y)
    while len(str(x)) < len(m):
        x *= 10
    while len(str(y)) < len(n):
        y *= 10
    return x, y
    
# 发现了一个很严重的问题，如果要抵达（100，100）必须经过（99， 100）或（100，99），如果数位之和的上限k为12，则（100，100）符合条件但是前一个点不合符条件，程序有误
