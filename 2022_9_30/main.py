if __name__ == "__main__":
    with open("C:\\Users\\s8874\\Desktop\\Electrician_experiment\\2022_9_30\\day1.txt","r") as f:
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
            
