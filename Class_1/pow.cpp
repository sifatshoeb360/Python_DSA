#include<iostream>
using namespace std;

double pow(int a,int b){
    double res=1;
    bool flag=0;
    if(b<0){
        flag=1;
        b*=-1;
    }
    
    for (int i = 0; i < b; i++)
    {
        res*=a;
    }
    if(flag == 1){
        return 1/res;
    }
    else{
        return res;
    }
    
    
}
int main()
{
    cout<<pow(3,-3);

    return 0;
}