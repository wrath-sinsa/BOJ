//#include<stdio.h>
//
//int N, M;
//int lst[10];
//int input_lst[10];
//int used_lst[10];
//
//void print_sequence(k);
//
//int main()
//{
//	scanf("%d %d", &N, &M);
//	for (int i = 0; i < N; i++)
//	{
//		scanf("%d", &input_lst[i]);
//	}
//	for (int i = 0; i < N - 1; i++)
//	{
//		for (int j = 0; j < N - i - 1; j++)
//		{
//			if (input_lst[j] > input_lst[j + 1]) 
//			{
//				int tmp = input_lst[j];
//				input_lst[j] = input_lst[j + 1];
//				input_lst[j + 1] = tmp;
//			}
//		}
//	}
//	print_sequence(0);
//	return 0;
//}
//
//void print_sequence(k)
//{
//	if (k == M)
//	{
//		for (int i = 0; i < M; i++)
//		{
//			printf("%d ", lst[i]);
//		}
//		printf("\n");
//		return;
//	}
//
//	for (int i = 0; i < N; i++)
//	{
//		if (!used_lst[i])
//		{
//			if (k != 0 && lst[k - 1] > input_lst[i])
//				continue;
//			lst[k] = input_lst[i];
//			used_lst[i] = 1;
//			print_sequence(k + 1);
//			used_lst[i] = 0;
//		}
//	}
//}