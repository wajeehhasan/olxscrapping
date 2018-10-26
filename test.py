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
title=[]
price=[]
for itm in lit2:
	if "Rs" in itm:
		price.append(itm)
	else:
		title.append(itm)

print(title)
print(price)
with open("final_olx_data.txt","w") as file:
	for count in range(21):
		file.write("========================================\n")
		file.write("Mobile: ")
		file.write(title[count])
		file.write("\n")
		file.write("price: ")
		file.write(price[count])
		file.write("\n")
		file.write("=========================================\n")