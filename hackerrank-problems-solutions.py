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
def seatingArrangement(n):
    seatPlacements = []
    i = 1

    while len(seatPlacements) < n:
        binaryNum = bin(i)[2:]
        if '11' not in binaryNum:
            seatPlacements.append(int(binaryNum))
        i += 1

    return seatPlacements
    
n = 12
placements = seatingArrangement(n)
print(placements)

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

'''
13. Find ‘k’ closest numbers
    Problem Statement: Given a sorted number array and two integers ‘K’ and ‘X’, find ‘K’ closest numbers to ‘X’ in the array. 
    Return the numbers in the sorted order. ‘X’ is not necessarily present in the array.
'''
def find_k_closest_numbers(arr, target, k):
    left, right = 0, len(arr) - 1
    while right - left + 1 > k:
        if abs(arr[left] - target) > abs(arr[right] - target):
            left += 1
        else:
            right -= 1

    return arr[left:right + 1]

# Example usage:
arr = [1, 2, 3, 4, 5]
target = 3
k = 2
result = find_k_closest_numbers(arr, target, k)
print(f"The {k} closest numbers to {target} are: {result}")

'''
14. Delete node with given key
    Problem statement: You are given the head of a linked list and a key. You have to delete the node that contains this given key.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_node(head, key):
        # print(head.next.data, key)
    # Case 1: If the key is in the head node
    if head and head.data == key:
        head = head.next
        return head

    # Case 2: Traverse the linked list to find the node with the given key
    current = head
    prev = None
    while current and current.data != key:
        prev = current
        current = current.next

    # If the key is not found, return the original head
    if not current:
        return head

    # Case 3: Delete the node with the given key
    prev.next = current.next

    return head

# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Delete node with key 3
head = delete_node(head, 3)

# Print the updated linked list
while head:
    print(head.data)
    head = head.next


'''
15. Copy linked list with arbitrary pointer
Problem statement: You are given a linked list where the node has two pointers. The first is the regular ‘next’ pointer. 
The second pointer is called ‘arbitrary_pointer’ and it can point to any node in the linked list.
Your job is to write code to make a deep copy of the given linked list. Here, deep copy means that any operations on the original list 
(inserting, modifying and removing) should not affect the copied list.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.arbitrary = None

def copy_linked_list_with_arbitrary_pointer(head):
    if not head:
        return None

    # Step 1: Create a copy of each node and insert it next to the original node
    current = head
    while current:
        new_node = Node(current.data)
        new_node.next = current.next
        current.next = new_node
        current = new_node.next
 
        
    # Step 2: Update arbitrary pointers in the copied nodes
    current = head
    while current:
        if current.arbitrary:
            current.next.arbitrary = current.arbitrary.next
        current = current.next.next

    # Step 3: Separate the original and copied linked lists
    new_head = head.next
    current = head
    new_current = new_head

    while current:
        current.next = new_current.next
        current = current.next

        if current:
            new_current.next = current.next
            new_current = new_current.next

    return new_head

# Example usage:
# Create a linked list with arbitrary pointers: 1 -> 2 -> 3 -> 4
# Arbitrary pointers: 1 -> 3, 2 -> 1, 3 -> 4, 4 -> 2
head = Node(1)
head.next = Node(2)
head.next.next = Node(7)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

head.arbitrary = head.next.next
head.next.arbitrary = head
head.next.next.arbitrary = head.next.next.next
head.next.next.next.arbitrary = head.next

# # Copy the linked list with arbitrary pointers
copied_head = copy_linked_list_with_arbitrary_pointer(head)


# Print the original and copied linked lists with arbitrary pointers
def print_linked_list_with_arbitrary_pointer(node):
    while node:
        arbitrary_data = node.arbitrary.data if node.arbitrary else None
        print(f"{node.data} (Arbitrary: {arbitrary_data})", end=" -> ")
        node = node.next
    print("None")

# # print("Original Linked List:")
print_linked_list_with_arbitrary_pointer(head)

# # print("\nCopied Linked List:")
print_linked_list_with_arbitrary_pointer(copied_head)

