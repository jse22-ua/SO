#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>

int  main(int argc, char *argv[]){
    int i;

    printf("ejecutando el programa invocado (prog2). Sus argumentos:");

    for(int i=0;i<argc;i++){
        printf("    argv[%d] : %s \n",i,argv[i]);
    }
    sleep(10);
    exit(0);
}