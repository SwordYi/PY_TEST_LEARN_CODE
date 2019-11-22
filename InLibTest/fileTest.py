
file = open("MyTestText.txt", "r")
readAll = file.read()
print(readAll)
file.close()

print("------break line--------")

file = open("MyTestText.txt", "r")
readline = file.readline()
print(readline)
file.close()

print("------break line--------")

file = open("MyTestText.txt", "r")
readlines = file.readlines()
print(readlines) # 读进去后是一个列表list哟
file.close()


file = open("MyTestText.txt", "a+")
file.write("xxxx\n")
file.close()

file = open("MyTestText2.txt", "w+")
file.write("gagegega" + "\n")
file.close()

print("------break line--------")
file = open("MyTestText.txt","r")
print(file.read())
file.close()

print("------break line--------")
file = open("MyTestText2.txt","r")
print(file.read())
file.close()


