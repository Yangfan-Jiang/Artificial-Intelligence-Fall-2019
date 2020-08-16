#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<tuple>
#include<ctime>

#define N 9

using namespace std;

int board[N][N];

// constrains
vector< tuple<int, int> > c;
vector<bool*> avaliable;
bool isfind = false;

int x = 0;

void initialize() {
	int init_num, tmp, cons_num;
	int x, y, x2, y2;

	for (int i = 0; i < N * N; i++) {
		bool *tmp = new bool[N + 1];
		for (int j = 0; j < N + 1; j++)
			tmp[j] = false;
		avaliable.push_back(tmp);
	}

	// initialize borad, 0 stands for empty element
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			board[i][j] = 0;

	cout << "# of initial numbers: ";
	cin >> init_num;
	for (int i = 0; i < init_num; i++) {
		cout << "position (x y): ";
		cin >> x >> y;
		cout << "value: ";
		cin >> tmp;
		board[x - 1][y - 1] = tmp;
	}

	cout << "# of constrains: ";
	cin >> cons_num;
	for (int i = 0; i < cons_num; i++) {
		cout << "positions (x1 y1) (x2 y2) constrain (>)";
		cin >> x >> y >> x2 >> y2;
		c.push_back(make_tuple((x - 1) * N + (y - 1), (x2 - 1) * N + (y2 - 1)));
	}
}


void free_mem() {
	for (auto iter = avaliable.begin(); iter != avaliable.end(); ++iter) {
		delete[] * iter;
	}
}

void unassigned(vector<int> &v) {
	for (int i = N - 1; i >= 0; i--) {
		for (int j = N - 1; j >= 0; j--) {
			if (board[i][j] == 0)
				v.push_back(i*N + j);
		}
	}
}

bool getCurDom(int pos, bool avaliable[]) {
	int x = pos / N;
	int y = pos % N;
	
	for (int i = 0; i < N + 1; i++)
		avaliable[i] = true;

	for (int i = 0; i < N; i++) {
		if (board[x][i] != 0) {
			avaliable[board[x][i]] = false;
		}
		if (board[i][y] != 0) {
			avaliable[board[i][y]] = false;
		}
	}

	// check all inequality constrains
	for (auto it = c.begin(); it != c.end(); ++it) {
		int p1 = get<0>(*it);
		int p2 = get<1>(*it);
		int x1 = p1 / N;
		int y1 = p1 % N;
		int x2 = p2 / N;
		int y2 = p2 % N;

		if (pos == p1) {
			avaliable[1] = false;
			if (board[x2][y2]) {
				for (int i = 1; i <= board[x2][y2]; i++)
					avaliable[i] = false;
			}
		}
		else if (pos == p2) {
			avaliable[N] = false;
			if (board[x1][y1]) {
				for (int i = N; i >= board[x1][y1]; i--)
					avaliable[i] = false;
			}
		}
	}

	for (int i = 1; i <= N; i++)
		if (avaliable[i]) {
			return false;
		}
	return true;
}


// find the index of minimum remaining values
int MRV(const vector<int>& v) {
	int min = 0x7fffffff;
	//int min = -1;	
	int index = -1;
	for (int i = 0; i < v.size() ; i++) {
		int cnt = 0;
		for (int j = 1; j < N + 1; j++) {
			if (avaliable[v[i]][j])
				cnt++;
		}
		if (min > cnt) {
			min = cnt;
			index = i;
		}
	}
	return index;
}



void FC() {
	++x;
	// v (vector<pos>): unassigned element
	vector<int> v;
	unassigned(v);
	if (!v.size()) {
		isfind = true;
		return;
	}
	// get current dom of each unassigned element
	for (auto iter = v.begin(); iter != v.end(); ++iter) {
		if (getCurDom(*iter, avaliable[*iter]))
			return;
	}

	int min_index = MRV(v);
	int curr_mem = v[min_index];
		
	for (int i = N; i >= 1; i--) {
		if (avaliable[curr_mem][i]) {
			board[curr_mem / N][curr_mem % N] = i;
			FC();
		}
		if (isfind)
			return;
	}
	v.erase(v.begin() + min_index);
	// assigned = false
	board[curr_mem / N][curr_mem % N] = 0;
	return;
}

void printans() {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cout << board[i][j] << " ";
		}
		cout << endl;
	}
}

void test() {
	const int n = 100;
	bool x[n];
	for (int i = 0; i < n; i++)
		x[i] = true;
	for (int i = 0; i < n; i++)
		cout << x[i] << " ";
}

void debug() {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cout << board[i][j] << " ";
		}
		cout << endl;
	}
	cout << endl;
	for (auto iter = c.begin(); iter != c.end(); ++iter) {
		int p1 = get<0>(*iter);
		int p2 = get<1>(*iter);
		cout << "(" << p1/N + 1 << "," << (p1%N) + 1<< ")" \
			 << "(" << p2/N + 1 << "," << (p2%N) + 1<< ")";
		cout << endl;
	}
}



void test_mrv() {
	// unassigned element
	vector<int> v;
	for (int i = 0; i < N; i++) {
		v.push_back(i);
	}

	cout << MRV(v) << endl;
}


int main()
{
	initialize();
	clock_t startTime, endTime;
	startTime = clock();
	FC();
	endTime = clock();
	cout << "Time used: " << (double)(endTime - startTime) / (CLOCKS_PER_SEC)
		<< "s" << endl;
	printans();
	free_mem();
	cout << x << " steps" << endl;
	system("pause");
	return 0;
}

