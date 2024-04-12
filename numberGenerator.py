from random import randint

file1 = open("numbers_100k.txt", "w")
with open("numbers_100k.txt", "w") as file1:
    for i in range(0, 100000):
        file1.write(str(randint(1, 100000)))
        file1.write(" ")
file1.close()



file2 = open("numbers_1kk.txt", "w")

with open("numbers_1kk.txt", "w") as file2:
    for i in range(0, 1000000):
        file2.write(str(randint(1, 100000)))
        file2.write(" ")
file2.close()




file3 = open("numbers_10k.txt", "w")

with open("numbers_10k.txt", "w") as file3:
    for i in range(0, 10000):
        file3.write(str(randint(1, 100000)))
        file3.write(" ")
file3.close()


file4 = open("numbers_1k.txt", "w")

with open("numbers_1k.txt", "w") as file4:
    for i in range(0, 1000):
        file4.write(str(randint(1, 100000)))
        file4.write(" ")
file4.close()



file5 = open("numbers_100.txt", "w")

with open("numbers_100.txt", "w") as file5:
    for i in range(0, 100):
        file5.write(str(randint(1, 100000)))
        file5.write(" ")
file5.close()
        