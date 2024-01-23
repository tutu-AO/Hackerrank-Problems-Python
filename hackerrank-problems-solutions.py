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
