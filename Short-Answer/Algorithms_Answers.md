#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - for every single digit increase in n, the while loop runs one more time. This means there is a linear relationship between time complexity and n.

b) O(nlog n) - the for loop is dependent on n. The inside of the for loop is a while loop, which is O(log n). Since it's nested, the loops are multiplied to determine time complexity. So, n*log n yields O(nlog n)

c) O(n) - Simple recursion. For each addition of a bunny, the function recurses a proportionate amount of times until it reaches the base case.

## Exercise II

I would use a binary search algorithm to find floor f.

Start at the floor mid way between the lowest and highest, and drop an egg. If it breaks, then I can eliminate any higher floors. If it doesn't, then I can eliminate the lower floors. I would keep dropping and egg from halfway up the remaining possible floors, and repeating these steps until I have one remaining option for f.

The runtime complexity of a binary search is O(log n)


