import os

path = "./"
directory_list = os.listdir(path)
# print(directory_list)

for filename in directory_list:
    src = filename
    dst = filename.split('-')[0].replace('_','').lower() + ".jpg"
    print(dst)
    
    if(dst[0] == 'e'):
        os.rename(os.path.join(path, src), os.path.join(path, dst))

# print("File renamed!")
# os.system("ls -la")

# d = "E18009"
# os.system("cd ./" + d)
# os.system("ls -la")
# os.system("cd ../")
