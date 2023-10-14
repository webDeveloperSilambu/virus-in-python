print("I am Become a Hacker")
for i in range(10000):
    myFile = "{}-silambu-virus.txt"
    myArr = myFile.format(i)
    open(myArr,"a")