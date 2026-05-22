#include <iostream>
using namespace std;

int price (int years, int curret_price){
    if (years == 0){
        return curret_price;
    } else {
        curret_price = curret_price - (curret_price-12000)*(curret_price-12000)/20000;
        return price(years-1, curret_price);
    }
}

int main () {
    int years, current_price;
    cin >> years >> current_price;
    cout << price(years, current_price) << endl;
    return 0;
}