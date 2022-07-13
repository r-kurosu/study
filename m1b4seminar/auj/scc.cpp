#include<bits/stdc++.h>

using namespace std;

typedef vector<int> vec;
const int N=1e4+10;

int V,E;
vec G[N],rG[N],res;
bool used[N];
int cmp[N];
int k;

void add(int s,int t)
{
    G[s].push_back(t);
    rG[t].push_back(s);
}

void dfs(int v)
{
    used[v]=true;
    for(int i=0;i<G[v].size();i++)
    {
        int to=G[v][i];
        if(!used[to])
        {
            dfs(to);
        }
    }
    res.push_back(v);
}

void rdfs(int v,int color)
{
    used[v]=true;
    cmp[v]=color;
    for(int i=0;i<rG[v].size();i++)
    {
        int to=rG[v][i];
        if(!used[to])
        {
            rdfs(to,color);
        }
    }
}

void scc()
{
    memset(used,0,sizeof(used));
    for(int i=0;i<V;i++)
    {
        if(!used[i])
        {
            dfs(i);
        }
    }
    memset(used,0,sizeof(used));
    k=0;
    for(int i=res.size()-1;i>=0;i--)
    {
        if(!used[res[i]])
        {
            rdfs(res[i],k++);
        }
    }
}

int main()
{
    cin>>V>>E;

    for(int i=0;i<E;i++)
    {
        int s,t;
        cin>>s>>t;
        add(s,t);
    }

    scc();

    int q;
    cin>>q;

    while(q--)
    {
        int u,v;
        cin>>u>>v;
        cout<<(cmp[u]==cmp[v])<<endl;
    }

    return 0;
}