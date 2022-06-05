/*Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. You don't need to validate the form of the Roman numeral.

Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.

Example:

solution("XXI"); // => 21

Help:

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
*/


#include <iostream>
#include <string>

using namespace std;

int solution(string roman) {
    int length = 0;
    int sol = 0;
    int temp = 0;
    int las_num =0;


    while (length < roman.length())
    {
        las_num = temp;
        switch(roman[length])
        {

            case 'I': temp = 1; break;
            case 'V': temp = 5; break;
            case 'X': temp = 10; break;
            case 'L': temp = 50; break;
            case 'C': temp = 100; break;
            case 'D': temp = 500; break;
            case 'M': temp = 1000; break;
        }
        if (temp <= las_num)
        {
            sol = sol + temp;

        }
        else
        {
            sol = sol - las_num + (temp-las_num);

        }
        las_num = temp;
        length++;
    }
  return sol;
}

int main(){
    cout<< solution("I")<<endl; //1
    cout<<solution("IV")<<endl; //4
    cout<<solution("MMVIII")<<endl; //2008
    cout<<solution("MDCLXVI")<<endl; //1666
    cout<<solution("XXI")<<endl; //21
    cout<<solution("CDXLV")<<endl; // 445
    cout<<solution("DXXXIII")<<endl; //533
    cout<<solution("DCCCXXXIV")<<endl; //834
    cout<<solution("CMXCIX")<<endl; //999
    cout<<solution("M")<<endl; //1000
    return 0;
}
