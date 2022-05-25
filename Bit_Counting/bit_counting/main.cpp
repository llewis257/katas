/*
Write a function that takes an integer as input, and returns the number of bits
that are equal to one in the binary representation of that number.
You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

raisonement:

19 = 2^4 + 2^1 +2^0
42 = 2^5 + 2^3 + 2^1
129 = 2^7 + 2^0

*/

#include <iostream>
#include<math.h>
#include <bits/stdc++.h>

using namespace std;

unsigned int countBits(unsigned long long n){
  /* bit-wise operations are used here:
  - Right shift:
    a>>1 = a/2 and a>> 2 = a/(2^2) and a>>3 = a/(2^3) and so on.
- left shift:
    a<<1 = a*2 and a<<2 = a*(2^2) and a<<3 = a*(2^3) and so on.
    */
  // the idea is to right shift the number n until it's equal to 1 and return the count
  int count_ = 0;
  while(n>=1)
  {


      if (n%2==1)
    {
        count_+=1;
        cout<<1;
      }
      else
    {
        cout<<0;
      }
      n = n>>1;

  }

return count_;

}

int main()
{
    unsigned long long f = 19, g = 42, h = 129;
    cout <<"couting bits of "<< f << "-> "<< countBits(f) <<endl;
    cout <<"couting bits of "<< g << "-> "<< countBits(g) <<endl;
    cout <<"couting bits of "<< h << "-> "<< countBits(h) <<endl;
    return 0;
}
