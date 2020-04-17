


class BinarySearchAlgo:


    #This method will ask the user for the element that the algorithm will look for and saved it to a variable and then return that element at the end.
    def precious_element(self):

        ask_user_elmt = input("What number you want me to look for: ")

        precious_int_elmt = int(ask_user_elmt)

        return precious_int_elmt


# #test the precious_element() method
# print(BinarySearchAlgo().precious_element())