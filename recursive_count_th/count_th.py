'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, count=0):
    
    # TBC
    #counter for "th" initialized at 0
    # split word into individual letters
    letters = list(word)
    # print(letters)
    # print("".join(letters))
    if len(letters) <= 1: #if there is no string or the list is down to 1
        return count
    else:
    # start at the end and see if values at n == "h" and n-1 == "t"
        if letters[len(letters)-1] == "h" and letters[len(letters)-2] == "t":
        #if true, then add 1 to counter
            count += 1
        # keep going to index n-1 until at the beginning of the word
        return count_th("".join(letters[:-1]), count)


print(count_th("abcthefthghith"))