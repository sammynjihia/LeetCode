# Thought process
"""
1. Convert the inputs to binary
2. Make the binary lengths even
3. compare the items

"""

class Solution:
    def hammingDistance(self, x, y):
        
        diff = 0
        x_stack = []
        y_stack = []
    
        # convert inputs to binary
        while x != 0:
            temp = x
            x = x//2
            x_stack.append(temp%2)
        
        while y != 0:
            temp = y
            y = y//2
            y_stack.append(temp%2)

        if len(x_stack) != len(y_stack):
            if len(x_stack) < len(y_stack):
                # do something
                for x in range(len(x_stack), len(y_stack)):
                    x_stack.append(0)
            else:
                # do something else
                for x in range(len(y_stack), len(x_stack)):
                    y_stack.append(0)

        print("x_stack {} y_stack {}".format(x_stack, y_stack))
            
        for w in range(0, len(y_stack)):
            
            if y_stack.pop() != x_stack.pop():
                diff += 1
                
        return diff

# Optimized solution

class Solution2:
    def hammingDistance(self, x, y):
        # convert int to binary
        x_binary_stack = self.intToBinary(x)
        y_binary_stack = self.intToBinary(y)
        diff = 0

        # make the binary stacks even
        if len(x_binary_stack) != len(y_binary_stack):
            if len(x_binary_stack) < len(y_binary_stack):
                for i in range(len(x_binary_stack), len(y_binary_stack)):
                    x_binary_stack.append(0)

            else:
                for i in range(len(y_binary_stack), len(x_binary_stack)):
                    y_binary_stack.append(0)

        # compare the stacks
        for i, j in zip(x_binary_stack, y_binary_stack):
            if i != j :
                diff += 1
        return diff

    def intToBinary(self, intNumber):
        binList = []
        while intNumber != 0:
            temp = intNumber
            intNumber = intNumber//2
            binList.append(temp%2)
        return binList

        
                

cd = Solution()
print(cd.hammingDistance(1,8))
        