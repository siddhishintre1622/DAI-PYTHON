def indices(list,indlist):
    for i in indlist:
        n = int(i)
        print(list[int(i)])


if __name__ == "__main__":
    l = input("Enter : ")
    l1 = l.split(" ")

    i = input("Enter list : ")
    i1 = i.split(" ")

    indices(l1,i1)


