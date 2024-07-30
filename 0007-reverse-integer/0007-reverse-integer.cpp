class Solution {
public:
    int reverse(int x) {
        int rem = 0, old = 0;
        while (x != 0) {
            rem = x % 10;
            // Check if the new number will cause overflow
            if (old > INT_MAX / 10 || (old == INT_MAX / 10 && rem > 7)) {
                return 0;
            }
            if (old < INT_MIN / 10 || (old == INT_MIN / 10 && rem < -8)) {
                return 0;
            }
            old = old * 10 + rem;
            x = x / 10;
        }
        return old;
    }
};
