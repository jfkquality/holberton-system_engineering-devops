#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

/**
 * main - create 5 zombie processes
 *
 * Return;0
 */
int main()
{
	int i = 0;

	for (i; i < 5; i++)
	{
		/* Fork returns process id in parent process */
		pid_t child_pid = fork();

		/* Parent process */
		if (child_pid > 0)
			sleep(5);

		/* Child process */
		else
		{
			printf("Zombie process created, PID: %ul\n", getpid());
			exit(0);
		}
	}
	int infinite_while(void)
	{
		while (1)
		{
			sleep(1);
		}
		return (0);
	}
	return 0;
}
