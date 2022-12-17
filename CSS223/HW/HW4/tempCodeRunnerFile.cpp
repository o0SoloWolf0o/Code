#include <iostream>
#include <vector>


using namespace std;

int won(int c[9], int n)
{
    // Check rows
    for (int i = 0; i < 9; i += 3)
    {
        if (c[i] == n && c[i + 1] == n && c[i + 2] == n)
        {
            return 1;
        }
    }
    // Check columns
    for (int i = 0; i < 3; i++)
    {
        if (c[i] == n && c[i + 3] == n && c[i + 6] == n)
        {
            return 1;
        }
    }
    // Check diagonals
    if (c[0] == n && c[4] == n && c[8] == n)
    {
        return 1;
    }
    if (c[2] == n && c[4] == n && c[6] == n)
    {
        return 1;
    }
    return 0;
}

main()
{
    int count = 0;
    std::vector<char> playerchoose = {' ', 'x', 'o'};
    int c[9] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
    for (c[0] = 0; c[0] < 3; c[0]++)
        for (c[1] = 0; c[1] < 3; c[1]++)
            for (c[2] = 0; c[2] < 3; c[2]++)
                for (c[3] = 0; c[3] < 3; c[3]++)
                    for (c[4] = 0; c[4] < 3; c[4]++)
                        for (c[5] = 0; c[5] < 3; c[5]++)
                            for (c[6] = 0; c[6] < 3; c[6]++)
                                for (c[7] = 0; c[7] < 3; c[7]++)
                                    for (c[8] = 0; c[8] < 3; c[8]++)
                                    {
                                        if (won(c, 1) == 1)
                                        {
                                            count++;
                                            cout << "Game " << count << endl;
                                            cout << " " << playerchoose[c[0]] << " | " << playerchoose[c[1]] << " | " << playerchoose[c[2]] << endl;
                                            cout << "-----------" << endl;
                                            cout << " " << playerchoose[c[3]] << " | " << playerchoose[c[4]] << " | " << playerchoose[c[5]] << endl;
                                            cout << "-----------" << endl;
                                            cout << " " << playerchoose[c[6]] << " | " << playerchoose[c[7]] << " | " << playerchoose[c[8]] << endl;
                                            cout << endl;
                                            cout << "1" << endl;
                                        }
                                        else if (won(c, 2) == 2)
                                        {
                                            count++;
                                            cout << "Game " << count << endl;
                                            cout << " " << playerchoose[c[0]] << " | " << playerchoose[c[1]] << " | " << playerchoose[c[2]] << endl;
                                            cout << "-----------" << endl;
                                            cout << " " << playerchoose[c[3]] << " | " << playerchoose[c[4]] << " | " << playerchoose[c[5]] << endl;
                                            cout << "-----------" << endl;
                                            cout << " " << playerchoose[c[6]] << " | " << playerchoose[c[7]] << " | " << playerchoose[c[8]] << endl;
                                            cout << endl;
                                            cout << "-1" << endl;
                                        }
                                        else{
                                            count++;
                                            cout << "Game " << count << endl;
                                            cout << " " << playerchoose[c[0]] << " | " << playerchoose[c[1]] << " | " << playerchoose[c[2]] << endl;
                                            cout << "-----------" << endl;
                                            cout << " " << playerchoose[c[3]] << " | " << playerchoose[c[4]] << " | " << playerchoose[c[5]] << endl;
                                            cout << "-----------" << endl;
                                            cout << " " << playerchoose[c[6]] << " | " << playerchoose[c[7]] << " | " << playerchoose[c[8]] << endl;
                                            cout << endl;
                                            cout << "0" << endl;
                                        }
                                    }
    cout << endl;
    cout << "Game finished " << count << endl;
}