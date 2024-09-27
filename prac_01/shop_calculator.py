number_of_items = int(input("Number of items: "))
total_price = 0
while number_of_items <= 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

for count in range(number_of_items):
    price = float(input("Price of item:  "))
    total_price += price
if total_price > 100:
    discount = total_price * 0.1
    total_price -= discount
print(f"Total price for {number_of_items} items is ${total_price:.2f}.")
