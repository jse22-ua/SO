#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <signal.h>

#define puerto 9999

const int MAX_CHARACTERS = 50;


int main(int argc, char *argv[]){
    int sc;//socket
    struct sockaddr_in dir_servidor, dir_cliente;
    unsigned int tam_dir_cliente;
    char comando[MAX_CHARACTERS];
    int caracteres;
    
    //crear servidor
    sc = socket(AF_INET,SOCK_STREAM, 0);

    //comprobar que se ha abierto
    if(sc == -1){
        printf("Error. No se pudo abrir el socket\n\r");
        exit(0);
    }else{
    printf("socket abierto\n\r");

    
    //Establezco direccion de escucha
    dir_servidor.sin_family = AF_INET;
    dir_servidor.sin_addr.s_addr = INADDR_ANY;
    dir_servidor.sin_port = htons(puerto);
    
    //comprobar si se ha asociado el puerto
    if(bind(sc, (struct sockaddr *)&dir_servidor, sizeof(dir_servidor)) < 0){
        printf("Error. No se pudo asociar puerto al servidor\n\r");
        close(sc);
        exit(0);
    }
    printf("Puerto de escucha establecido\n\r");

    //prepara para la escucha
    if(listen(sc,4)==-1){
        printf("Error de preparacion para escucha \n\r");
        close(sc);
        exit(0);
    }
    printf("Socket preparado\n\r");

    //esperar peticiones
    while(1){
        printf("Esperando peticion");
        printf("Escuchando puerto 9999...");

        tam_dir_cliente = sizeof(dir_cliente);

        //se queda parado el programa hasta que recibe una peticion
        //entonces guarda el cliente
        int cliente = accept(sc, (struct sockaddr *)&dir_cliente, &tam_dir_cliente);

        //crea un nuevo proceso hijo para seguir atendiendo peticiones
        int pid = fork();
        if(pid == -1){
            exit(1);
        }
        if(pid == 0){///hijo
            caracteres = read(cliente,comando,MAX_CHARACTERS);
            if(caracteres == -1){
                printf("Error de lectura");
                exit(1);
            }
            comando[caracteres] = '\0';
            execlp(comando,comando,NULL);
            close(cliente);
            exit(0);//se muere el hijo
        }
        else{//soy padre
            close(cliente); //deja libre el canal para escuchar otra peticion
        }
    }
    }
    return 0;
}