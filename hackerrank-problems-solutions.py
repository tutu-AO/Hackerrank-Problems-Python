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

'''
3. Semester exams are going on for university students. Examiners noticed that a group of people are trying to cheat. 
They marked students of that group as ‘1’ and students of another group ( who are not cheating ) as ‘0’ 
We can reduce cheating by not allowing students from group 1 to sit together, means no two students from group 1 can sit together. 
Seatings are marked using above conditions. Your task is to give the seating placement of nth possibility Possibility order from 1 to 10 is given below

[1  10  100  101  1000  1001  1010  10000  10001  10010]
Examples:
4 -> 101
6 -> 1001
9 -> 10001
'''
pos = 10
n = pos + 1
arr = ["0"] * (n)
arr[0] = "1"
counter = 1
i = 0
while counter < n:
    if arr[i][-1] == "0":
        arr[counter] = arr[i] + "0"
        counter += 1
        if counter >= n:
            break
        arr[counter] = arr[i] + "1"
        counter += 1
        if counter >= n:
            break
        i += 1
    elif arr[i][-1] == "1":
        arr[counter] = arr[i] + "0"
        counter += 1
        if counter >= n:
            break
        i += 1
input = 4  # you can pass 6 and 9 as well
print(arr[input - 1])

'''
4. Ryuk, the Shinigami (God of death) had allowed Light Yagami, a school student, to kill as many people as he can by using a death note. 
But writing the names barely will allow other people to watch them. So he encrypts the names using digits, where a means 1, b means 2 and so on upto z is 26. 
Now if he gives numbers, there is a communication error because a number string can be decrypted by the death note in various ways and eventually killing them all. 
If everyone in the world has a unique name, for a given number, how many people can die?

NOTE THAT: There is every possible name in the world with the 26 letters, and capital or small letters is not a problem.

Input format:
A number stream denoting the first name’s encrypted version

Output Format:
Number of people dying by this.

Example:
Sample Input: 1267
Sample Output: 3 -> azg, lfg, abfg
'''
def deathNote(string, n):
    if n == 0 or n == 1:
        return 1
    
    ans = 0
    if string[n - 1] > "0":
        ans = deathNote(string, n-1)
    if string[n - 2] == "1" or string[n - 2] == "2":
        ans += deathNote(string, n-2)
        
    return ans  
    
s = "1267"
l = len(s)
print(deathNote(s, l))

'''
5. Choco, a chocolate lover, has N amount of money with him. He wants to buy as much chocolate as possible. 
So, he goes to a chocolate shop “Bandyman ”. Mike, the owner of “Bandyman ” has different types of chocolate in his store (represented by a character) placed in a row.
Mike, give an offer to Choco that he can buy a selected type of chocolate for free and need to pay for the other types of chocolates and Choco can only buy consecutive chocolates.
Now, you need to write a code to find the maximum amount of chocolates Choco can get by selecting the chocolates optimally.

Input format :
1st line contains 2 space separated integers A and B denoting the number of chocolates and the amount of money Choco has.
The 2nd line contains A chocolates represented by a string. All chocolates represented by lowercase alphabets.
The 3rd line represents 26 space separated integers representing the cost to buy the chocolates.
[First integer represents the cost of the chocolate of type ‘a’, 2nd integer represents the cost of the chocolates of type ‘b’ and so on]

Output format :

Print the maximum number of chocolates Choco can buy.
Sample input 1 :
6 10
aabcda
5 4 4 5 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1

Sample output 1 :
4

Explanation :
Choco can select the chocolate of type ‘a’ for free and start buying from index 0 and if he buys “aabc” then he has to pay less (0+0+4+4=8) than the total money he has.
This is the maximum number of chocolates he can get in this case.
'''

input1 = """6 10"""
input2 = """aabcda"""
input3 = """5 4 4 5 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1"""

num, cash = map(int, input1.split())
types = input2.strip()
cost = list(map(int, input3.split()))

disTypes = list(set(types))
maxQuantity = 0
for i in disTypes:
    arr = []
    for j in types:
        if i == j:
            arr.append(0)
        else:
            arr.append(cost[ord(j) - 97])
            
    counter = 0
    sum = 0
    totalCho = 0
    while counter < num:
        sum += arr[counter]
        if sum < cash:
            totalCho += 1
        else:
            maxQuantity = max(maxQuantity, totalCho)
            break
        
        counter += 1
print(maxQuantity)

'''
6. Suppose you are in a number system, where if the number doesn’t contain 2 in the unit digit then the number is not valid. 
So the first number of the number system is 2, the second number is 12, and the third is 22.
for a given integer n, you have to print the nth element of the number system.

Input Format:
First line, containing n denoting the number of test cases.
then n number of lines for the query.

Output Format:
Print the consecutive number in the number system for each query.

Sample Input:
3

Sample Output:
22

Explanation:
1st number will be 2 , 2nd number will be 12 and third number will be 32
'''
def numSys(n):
    return (n - 1) * 10 + 2

input = 3   '''put the nth integer here'''
output = ""
for i in range(1, input + 1):
    output += str(numSys(i)) + " "

print(output)

'''
7. There is an encryption game going on. You will be given a number. If a digit is prime, it will take a vowel. 
Otherwise it will take a consonant value. By this process, you have to make the string the lexicographically smallest possible. 
For a given number, print the output as a string.;

Input Format:
An integer n denoting the number.
Output Format:
The encrypted word.

Sample Input: 123421
Sample Output: baecab
'''
input  = "123421"
vowels = "aeiou"
conso  = "bcdfghjklmnpqrstvwxyz"
primeDigits = "2357"
x, y = 0, 0
sortedInput = sorted(set(input))
arr = []
for i in sortedInput:
    if i in primeDigits:
        arr.append(vowels[x])
        x += 1
    else:
        arr.append(conso[y])
        y += 1

