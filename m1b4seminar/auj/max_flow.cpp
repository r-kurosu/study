#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
const int INF = 1e9;
const int MAX_V = 10000;

struct Flow{
    struct edge{
        int to, cap, rev;
    };
    vector<edge> G[MAX_V];//隣接リスト
    bool used[MAX_V];

    void add_edge(int from, int to, int cap){
        G[from].push_back((edge){to, cap,(int) G[to].size()});
        G[to].push_back((edge){from, 0, (int) G[from].size() - 1});
    }

    //増加パスを探す
    int dfs(int v, int t, int f){
        if(v == t) return f;
        used[v] = true;
        for (int i = 0; i < G[v].size(); ++i){
            edge &e = G[v][i];
            if(!used[e.to] && e.cap > 0){
                int d = dfs(e.to, t, min(f, e.cap));
                if(d > 0){
                    e.cap -= d;
                    G[e.to][e.rev].cap += d;
                    return d;
                }
            }
        }
        return 0;
    }
    
    //sからtへの最大流
    int max_flow(int s, int t){
        int flow = 0;
        while(1){
            memset(used, 0, sizeof(used));
            int f = dfs(s, t, INF);
            if(f == 0) return flow;
            flow += f;
        }
    }
};

int main(){
 int V,E; 
 cin >> V >> E;
  Flow mf;
  for(int i = 0; i < E; i++){
   int u,v,c; 
   cin >> u >> v >> c; 
    // u and v have already been 0-indexed
    mf.add_edge(u,v,c);}
  
  cout << mf.max_flow(0, V - 1) << endl; 
  return 0;
  }