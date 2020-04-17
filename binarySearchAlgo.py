


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


        return 1

    #Finds the midpoint of the given list.
    def midpoint(self, ls):

        # ls = [1, 2, 3, 4, 5, 6, 7]   #Keep commented if not debugging! This list is used to test the midpoint() return.

        #get the length of the list and divide by two to get the middle point
        ls_midpoint = len(ls) / 2

        #when ls_midpoint divide odd numbers it will give a float number. So this var will use round() to round it to a whole number
        midpoint_rounded = round(ls_midpoint)

        #needs to subtract 1 so we can get the index real index number
        midpoint_idx = midpoint_rounded - 1

        #Convert the index number into the value of the midpoint in the list
        the_ls_midpoint_value = ls[midpoint_idx]

        return the_ls_midpoint_value


    def bi_search(self):

        # Variable that gets updated every time the list get divided
        counter = 0

        #index in the og_list of the element(og_element) we are looking for
        self.idx_og_element = []

        #this variable holds the original list given in init
        og_list = self.ls

        #find the midpoint of the original list
        og_ls_midpoint = self.midpoint(og_list)

        #while current element is not the element we looking for(og element) enter this loop.
        while(og_ls_midpoint != self.precious_element()):


            if (self.precious_element() > og_ls_midpoint):

                # Find the index of the midpoint
                midpoint_idx = self.ls.index(og_ls_midpoint)

                # update the index number of the current midpoint
                self.idx_og_element.append(midpoint_idx)

                # give the index of the next number after the midpoint. By adding one to the midpoint index.
                midpoint_plus_one = midpoint_idx + 1

                #The algorithm is going to divide the list and create a new one so we add one to the counter
                counter += 1

                # Creates a local list with the rest of the list after we first divide the original list.  And then assign the value of the new local variable to the og_ls. That way we can reuse this if loops and keep dividing the list until we find the element.
                local_ls = og_list[midpoint_plus_one:]

                og_ls = local_ls


            if (self.precious_element() < og_ls_midpoint):

                # Find the index of the midpoint
                midpoint_idx = self.ls.index(og_ls_midpoint)
                #return midpoint_idx

                # update the index number of the current midpoint
                self.idx_og_element.append(midpoint_idx)

                # The algorithm is going to divide the list and create a new one so we add one to the counter
                counter += 1

                # Creates a local list with the rest of the list after we first divide the original list. And then assign the value of the new local variable to the og_ls. That way we can reuse this if loops and keep dividing the list until we find the element.
                local_ls = og_list[: midpoint_idx]

                # Dont need midpoint_idx + 1 for this one.
                og_ls = local_ls


            #find the midpoint of the new list
            og_ls_midpoint = self.midpoint(og_ls)


        # if loops will check if the midpoint is the element else keep dividing and looking for the element
        if (og_ls_midpoint == self.precious_element()):

            print("Iterations: " + str(counter))
            print(self.idx_og_element)
            return "Found the element Yay!"











# #test the precious_element() method
# print(BinarySearchAlgo().precious_element())

# #test the midpoint() method. Needs to print --> 4
# print(BinarySearchAlgo().midpoint())

#test bi_search() method
print(BinarySearchAlgo().bi_search())

