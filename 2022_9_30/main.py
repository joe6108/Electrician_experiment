if __name__ == "__main__":
    f = open("day1.txt", "r")
    data = f.read()
    print(type(data))
    data = f.read().splitlines()
    print(type(data))
    data_length = len(data)
    count = 0
    #for i in range(0, 10, 1)
    for i in range(data_length):
        data[i] = int(data[i])
    for i in range(data_length - 1):
        if data[i+1] - data[i] > 0:
            count = count + 1
    #print(data)
    print(count)
            
