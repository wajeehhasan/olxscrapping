lit=[]
lit2=[]
sttr=""
with open("olx_scraped.txt","r") as file:
	for line in file:
		lit.append(file.readline())
# print(lit)
for itm in lit:
	sttr=""
	for x in itm:
		if x=="\n" or x=="\t":
			sttr+=""
		else:
			sttr+=x
	lit2.append(sttr)
print(lit2)