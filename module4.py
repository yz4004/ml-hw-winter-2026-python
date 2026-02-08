"""
The program asks the user for input N (positive integer) and reads it

Then the program asks the user to provide N numbers (one by one) and reads all of them (again, one by one)

In the end, the program asks the user for input X (integer)
and outputs: "-1" if there were no such X among N read numbers,

or the index (from 1 to N) of this X if the user inputed it before.
"""
print("please input a number and enter:")
N = int(input())

nums = []
print(f"please input {N} numbers you just entered and click enter after each input:")
for _ in range(N):
    nums.append(int(input()))
print("here is your input: ", nums)
print("please input another number x:")
X = int(input())

if X in nums:
    print("here is the index of x in your previous input：", nums.index(X) + 1)
else:
    print(-1)
