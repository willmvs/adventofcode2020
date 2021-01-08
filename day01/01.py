# TODO Check why simply using open('input.txt') didn't work
with open('C:\\#git\\adventofcode2020\\day01\\input.txt') as input_file:
    # Read file putting each line as an item on a list
    input_list = input_file.readlines()

    # Use list comprehension to convert all  values to int
    input_list = [int(z) for z in input_list]

    part2_found = False
    # Use enumerate so we have the index
    for i, num1 in enumerate(input_list):
        # Skip numbers above 2020, as we don't have negative numbers that could be sum'd
        if num1 < 2020:
            # Add + 1 to the index so we can be faster when the if is looking at the list
            # and avoid checking the number against itself, since we need two different numbers
            new_i = i + 1
            # How much we need for this number to get to 2020
            num2 = 2020 - num1

            # Is the one we need on the list?
            if num2 in input_list[new_i:]:
                # TODO Fix this lazy print job
                print("Part 1")
                print("Our numbers are: ",num1)
                print("Our numbers are: ",num2)
                print("Their product is: ",num1 * num2)

            # To avoid entering this second loop after part2 is found
            if not part2_found:
                # For each number in the sliced list smaller than num2
                # I can find a third number and see if it exists on the list
                for nb in input_list[new_i:]:
                    if nb < num2:
                        num3 = num2 - nb

                        if num3 in input_list[new_i:]:
                            print("Part 2")
                            print("Our numbers are: ",num1)
                            print("Our numbers are: ",nb)
                            print("Our numbers are: ",num3)
                            print("Their product is: ",num1 * nb * num3)
                            part2_found = True
                            break