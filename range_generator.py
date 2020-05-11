#This function will generate a range from minimum to maximum with step
def range_generator(minimum, maximum, step):
    my_list = []
    while minimum <= maximum and step > 0:
        my_list.append(minimum)
        minimum += step
    return(my_list)
if __name__=='__main__':
    print(range_generator(1,10,1))
    print(range_generator(1,10,2))
    print(range_generator(1,10,3))
