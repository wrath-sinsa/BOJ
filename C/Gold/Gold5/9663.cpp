//#include <stdio.h>
//
//int used_lst[14][14] = { 0, };
//int move_to_x[4] = { 1, -1 };
//int move_to_y[4] = { 1, 1 };
//int N, cnt = 0;
//void put_queen_sequence(k);
//
//int main()
//{
//	scanf("%d", &N);
//	put_queen_sequence(0);
//	printf("%d", cnt);
//	return 0;
//}
//
//void put_queen_sequence(k)
//{
//	/*for (int i = 0; i < N; i++)
//	{
//		for (int j = 0; j < N; j++)
//		{
//			printf("%d ", used_lst[i][j]);
//		}
//		printf("\n");
//	}
//	printf("\n");*/
//	// ¸¶Áö¸· 
//	if (k == N)
//	{
//		cnt += 1;
//		return;
//	}
//
//
//
//	int x, y;
//	for (int j = 0; j < N; j++)
//	{
//		if (!used_lst[k][j])
//		{
//			for (int p = 0; p < N; p++)
//			{
//				if (!used_lst[k][p])
//				{
//					used_lst[k][p] = k+1;
//				}
//			}
//			for (int q = 0; q < N; q++)
//			{
//				if (!used_lst[q][j])
//				{
//					used_lst[q][j] = k+1;
//				}
//			}
//			for (int l = 0; l < 2; l++)
//			{
//				x = j + move_to_x[l];
//				y = k + move_to_y[l];
//
//				while (0 <= x && x < N && 0 <= y && y < N)
//				{
//					if (!used_lst[y][x])
//					{
//						used_lst[y][x] = k+1;
//					}
//					x += move_to_x[l];
//					y += move_to_y[l];
//				}
//			}
//			put_queen_sequence(k + 1);
//			for (int p = 0; p < N; p++)
//			{
//				if (used_lst[k][p]==k+1)
//				{
//					used_lst[k][p] = 0;
//				}
//			}
//			for (int q = 0; q < N; q++)
//			{
//				if (used_lst[q][j]==k+1)
//				{
//					used_lst[q][j] = 0;
//				}
//			}
//			for (int l = 0; l < 2; l++)
//			{
//				x = j + move_to_x[l];
//				y = k + move_to_y[l];
//				while (0 <= x && x < N && 0 <= y && y < N)
//				{
//					if (used_lst[y][x]==k+1)
//					{
//						used_lst[y][x] = 0;
//					}
//					x += move_to_x[l];
//					y += move_to_y[l];
//				}
//			}
//
//		/*	for (int i = 0; i < N; i++)
//			{
//				for (int j = 0; j < N; j++)
//				{
//					printf("%d ", used_lst[i][j]);
//				}
//				printf("\n");
//			}
//			printf("\n");*/
//		}
//	}
//}