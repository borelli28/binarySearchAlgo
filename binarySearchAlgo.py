from math import floor


class BinarySearchAlgo:

    def __init__(self):
        self.counter = 0    #Used to count how many times the algorithm goes trough the while loop to find the term

    #Method take a list and the term we going to search as parameters
    def bi_search(self, ls, target):
        ls_len = len(ls)
        start = 0               #first index of list
        end = ls_len - 1        #last index on the list



        while start <= end:

            midpoint = floor((start + end) / 2)
            if ls[midpoint] < target:
                start = midpoint + 1

            elif ls[midpoint] > target:
                r = midpoint -1

            else:
                return midpoint

            self.counter += 1
            print("Iterations: {}".format(self.counter))

        return -1


# Insert your list here
list = [1,2,3,4,7,9,12,14,18,20,27,45,100]

#Target
term = 12

index = BinarySearchAlgo().bi_search(list, term)

if index >= 0:
    print("{} is at index {}".format(list[index], index))
else:
    print("Search term not found")
