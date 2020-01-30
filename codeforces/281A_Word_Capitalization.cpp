#include<iostream>

using namespace std;

int main(){
    string s;
    cin>>s;

    int ascii_val = int(s[0]);

    if(ascii_val >= 97 && ascii_val <= 122){
        s[0] = ascii_val - (97 - 65);
    }
    
    cout<<s<<endl;
}