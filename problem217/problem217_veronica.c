#include <stdio.h>
#include<time.h>
int main () {
  int num;
  int i;
  int found = 0;
  clock_t start, stop;
  scanf("%d", &num);
  start = clock();
  for (i=0; i<10000; i++) {
    while (found == 0) {
      if ( (num & (num>>1)) == 0 )
        found = num;
      num++;
    }
  }
  stop = clock();
  printf("%6.3f", start - stop);
  return 0;
}
