//Link bai tap https://oj.vnoi.info/problem/chain2
#include<iostream>
#include<string>

using namespace std;

const int ALPHABET_SIZE = 26;

struct Node {
	Node* child[ALPHABET_SIZE];
	bool isEnd;
};

Node *get_node() {
	struct Node *p = new Node;
	p->isEnd = false;
	for (int i = 0; i < ALPHABET_SIZE; i++) p->child[i] = NULL;
	return p;
}

void insert(Node* root, string str) {
	for (auto _char : str) {
		int i = _char - 'a';
		if (!root->child[i]) {
			root->child[i] = get_node();
		}
		root = root->child[i];
	}
	root->isEnd = true;
}


void longest_path(Node* root, int num_of_prefix, int& max_num_of_prefix) {
	if (root) {
		for (int i = 0; i < ALPHABET_SIZE; i++) {
			int t = 0;
			if (root->isEnd) t = 1;
			longest_path(root->child[i], num_of_prefix + t, max_num_of_prefix);
		}
	}
	else {
		if (num_of_prefix > max_num_of_prefix) max_num_of_prefix = num_of_prefix;
	}
}

int main() {
	Node* trie = get_node();
	int t; cin >> t; cin.ignore();
	while (t--) {
		string str;
		getline(cin, str);
		insert(trie, str);
	}
	int longest_num_of_prefix = 0;
	longest_path(trie, 0, longest_num_of_prefix);
	cout << longest_num_of_prefix;
}
