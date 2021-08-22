with open("./items_of_interest.txt", "w") as f:
    while True:
        item = input("Enter the official name of the item of interest: ")
        item = item.split(' ')
        result = "_".join(item)
        f.write(result)
        f.write('')
        print("\n" + result + " has been added to the tracking list!\n")