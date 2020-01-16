#include <stdio.h>
int main () {
  int num;
  int found = 0;
  scanf("%d", &num);
  while (found == 0) {
    if ( (num & (num>>1)) == 0 )
      found = num;
    num++;
  }
  printf(">%d\n", found);
  return 0;
}
