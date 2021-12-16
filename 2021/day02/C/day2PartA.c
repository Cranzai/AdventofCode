#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define strLength 10

void main()
{ 
  int i;
  char dum; 
  int numLines=0;
  int comInt;
  char comChar[strLength];
  char fileName[strLength];

  int hor=0;
  int dep=0;

  //read fileName from terminal
  scanf("%s", fileName);

  FILE* fileIn = fopen(fileName, "r");
  if (fileIn == NULL)
  {
    printf("Could not open file %s \n", fileName);
    exit(0);
  }
   
  //read number of lines
  for (dum = getc(fileIn); dum != EOF; dum = getc(fileIn))
    if (dum == '\n')
      numLines = numLines + 1;
 
  rewind(fileIn);

  //scan all lines
  for (i = 0; i < numLines; ++i)
  {
    fscanf(fileIn, "%s %d", comChar, &comInt);
    if (comChar[0]=='f')
    {
      hor = hor + comInt;
    }
    if (comChar[0]=='u')
    {
      dep = dep - comInt;
    }
    if (comChar[0]=='d')
    {
      dep = dep + comInt;
    }
  }

  printf("Depth %d, Horizontal %d, Mult %d \n", dep, hor, (dep * hor));

  fclose(fileIn);
}
