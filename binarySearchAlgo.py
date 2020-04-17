


class BinarySearchAlgo:

    #Take the list where we will conduct the binary search as a parameter.
    def __init__(self):
        #self.ls = ls
        self.ls = [1, 2, 3, 4, 5, 6, 7]     #temporary list created to test methods while creating program. When done with the program, should delete this list and add ls as a parameter of __init__

    #This method will ask the user for the element that the algorithm will look for and saved it to a variable and then return that element at the end.
    def precious_element(self):

        # ask_user_elmt = input("What number you want me to look for: ")
        #
        # precious_int_elmt = int(ask_user_elmt)

        precious_int_elmt = 7   #This is a temporary variable used when creating the program to test the methods. We finished creating the program, Uncomment the above to lines and delete this variable.

        return precious_int_elmt

    #Finds the midpoint of the given list.
    def midpoint(self, ls):

        # ls = [1, 2, 3, 4, 5, 6, 7]   #Keep commented if not debugging! This list is used to test the midpoint() return.

        #get the length of the list and divide by two to get the middle point
        ls_midpoint = len(ls) / 2

        #when ls_midpoint divide odd numbers it will give a float number. So this var will use round() to round it to a whole number
        midpoint_rounded = round(ls_midpoint)

        return int(midpoint_rounded)


    def bi_search(self):

        #this variable holds the element we looking for in the list
        og_element = self.precious_element()

        #this variable holds the original list given in init
        og_list = self.ls

        #find the midpoint of the original list
        og_ls_midpoint = self.midpoint(og_list)

        #if loops will check if the midpoint is the element else keep dividing and looking for the element
        if og_ls_midpoint == og_element:
            return "Found the element Yay!"

        elif (og_element > og_ls_midpoint):

            #Find the index of the midpoint
            midpoint_idx = og_list.index(og_ls_midpoint)

            #give the index of the next number after the midpoint. By adding one to the midpoint index.
            midpoint_plus_one = midpoint_idx + 1

            #Creates a local list with the rest of the list after we first divide the original list.
            local_ls = og_list[midpoint_plus_one: ]


            return local_ls




        elif (og_element < og_ls_midpoint):
            pass





# #test the precious_element() method
# print(BinarySearchAlgo().precious_element())

# #test the midpoint() method. Needs to print --> 4
# print(BinarySearchAlgo().midpoint())

#test bi_search() method
print(BinarySearchAlgo().bi_search())

