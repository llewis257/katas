#include<stdlib.h>
#include<stdio.h>
char* reverseWords(const char* text) {
    char *reverse = calloc(strlen(text) +1 , sizeof(char));
    char *rev_ptr = reverse;
    int j=0;
    for (char *txt_ptr = text; *txt_ptr!= '\0'; txt_ptr++)
    {
        if (*txt_ptr == ' '){
            printf("we caught a space");
            }
        printf("%c", *txt);
        // allocating memory size of string
        reverse = calloc(strlen(text) +1 , sizefof(char));
        j++;
        printf("%s", reverse);
    }
    reverse[j] = '\0';
    return reverse;
}

/*

// allocating memory space
char *ret = calloc(strlen(text) + 1, sizeof(char)), *q = ret;
  int wordlen = 0;
  for (char *p = text; ; p++) {
    if (*p == ' ' || *p == '\0') {
      for (int i = 0; i < wordlen; i++) *q++ = *(p - 1 - i);
      if ((*q++ = *p) == '\0') break;
      wordlen = 0;
    } else wordlen++;
  }
  return ret;
}

*/
int main(){
    const char* text1 = "Double spaced   text";
    printf("%s",text1);
    printf("%s", reverseWords(text1));
    return 0;
}
