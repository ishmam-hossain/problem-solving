#include<iostream>
#include<math.h>
using namespace std;

int main(){
    int a = 4;
    int b = 7;
    int i = 1000;
    int res[20];
    int j = 0;

    for(;i>=4;i--){
        int x = i;
        int no_of_digits = int(log10(i)) + 1;
        bool is_lucky = true;

        for(int n=1;n<=no_of_digits;n++){
            cout<<n<<endl;
            int rem = x % int(pow(10, n));
            // cout<<int(pow(10, n))<<endl;
            if(rem != 4 or rem != 7){
                is_lucky = false;
                break;
            } 
        }
        cout<<"----------------"<<endl;

        if(is_lucky){
            res[j] = i;
            j++;
        }
     }

    //  for(int y = 0;y<i;y++){
    //      cout<<res[y]<<endl;
    //  }


    // for(int i=10;i<=100;i+=10){
    //     int x = i;
    //     while(x >= 10){
    //         x /= 10;
    //         cout<<x<<endl;
    //     }
    //     // cout<<a*i + b<< " " << b*i + a << endl;
    // }
}