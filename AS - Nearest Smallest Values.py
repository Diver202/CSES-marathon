def printPrevSmaller(arr):
    stack = []

    # Traverse all elements in arr
    for i in range(len(arr)):
      
        # Remove elements from stack that are greater 
        # than or equal to arr[i]
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()

        # Print "_" if stack is empty, else print top of stack
        if not stack:
            print("0", end=' ')
        else:
            print(stack[-1] + 1, end=' ')

        # Push current element to stack
        stack.append(i)

n = int(input())
del n
printPrevSmaller(tuple(map(int,input().split())))