#create a system that visualizes different sorting algorithms 
#plan - 
#1 generate the list of numbers
#2 create a bubble sort algorithm
#3 create visualization system 
#4 add more algorithms 
#5 add menu
import random 
import time
import os

def gen_num_list(sizex):
    arr1 = list(range(1,sizex))
    random.shuffle(arr1)
    return(arr1)


def bubble_sort(bubble_list):
    sorted = False
    while sorted == False:

        prev = 0 
        next = 1
        sorted_check = True

        for i in range(len(bubble_list)-1):
            
            if bubble_list[prev] > bubble_list[next]:
                temp = bubble_list[prev]
                bubble_list[prev] = bubble_list[next]
                bubble_list[next] = temp
                sorted_check = False

            prev += 1
            next += 1

            os.system("cls")

            visual_sort = visualize(bubble_list)
            for k in range(len(visual_sort)):
                print(visual_sort[k])

            time.sleep(0.03)

        if sorted_check == True:
            sorted = True
    print(bubble_list)
    return bubble_list

def bogo_sort(bogo_list,sizex):
    sorted = False
    while sorted == False:
        temparr = []
        for i in range(len(bogo_list)):
            temparr.append(1)
        sorted_check = True

        places = list(range(0,sizex-1))
        random.shuffle(places)
        #print("places",str(places)) debug


        for i in range(0,len(bogo_list)):
            #print("i",str(i)) debug
            #print("temparr",temparr) debug
            #print("bogo_list",bogo_list) debug

            temparr[places[i]] = bogo_list[i]
        for j in range(len(temparr)-1):
            if temparr[j] > temparr[j+1]:
                sorted_check = False
        if sorted_check == True:
            sorted = True

        os.system("cls")
        
        visual_sort = visualize(temparr)
        for k in range(len(visual_sort)):
            print(visual_sort[k])

        time.sleep(0.03)
    print(temparr)
    return(temparr)

def visualize(visual_list):
    arr2 = []
    for i in range(len(visual_list)):
        length1 = visual_list[i] 
        hashtags = "#" *length1
        arr2.append(hashtags)
    return arr2

userinp = int(input("input the length of the list you wish to sort: "))
size = userinp + 1


sort_inp = gen_num_list(size)
print(sort_inp)
bubble_out = bubble_sort(sort_inp)
time.sleep(5)
bogo_out = bogo_sort(sort_inp,size)

print("bubble sort output",bubble_out)
print("bogo sort output",bogo_out)