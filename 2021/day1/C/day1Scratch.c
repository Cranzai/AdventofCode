#include<stdio.h>
#include<stdlib.h>

#define maxFileName 10

int *readIntList(const char *fileName, int *numLines);

void main()
{
  int i;
  int depthsLen=0;
  int incrs = 0;
  int decrs = 0;
  char fileName[maxFileName];

  //read fileName from terminal
  scanf("%s", fileName);

  //call readIntList function
  int *depths = readIntList(fileName, &depthsLen);

  //reading per two measurements, start at 1
  for (i = 1; i < depthsLen; ++i)
  {
    if (depths[i] > depths[i-1])
    {
      incrs = incrs + 1;
    }
  } 
  printf("Part A) increases %d", incrs);

  int depthsThree[depthsLen-1];
  //three measurement sliding window
  for (i = 0; i < depthsLen-2; ++i)
  {
    depthsThree[i] = depths[i] + depths[i+1] + depths[i+2];    
  }
 
  incrs=0;
  decrs=0;
 
  for (i = 1; i < depthsLen-2; ++i)
  {
    if (depthsThree[i] > depthsThree[i-1])
    {
      incrs = incrs + 1;
    }
  } 
  printf("Part B) increases %d", incrs);
}

int *readIntList(const char *fileName, int *numLines)
{
  int *intList; 
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

  //dynamically allocate intList
  intList = (int*)malloc(*numLines * sizeof(int));
  //verify allocation
  if (intList == NULL)
  {
    printf("Could not allocate intList \n");
    exit(1);
  }

  for (i = 0; i < *numLines; ++i)
  {
    fscanf(fileIn, "%d", &intList[i]);
  }

  fclose(fileIn);
  return intList;
}
