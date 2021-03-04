//#include <stdio.h>
//
//int N, P, E, s;
////int TF = 0;
//int lst[20][2], used_lst[20], ans_lst[20];
//
//void duck(int k);
//void cal(int k);
//
//int main()
//{
//	scanf("%d %d %d", &N, &P, &E);
//	for (int i = 0; i < N; i++)
//	{
//		scanf("%d %d", &lst[i][0], &lst[i][1]);
//	}
//	duck(0);
//	printf("%d", -1);
//	return 0;
//}
//
//void duck(int k)
//{
//	//if (TF) return;
//
//	if (k == P)
//	{
//		for (int i = 0; i < N; i++)
//		{
//			ans_lst[i] = 0;
//		}
//		cal(0);
//		return;
//	}
//
//	for (int i = 0; i < N; i++)
//	{
//		if (!used_lst[i])
//		{
//			used_lst[i] = 1;
//			duck(k + 1);
//			used_lst[i] = 0;
//		}
//	}
//}
//
//void cal(int k)
//{
//	//if (TF) return;
//
//	if (k == P)
//	{
//		// s = sum(ans_lst)
//		s = 0;
//		for (int i = 0; i < N; i++)
//		{
//			s += ans_lst[i];
//		}
//		//printf("%d ", s);
//		if (s == E)
//		{
//			for (int i = 0; i < N; i++)
//			{
//				printf("%d ", ans_lst[i]);
//			}
//			exit(0);
//		}
//	}
//
//	for (int i = 0; i < N; i++)
//	{
//		if (used_lst[i])
//		{
//			for (int j = lst[i][0]; j <= lst[i][1]; j++)
//			{
//				used_lst[i] = 0;
//				ans_lst[i] = j;
//				cal(k + 1);
//				//if (TF) return;
//				used_lst[i] = 1;
//			}
//		}
//	}
//}
