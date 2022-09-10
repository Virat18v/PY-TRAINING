# A program to print 3rd,5th,7th elementfrom a list
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for index, item in enumerate(l):
    if index==2 or index== 4 or index==6:
        # print(index, item)
        print(f"The {index + 1}th element is {item}")