#include <stdio.h>
#include <stdlib.h>
#include <string.h>

long addNum(long x, long y)
{
	return x + y; //return the value of X + Y
}

long multNum(long x, long y)
{
	return x * y; //return the value of X * Y
}

int main()
{

  FILE *fp = stdin;  //read file from standard input

  if(fp == NULL)  //check if the file is readable or not
  {
    puts("Invalid Input");
    return -1;
  }

  char *buffer = malloc(sizeof(fp)); //temporally allocating memory to get file info
  char *currentPosition = NULL; //set up the current pointer position for reading file
  long firstInput, secondInput; //set longs, so we can plug them into X and Y

  while(fgets(buffer, sizeof(fp), fp) != NULL) //while loop goes until it hits end of the file
  {
    //read the string from buffer, turn it to long int, and move current position to after firstInput
    firstInput = strtol(buffer, &currentPosition, 10); 
    if(*currentPosition != '\n') //check if we are not done yet
    {
      secondInput = strtol(currentPosition, &currentPosition, 10);
       //read the string from buffer, turn it to long int, and move current position to after secondInput
      long retAdd = addNum(firstInput, secondInput);
      long retMult = multNum(firstInput, secondInput);
      //set added and muilted value for return values
      printf("%ld %ld\n", retAdd, retMult);
      //print out added and multed value out
    }
  }
  //then close the file and free the buffer, since we are done using it.
  fclose(fp);
  free(buffer);
}