import pulp

CPLEX_PATH = "/Applications/CPLEX_Studio221/cplex/bin/x86-64_osx/cplex"

K = 4 # 彩色数
n = 3 # 頂点数
A = [[0,0,0],[0,0,0],[0,0,0]] #隣接行列

def gcp(n, A, K):
    model = pulp.LpProblem("graph coloring problem", pulp.LpMinimize)
    
    # 変数定義
    x = [[0]*K]*n
    for i in range(n):
        for k in range(K):
            x[i][k] = pulp.LpVariable(f"x_{i}{k}", cat=pulp.LpBinary)

    # 制約条件
    for i in range(n):
        for j in range(n):
            if A[i][j] == 1:
                model += [x[i][k] != x[j][k] for k in range(K)]
        
        model += pulp.lpSum(x[i]) == 1

    # 目的関数
    model += 1
    
    # 求解
    status = model.solve(pulp.CPLEX(path=CPLEX_PATH))

    return

gcp(n, A, K)