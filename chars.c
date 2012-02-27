#include <stdio.h>

int main()
{
  char i;
  for (i = '!'; i <= '~'; i++) {
    if (i != '*')
      printf("%c ", i);
  }
  printf("\n");
  return 0;
}
