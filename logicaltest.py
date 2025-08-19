# string1="hello world this is js"
# print(string1.replace(" ","-"))


i=1
while(i<=5):
    j=1
    while(j<=5/2):
        if(j==i or j==i+4):
            print("*\t")
            j+=1
        else:
            print("\t")
            j+=1
    print("\n")
    i+=1

    