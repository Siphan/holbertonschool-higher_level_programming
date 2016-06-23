/*
 * This function prints all the numbers of base 16, from 0 to F.
 */
#include "my_functions.h"

void print_base16(void)
{
  int i;

  for(i = 0; i < 71; i++)
  {
    if((i >= 48 && i <= 57) || (i >= 65 && i <= 70))
    {
    print_char(i);
    }
  }
}
