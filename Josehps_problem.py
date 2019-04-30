//The Program solves the Josphs Problem

a = input("Enter a Number to solve for the jospehs problem")
s = str (bin(a))
s = s[2:]
final = ""
for i in range(1,len(s)):
    final = final + s[i] 
else :
    final = final + s[0]
print "The number to be safe so you dont get killed",int(final, 2)


