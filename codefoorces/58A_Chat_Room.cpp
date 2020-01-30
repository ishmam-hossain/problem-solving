#include<iostream>
#include<string>

using namespace std;

string is_equilibrium(string s){
    string t = "hello";
    int res[t.size()];
    int j = 0;
    for(int i=0;i<s.size();i++){
        if(s[i] == t[j]){
            res[j] = 1;
            j++;
        }
    }
    for(int i=0;i<t.size();i++){
        if(res[i] != 1){
            return "NO";
        }
    }
    return "YES";
}

int main(){
    string x;
    cin>>x;
    cout<<is_equilibrium(x)<<endl;
}
