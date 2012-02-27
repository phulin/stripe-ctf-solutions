#include <stdio.h>
#include <sys/time.h>

int main()
{
  char c;
  struct timeval tv;
  while ((c = getchar_unlocked()) != EOF) {
    gettimeofday(&tv, NULL);
    printf("%d\t%c\n", tv.tv_usec, c);
  }
  return 0;
}
