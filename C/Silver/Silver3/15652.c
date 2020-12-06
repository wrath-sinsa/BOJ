//#include<stdio.h>
//
//int N, M;
//int lst[10] = { 0 , };
//
//void print_sequence(k);
//
//int main()
//{
//	scanf("%d %d", &N, &M);
//	print_sequence(0);
//	return 0;
//
//}
//
//void print_sequence(k)
//{
//	if (k == M)
//	{
//		for (int i = 0; i < M; i++)
//			printf("%d ", lst[i]);
//		printf("\n");
//		return;
//	}
//
//	for (int i = 0; i < N; i++)
//	{
//		if (k != 0 && lst[k - 1] > i + 1)
//			continue;
//		lst[k] = i + 1;
//		print_sequence(k + 1);
//	}
//}