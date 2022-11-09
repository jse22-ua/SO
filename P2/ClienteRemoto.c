#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <netinet/in.h>
#include <netdb.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>

const int port = 9999;

int main(int argc,char **argv){
    //Comprobamos los parametros
    if(argc == 3){
        //Los argumentos seran IP y comando
        //referencia al host
        char *ip = argv[1];
        char *comando = argv[2];

        //tamanyo socket, para poder conectar cliente-servidor
        int tamS = sizeof(struct sockaddr);

        int fd, numbytes;

        char buffer[100];

        //Para conectar cliente->servidor
        struct hostent *he;
        struct sockaddr_in server;

        //Comprobar que la IP es correcta 
        he = gethostbyname(ip);
        if(he == NULL){
            printf("Erro de host");
            exit(-1);
        }

        //Creacion socket
        fd = socket(AF_INET, SOCK_STREAM, 0);

        //Comprobar que el socket se creo correctamente
        if(fd == -1){
            printf("Error en socket");
            exit(-1);
        }

        //Conectamos cliente-servidor mediante el puerto
        server.sin_family = AF_INET;
        server.sin_port = htons(port);
        server.sin_addr = *((struct in_addr*)he->h_addr);

        //Comprobamos que se conecta correctamente
        if(connect(fd, (struct sockaddr*)&server, tamS) == -1){
            printf("Error al conectar");
            exit(-1);
        }

        //El cliente envia el comando a ejecutar al servidor
        send(fd, comando, sizeof(comando), 0);

        //Mostramos lo que envia el cliente al servidor
        while((numbytes - recv(fd, buffer, sizeof(buffer), 0))>0){
            buffer[numbytes] = '\0';
            printf("%s\n",buffer);
        }

        //Cerrar socket
        close(fd);
    }else{
        printf("Error en los parametros");
        exit(-1);
    }
}