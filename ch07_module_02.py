import os

print("현재 운영체제 :", os.name)
print("현재 폴더 :", os.getcwd())
print("현재 폴더의 내부 요소 :", os.listdir())

os.mkdir("test")
os.rmdir("test")

with open("test.txt", "w") as file:
    file.write("test")
os.rename("test.txt", "renamed_test.txt")

os.remove("renamed_test.txt") # os.unlink와 동일

os.system("ls -la")