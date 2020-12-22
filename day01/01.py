with open('C:\\#git\\adventofcode2020\\day01\\input.txt') as input_file:
    # Read file putting each line as an item on a list
    input_lines = input_file.readlines()

    # Use list comprehension to convert all  values to int
    input_lines = [int(z) for z in input_lines]

    # Use enumerate so we have the index
    for i, num1 in enumerate(input_lines):
        # Skip numbers above 2020, as we don't have negative numbers that could be sum'd
        if num1 < 2020:
            # Add + 1 to the index so we can be faster when the if is looking at the list
            # and avoid checking the number against itself, since we need two different numbers
            new_i = i + 1
            # How much we need for this number to get to 2020
            num2 = 2020 - num1

            # Is the one we need on the list?
            if num2 in input_lines[new_i:]:
                print("Part 1")
                print("Our numbers are: ",num1)
                print("Our numbers are: ",num2)
                print("Their product is: ",num1 * num2)

            # TODO Fix part 2 printing twice.
            for nb in input_lines[new_i:]:
                if nb < num2:
                    num3 = num2 - nb

                    if num3 in input_lines[new_i:]:
                        print("Part 2")
                        print("Our numbers are: ",num1)
                        print("Our numbers are: ",nb)
                        print("Our numbers are: ",num3)
                        print("Their product is: ",num1 * nb * num3)