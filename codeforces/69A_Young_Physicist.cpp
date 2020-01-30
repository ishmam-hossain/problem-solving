#include<iostream>

using namespace std;

int main(){
    int n;
    cin>>n;
    int mat[n][3];

    for(int i=0;i<n;i++){
        for(int j=0;j<3;j++){
            cin>>mat[i][j];
        }
    }

    int tot_sum = 0;

    for(int x=0;x<3;x++){
        for(int y=0;y<n;y++){
            tot_sum += mat[y][x];
        }
        if(tot_sum != 0){
            cout<<"NO"<<endl;
            return 0;
        }
    }

    cout<<"YES"<<endl;
}