output = ""
for i in input:
    output += arr[sortedInput.index(i)]

print(output)

'''
8. Jack is learning to type english from the beginning and he is making an error of repeating the same words in his texts over whatsapp. 
Write a function that will take input for his text sent to you and then keep only the unique texts. Note that, 
the uniqueness is about being word specific not position, there are nothing but alphabets in the sentences and words are separated only with white space.

Sample Input:
Send send the image send to to to me

Output:
Send the mage to me
'''
input = "Send send the image send to to to me"
arr = input.split()
output = []
res = ""
for i in arr:
    if i not in output:
        output.append(i.lower())
        res += i + " "

print(res)

'''
9. A prime number is a number which is divisible by one and itself. 
Also a number is called a good  prime number if the sum of its digits is a prime number. 
For example a number 23 is a good prime number because the sum of 2 and 3 ( 2+3=5) is 5 which is a prime number. 
You are given an integer K. Your task is to find the kth good prime number that is greater than a provided number N.

For example , 232 is a good prime number since the sum of all digits is 7 which is a prime number whereas 235 is not a good prime number.

Input format :
    The first line contains an integer N.
    The next line contains an integer K.

Output format :
A single integer which is a Kth good prime number that is greater than a provided number N.

Sample Input 1:
4  4

Sample Output 1:
12

Explanation :
Good prime numbers starting from 4 are 5,7,11(1+1=2 which is prime number),12(1+2=3 which is prime number),14(1+4=5 which is a prime number) and so on. 
Because the sum of digits of an individual number is a prime number And 4 th good prime number is 12 in this series.Hence the output is 12. 
'''
def isPrime(num):
    flag = True
    if num == 1:
        flag = False
    elif num > 2:
        for i in range(2, num):
            if (num % i) == 0:
                flag = False
                break

    return flag
    
input = """4 4"""
n, m = map(int, input.split())
counter = 0
arr = []
for i in range(n + 1, 100000):
    temp = i
    sum = 0
    while temp != 0:
        sum += temp % 10
        temp = temp // 10
    if(isPrime(sum)):
        arr.append(i)
        counter += 1
        
    if counter == m:
        break

print(arr, "output:", arr[n-1])

'''
10. Given word return the next alphabetically greater string in all permutations of the word. 
If there is no greater permutation return the string ‘no answer’ instead. Write a code for it

Example:
input -> "baca"
output -> "bcaa"
'''
from itertools import permutations

def next_permutation(word):
    # Generate all permutations of the word
    all_permutations = sorted(set(permutations(word)))

    # Find the index of the given word in the sorted list
    current_index = all_permutations.index(tuple(word))

    # If the current index is the last one, there is no next permutation
    if current_index == len(all_permutations) - 1:
        return "no answer"

    return ''.join(all_permutations[current_index + 1])

word = "baca"
result = next_permutation(word)
print(result)

'''
11. Given a string colors, where each character is either white or black, Wendy and Bob play a game to manipulate this string as follows:
• They perform moves alternatively in turns and Wendy makes the first move.
• In a single move, Wendy can remove from the string any white character that has exactly 2 white neighbors.
• Similarly, in a single move, Bob can remove from string any black character that has exactly 2 black neighbors.
• When a character is removed, the strings shrink itself, so if a character Y had neighbors X and Z on its left and right respectively before the move, after the move is made, X and Z become each other's neighbors.
• The first player who cannot perform a move loses the game. For example, if the colors string is wwwbb, with the first move Wendy will change it to wwbb, and Bob can no longer perform a move. 
Determine who has a winning strategy assuming that both Wendy and Bob play optimally

Example:
input -> "wwwbbbbwww"
output -> bob
'''
def game_winner(colors):
    players = {"wendy", "bob"}
    curr_player = "wendy"
    winner = ""

    while True:
        move_made = False
        index = colors.find("www" if curr_player == "wendy" else "bbb")
        if index != -1:
            # 3 consecutive characters found, remove the middle one
            colors = colors[:index + 1] + colors[index + 2:]
            move_made = True
            winner = curr_player
            curr_player = players.difference({curr_player}).pop()

        # If no moves possible, break
        if not move_made:
            if winner == "":
                winner = players.difference({curr_player}).pop()
            break
    return winner

# Example usage:
colors = "wwwb"
result = game_winner(colors)
print(f"The winner is: {result}")

'''
12. Find the kth largest element in a number stream
    Problem Statement: Design a class to efficiently find the Kth largest element in a stream of numbers. The class should have the following two things: ​
        The constructor of the class should accept an integer array containing initial numbers from the stream and an integer ‘K’.
        The class should expose a function add(int num) which will store the given number and return the Kth largest number.
'''
class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.nums = nums

    def add(self, val):
        self.nums.append(val)
        self.nums.sort(reverse=True)
        return self.nums[self.k - 1]

# Example usage:
k = 3
nums = [4, 5, 8, 2]
kth_largest = KthLargest(k, nums)

print(kth_largest.add(3))  # Output: 4
print(kth_largest.add(5))  # Output: 5
print(kth_largest.add(10)) # Output: 5
print(kth_largest.add(9))  # Output: 8
print(kth_largest.add(4))  # Output: 8
