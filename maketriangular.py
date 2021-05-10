def triangular(num):
    """
        This function make triangular number such (n*(n+1))// 2.
    """
    return (num *(num + 1))// 2

if __name__ =="__main__":
    # my_list = list(range(1, 11))
    print(list(map(triangular, range(1, 11))))
