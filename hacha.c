#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>

int main(int argc, char *argv[]){
    
    int fd[2], read_file, write_file;
    int nbytes = atoi(argv[2]);
    char copyfile[50];
    strcpy(copyfile,argv[1]);
    strcat(copyfile,".h0");

    if(pipe(fd)!=-1){
        read_file = open(argv[1],O_RDONLY);
        char piece[nbytes];
        int count = 0;
        while(read(read_file,&piece,nbytes)){
            if(fork()==0){
               char copypiece[nbytes];
               char text[10];
               sleep(5);
               close(fd[1]);
               sprintf(text,"%d",count);
               strcat(copyfile,text);

               write_file = creat(copyfile,0666);
               read(fd[0],&copypiece,nbytes);
               write(write_file,&copypiece,nbytes);
               close(write_file);

               count ++;


            }
            else{
                close(fd[0]);
                
                write(fd[1],&piece,nbytes);
                
            }
            close(read_file);
        }
        
        

        
    }else{
        perror("ERROR: the pipe has not been created");
    }
}
