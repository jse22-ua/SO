#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(){
    int df, tam;
    long numero;
    char buffer[10];

    df = open("/dev/tty", O_RDONLY);
    if(df<0){
        perror("error al abrir");
        exit(-1);
    }
    tam = read(df,buffer, 9);
    if(tam == 1){
        perror("error de lectura");
    }
    else{
        buffer[tam]=0;
        numero = atoi(buffer);
        printf("resultado : %ld\n", numero*2);
    }
}