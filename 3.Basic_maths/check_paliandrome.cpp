#include<iostream>
using namespace std;


int reversed_no(int n){
    int reversed_no = 0, remainder;
 
    while(n!=0){
        remainder = n%10;
        reversed_no = reversed_no*10 + remainder;
        n = n/10;
    }
    cout<<"Reversed_no"<<reversed_no;
    return reversed_no;

}
int check_paliadrome(int n){
    int temp;
    
    temp = n;


    if(temp == reversed_no(n)){
        return true;
    }
    else return false;


}


int main(){
    int n;
    bool ans;
    
    cout<<"Enter the no. to check the paliandrone :";
    cin>>n;

    ans = check_paliadrome(n);

    cout<<"The answer"<<ans;
}