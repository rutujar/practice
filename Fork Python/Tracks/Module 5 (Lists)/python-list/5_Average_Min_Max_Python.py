#Average_Min_Max - Python
"""
Great...! You are now up with various inbuilt functions in Python List. Now, the time is to get introduced to some other useful functions, described below:
a. sum(list) : returns the sum of all elements in the list.
b. min(list) : returns the minimum element from the list.
c. max(list) : return the maximum element from the list.

Now, let's use these methods through a question. Given a list A of integers, the task is to find the average of all elements in the list, ignoring the minimum and maximum from the list. If more than one copy of min and max element exists, ignore one.

Input Format:
First line of input contains number of testcases T. For each testcase, first line of input contains N, number of elements in the list. Next line contains N elements.

Output Format:
For each testcase, print the required average.

Constraints:
1 <= T <= 100
3 <= N <= 104
1 <= A[i] <= 104

User Task:
The task is to complete the function calc_average() which returns the required average.

Example:
Input:
1
5
6 4 8 12 3

Output:
6

Explanation:
Testcase 1: Minimum element in the list is 3 and maximum is 12, so average excluding min and max is 18/3 = 6
"""

#solution.py
def calc_average(nums):

    m1=max(nums)

    m2=min(nums)

    s=(sum(nums)-m1-m2)//(len(nums)-2)

    
    return s
