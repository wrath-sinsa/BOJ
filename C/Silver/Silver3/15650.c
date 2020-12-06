#include <stdio.h>

int N, M;
int lst[10] = { 0, };
int isused_lst[10] = { 0, };

void print_sequence(k);

int main()
{
    scanf("%d %d", &N, &M);
    print_sequence(0);
    return 0;
}

void print_sequence(k)
{
    if (k == M)
    {
        for (int i = 0; i < M; i++)
        {
            printf("%d ", lst[i]);
        }
        printf("\n");
        return;
    }

    for (int i = 0; i < N; i++)
    {
        if (isused_lst[i] == 0)
        {
            if (k == 0)
            {
                lst[k] = i + 1;
            }
            else
            {
                if (lst[k - 1] < i + 1)
                    lst[k] = i + 1;
                else continue;
            }
            // if (k != 0 && lst[k-1] >= i + 1)
            //     continue;
            // lst[k] = i + 1
            isused_lst[i] = 1;
            print_sequence(k + 1);
            isused_lst[i] = 0;
        }
    }
}