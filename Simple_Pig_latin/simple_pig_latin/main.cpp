#include <iostream>
#include <string>
#include <cstring>

using namespace std;

/* Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
Examples

pigIt('Pig latin is cool'); // igPay atinlay siay oolcay
pigIt('Hello world !');     // elloHay orldway !

*/

void pig_it(string str)
{
    //code here
    int MAX = str.length();
    string strings[MAX];
    int currIndex = 0, startIndex = 0, endIndex = 0;
    string currStr;
    size_t i = 0;
    while (i <=str.length())
    {
        currStr = str[i];
        if (currStr == " " || i == str.length())
            {
                endIndex = i;
                string sub_str = "";
                sub_str.append(str, startIndex, endIndex-startIndex);
                strings[currIndex] = sub_str;
                currIndex += 1;
                startIndex = endIndex +1;
            }
        i++;
    }

    for (int j = 0; j < MAX; j++)
    {
        cout << strings[j] << endl;
    }

}

int main()
{
    string inp;
    cout<< "Type in a sentence:"<<endl;
    getline(cin, inp);
    //string inp = "Hello WOrld!";
    pig_it(inp);
    return 0;
}
