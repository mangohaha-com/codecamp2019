def countnum(n):
    tmp = ""
    count = 1
    word = []
    num = []
    for i in n:
        print("tmp and i: {0}, {1}".format(tmp, i))
        if tmp == i:
            count += 1
        else:
            if tmp == "":
                tmp = i
                continue
            num.append(count)
            word.append(tmp)
            count = 1
        print("i, count is : {0}, {1}".format(i, count))
        tmp = i
    num.append(count)
    word.append(tmp)
    
    return num, word
    
def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    say = "1"
    for _ in range(n - 1):
        rst = ""
        num, word = countnum(say)
        print("num, word: {0}, {1}".format(num, word))
        for nu, wd in zip(num, word):
            rst += str(nu)
            rst += wd
        say = rst
    print(say) 

countAndSay(6)