'''
16. Mirror binary trees
    Problem statement: Given the root node of a binary tree, swap the ‘left’ and ‘right’ children for each node.

    travesal techniques: Inorder(using this) -> Left, Root, Right
                         Preorder  -> Root, Left, Right
                         Postorder -> Left, Right, Root
'''
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def mirror_binary_tree(root):
    if root is None:
        return None

    # Swap left and right subtrees
    root.left, root.right = root.right, root.left

    # Recursively mirror the left and right subtrees
    mirror_binary_tree(root.left)
    mirror_binary_tree(root.right)

    return root

# Utility function to print the inorder traversal of a binary tree
def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.value)
        print_inorder(root.right)

# Example usage:
# Create a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Original Binary Tree (Inorder):")
print_inorder(root)

# Mirror the binary tree
mirrored_root = mirror_binary_tree(root)

print("\nMirrored Binary Tree (Inorder):")
print_inorder(mirrored_root)

'''
17. Find all paths for a sum
    Problem statement: Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.

    Here, I'm using Depth-First Search to traverse the tree. There is also Breadth-First Search.
    DFS: DFS, Depth First Search, is an edge-based technique. 
         It uses the Stack data structure and performs two stages, 
         first visited vertices are pushed into the stack, and 
         second if there are no vertices then visited vertices are popped.
         
    BFS: BFS, Breadth-First Search, is a vertex-based technique for finding the shortest path in the graph. 
         It uses a Queue data structure that follows first in first out. In BFS, one vertex is selected at 
         a time when it is visited and marked then its adjacent are visited and stored in the queue. It is slower than DFS. 
'''
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_paths_with_sum(root, target_sum):
    paths = []
    def dfs(node, current_path, current_sum):
        if not node:
            return

        current_path.append(node.value)
        current_sum += node.value

        if not node.left and not node.right:
            # Leaf node, check if the path has the target sum
            if current_sum == target_sum:
                paths.append(list(current_path))

        dfs(node.left, current_path, current_sum)
        dfs(node.right, current_path, current_sum)

        current_path.pop()  # Backtrack
    
    dfs(root, [], 0)
    return paths

# Example usage:
# Create a sample binary tree
root = TreeNode(10)
root.left = TreeNode(-5)
root.right = TreeNode(-3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.right.right = TreeNode(1)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right.right = TreeNode(1)

target_sum = 8
result_paths = find_paths_with_sum(root, target_sum)

print(f"All paths with sum {target_sum}:")
for path in result_paths:
    print(path)


'''
18. Longest substring with no more than ‘k’ distinct characters
    Problem statement: Given a string, find the length of the longest substring in it with no more than K distinct characters.

    I used the sliding window technique:
            The sliding window approach is particularly useful for solving problems that involve 
            finding subarrays or substrings that meet certain conditions, such as the longest subarray 
            with a specific sum, the shortest substring with certain properties, or, as in the previous 
            example, the longest substring with a limited number of distinct characters.
'''
def longest_substring_with_k_distinct_chars(s, k):
    if k == 0:
        return ""

    char_count = {}
    start = 0
    max_length = 0
    max_start = 0

    for end, char in enumerate(s):
        
        char_count[char] = char_count.get(char, 0) + 1

        while len(char_count) > k:
            char_count[s[start]] -= 1
            if char_count[s[start]] == 0:
                del char_count[s[start]]
            start += 1
    
        current_length = end - start + 1
        if current_length > max_length:
            max_length = current_length
            max_start = start

    return s[max_start:max_start + max_length]

# Example usage:
s = "abcabcbb"  #output: bcbb
k = 2
result = longest_substring_with_k_distinct_chars(s, k)
print(f"The longest substring with no more than {k} distinct characters is: {result}")

'''
19. Longest substring with no repeating characters
    Problem statement: Given a string, find if its letters can be rearranged in such a way that no two same characters come next to each other.
'''
def longest_substring_without_repeating(s):
    char_index = {}
    start = 0  
    max_length = 0 
    max_start = 0  

    for end, char in enumerate(s):
    
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1

        #print(char_index, char,max_start, max_length, start, end)
        char_index[char] = end
        current_length = end - start + 1
        
        if current_length > max_length:
            max_length = current_length
            max_start = start

    return s[max_start:max_start + max_length]

# Example usage:
input_str = "bbcabcbb" #output: bca
result = longest_substring_without_repeating(input_str)
print(f"The longest substring without repeating characters is: {result}")

'''
20. Equal subset sum partition
    Problem statement: Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both subsets is equal.

    I used dynamic programming to solve this problem. 
    DP is used to solve a variety of problems, including optimization problems, pathfinding problems, and problems related to combinatorics. 
    Classic examples of problems solved using dynamic programming include the Fibonacci sequence, the knapsack problem, and the longest common subsequence problem.
    This technique is particularly useful for optimization problems where the goal is to find the best solution among a set of feasible solutions.
'''
def can_partition(nums):
    total_sum = sum(nums)

    # If the total sum is odd, it cannot be partitioned into two equal subsets
    if total_sum % 2 != 0:
        return False

    target_sum = total_sum // 2
    n = len(nums)

    # Create a 2D DP table to store the intermediate results
    dp = [[False] * (target_sum + 1) for _ in range(n + 1)]

    # Base case: an empty subset can achieve a sum of 0
    for i in range(n + 1):
        dp[i][0] = True

    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= nums[i - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i - 1]]

    return dp[n][target_sum]

