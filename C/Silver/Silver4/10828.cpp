//#include <stdio.h>
//#include <string.h>
//typedef int element;
//typedef struct {
//	element data[500];
//	int top;
//}Stack;
//
//void init_stack(Stack* s)
//{
//	s->top = -1;
//}
//int full(Stack* s)
//{
//	return (s->top == 500 - 1);
//}
//int empty(Stack* s)
//{
//	if (s->top == -1) printf("%d\n", 1);
//	else printf("%d\n", 0);
//}
//void push(Stack* s, element x)
//{
//	if (full(s))
//	{
//		fprintf(stderr, "스택이 꽉참");
//		exit(1);
//	}
//	else s->data[++(s->top)] = x;
//}
//void pop(Stack* s)
//{
//	if (s->top == -1) printf("%d\n", -1);
//	else printf("%d\n", s->data[(s->top)--]);
//}
//void size(Stack* s)
//{
//	printf("%d\n", (s->top)+1);
//}
//void top(Stack* s)
//{
//	if (s->top == -1)
//	{
//		printf("%d\n", -1);
//		return;
//	}
//	printf("%d\n", s->data[s->top]);
//}
//
//int main()
//{
//	int N, str[10], x;
//	Stack* s = (Stack*)malloc(sizeof(Stack));
//	if (!s)
//	{
//		fprintf(stderr, "스택 메모리 할당 실패");
//		exit(1);
//	}
//	init_stack(s);
//
//	scanf("%d", &N);
//	for (int i = 0; i < N; i++)
//	{
//		scanf("%s", str);
//		if (!strcmp(str, "push"))
//		{
//			scanf("%d", &x);
//			push(s, x);
//		}
//		else if (!strcmp(str, "pop")) pop(s);
//		else if (!strcmp(str, "size")) size(s);
//		else if (!strcmp(str, "empty")) empty(s);
//		else if (!strcmp(str, "top")) top(s);
//	}
//	return 0;
//}