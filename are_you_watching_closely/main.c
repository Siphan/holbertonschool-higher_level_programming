/*
 * main (varargs?)
 * do
 * read_line
 * string_split
 * string_compare? if so, compare to what?
 * string_to_integer?
 * print_number?
 * print_char
 * fork
 * get_path?
 * execve
 * don't forget to free all mallocs
 *
 * va_start
 * va_end
 */

#include <stdio.h>
#include "prototypes.h"

int main(char **av) {
  char *input;
  /* char **args; */
  /* pid_t pid; */

  do { /* Reads input at least once? */
    input = read_line(0); /* Reads stdin and stores it into a malloced array */
    /* args = string_split(input, ' '); Splits string from stdin into arguments to be interpreted */
    printf("read_line ok");
  } while (0); 
  return(0);
}

