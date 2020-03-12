//Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.
// Leetcode: https://leetcode.com/problems/shortest-palindrome
#include <iostream>
#include <string.h>
#include <stdio.h>
#include <string.h>
#include <bits/stdc++.h> 
using std::string;

class Solution {
    public:
    // Find current longest palindrome
    // Reverse remaining letters of palindrome and prepend them to the current longest palindrome.

string shortestPalindrome(string s)
{
    int n = s.size();
    string rev(s);
    std::reverse(rev.begin(), rev.end()); 
    int j = 0;
    for (int i = 0; i < n; i++) {
        std::cout<< s.substr(0, n - i) << "\t vs  "   << rev.substr(i) <<std::endl; 
        if (s.substr(0, n - i) == rev.substr(i))

            return rev.substr(0, i) + s;
    }
    return "";
}
};

int main () {
    Solution driver;
    std::cout<<(driver.shortestPalindrome("hello"));

} 