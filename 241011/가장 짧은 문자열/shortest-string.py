str1 = input()
str2 = input()
str3 = input()

strl1=len(str1)
strl2=len(str2)
strl3=len(str3)

print(max(strl1, strl2, strl3) - min(strl1,strl2,strl3))