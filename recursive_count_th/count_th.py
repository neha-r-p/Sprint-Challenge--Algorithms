'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    #counter for "th" initialized at 0
    count = 0
    # split word into individual letters
    letters = list(word)
    print(letters)
    print("".join(letters))
    if len(letters) == 1:
        return count
    else:

    # start at the end and see if values at n == "h" and n-1 == "t"
        #if true, then add 1 to counter
    # keep going to index n-1 until at the beginning of the word (don't check if n is the first letter, because there is no n-1)

count_th("abcthefthghith")