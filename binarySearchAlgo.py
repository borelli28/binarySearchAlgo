


class BinarySearchAlgo:

    #Take the list where we will conduct the binary search as a parameter.
    def __init__(self, ls):
        self.ls = ls


    #This method will ask the user for the element that the algorithm will look for and saved it to a variable and then return that element at the end.
    def precious_element(self):

        ask_user_elmt = input("What number you want me to look for: ")

        precious_int_elmt = int(ask_user_elmt)

        return precious_int_elmt

    #Finds the midpoint of the given list.
    def midpoint(self):

        # self.ls = [1, 2, 3, 4, 5, 6, 7]   #Keep commented if not debugging! This list is used to test the midpoint() return.

        #get the lenght of the list and divided by two to get the middle point of the list
        ls_midpoint = len(self.ls) / 2

        #when ls_midpoint divide odd numbers it will give a float number. So this var will use round() to round it to a whole number
        midpoint_rounded = round(ls_midpoint)

        return int(midpoint_rounded)



# #test the precious_element() method
# print(BinarySearchAlgo().precious_element())

# #test the midpoint() method
# print(BinarySearchAlgo().midpoint())