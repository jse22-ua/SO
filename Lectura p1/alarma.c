#include <signal.h>
#include <stdio.h>
#include <unistd.h>

void alarma(){
    printf("Hola, han pasado 3 segundos\n");
}

int main(){
    signal(SIGALRM,alarma);//la funcion que llamará cuando termine el temporizador
    printf("Acabo de programar la captura de un SIGALRM\n");
    alarm(3);//programa el temporizador
    printf("Ahora he programado la alarma en 3 seg.\n");
    pause();//empieza la cuenta atras, cuando llega a 3 llama a alarma y sigue su curso
    printf("Ahora continuo con la ejecucion normal\n");
    printf("Vuelvo a programar la alarma\n");
    alarm(3);
    pause();
    printf("En POSIX esta linea no se ejecutaria porque el sigalrm me ha matado\n");
   
}