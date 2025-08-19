# file=open("sample2.txt","w")
# file.close()

# file=open("sample2.docx","w")
# file.close()

# file=open("D:/SAMPLE.txt","w")
# file.close()

# file=open("sample2.txt","w")
# lines="css"
# file.write(lines)
# file.close()

# file=open("sample2.txt","r")
# content=file.read()
# print(content)
# file.close()


# file=open("sample2.txt","r")
# content=file.readlines()
# print(content)
# file.close()

# file=open("sample2.txt","r")
# content=file.readline()
# print(content)
# file.close()

file=open("sample2.txt","w")
content=["hello\nthis is python handling"]
file.writelines(content)
file.close()

# file=open("sample2.txt","a")
# file.write("\nappended text.\n")
# file.close()

# with open("sample2.txt","r")as file:
#     content=file.read()
#     print(content)

# with open("sample2.txt","r")as file:
#      content=file.read()
#      position=file.tell()
#      print(position)

# file=open("sample2.txt","r")
# file.seek(3)
# print(file.read())

# try:
#     file=open("sample189.txt","r")
#     file.readline()
#     file.close()
# except FileNotFoundError:
#     print("file not found")

# with open("Screenshot (88).png","rb")as file:
#       content=file.read()
#       print(content)













