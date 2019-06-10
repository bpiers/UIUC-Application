//Linked List
//takes string. if you are trying to sort numerically, you will be disapointed.
#include <iostream>
#include <string>
#include <fstream>
#include <stdlib.h>
using namespace std;

class linked_list {
  struct Node {
    string key;
    Node* next = nullptr;
    Node* prev = nullptr;

  };
  public:
  Node* root_ptr = nullptr;

  Node* create_node(string t_key){
    Node* temp = new Node;
    temp->key = t_key;
    return temp;
  }

  void insert(string t_key){
    if(!root_ptr){
      cout << "linked list does not exist. creating root node now." << endl;
      root_ptr = create_node(t_key);
      return;
    }
    Node* temp = create_node(t_key);
    root_ptr->prev = temp;
    temp->next = root_ptr;
    root_ptr = temp;
    return;
  }

  void remove(string t_key){
    if(!root_ptr){
      cout << "list does not exist" << endl;
      return;
    }
    if(root_ptr->key == t_key){
      Node* temp = root_ptr->next;
      delete root_ptr;
      root_ptr = temp;
      return;
    }
    Node* t_node = root_ptr;
    while(t_node->key != t_key){
      t_node = t_node->next;
      if(!t_node){
        cout << "key not found" << endl;
        return;
      }
    }
    t_node->prev->next = t_node->next;
    if(t_node->next){
      t_node->next->prev = t_node->prev;
    }
    delete t_node;
    return;
  }

  void remove_list(){
    Node* node_t = root_ptr;
    root_ptr = nullptr;
    while(node_t){
      Node* temp = node_t->next;
      delete node_t;
      node_t = temp;
    }
    return;
  }

  void print_list(){
    if(!root_ptr){
      cout << "list does not exist" << endl;
      return;
    }
    Node* t_node = root_ptr;
    while(t_node){
      cout << t_node->key << endl;
      t_node = t_node->next;
    }
    return;
  }

}; //END OF linked_list CLASS


int main() {
  linked_list list;
  ifstream myFile;
  //myFile.open("sample_number");
  //myFile.open("words");
  myFile.open("dictionary");
  string str;
  while(myFile >> str) {
    //list.insert(strtol(str.c_str(), nullptr, 10));
    list.insert(str);
  }
  myFile.close();
  //list.remove("39");
  //list.remove("100");
  //list.remove("7");
  //list.print_list();
  list.print_list();
  cout << "deleting list" << endl;
  list.remove_list();
  list.print_list();
  cout << "end of main" << endl;
  return 0;
}
