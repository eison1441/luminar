path="C:\\Users\\ASUS\\Desktop\\pythonworks\\datasets\\homework\\eison.txt"
f=open(path,"r")
lst=[]
for line in f:
    line=line.rstrip("\n")
    line=line.split(" ")
    lst.extend(line)
long_word=max(lst,key=lambda l:len(l))
print(long_word)
f.close()
    
    
# path = "C:\\Users\\ASUS\\Desktop\\pythonworks\\datasets\\homework\\eison.txt"

# try:
#     with open(path, "r") as f:
#         lst = []
#         for line in f:
#             line = line.rstrip("\n")
#             line = line.split()  # splits on any whitespace
#             lst.extend(line)

#     long_word = max(lst, key=len)
#     print(long_word)

# except FileNotFoundError:
#     print(f"Error: The file at {path} was not found.")
# except Exception as e:
#     print(f"An error occurred: {e}")
