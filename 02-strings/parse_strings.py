my_name = "vicky"
name_list = []
for letter in my_name:
	name_list.append(letter)
print name_list

str = "1,2,3,4,5"
print str.split(",")

string = "One fish two fish red fish blue fish"
print string.split(" ")

items = ["item:apples,quantity:4,price:1.50\n", "item:pears,quantity:5,price:2.00\n", "item:cereal,quantity:1,price:4.49\n"]
sum = 0
for thing in items:
	split_str = thing.split(",")
	quantity = float(split_str[1].split(":")[1])
	price = float(split_str[2].split(":")[1])
	sum += price * quantity
print sum
