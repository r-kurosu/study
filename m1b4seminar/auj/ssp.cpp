#include <iostream>

using namespace std;

const int Inf = 1000000000;


int main(){
    // input
    int V,E,R;
    cin >> V >> E >> R;

    int S[E], T[E], D[E];
    for (int i=0; i<E; ++i)
        cin >> S[i] >> T[i] >> D[i];

    //initialize cost of path
    int C[V];
    for(int i=0;i<V;i++){
        C[i] = Inf;
    }
    C[R] = 0;


    //calculate all paths
    for (int t=0; t<V; t++) {
        bool update = false;
        for (int i=0; i<E; i++) {
            int s = S[i], t = T[i], d = D[i];
            if (C[s] < Inf && C[t] > C[s]+d) {
                C[t] = C[s]+d;
                update = true;
            }
        }
        if (!update) break;
    }

    // output
    for(int i=0;i<V;i++){
        if(C[i]!=Inf)
            cout << C[i] << endl;
        else
            cout << "INF" << endl;
    }
}