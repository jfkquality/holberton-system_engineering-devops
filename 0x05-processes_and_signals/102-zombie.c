#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

/**
 * infinite_while - infinite loop
 *
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - create 5 zombie processes
 *
 * Return: 0
 */
int main(void)
{
	int i = 0;
	pid_t child_pid;

	for (; i < 5; i++)
	{
		/* Fork returns process id in parent process */
		child_pid = fork();

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
	infinite_while();
	return (0);
}
