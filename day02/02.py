import re

# TODO Check why simply using open('input.txt') didn't work
with open('C:\\#git\\adventofcode2020\\day02\\input.txt') as input_file:
    # Read file putting each line as an item on a list
    input_list = input_file.readlines()

    valid_p1 = 0
    valid_p2 = 0

    for line in input_list:
        try:
            low, high, letter, password, linebreak = re.split('\W+',line)
        except ValueError:
            # Cover for the last line exception
            low, high, letter, password = re.split('\W+',line)

        low = int(low)
        high = int(high)
        password_as_list = list(password)
        ocurrences = password_as_list.count(letter) 

        if (ocurrences >= low) and (ocurrences <= high):  
            valid_p1 = valid_p1 + 1
            # Print just for the sake of testing
            # print("Low: {0}; High: {1}; Letter: {2}; Password: {3}".format(low, high, letter, password))

        # To account for index 0
        p2_low = low - 1
        p2_high = high - 1
        # TODO Keeping it simple but there's probably a better way to do this
        if password_as_list[p2_low] == letter and password_as_list[p2_high] != letter:
            valid_p2 = valid_p2 + 1
        elif password_as_list[p2_high] == letter and password_as_list[p2_low] != letter:
            valid_p2 = valid_p2 + 1

    print("Part One - Valid passwords: ",valid_p1)
    print("Part Two - Valid passwords: ",valid_p2)