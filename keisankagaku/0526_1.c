#include <stdio.h>
#include <math.h>



int main( void ) {

  float a = powf(2, 100);
  float b = - powf(2, 100);
  float c = 2;

  float x = a + b + c;
  float y = a + c + b;

  printf("a=%f\nb=%f\nc=%f\n", a,b,c);

  printf("x=%f\n", x);
  printf("y=%f\n", y);

  printf( "hello!\n" );

  return 0;
}
