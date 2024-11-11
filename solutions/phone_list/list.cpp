#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

signed main() {
    uint cases{};

    cin >> cases >> ws;

    for (uint i = 0; i < cases; i++) {
        uint num_nums{};

        cin >> num_nums >> ws;

        vector<string> nums(num_nums);

        for (ll j = 0; j < num_nums; j++) {
            string new_num{};
            cin >> new_num >> ws;
            nums.at(j) = new_num;
        }

        sort(nums.begin(), nums.end());

        bool valid = true;
        for(uint k = 1; k < num_nums; k++) {
            string prev = nums[k - 1];
            string curr = nums[k].substr(0, prev.size());

            if (curr == prev) {
                valid = false;
                break;
            }
        }

        cout << (valid ? "YES" : "NO") << endl;
    }
}
