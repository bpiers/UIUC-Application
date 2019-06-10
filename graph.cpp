#include <iostream>  //cin and cout, inputs and outputs
#include <fstream>   //fstream, reading files
#include <string>    //string, making strings
#include <vector>    //,making vectors
using namespace std;

class Graph{
  public:

    //declare prototype Edge because Vertex uses it
    struct Edge;

    struct Vertex{
      int key;
      vector<Edge> edges;
    };

    struct Edge{
      int weight;
      Vertex* source;
      Vertex* destination;
    };

    vector<Vertex> v_list;

    Vertex* find_vertex(int v){
      for(int i = 0; i < v_list.size(); i++){
        if(v_list.at(i).key == v){
          return &v_list[i];
        }
      }
      return nullptr;
    }

    void add_vertex(int v){
      if(!find_vertex(v)){
        Vertex temp;
        temp.key = v;
        v_list.push_back(temp);
      }
      return;
    }

    void add_edge(int s, int d, int w){
      //cout << s << w << d << endl;
      Edge e;
      e.weight = w;
      e.destination = find_vertex(d);
      Vertex* src = find_vertex(s);
      e.source = src;
      vector<Edge>::iterator it;
      it = src->edges.begin();
      while(it != src->edges.end() && w > it->weight){
          it++;
      }
      src->edges.insert(it, e);
      return;
    }

    void add_edge2(int a, int b, int w){
        add_edge(a, b, w);
        add_edge(b, a, w);
      return;
    }

    void print_vertices(){
      for(int i = 0; i < v_list.size(); i++){
        cout << v_list.at(i).key << endl;
      }
      return;
    }

    void print_graph(){
      vector<Edge> edges_list;
      for(int i = 0; i < v_list.size(); i++){
        cout << v_list.at(i).key << " |";
        edges_list = v_list.at(i).edges;
        for(int j = 0; j < edges_list.size(); j++){
          Edge e = edges_list.at(j);
          cout << " " << e.destination->key << "(" << e.weight << ")";
        }
        cout << endl;
      }
      return;
    }

/*
    Edge min_edge(Vertex v){
      vector<Edge> ve = v.edges;
      Edge min_e = ve.at(0);
      for(int i = 1; i < ve.size(); i++){
        if(ve.at(i).weight < min_e.weight){
          min_e = ve.at(i);
        }
      }
      //cout << min_e.weight << endl;
      //cout << &min_e;
      return min_e;
    }
*/

    void min_dist(int s, int d){
      return;
    }



    // void MST(){
    //   vector<Edge> all_e;
    //   vector<Vertex> all_v;
    //   all_v.push_back(v_list.at(0));
    //   int min_w = 0;
    //
    //   Vertex* temp_v = v_list.at(0);
    //
    //   while
    //
    //
    //     return;
    // }



};//END OF graph CLASS

int main(){
  Graph test;
  test.add_vertex(1);
  test.add_vertex(2);
  test.add_vertex(3);
  test.add_vertex(4);
  test.add_vertex(5);
  test.add_vertex(6);
  test.add_edge2(1, 6, 5);
  test.add_edge2(1, 4, 2);
  test.add_edge2(4, 6, 1);
  test.add_edge2(6, 5, 4);
  test.add_edge2(6, 3, 2);
  test.add_edge2(5, 3, 3);
  test.add_edge2(3, 2, 1);
  cout << "print" << endl;
  test.print_graph();

  cout << "end of main" << endl;
}
