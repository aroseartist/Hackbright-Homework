"""
Assess the customer list

Return any over/under payments
"""

customer_list = open("customer-orders.txt") #access the accounting orders text file

for line in customer_list: #per line within the retrieved file:
    line = line.split('|') #split on the |

    customer_name = line[1] 
    customer_name = customer_name.split(" ")[0] #indicie 0 is the customer name
    melon_nums = float(line[2]) #indicie 2 is presented as a float and defined
    paid_amount = float(line[3]) #indicie 3 is presented as a float and defined

    melon_cost = 1.00

    customer_expected = melon_nums * melon_cost #establishes the amount owed

    if customer_expected < paid_amount: #if they paid too much, tell me
        print "{} is owed a refund. They paid ${:.2f} but only owed ${:.2f}". \
            format(customer_name, paid_amount, customer_expected)

    elif customer_expected > paid_amount: #if they didn't pay enough, tell me
        print "{} owes Ubermelon funds. They paid ${:.2f} but owed ${:.2f}". \
            format(customer_name, paid_amount, customer_expected)

customer_list.close() #no longer in need of accessed file



'''
melon_cost = 1.00

customer1_name = "Joe"
customer1_melons = 5
customer1_paid = 5.00

customer2_name = "Frank"
customer2_melons = 6
customer2_paid = 6.00

customer3_name = "Sally"
customer3_melons = 3
customer3_paid = 3.00

customer4_name = "Sean"
customer4_melons = 9
customer4_paid = 9.50

customer5_name = "David"
customer5_melons = 4
customer5_paid = 4.00

customer6_name = "Ashley"
customer6_melons = 3
customer6_paid = 2.00

customer1_expected = customer1_melons * melon_cost
if customer1_expected != customer1_paid:
    print customer1_name, "paid {:.2f}, expected {:.2f}".format(
        customer1_paid, customer1_expected)

customer2_expected = customer2_melons * melon_cost
if customer2_expected != customer2_paid:
    print customer2_name, "paid {:.2f}, expected {:.2f}".format(
        customer2_paid, customer2_expected)

customer3_expected = customer3_melons * melon_cost
if customer3_expected != customer3_paid:
    print customer3_name, "paid {:.2f}, expected {:.2f}".format(
        customer3_paid, customer3_expected)

customer4_expected = customer4_melons * melon_cost
if customer4_expected != customer4_paid:
    print customer4_name, "paid {:.2f}, expected {:.2f}".format(
        customer4_paid, customer4_expected)

customer5_expected = customer5_melons * melon_cost
if customer5_expected != customer5_paid:
    print customer5_name, "paid {:.2f}, expected {:.2f}".format(
        customer5_paid, customer5_expected)

customer6_expected = customer6_melons * melon_cost
if customer6_expected != customer6_paid:
    print customer6_name, "paid {:.2f}, expected {:.2f}".format(
        customer6_paid, customer6_expected)
'''