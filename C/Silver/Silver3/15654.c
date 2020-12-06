#include <stdio.h>

int N, M;
int lst[10];
int N_lst[10];
int used_lst[10];

void print_sequence(k);
int main()
{
	scanf("%d %d", &N, &M);

	// __init__
	for (int i = 0; i < N; i++)
	{
		scanf("%d", &N_lst[i]);
	}
	// __bubble_sort__
	for (int i = 0; i < N - 1; i++)
	{
		for (int j = 0; j < N - i - 1; j++)
		{
			if (N_lst[j] > N_lst[j + 1])
			{
				int tmp = N_lst[j];
				N_lst[j] = N_lst[j + 1];
				N_lst[j + 1] = tmp;
			}
		}
	}
	print_sequence(0);
	return 0;
}

void print_sequence(k)
{
	if (k == M)
	{
		for (int i = 0; i < M; i++)
			printf("%d ", lst[i]);
		printf("\n");
		return;
	}

	for (int i = 0; i < N; i++)
	{
		if (!used_lst[i])
		{
			lst[k] = N_lst[i];
			used_lst[i] = 1;
			print_sequence(k + 1);
			used_lst[i] = 0;
		}
	}
}