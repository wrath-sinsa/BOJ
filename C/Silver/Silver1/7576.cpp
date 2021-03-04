//#include <stdio.h> 
//
//int M, N;
//int tomato_lst[1000][1000], lst[2000][3];
//
//void BFS();
//
//int main()
//{
//	scanf("%d %d", &M, &N);
//
//	int chk1 = 0;
//	for (int i = 0; i < N; i++)
//	{
//		for (int j = 0; j < M; j++)
//		{
//			scanf("%d", &lst[i][j]);
//			if (tomato_lst[i][j] == 0)
//			{
//				chk1 = 1;
//			}
//		}
//	}
//	if (chk1 == 0)
//	{
//		printf("%d", 0);
//		return 0;
//	}
//
//	int a = 0;
//	for (int i = 0; i < N; i++)
//	{
//		for (int j = 0; j < M; j++)
//		{
//			if (tomato_lst[i][j] == 1)
//			{
//				lst[a][0] = i;
//				lst[a][1] = j;
//				lst[a++][2] = 0;
//			}
//		}
//	}
//	return 0;
//}
//
//void BFS()
//{
//
//}