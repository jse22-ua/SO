#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>


int main(){
    int status;
    char respuesta;
        printf("¡Oye!\n");
        printf("¿Quieres ver algo chulo?\n");
        scanf("%c",&respuesta);
        if(respuesta=='s'||respuesta=='S'){
            printf("Vale mira...\n");
            sleep(3);
            switch(fork()){
                case -1:
                    perror("Error en fork");
                    exit(1);
                case 0:
                    execlp("sl","sl",NULL);
                    exit(-1);
                default:
                    wait(&status);
                    printf("Has fiplado \n");
                    exit(0);
            }
        }
        else if(respuesta=='n'|| respuesta=='N'){
            printf("Jooo...\n");
        }
        else{
            printf("te confundiste. Tienes que poner si o no");
        }
    
}