# Example usage:
nums = [1, 5, 11, 5]
result = can_partition(nums)
print(f"Can the set be partitioned into two equal subsets? {result}")

'''
21. Determine if the number is valid
    Problem statement: Given an input string, determine if it makes a valid number or not. 
    For simplicity, assume that white spaces are not present in the input.
'''
def is_valid_number(s):
    s = s.strip()  # Remove leading and trailing whitespaces
    if not s:
        return False  # Empty string is not a valid number
    
    # Check for the sign
    if s[0] in ('+', '-'):
        s = s[1:]
    
    # Check if the remaining characters are digits, a dot, or 'e'
    is_dot_used = False
    is_e_used = False
    for char in s:
        if char.isdigit():
            continue
        elif char == '.' and not is_dot_used and not is_e_used:
            is_dot_used = True
        elif char.lower() == 'e' and not is_e_used:
            is_e_used = True
            is_dot_used = True  # Reset dot flag as 'e' allows a dot after it
        elif char in ('+', '-') and is_e_used:
            continue  # Allow '+' or '-' immediately after 'e'
        else:
            return False  # Character is not a valid digit, dot, or 'e'
    
    return s[-1] != 'e'  # 'e' should not be the last character

# Example usage:
input_string = "+4.6E+87"
result = is_valid_number(input_string)
print(f"Is '{input_string}' a valid number? {result}")

# the easier way using float(str)
def is_valid_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

# Example usage:
number = "454.635e-4980"
result = is_valid_float(number)
print(f"Is {number} a valid float? {result}")

'''
22. Print balanced brace combinations
    Problem statement: Print all braces combinations for a given value ‘N’ so that they are balanced.
    
    I used the recursive approach to solve this problem.
    The helper function recursively adds either an opening or closing brace to the current 
    combination while ensuring that the number of left and right braces stays balanced.
'''
def generate_balanced_braces(n):
    result = []
    def generate_helper(s, left, right):
        if left == 0 and right == 0:
            result.append(s)
            return
        if left > 0:
            generate_helper(s + '(', left - 1, right)
        if right > left:
            generate_helper(s + ')', left, right - 1)
            print(s, left, right)

    
    generate_helper('', n, n)
    return result

# Example usage:
n = 2
balanced_braces = generate_balanced_braces(n)
for combination in balanced_braces:
    print(combination)

'''
23. Given a number of tasks, determine if they can all be scheduled
    Problem statement: There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. 
    Each task can have some prerequisite tasks which need to be completed before it can be scheduled. 
    Given the number of tasks and a list of prerequisite pairs, find out if it is possible to schedule all the tasks.

    I used topological sorting to solve this problem.
    Topological sorting is a linear ordering of tasks that respects their partial order, 
    meaning that if task A depends on task B, then task B comes before task A in the ordering.
'''
from collections import defaultdict, deque

