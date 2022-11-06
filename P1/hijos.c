#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
    if(argc==3){
        int x = atoi(argv[1]);
        int y = atoi(argv[2]);

        for(int i=0;i<x;i++){
            if(fork()>0){
                if(i==x-1){
                    for(int j=0;j<y-1;j++){
                        if(fork()==0){
                            break;
                        }
                    }
                }
                break;
            }
        }
    }
    else{
        perror("Numero de argumentos incorrectos");
    }
    sleep(10);
}