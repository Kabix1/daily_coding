#include <stdio.h>
#include<time.h>
int main () {
  int num;
  long long i;
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
  printf("%6.3f, %6.3f, %6d\n", start, stop, found);
  return 0;
}
