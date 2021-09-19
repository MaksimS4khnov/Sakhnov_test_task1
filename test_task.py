import random

def test_task(n):
    #create empty array
    start_arr = []

    #add arrays to start_array
    for i in range (0, n + 1):
        #create transit_arr which we will fill in with random numbers
        transit_arr = []
        #create random length for array
        transit_len = int((random.random())*100)
        for j in range (0, transit_len + 1):
            transit_arr.append(int((random.random())*100))

        #sorting an array based on the following conditions
        if ( i % 2 == 0 ):
            transit_arr.sort()
        else:
            transit_arr.sort(reverse=True)

        start_arr.append(transit_arr)

    return (start_arr)


print("Input n")
n = int(input())
print(test_task(n))