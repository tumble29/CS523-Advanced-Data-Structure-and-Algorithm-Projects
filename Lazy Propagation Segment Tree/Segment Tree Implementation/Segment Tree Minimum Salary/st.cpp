#include<iostream>
#include<vector>
#include<string>
#include<fstream>
#include<math.h>
using namespace std;

class Node {
public:
	int value, lazy_value;
	Node(int v, int lv) { value = v; lazy_value = lv; }
};

class LazySegmentTree {
private:
	vector<Node> lst;
	int arr_size;
	void construct_tree_util(vector<int>arr, int ss, int se, int si) {
		if (ss > se) return;
		if (ss == se) {
			this->lst[si] = Node(arr[ss], 0);
			return;
		}
		int mid = (ss + se) / 2;
		construct_tree_util(arr, ss, mid, si * 2 + 1);
		construct_tree_util(arr, mid + 1, se, si * 2 + 2);
		this->lst[si] = Node(min(lst[si * 2 + 1].value, lst[si * 2 + 2].value), 0);
	}
	void update_range_util(int si, int ss, int se, int us, int ue, int diff) {
		if (this->lst[si].lazy_value) {
			lst[si].value += lst[si].lazy_value;
			if (ss != se) {
				lst[si * 2 + 1].lazy_value += lst[si].lazy_value;
				lst[si * 2 + 2].lazy_value += lst[si].lazy_value;
			}
			lst[si].lazy_value = 0;
		}

		// Ngoai pham vi
		if (ss > se || ss > ue || se < us) return;

		// Pham vi nam hoan toan trong pham vi can cap nhat
		if (ss >= us && se <= ue) {
			lst[si].value += diff;
			if (ss != se) {
				lst[si * 2 + 1].lazy_value += diff;
				lst[si * 2 + 2].lazy_value += diff;
			}
			return;
		}

		// Pham vi khong nam hoan toan
		int mid = (ss + se) / 2;
		update_range_util(si * 2 + 1, ss, mid, us, ue, diff);
		update_range_util(si * 2 + 2, mid + 1, se, us, ue, diff);
		lst[si] = Node(min(lst[si * 2 + 1].value, lst[si * 2 + 2].value), 0);
	}
	int get_min_util(int ss, int se, int qs, int qe, int si) {
		if (lst[si].lazy_value) {
			lst[si].value += lst[si].lazy_value;
			if (ss != se) {
				lst[si * 2 + 1].lazy_value += lst[si].lazy_value;
				lst[si * 2 + 2].lazy_value += lst[si].lazy_value;
			}
			lst[si].lazy_value = 0;
		}

		if (ss > se || ss > qe || se < qs) return numeric_limits<int>::max();

		if (ss >= qs && se <= qe) return lst[si].value;

		int mid = (ss + se) / 2;
		return min(get_min_util(ss, mid, qs, qe, si * 2 + 1), get_min_util(mid + 1, se, qs, qe, si * 2 + 2));
	}
	

public:
	void construct_tree(vector<int> arr) {
		this->arr_size = arr.size();
		int size = 2 * pow(2, ceil(log2(arr.size()))) - 1;
		lst.assign(size, { 0,0 });
		construct_tree_util(arr, 0, arr_size - 1, 0);
	}
	void update_range(int us, int ue, int diff) {
		update_range_util(0, 0, arr_size - 1, us, ue, diff);
	}
	int get_min(int qs, int qe) {
		if (qs<0 || qe>arr_size - 1 || qs > qe) return 0;
		return get_min_util(0, arr_size - 1, qs, qe, 0);
	}

};


int main() {
	LazySegmentTree lst;

	//Get data from csv file
	fstream f("thunhapbinhquan.csv", fstream::in);
	vector<int>total_average_income;
	string t;
	getline(f, t);
	for (; f >> t;) {
		string str;
		getline(f, str);
		if (str.size() == 0) break;
		size_t found = 0;
		for (int i = 0; i < 3; i++)
			found = str.find("\t", found + 1);
		string s = str.substr(found + 1, str.find('\t', found + 1) - found - 1);
		s.erase(remove(s.begin(), s.end(),'\0'), s.end());
		total_average_income.push_back(stoi(s));
	}
	f.close();

	lst.construct_tree(total_average_income);
	cout << numeric_limits<int>::min() << endl;
	lst.update_range(0, 10, 500);
	cout<<lst.get_min(0, 20)<<endl;
}
