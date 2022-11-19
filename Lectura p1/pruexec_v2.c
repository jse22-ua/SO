#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main(){
    int status;
    printf("Este es el listado de archivos \n");
    switch(fork()){
        case -1:
            perror("Error en fork");
            exit(1);
        case 0:
            execlp("sl","sl",NULL);
            exit(-1);
        default:
            wait(&status);
            printf("Esto ha sido todo \n");
            exit(0);
    }
}