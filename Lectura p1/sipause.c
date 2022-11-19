#include <signal.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>

int status, pid;

void finhijo(){
    pid = wait(&status);
}

void main(){
    signal(SIGCHLD,finhijo);
    if(fork()==0){
        sleep(3);
        exit(5);
    }
    pause();
    printf("mi hijo a muerto con un estado %d\n",status/256);
    printf("ahroa continuo la ejecucion\n");
}