#include<stdio.h>
#include<string.h>

int copier(char *str){
	char buffer[100];
	strcpy(buffer,str);		// vulnerable function
}

void main(int argc, char *argv[]){
	copier(argv[1]);
	printf("Done\n");
}