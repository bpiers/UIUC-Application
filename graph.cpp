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

    void print_vertices(vector<Vertex> v){
      for(int i = 0; i < v.size(); i++){
        cout << v.at(i).key << " ";
      }
      cout << endl;
      return;
    }

    void print_edges(vector<Edge> e){
      vector<Edge>::iterator it;
      for(it = e.begin(); it != e.end(); ++it){
        cout << it->source->key << " (" << it->weight << ") " << it->destination->key << endl;
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

    void min_dist(int s, int d){
      return;
    }

    vector<Edge> combine_edges(vector<Edge> e1, vector<Edge> e2){
      vector<Edge>::iterator it;

      for(it = e2.begin(); it != e2.end(); ++it){
        e1.push_back(*it);
      }
      return e1;
    }

    Edge find_min_edge(vector<Edge> e){
      //cout << "entered find_min_edge func..." << endl;
      Edge min_e = e.at(0);
      vector<Edge>::iterator it;
      for(it = e.begin(); it != e.end(); ++it){
        if(it->weight < min_e.weight){
          min_e = *it;
        }
      }
      return min_e;
    }

    //remove all Edges, e, that have destination Vertex, v
    //returns all edges under consideration
    vector<Edge> cleanup_dead_edges(vector<Vertex> v, vector<Edge> e){
      vector<Vertex>::iterator it_v;
      vector<Edge>::iterator it_e;

      it_e = e.end();
      while(it_e != e.begin()){
        it_e--;
        it_v = v.begin();
        while(it_v != v.end()){
          if(it_e->destination->key == it_v->key){
            e.erase(it_e);
            break;
          }
          it_v++;
        }
      }
      return e;
    }

    void MST(){
      vector<Vertex> mst_v;
      vector<Edge> mst_e;
      vector<Edge> all_e;
      Vertex current_v = v_list.at(0);
      while(mst_v.size() < v_list.size()){
        mst_v.push_back(current_v);
        all_e = combine_edges(all_e, current_v.edges);
        all_e = cleanup_dead_edges(mst_v, all_e);
        if(mst_v.size() < v_list.size()){
          mst_e.push_back(find_min_edge(all_e));
          current_v = *((mst_e.end()-1)->destination);
        }
      }
      print_edges(mst_e);
    }



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
  cout << "printing graph..." << endl;
  test.print_graph();
  cout << endl << "printing minimum spanning tree..." << endl;
  test.MST();
  //cout << "end of main" << endl;
}
