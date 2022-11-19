#include <stdio.h>
#include <unistd.h>

int main(){
    execlp("ls","ls","-al",NULL);
    perror("Error al ejecutar comando");
}