#include <iostream>  //cin and cout, inputs and outputs
#include <fstream>   //fstream, reading file
#include <string>    //string, string def type
#include <stdlib.h>  //strtol, string to int type conversion, not currently used
using namespace std;

class avl_tree
{
  public:

    //class for each node on the avl tree
    //should it be a "struct" instead?
    struct node {
      public:
        string data;
        int height = 1;
        node* left = nullptr;
        node* right = nullptr;
    };

    //initialization and declaration of root_ptr and height_ctr
    node* root_ptr = nullptr;
    int rot_ctr = 0;
    int ins_ctr = 0;
    int rem_ctr = 0;

    //gives height of node
    //separate funciton to return 0 for null nodes
    int height(node* n) {
      if(n) {
        return n->height;
      }
      return 0;
    }

    //determines difference in height between each node
    //used to determine if node tree needs balancing
    //separate funciton to return 0 for null nodes
    int get_balance(node* n) {
      if(n) {
        return height(n->left) - height(n->right);
      }
      return 0;
    }

    //compares 2 integers and returns max values
    int max(int a, int b) {
      if(a > b) {
        return a;
      }
      else {
        return b;
      }
    }

      //performs a right rotation for balancing the tree
      //pre-rotate root = n1, post rotate root = n3
      //least to greatest data value {n0, n1, n2, n3, n4}
    node* rotate_left(node* n1) {
      //cout << "rotating left on " << n1->data << endl;
      //rearrange the nodes for a left rotation
      node* n3 = n1->right;
      node* n2 = n3->left;
      n3->left = n1;
      n1->right = n2;
      //update the heights with the node new configurate
      n1->height = 1 + max(height(n1->left), height(n1->right));
      n3->height = 1 + max(height(n3->left), height(n3->right));
      rot_ctr++;
      return n3;
    }

    //performs a right rotation for balancing the tree
    //pre-rotate root = n3, post rotate root = n1
    //least to greatest data value {n0, n1, n2, n3, n4}
    node* rotate_right(node* n3) {
      //cout << "rotating right on " << n3->data << endl;
      //rearrange the nodes to complete right roatation
      node* n1 = n3->left;
      node* n2 = n1->right;
      n1->right = n3;
      n3->left = n2;
      //update the heights with the node new configurate
      n3->height = 1 + max(height(n3->left), height(n3->right));
      n1->height = 1 + max(height(n1->left), height(n1->right));
      rot_ctr++;
      return n1;
    }


    //inserts all nodes on tree after the root node
    //lesser values sent to left. greater values sent right.
    //equal values are ignored
    node* _insert(string data, node* current_node) {
      if(!current_node) {
        node* new_node = new node;
        new_node->data = data;
        ins_ctr++;
        return new_node;
      }
      else if(data < current_node->data) {
        current_node->left = _insert(data, current_node->left);
      }
      else if(data > current_node->data) {
        current_node->right = _insert(data, current_node->right);
      }
      else {
        return current_node;
      }
      //update the heights of parent nodes after adding new node
      current_node->height = 1 + max(height(current_node->left),height(current_node->right));
      //get the balance to determine if rotations are needed for balancing the tree
      int balance = get_balance(current_node);
      //cout << current_node->data << " " << current_node->height << " " << balance << endl;
      //if balance >1 or <-1, then balancing is required
      //4 different configurations to consider when balancing
      if(balance > 1 && data < current_node->left->data) {
        return rotate_right(current_node);
      }
      if(balance < -1 && data > current_node->right->data) {
        return rotate_left(current_node);
      }
      if(balance > 1 && data > current_node->left->data) {
        current_node->left = rotate_left(current_node->left);
        return rotate_right(current_node);
      }
      if(balance < -1 && data < current_node->right->data) {
        current_node->right = rotate_right(current_node->right);
        return rotate_left(current_node);
      }

      return current_node;
    } //END OF _insert()

    //if root node exists, it forwards the new value to the _insert() function
    //creates root node if none exists
    //otherwise forwards
    void insert(string data) {
      //cout << "inserting " << data << endl;
      if(root_ptr) {
        root_ptr = _insert(data, root_ptr);
      }
      else {
        root_ptr = _insert(data, root_ptr);
        cout << "root does not exist. making root node. value = " << root_ptr->data << endl;
      }
      return;
    }

    node* find_minimum(node* current_node) {
      if(current_node->left) {
        return find_minimum(current_node->left);
      }
      return current_node;
    }

