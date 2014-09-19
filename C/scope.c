#include <stdio.h>
#include <unistd.h>

int value = 5;
int * val = & value;

int main()
{
    pid_t pid;
    pid = fork();
    if (pid == 0) { /* child process */
        value += 15;
        *val += 10;
        return 0;
    }
    else if (pid > 0) { /* parent process */
        wait(NULL);
        printf("PARENT: value = %d\n",value); /* LINE A */
        printf("val, PARENT: val = %d\n",*val); /* LINE A */
        return 0;
    }
}

