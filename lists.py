

# lists are very useful, this only covers basics. research futher.
# all of these are lists
# lotto_numbers+[17, 43, 29, 5, 36]
# rbrm = ["ronnie", "bobby", "ricky", "mike",]
# sequence, similar to string.
# surrounded by brackets " [   ]"
# can be indexed
# # can get length
my_bag = ['katana','nunchucks','sandwhich']
# #  my_bag.append('club') <adds into list
#  my_bag.remove('club') < removes what you want
# print(my_bag[2])

index = 0
while index < len(my_bag):
    
    # adds each one to index after each loop.  
    print(my_bag[index])
    index = index+1

    if 'staff' in my_bag:
        print("in the list")

    else:
        print("not in list")
