#include <iostream>
#include <stack>
#include <list>
#include <fstream>
#include <climits>
#include <queue>
#include <string>

using namespace std;

struct Edge{
    int des_vertex;
    int weight;
    Edge(int des, int wei) : des_vertex(des), weight(wei) {}
};

struct Node{
    int id;
    int sp_est; // estimate of shortest-path distance

    Node(int id_, int sp_est_) : id(id_), sp_est(sp_est_) {}
    void update(int id_, int sp_est_){
        this->id = id_; this -> sp_est = sp_est_;
    }
    bool operator < (const Node &ref_node) const{
        return this-> sp_est > ref_node.sp_est;
    }
};

struct Graph{
    int V; //number of vertexes
    int srcVer; // the source vertex
    list<Edge>* adj; //pointer to save adjacent vertexes of each vertex

    Graph(int nv, int s){
        V = nv; // number of vertices in the graph
        srcVer = s; // the source vertex
        adj = new list<Edge>[nv];
    };
    void addEdge(int u, int v, int d){
            Edge myEdge(v, d);
            adj[u].push_back(myEdge);
    };
    void printGraph(){
        cout << "my graph:\n";
        for (int i = 0; i < V; i++) {
            cout <<  "adj[" << i << "]: ";
            list<Edge>::iterator it;
            for(it = adj[i].begin(); it != adj[i].end(); ++it) {
                cout << "(" << it->des_vertex << ", " << it->weight << ") ";
            }
            cout << "\n";
        }
    };
    void dijkstra(); // Single Source Shortest Path
};

// input cmd 
Graph input_cmd () {
   int number_of_Vertex, number_of_Edge, r;
   cin >> number_of_Vertex >> number_of_Edge >> r;

   Graph myGraph(number_of_Vertex, r);
   int a, b, c;
   for (int i = 0; i < number_of_Edge; i++) {
       cin >> a >> b >> c;
       myGraph.addEdge(a, b, c);
   }

   return myGraph;
}

int main(){
    Graph myGraph = input_cmd();
    myGraph.dijkstra();
    return 0;
}


void Graph::dijkstra() { 
     int distance[V]; //temp solution
     int parent_node[V]; // parent node of temp shotest path
     bool isDetermined[V]; // false: not determined, true: determined

     for (int i = 0; i < V; i++) {
        distance[i] = INT_MAX; parent_node[i] = -1; isDetermined[i] = false;
     }

     // determin v_0
     distance[srcVer] = 0; 
     isDetermined[srcVer] = true;

     //define priority_queue and push v_0
     priority_queue<Node> prique;
     Node node(srcVer, 0);
     prique.push(node);

     while (!prique.empty()) {
         // find the vertex having the shortest path
         node = prique.top(); prique.pop();
         int u = node.id;
         isDetermined[u] = true;

         // relax each edge terminating from u
         list<Edge>::iterator it;
         for(it = adj[u].begin(); it != adj[u].end(); ++it) {
             if (!isDetermined[it->des_vertex]) {
                 if (distance[it->des_vertex] > distance[u] + it->weight) {
                     distance[it->des_vertex] = distance[u] + it->weight;
                     parent_node[it->des_vertex] = u; // for printing the shortest paths later
                     node.update(it -> des_vertex, distance[it->des_vertex]);
                     prique.push(node);
                 }
             }
         }
     }

     // print out the shortest-paths distance
     for (int i = 0; i < V; i++) {
         if (distance[i] < INT_MAX) {cout << distance[i] << endl;} else {cout << "INF\n";}
     }
 }
