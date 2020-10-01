def swap_case(k):
        a = ""
        for i in k:
            if i.isupper() == True:
                a+= (i.lower())
            else:
                a+= (i.upper())
        return a

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
