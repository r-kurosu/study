#include<iostream>
#include<bits/stdc++.h>
// #include <algorithm>
using namespace std;
const int INTMAX=10000000;

pair<int, pair<int, int> >p[INTMAX];

int index_i[INTMAX];
int cost,n,m;

int findroot(int i){
	int i_d = i;
	while(i_d!=index_i[i_d]){
		i_d=index_i[i_d];
	}
	index_i[i] = i_d;
	return i_d;
}

void spanning(){
	for(int i=0;i<m;i++){
		int w=p[i].first;
		int u=p[i].second.first;
		int v=p[i].second.second;

		int x=findroot(u); //始点のrootを取得
	    int y=findroot(v); //終点のrootを取得

		if(x!=y){
            u=findroot(u);
	        v=findroot(v);
	        index_i[u]=v;
			cost+=w;
		}

	}
}

int main(){
	int i,j;
	cin>>n>>m;
	for(i=0;i<m;i++){
		int x,y,z;
		cin>>x>>y>>z;
		p[i]=make_pair(z,make_pair(x,y));
	}

    for(int i=0;i<n;i++){
		index_i[i]=i;
	}

	sort(p, p+m);
	// sort(p.begin(), p.end());

	spanning();

	cout<<cost<<"\n";


}