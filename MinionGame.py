def minion_game(x):
    # your code goes here
    n = len(x)

    stuart = 0
    kevin = 0

    for i in range(n):
        if x[i] in ('A','E','I','O','U'):
            kevin += n - i
        else:
            stuart += n - i


    if kevin > stuart:
        return print("Kevin",kevin)
    elif stuart > kevin:
        return print("Stuart",stuart)
    else:
        return print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)