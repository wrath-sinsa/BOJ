#include <bits/stdc++.h>
using namespace std;
#define couple pair<int, int>

int N, M, lst[8][8], tmp_lst[8][8];
queue<couple> q;
queue<couple> tmp_q;
queue<couple> wall;
int move_x[4] = { 1, -1, 0, 0 };
int move_y[4] = { 0, 0, 1, -1 };
int ans = 0, tmp_ans;

void BFS();
void print();
void safe_territory_DFS(int k);
void init_lst();
//void print_q(queue<couple> pq);

int main() { // 64 C 3 
	ios_base::sync_with_stdio(false);cout.tie(NULL);cin.tie(NULL);
	cin >> N >> M;
	int a;
	for (int i = 0; i < N; i++)
		for (int j = 0; j < M; j++) {
			cin >> a;
			lst[i][j] = a;
			if (a == 2) q.push(couple(i, j));
		}
	safe_territory_DFS(0);
	cout << ans;

	return 0;
}

void safe_territory_DFS(int k) {
	if (k == 3) {
		BFS();
		return;
	}

	for (int i = 0; i < N; i++)
		for (int j = 0; j < M; j++) {
			if (lst[i][j] == 0) {
				lst[i][j] = 1;
				safe_territory_DFS(k + 1);
				lst[i][j] = 0;
			}
		}
}

void BFS() {
	init_lst();
	tmp_q = q;
	//print_q(tmp_q);
	
	while (!tmp_q.empty()) {
		couple now = tmp_q.front();
		tmp_q.pop();
		int y = now.first;
		int x = now.second;
		for (int i = 0; i < 4; i++) {
			int tmp_y = y + move_y[i];
			int tmp_x = x + move_x[i];
			//cout << tmp_y << " " <<tmp_x << "\n";
			if (0 <= tmp_y and tmp_y < N and 0 <= tmp_x and tmp_x < M) {
				if (tmp_lst[tmp_y][tmp_x] == 0) {
					tmp_lst[tmp_y][tmp_x] = 2;
					//print();
					tmp_q.push(couple(tmp_y, tmp_x));
				}
			}
		}
	}
	tmp_ans = 0;
	/*for (int i = 0; i < N; i++) {
		tmp_ans += count(tmp_lst[i], tmp_lst[i]+M, 0);
	}*/
	for (int i = 0; i < N; i++)
		for (int j = 0; j < M; j++)
			if (tmp_lst[i][j] == 0) tmp_ans += 1;
	//cout << tmp_ans << "\n";
	if (ans < tmp_ans) ans = tmp_ans;
}

void print() {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) cout << tmp_lst[i][j] << " ";
		cout << "\n";
	}
}

void init_lst() {
	for (int i = 0; i < N; i++) 
		for (int j = 0; j < M; j++) tmp_lst[i][j] = lst[i][j];
}

//void print_q(queue<couple> pq) {
//	int n = pq.size();
//	for (int i = 0; i < n; i++) {
//		couple a = pq.front();
//		cout << a.first << " " << a.second << "\n";
//		pq.pop();
//		pq.push(a);
//	}
//}