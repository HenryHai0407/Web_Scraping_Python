par = input("Enter the paragraph: ")
taboo_list =["hate","damn"]
par1 = par.split()
for word in par1:
    if word in taboo_list:
        par2 = par.replace(word,"****")
print(par2)