#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main (){

    for(int i=0;i<5;i++){

     fork();
    }

    sleep(20);
    
        
    printf("Fin");
    exit(0);
}