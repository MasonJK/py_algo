#pragma once
#include <iostream>
#define WIDTH 10
#define HEIGHT 10
#include <queue>
#include <vector>
#include <unordered_map>

class Node{
private:
    double g_cost_;
    bool occupied_;
public:
    Node(){
        g_cost_ = INT_MAX;
        occupied_ = 0;
    }
    void set_occupied(bool occupied){occupied_ = occupied;}
    void set_gcost(double g_cost){g_cost_ = g_cost;}
    bool get_occupied(){return occupied_;}
    double get_gcost(){return g_cost_;}
};

struct cmp{
    bool operator()(Node* n1, Node* n2){
        if(n1->get_gcost() >= n2->get_gcost())
            return true;
        else
            return false;
    }
};

class Dijstra{
private:
    Node** node_map;
    Node* current_node;
    std::priority_queue<Node*, std::vector<Node*>, cmp> open_list;
    // Node가 key가 되고, parent Node가 value가 되는 closed_list
    std::unordered_map<Node*, Node*> closed_list;
    std::vector<Node*> path;
    int start_x_, start_y_, goal_x_, goal_y_;
    
public:
    Dijstra(int map[WIDTH][HEIGHT], int start_x, int start_y, int goal_x, int goal_y);
    ~Dijstra();
    void calculate();
    void evaluaterResults();
    void printMap();
    double cost_function(int x1, int y1, int x2, int y2);
    void generatePath();
    void printOpenList();
};


int main(int argc, char** argv){
    int map[WIDTH][HEIGHT] = {{0,0,0,0,0,0,0,0,0,0},
                              {1,1,0,0,0,0,0,0,0,0},
                              {0,0,1,1,1,1,1,1,1,0},
                              {0,0,1,0,0,0,0,0,0,0},
                              {0,0,1,1,1,1,1,1,1,0},
                              {0,0,0,0,0,0,0,0,0,0},
                              {0,0,1,1,1,1,1,1,1,1},
                              {0,0,0,0,0,0,0,0,0,0},
                              {0,0,0,0,0,0,0,0,0,0},
                              {0,0,0,0,0,0,0,0,0,0}};

    std::cout<<"hi"<<std::endl;
    Dijstra dijstra(map,3,1,9,9);
    dijstra.calculate();
    dijstra.generatePath();
    dijstra.printMap();
    return 0;
}