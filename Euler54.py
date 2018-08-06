with open("pyFiles/poker.txt", "r") as open:
    list1 = open.readline()
    list1 = list1.rstrip("\n")
    list1 = list1.split(" ")
    print list1

