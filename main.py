# def countWords(fileName):
#   file = open(fileName,"r")
#   words = file.readlines()
#   words = str(words)
#   strList = words.split()
#   return len(strList)
# fileName = input("Enter a filename: ")
# print("The Number of words in the file is:", countWords(fileName))

def swappingFiles(file1, file2):
  f1 = open(file1, "r")
  f2 = open(file2, "r")
  f1Content = f1.readlines()
  f2Content = f2.readlines()
  w1 = open(file1, "w")
  w2 = open(file2, "w")
  w1.writelines(f2Content)
  w2.writelines(f1Content)
swappingFiles("sample1.txt", "sample2.txt")