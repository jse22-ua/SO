#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
    int i;

    printf("\nEjecutando el programa invocador (prog1). Sus argumentos:\n");

    for(int i=0; i< argc; i++){
        printf("    argv[%d] : %s \n", i, argv[i]);
    }

    sleep(10);

    if(execvp("./prog2",argv)<0){
        printf("Error en la invocacion a prog2\n");
        exit(1);
    }
    exit(0);
}