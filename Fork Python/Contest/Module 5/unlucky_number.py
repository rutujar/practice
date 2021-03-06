
Unlucky number
You are given a list. Print the sum of the list numbers. If the list is empty then 0 gets printed. Also, the element 7 and the element next to it won't contribute to the sum.

# Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains one line of input containing the elements of the list separated by spaces.

# Output Format:
For each testcase, in a new line, print the sum as directed.

# Your Task:
This is a function problem. You don't need to take input. Complete the function realSum and return the sum.

# Constraints:
1 <= T <= 100

# Examples:
Input:
2
1 2 2 1
7 4 7 3 7 1 9
Output:
6
9

# Explanation:
Testcase 2 : 7 and its next element are skipped. skip(7,4), skip(7,3), skip(7,1). Add only 9.


#solution.py
{
#Initial Template for Python 3

//Position this line where user code will be pasted.

def main():

    testcases=int(input())
 #testcases

    while(testcases>0):

        
        mylist= [int(x) for x in input().split()]

        print(realSum(mylist))

        testcases-=1

        
if __name__=='__main__':

    main()

}


''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.

Driver Code to call/invoke your function is mentioned above. '''


#User function Template for python3

def realSum(mylist):


  if(len(mylist)==0):

    return 0

  sum=0

  
  i=0

  while(i<len(mylist)):

    if(mylist[i]==7):

      i=i+2

      continue

    sum+=mylist[i]

    i+=1

    
  return sum
