#include <iostream>
using namespace std;

class Graph
{
    int v;
    int **adj;

public:
    Graph(int v);
    void addEdge(int start, int e);
    void printMatrix();
    void nonConnected(int start);
    void friendRecommend(int start);
};

Graph::Graph(int v)
{
    this->v = v;
    adj = new int *[v];
    for (int row = 0; row < v; row++)
    {
        adj[row] = new int[v];
        for (int column = 0; column < v; column++)
        {
            adj[row][column] = 0;
        }
    }
}

// Add an edge to the graph
void Graph::addEdge(int i, int j)
{
    adj[i][j] = 1;
    adj[j][i] = 1;
}

// Print the Matrix
void Graph::printMatrix()
{
    for (int i = 0; i < v; i++)
    {
        cout << i << " : ";
        for (int j = 0; j < v; j++)
            cout << adj[i][j] << " ";
        cout << "\n";
    }
}

char friends(int n)
{
    if (n == 0)
    {
        return 'N';
    }
    else if (n == 1)
    {
        return 'X';
    }
    else if (n == 2)
    {
        return 'U';
    }
    else if (n == 3)
    {
        return 'A';
    }
    else if (n == 4)
    {
        return 'B';
    }
    else if (n == 5)
    {
        return 'P';
    }
    else if (n == 6)
    {
        return 'K';
    }
    else if (n == 7)
    {
        return 'M';
    }
    else
    {
        return 'C';
    }
}

void Graph::nonConnected(int start)
{

    cout << friends(start) << " is not friends with: ";

    for (int i = 0; i < v; i++)
    {

        if (adj[start][i] == 0 and i != start)
        {
            cout << friends(i) << " ";
        }
    }
    printf("\n");
}

void Graph::friendRecommend(int start)
{
    int max = 0;
    int maxIndex = 0;
    for (int i = 0; i < v; i++)
    {
        int count = 0;
        for (int j = 0; j < v; j++)
        {
            if (adj[start][j] == 1 && adj[i][j] == 1)
            {
                count++;
            }
        }
        if (count > max && i != start)
        {
            max = count;
            maxIndex = i;
        }
    }
    cout << friends(start) << " is friends with: ";
    for (int i = 0; i < v; i++)
    {
        if (adj[start][i] == 1)
        {
            cout << friends(i) << " ";
        }
    }
    cout << "and also recommend to " << friends(maxIndex) << " who are friends with: ";
    for (int i = 0; i < v; i++)
    {
        if (adj[maxIndex][i] == 1)
        {
            cout << friends(i) << " ";
        }
    }
    cout << endl;
}

int main()
{
    int v = 9;
    char arr[9] = {'N', 'X', 'U', 'A', 'B', 'P', 'K', 'M', 'C'};

    // Create the graph
    Graph G(v);
    // friends of N
    G.addEdge(0, 1);
    G.addEdge(0, 2);
    G.addEdge(0, 5);
    G.addEdge(0, 6);

    // friends of X
    G.addEdge(1, 0);
    G.addEdge(1, 3);
    G.addEdge(1, 4);
    G.addEdge(1, 8);

    // friends of U
    G.addEdge(2, 0);
    G.addEdge(2, 3);
    G.addEdge(2, 4);

    // friends of A
    G.addEdge(3, 1);
    G.addEdge(3, 2);
    G.addEdge(3, 5);

    // friends of B
    G.addEdge(4, 1);
    G.addEdge(4, 2);

    // friends of P
    G.addEdge(5, 0);
    G.addEdge(5, 3);
    G.addEdge(5, 6);

    // friends of k
    G.addEdge(6, 0);
    G.addEdge(6, 5);
    G.addEdge(6, 7);

    // friends of M
    G.addEdge(7, 0);
    G.addEdge(7, 6);
    G.addEdge(7, 8);

    // friends of C
    G.addEdge(8, 1);
    G.addEdge(8, 6);

    G.printMatrix();

    cout << endl;

    G.friendRecommend(0);
    G.friendRecommend(1);
    G.friendRecommend(2);
    G.friendRecommend(3);
    G.friendRecommend(4);
    G.friendRecommend(5);
    G.friendRecommend(6);
    G.friendRecommend(7);
    G.friendRecommend(8);

    cout << endl;

    // G.nonConnected(0);
    // G.nonConnected(1);
    // G.nonConnected(2);
    // G.nonConnected(3);
    // G.nonConnected(4);
    // G.nonConnected(5);
    // G.nonConnected(6);
    // G.nonConnected(7);
    // G.nonConnected(8);

    // Time Complecity: O(n^2)
    cout << "Time Complecity: O(n^2) " << endl;
}