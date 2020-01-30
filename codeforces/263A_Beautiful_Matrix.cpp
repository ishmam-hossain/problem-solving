#include<iostream>
#include<cstdlib>

using namespace std;

int main(){
    int td[5][5];
    int target_row = 2;
    int target_col = 2;
    int cur_row;
    int cur_col;

    for(int i=0;i<5;i++){
        for(int j=0;j<5;j++){
            cin>>td[i][j];
            if(td[i][j] == 1){
                cur_row = i;
                cur_col = j;
            }
        }
    }

    int result = abs(target_col - cur_col);
    result += abs(target_row - cur_row);

    cout<<result<<endl;
}