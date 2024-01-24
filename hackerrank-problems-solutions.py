'''
1. Ashish was copying from Rahit in the exam. So, Rahit told him to change the answers a little bit so that the examiner cannot find the fraud. 
But silly Ashish in the way started to change all the answers that were needed. 
He shuffled the letters in each word in a way where the maximum number of letters were misplaced.
For a given word, find the maximum difference that Ashish can generate between his answer and Rahit’s answer.
Suppose Rahit wrote “car” for an answer, Ashish can write “acr” with difference 2, or “arc” with differnece 3.

Try these inputs:
abababa
bbj
kj
kk
'''

from itertools import permutations 

def maxDiff(string):
    K = 0
    ans = 0 
    for characters in permutations(string):
        maxD = 0
        for i in range(len(string)):
            if characters[i] != string[i]:
                maxD += 1
        ans = max(ans, maxD)

    return ans
print(maxDiff("abab"))

'''
2. Here is about to introduce a new kind of number system. Where instead of 10 digits there is 20, from a to t, all in small. 
Now a means 1, b means 2 and t means 20, thenn aa means 21. Now for  a new number you have to print the decimal form it.
Note that the letters in the input string will be lower case and from a to t.
Examples:
Sample input 1: e     -> Sample Output: 5
Sample  Input 2: ac   -> Sample Output: 23
'''
def newNumSys(string, lenStr, i):
    if lenStr < 0:
        return 0
    return (ord(string[lenStr]) - ord("a") + 1) * (20**i) + newNumSys(string, lenStr - 1, i + 1)

s="aba"
print(newNumSys(s, len(s)-1, 0))
