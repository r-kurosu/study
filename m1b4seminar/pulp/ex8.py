import pulp

CPLEX_PATH = "/Applications/CPLEX_Studio221/cplex/bin/x86-64_osx/cplex"

n = 4

def suudoku(n):
    model = pulp.LpProblem("suudoku", pulp.LpMaximize)
    
    # 変数定義
    x = [[[0]*n]*n]*n
    for i in range(n):
        for j in range(n):
            for k in range(n):
                x[i][j][k] = pulp.LpVariable(f"x_{i}{j}{k}", cat=pulp.LpBinary)

    # 制約条件
    # 1. 各マス
    for i in range(n):
        for j in range(n):
            model += pulp.lpSum(x[i][j] for k in range(4)) == 1
    # 2. 行
    for i in range(n):
        for k in range(n):
            model += pulp.lpSum(x[i][j][k] for j in range(4)) == 1
    # 3. 列
    for j in range(n):
        for k in range(n):
            model += pulp.lpSum(x[i][j][k] for i in range(4)) == 1
    # 4. ブロック
    for i in [0,2]:
        for j in [0,2]:
            for k in range(n):
                model += x[i][j][k] + x[i+1][j][k] + x[i][j+1][k] + x[i+1][j+1][k] == 1
    # 5. 初期値
    model += x[0][0][1] == 1
    model += x[0][3][3] == 1
    model += x[2][2][1] == 1
    model += x[3][1][2] == 1
    
    # 目的関数
    model += pulp.lpSum(x[i][j][k] for i,j,k in range(4))
    
    # 求解
    status = model.solve(pulp.CPLEX(path=CPLEX_PATH))

    return