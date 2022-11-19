#include <signal.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main(){
    switch(fork()){
        case -1: 
            perror("Error");
            exit(1);
        case 0: 
            printf("Hola, soy el hijo. Esperando 2 segundos...\n");
            sleep(2);
            kill(getppid(),SIGUSR1);
            printf("Soy el hijo. He señalado a mi padre. Adios.\n");
            exit(0);
        default: 
            printf("Hola,soy el padre y voy a esperar la señal.\n");
            signal(SIGUSR1,SIG_IGN);//ignoro para no morir
            pause();
            printf("Soy el padre y ya he recibido la señal. \n");
            exit(0);
    }
}