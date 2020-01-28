#include<iostream>
#include<set>

using namespace std;

int main(){
    string name;
    cin>>name;
    set <int, greater <int> > distinct_char; 

    for(int i=0;i<name.size();i++){
        distinct_char.insert(name[i]);
    }

    if(distinct_char.size() % 2 == 0){
        cout<<"CHAT WITH HER!"<<endl;
    }
    else{
        cout<<"IGNORE HIM!"<<endl;
    }
}