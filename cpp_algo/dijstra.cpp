#include "dijstra.h"
#include <cmath>
#include <string>
#include <algorithm>

Dijstra::Dijstra(int map[WIDTH][HEIGHT], int start_x, int start_y, int goal_x, int goal_y){
    // map generation
    node_map = new Node*[WIDTH];
    for(int i = 0; i< WIDTH; i++)
        node_map[i] = new Node[HEIGHT];

    // populating map
    for(int i = 0; i<WIDTH; i++){
        for(int j = 0; j<HEIGHT; j++){
            if(map[i][j] == 0)
                node_map[i][j].set_occupied(false);
            else
                node_map[i][j].set_occupied(true);
        }
    }
    start_x_ = start_x;
    start_y_ = start_y;
    goal_x_ = goal_x;
    goal_y_ = goal_y;

    // prior setting
    std::cout<<"start_x: "<<start_x<<", start_y: "<<start_y<<std::endl;
    current_node = &node_map[start_x][start_y];
    current_node->set_gcost(0);
    std::cout<<"0,0 address: "<<&node_map[0][0]<<std::endl;
    std::cout<<"current_node address: "<<current_node<<std::endl;
    std::cout<<"sizeof(node_map[0]): "<<sizeof(node_map[0])<<std::endl;
    int current_x = int((current_node - &node_map[0][0])/sizeof(node_map[0]));
    int current_y = int((current_node - &node_map[current_x][0])/sizeof(node_map[0][0]));
    std::cout<<"x: "<<current_x<<", y: "<<current_y<<std::endl;
    std::cout<<"generated_dijstra"<<std::endl;
}
Dijstra::~Dijstra(){
    for(int i = 0; i<WIDTH; i++)
        delete node_map[i];
    delete node_map;
}

double Dijstra::cost_function(int x1, int y1, int x2, int y2){
    return sqrt(pow(x1-x2,2) + pow(y1-y2, 2));
}

void Dijstra::calculate(){
    while(current_node != &node_map[goal_x_][goal_y_]){
        // if current_node is in closed_list -> continue
        auto finder = closed_list.find(current_node);
        if (finder != closed_list.end())
            continue;

        int current_x = int((current_node - &node_map[0][0])/sizeof(node_map[0]));
        int current_y = int((current_node - &node_map[current_x][0])/sizeof(node_map[0][0]));
        std::cout<<"x: "<<current_x<<", y: "<<current_y<<std::endl;
        // visit all the neighbors
        for(int i = -1; i <= 1; i++){
            for(int j = -1; j <= 1; j++){
                int neighbor_x = current_x + i;
                int neighbor_y = current_y + j;
                if(neighbor_x < 0 || neighbor_x >= WIDTH || neighbor_y < 0 || neighbor_y >= HEIGHT || (neighbor_x==0&&neighbor_y==0) || node_map[neighbor_x][neighbor_y].get_occupied() == true)
                    continue;
                std::cout<<"neighbor_x : "<<neighbor_x<<", neighbor_y: "<<neighbor_y<<std::endl;
                double temp_g_cost = cost_function(current_x, current_y, neighbor_x, neighbor_y) + current_node->get_gcost();
                if(node_map[neighbor_x][neighbor_y].get_gcost() > temp_g_cost){
                    node_map[neighbor_x][neighbor_y].set_gcost(temp_g_cost);
                    // even if the node is in open_list, because we updated the value, we insert again
                    open_list.push(&node_map[neighbor_x][neighbor_y]);
                }
            }
        }
        printOpenList();
        // choose next current_node, and insert it into closed list
        Node* temp_current_node = current_node;
        current_node = open_list.top();
        open_list.pop();
        closed_list.insert(std::make_pair(current_node, temp_current_node));
    }
}

void Dijstra::generatePath(){
    // backtrack closed_list starting from goal node to start node
    Node* printer = &node_map[goal_x_][goal_y_];
    while(true){
        path.push_back(printer);
        printer = closed_list[printer];
        if(printer == &node_map[start_x_][start_y_]){
            path.push_back(printer);
            break;
        }
    }
}

void Dijstra::printMap(){
    // print map
    std::cout<< "map: " << std::endl;
    for(int i = 0; i<WIDTH; i++){
        for(int j = 0; j<HEIGHT; j++){
            auto iter = find(path.begin(), path.end(), &node_map[i][j]);
            if(iter == path.end())
                std::cout<<int(node_map[i][j].get_occupied())<<" ";
            else
                std::cout<<"p ";
        }
        std::cout<<std::endl;
    }
}

void Dijstra::printOpenList(){
    std::vector<Node*> temp;
    std::cout<<"open list: ";
    while(!open_list.empty()){
        temp.push_back(open_list.top());
        int current_y = (open_list.top() - &node_map[0][0])/sizeof(Node[WIDTH]);
        int current_x = (open_list.top() - &node_map[0][current_y])/sizeof(Node);
        std::cout<<"x: "<<current_x<<", y: "<<current_y<<std::endl;
        open_list.pop();
    }
    for(auto iter = temp.begin(); iter != temp.end(); iter++)
        open_list.push(*iter);
}