    void remove(string data) {
      if(root_ptr){
        _remove(data, root_ptr);
      }
      else {
        cout << "tree does not exist" << endl;
      }
      return;
    }

    node* _remove(string data, node* current_node) {
      if(!current_node){
        cout << "Unable to find "<< data <<". No nodes were removed" << endl;
        return nullptr;
      }
      if(data < current_node->data){
        current_node->left = _remove(data, current_node->left);
      }
      else if(data > current_node->data) {
        current_node->right = _remove(data, current_node->right);
      }
      else if (data == current_node->data) {
        if(!current_node->left) {
          node* temp_node = current_node->right;
          delete current_node;
          rem_ctr++;
          return temp_node;
        }
        else if(!current_node->right) {
          node* temp_node = current_node->left;
          delete current_node;
          rem_ctr++;
          return temp_node;
        }
        else {
          node* temp_node = find_minimum(current_node->right);
          current_node->data = temp_node->data;
          current_node->right = _remove(temp_node->data, current_node->right);
        }
      }

      current_node->height = 1 + max(height(current_node->left),height(current_node->right));

      int balance = get_balance(current_node);
      //cout << current_node->data << " " << current_node->height << " " << balance << endl;

      if(balance > 1) {
        return rotate_right(current_node);
      }
      if(balance < -1) {
        return rotate_left(current_node);
      }
        return current_node;
    }

    void lower_height(node* current_node) {
      if(current_node) {
        if(current_node->left) {
          lower_height(current_node->left);
        }
        if(current_node->right){
          current_node->height--;
          lower_height(current_node->right);
        }
        else {
          current_node->height--;
        }
      }
      return;
    }

    void print_tree() {
      cout << "begin printing tree..." << endl;
      if(root_ptr) {
        _print_tree(root_ptr);
      } else {
      cout << "tree does not exist" << endl;
      }
      cout << "...done printing tree" << endl;
      return;
    } //END OF print_tree

    void _print_tree(node* current_node) {
      if(current_node->left) {
        _print_tree(current_node->left);
      }
      if(current_node->right){
        //cout << current_node->data << " " << current_node->height << endl;
        cout << current_node->data << endl;
        _print_tree(current_node->right);
      }
      else {
        //cout << current_node->data << " " << current_node->height << endl;
        cout << current_node->data << endl;
      }
      return;
    } //END OF _print_tree

    void invert_tree(node* n){
      if(!n){
        return;
      }
      invert_tree(n->left);
      invert_tree(n->right);
      node* temp = n->left;
      n->left = n->right;
      n->right = temp;
      return;
    }

    void _remove_tree(node* n){
      if(!n){
        return;
      }
      _remove_tree(n->left);
      _remove_tree(n->right);
      delete n;
      return;
    }

    void remove_tree(){
      _remove_tree(root_ptr);
      root_ptr = nullptr;
      rot_ctr = 0;
      ins_ctr = 0;
      rem_ctr = 0;
      return;
    }

    void print_info(){
      if(!root_ptr){
        cout << "tree does not exist" << endl;
        return;
      }
      cout << "--Tree Info--" << endl;
      cout << "\"" << root_ptr->data << "\" is the value of the root node" << endl;
      cout << ins_ctr << " items were inserted into table" << endl;
      cout << rem_ctr << " items were removed from table" << endl;
      cout << ins_ctr - rem_ctr << " items are in table" << endl;
      cout << rot_ctr << " rotations were made" << endl;
      cout << "-------------" << endl;
    }


}; //END OF avl_tree CLASS

avl_tree tree;
ifstream myFile;
//myFile.open("words");
//myFile.open("sample_number");
myFile.open("dictionary");
string str;
//int i = 0;
while(myFile >> str) {
  //tree.insert(strtol(str.c_str(), nullptr, 10));
  tree.insert(str);
}
myFile.close();

int main() {
  // avl_tree tree;
  // ifstream myFile;
  // //myFile.open("words");
  // //myFile.open("sample_number");
  // myFile.open("dictionary");
  // string str;
  // //int i = 0;
  // while(myFile >> str) {
  //   //tree.insert(strtol(str.c_str(), nullptr, 10));
  //   tree.insert(str);
  // }
  // myFile.close();
  tree.print_tree();
  tree.print_info();
  cout << "deleting tree" << endl;
  tree.remove_tree();
  tree.print_info();

  //cout << "end of main" << endl;
  return 0;
}
