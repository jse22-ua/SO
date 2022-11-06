#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>

void espera(){

}

void ejecutar(){
    execlp("pstree","pstree","-p",NULL);
}



int main(int argc, char *argv[]){
    int pid_arb;
    int pids[3];//A,B,x
    int y,z;
    int estado;

    pid_arb=getpid();
    printf("Soy el proceso ejec: mi pid es %d.\n",pid_arb);
    if(fork()==0){
        
        pids[0]=getpid();//Proceso A
        printf("Soy el proceso A: mi pid es %d. Mi padre es %d.\n", pids[0],pid_arb);
        if(fork()==0){
            pids[1]=getpid();//Proceso B
            printf("Soy el proceso B: mi pid es %d. Mi padre es %d. Mi abuelo es %d.\n", pids[1],pids[0],pid_arb);
                    
            for(int j=0;j<3;j++){
                    if(fork()!=0){

                        switch(j){
                            case 0: // Proceso X
                                pids[2]=getpid();
                                printf("Soy el proceso X: mi pid es %d. Mi padre es %d. Mi abuelo es %d. Mi bisabuelo es %d\n", pids[2], pids[1],pids[0],pid_arb);
                                signal(SIGALRM,espera);
                                alarm(8);
                                pause();
                               
                                printf("Soy X (%d) y muero\n",pids[2]);
                                exit(0);
                                break;
                            case 1: //Proceso Y
                                y=getpid();
                                printf("Soy el proceso Y: mi pid es %d. Mi padre es %d. Mi abuelo es %d. Mi bisabuelo es %d\n", y, pids[1],pids[0],pid_arb);
                                signal(SIGALRM,espera);
                                alarm(6);
                                pause();
                                
                                printf("Soy Y (%d) y muero\n",y);
                                exit(0);
                                break;
                            default://proceso z
                            
                                z=getpid();
                                printf("Soy el proceso Z: mi pid es %d. Mi padre es %d. Mi abuelo es %d. Mi bisabuelo es %d\n", z, pids[1],pids[0],pid_arb);
                                signal(SIGALRM,ejecutar);
                                alarm(5);
                                pause();
                                printf("Soy Z (%d) y muero\n",z);
                                exit(0);
                                break;
                                
                                
                                
                        }
                    }
                    
                }
                    for(int i=0;i<3;i++){
                        wait(&estado);
                    }
                    printf("Soy B (%d) y muero\n",pids[1]);
                    exit(0);
        }else{
            //proceso A
            
                    wait(&estado);
                    printf("Soy A (%d) y muero\n",pids[0]);
                    exit(0);
        }

    }
    wait(&estado);
    printf("Soy ejec (%d) y muero\n",pid_arb);
    exit(0);
    return 0;
}