def can_schedule_tasks(tasks, dependencies):
    # Build a graph to represent task dependencies
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for u, v in dependencies:
        graph[v].append(u)
        in_degree[u] += 1

    # Initialize a queue with tasks having no dependencies
    queue = deque([task for task in tasks if in_degree[task] == 0])

    # Perform topological sorting
    result_order = []
    while queue:
        current_task = queue.popleft()
        result_order.append(current_task)

        for dependent_task in graph[current_task]:
            in_degree[dependent_task] -= 1
            if in_degree[dependent_task] == 0:
                queue.append(dependent_task)

    # If the result order doesn't contain all tasks, there are cycles (dependencies cannot be satisfied)
    return len(result_order) == len(tasks)

# Example usage:
tasks = [1, 2, 3, 4, 5]
dependencies = [(2, 1), (3, 2), (4, 3), (5, 4)]
result = can_schedule_tasks(tasks, dependencies)
print(f"Can tasks be scheduled? {result}")

'''
24. Implement a LRU cache
    Least Recently Used (LRU) is a common caching strategy. 
    It defines the policy to evict elements from the cache to make room for new 
    elements when the cache is full, meaning it discards the least recently used items first.

    I used combination of OrderedDict from the 'collection' module and a custom class.
'''
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key in self.cache:
            # Move the accessed key to the end to mark it as the most recently used
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1  # Key not found

    def put(self, key, value):
        if key in self.cache:
            # Remove the existing key to update its order
            del self.cache[key]
        elif len(self.cache) >= self.capacity:
            # Remove the least recently used key if the cache is full
            self.cache.popitem(last=False)

        # Add the new key-value pair
        self.cache[key] = value
        # Move the new key to the end to mark it as the most recently used
        self.cache.move_to_end(key)

# Example usage:
lru_cache = LRUCache(3)
lru_cache.put(1, 1)
lru_cache.put(2, 2)
lru_cache.put(3, 3)

print(lru_cache.get(1))  # Output: 1 (1 is the most recently used)
print(lru_cache.get(2))  # Output: 2 (2 is now the most recently used)

lru_cache.put(4, 4)  # Remove the least recently used key (3) to make space for 4
print(lru_cache.get(3))  # Output: -1 (3 was removed, so it's not in the cache anymore)

'''
25. Find the high and low index
    Problem statement: Given a sorted array of integers, return the low and high index of the given key. 
    Return -1 if not found. 
    The array length can be in the millions with many duplicates.

    I used the binary search algorithm.
    Binary search is a search algorithm used to find the position of a target value within a sorted array. 
    It works by repeatedly dividing the search interval in half. Binary search is an efficient algorithm with a time complexity of O(log n), 
    where n is the number of elements in the array.
'''
def find_low_high_indices(arr, target):
    def binary_search(arr, target, find_low):
        low, high = 0, len(arr) - 1
        result = -1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == target:
                result = mid
                if find_low:
                    high = mid - 1  # Search for the lower index
                else:
                    low = mid + 1   # Search for the higher index
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return result

    low_index = binary_search(arr, target, True)
    high_index = binary_search(arr, target, False)

    return low_index, high_index

# Example usage:
sorted_array = [1, 2, 2, 2, 3, 4, 4, 5]
target_value = 2
low, high = find_low_high_indices(sorted_array, target_value)

print(f"Low Index: {low}")
print(f"High Index: {high}")

'''
26. Merge overlapping intervals
    You are given an array (list) of interval pairs as input where each interval has a start and end timestamp. 
    The input array is sorted by starting timestamps. 
    You are required to merge overlapping intervals and return output array (list).
'''
def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort intervals based on their start points
    intervals.sort(key=lambda x: x[0])

    print(intervals)

    merged = [intervals[0]]

    print(merged)

    for i in range(1, len(intervals)):
        current_start, current_end = intervals[i]
        previous_start, previous_end = merged[-1]

        # Check for overlap
        if current_start <= previous_end:
            # Merge intervals
            merged[-1] = [previous_start, max(current_end, previous_end)]
        else:
            # No overlap, add the current interval to the result
            merged.append([current_start, current_end])

    # return merged

# Example usage:
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
merged_intervals = merge_intervals(intervals)
print("Merged Intervals:", merged_intervals)

