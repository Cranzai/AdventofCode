#include<stdio.h>
#include<stdlib.h>

#define strLength 10

void main()
{  
  char fileName[strLength];
  //read fileName from terminal
  scanf("%s", fileName);

  int comLen;
   

  readComList(fileName, &comChar, &comChar, &comLen)
}

void readComList(const char *fileName, char *comChar, int *comInt, int *numLines)
{
  int i;
  char dum;

  FILE* fileIn = fopen(fileName, "r");
  if (fileIn == NULL)
  {
    printf("Could not open file %s \n", fileName);
    exit(0);
  }

  //read number of lines for allocation
  for (dum = getc(fileIn); dum != EOF; dum = getc(fileIn))
    if (dum == '\n')
      *numLines = *numLines + 1;

  //return to beginning of file for actual reading
  rewind(fileIn);

  //dynamically allocate com... Lists
  //for an array of strings I need a 2D char array
  char **comChar;  
  comChar = malloc(sizeof(char *) * *numLines);
  //loop through numLines to set each to 10;
  for (i=0; i< *numLines; i++)
    comChar[i]=malloc(strLength)
 
  comInt = (int*)malloc(*numLines * sizeof(int));

  //verify allocation
  if ((comChar == NULL)||(comInt == NULL))
  {
    printf("Could not allocate com... \n");
    exit(1);
  }

  //scan all lines
  for (i = 0; i < numLines; ++i)
  {
    fscanf(fileIn, "%s %d", comChar, &comInt);
    printf("%s %d \n", comChar, comInt);
  }

  fclose(fileIn);
}
