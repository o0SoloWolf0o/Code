#include <iostream>
#include <cstring>
using namespace std;

class AQueue{
public:
  int maxSize;               // Maximum size of queue
  int front;                 // Index of front element
  int rear;                  // Index of rear element
  int *listArray;           // Array holding queue elements

  AQueue(int size) {  // Constructor
    // Make list array one position larger for empty slot
    maxSize = size+1;
    rear = 0;  front = 1;
    listArray = new int[maxSize];
  }

  ~AQueue() { delete [] listArray; } // Destructor

  void clear() { rear = 0; front = 1; } // Reinitialize

  void enqueue(int it) {     // Put "it" in queue
    if(((rear+2) % maxSize) == front)
        cout<< "Queue is full"<< endl;
    else{
    rear = (rear+1) % maxSize;       // Circular increment
    listArray[rear] = it;
    }
  }

  int dequeue() {           // Take element out
    if(length() == 0){
        cout << "Queue is empty" << endl;
        return 0;
    }
    int it = listArray[front];
    front = (front+1) % maxSize;    // Circular increment
    return it;
  }

  int frontValue() {  // Get front value
    if(length() == 0)
    {
        cout << "Queue is empty" << endl;
        return 0;
    }
    return listArray[front];
  }

  int length()          // Return length
   { return ((rear+maxSize) - front + 1) % maxSize; }

};

class tictactoe{
public:
    char board[3][3];
    int turn;

    tictactoe(){
        for(int j=2;j>=0;j--)
        for(int i=0;i<3;i++)
                board[i][j]='_';
        turn = 0;
    }

    void update(int x,int y,char player){
        board[x][y]=player;
        turn++;
    }

    int endGameCheck(){
        char p; //player
        if(turn%2==1)
            p='x';
            else
                p='o';

        if((board[0][0]==p&&board[1][1]==p&&board[2][2]==p)||
           (board[0][2]==p&&board[1][1]==p&&board[2][0]==p)||
           (board[0][0]==p&&board[0][1]==p&&board[0][2]==p)||
           (board[1][0]==p&&board[1][1]==p&&board[1][2]==p)||
           (board[2][0]==p&&board[2][1]==p&&board[2][2]==p)||
           (board[0][0]==p&&board[1][0]==p&&board[2][0]==p)||
           (board[0][1]==p&&board[1][1]==p&&board[2][1]==p)||
           (board[0][2]==p&&board[1][2]==p&&board[2][2]==p))
            return 1;
            else return 0;
    }

    int availableMove(int x,int y){
        if(board[x][y]=='_')
            return 1;
        else return 0;
    }

    void printboard()
    {
        cout << "----board----" <<endl;
        for (int j=2;j>=0;j--)
        {
            for (int i=0;i<3;i++)
                cout << board[i][j];
            cout << endl;
        }

        if(endGameCheck()==1)
            cout << "----End Game----" <<endl;
    }
};

class node{
public:
    int parent;
    tictactoe *board;
};

class upTree{
public:
    int maxSize;
    int root;
    int nextLeaf;
    node *listArray;

    upTree(int size){
        maxSize = size+1;
        root=0;
        nextLeaf=1;
        listArray = new node[maxSize];
        listArray[0].board = new tictactoe();
        listArray[0].parent = -1;
    }

    traceBack(int pos){
        if(listArray[pos].parent!=-1)
            traceBack(listArray[pos].parent);
        listArray[pos].board->printboard();
    }

    traceBack2(int pos,string t1,string t2,string t3){
        if(listArray[pos].parent!=-1)
        {
          for (int i=2;i>=0;i--)
                t1=listArray[pos].board->board[i][2]+t1;
          for (int i=2;i>=0;i--)
                t2=listArray[pos].board->board[i][1]+t2;
          for (int i=2;i>=0;i--)
                t3=listArray[pos].board->board[i][0]+t3;
        traceBack2(listArray[pos].parent,"|"+t1,"|"+t2,"|"+t3);
        }else
        {
            cout<< t1<<endl;
            cout<< t2<<endl;
            cout<< t3<<endl;
        }
    }

    span(int current,AQueue *Que){
        int spanTime = 0;

        if(listArray[current].board->endGameCheck()==0)
        {
            for(int j=2;j>=0;j--)
            for(int i=0;i<=2;i++)
            {
                if(listArray[current].board->availableMove(i,j)==1)
                {
                    listArray[nextLeaf].board = new tictactoe();
                    *listArray[nextLeaf].board = *listArray[current].board;
                    listArray[nextLeaf].parent = current;
                    if(listArray[nextLeaf].board->turn%2==0)
                    {
                        listArray[nextLeaf].board->update(i,j,'x');
                    }
                        else
                        {
                            listArray[nextLeaf].board->update(i,j,'o');
                        }
                        Que->enqueue(nextLeaf);
                        nextLeaf++;
                        spanTime++;
                }
            }

        }else
        { cout << "node number " << current << ":";
        if(listArray[current].board->turn%2==0)
            cout << " o wins" << endl;
                else cout << " x wins" << endl;
          //cout << " nextLeaf " << nextLeaf<<endl;
          traceBack2(current,"","","");
          }
    }

};

int main()
{
    upTree Tree(600000);
    AQueue Que(220000);
    Tree.listArray[0].board->printboard();
    Que.enqueue(0);
    while(Que.length()>0)
    {
     //cout << "Queue Size = " << Que.length() << " span " <<Que.frontValue() << endl;
        Tree.span(Que.dequeue(),&Que);
    }
    cout << "done" << endl;
    return 0;
}
