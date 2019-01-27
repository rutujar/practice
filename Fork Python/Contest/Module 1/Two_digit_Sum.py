#Two digit Sum
"""
You are given a two digit number n. Find the sum of its digits

#Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains one line of input containing n.

#Output Format:
For each testcase, in a new line, print the sum of digits of n.

#Your Task:
This is a function problem. You do not need to take any input. Complete the function digitsSum and return the sum of digits of n.

#Constraints:
1 <= T <= 100
10 <= n <= 99

#Example:
Input:
1
25
Output:
7
"""

#solution.py

def digitsSum(n):

    s = 0

    while n:

        s += n % 10

        n //= 10

    return s
