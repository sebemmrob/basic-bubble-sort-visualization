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
def gen_num_list():
    arr1 = list(range(1,26))
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
            for k in range(len(visual_sort)-1):
                print(visual_sort[k])

            time.sleep(0.05)

        if sorted_check == True:
            sorted = True

    return bubble_list

def visualize(visual_list):
    arr2 = []
    for i in range(len(visual_list)-1):
        length1 = visual_list[i] 
        hashtags = "#" *length1
        arr2.append(hashtags)
    return arr2


sort_inp = gen_num_list()
print(sort_inp)
print(bubble_sort(sort_inp))