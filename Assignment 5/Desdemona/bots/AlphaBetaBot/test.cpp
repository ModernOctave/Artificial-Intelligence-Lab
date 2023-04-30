#include<iostream>
#include<list>
#include<cstdlib>
#include<stdio.h>

using namespace std;

struct a
{
  int a1;
  int a2;  
};

int main()
{
    list<a>ALL_a;

    auto it1 = ALL_a.begin();

    a element = *it1;

    it1++;

    a element = *it1;



}
