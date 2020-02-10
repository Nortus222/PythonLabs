import Lab6_module as mod
import random


class Cafe:
    def __init__(self, exs_regular_customer=False):
        self.regular_customer = exs_regular_customer
        self.day = random.choice(list(mod.discounts.keys()))

    def receipt(self, num_meals):
        meals = random.sample(list(mod.menu.keys()), num_meals)
        price_raw = 0

        for i in meals:
            price_raw += mod.menu[i]
        if self.regular_customer:
            discount = mod.discounts[self.day] + mod.discounts_regular_customers
        else:
            discount = mod.discounts[self.day]
        price = price_raw - ((price_raw * discount) / 100)

        print("\nThe receipt:\n\nMeals ordered:")
        for i in meals:
            print("{0:30} - {1:3}$".format(i, mod.menu[i]))
        print("\nToday is {1}\n{2:25} - {0:2}%".format(mod.discounts[self.day], self.day, "Day of the week discount"))
        if self.regular_customer:
            print("{1:25} - {0:2}%".format(mod.discounts_regular_customers, "Regular customer discount"))
            print("{1:25} - {0}%\n".format(mod.discounts[self.day] + mod.discounts_regular_customers,"Overall discount"))
        else:
            print("Overall discount - {:2}%".format(mod.discounts[self.day]))
        print("{2:23} - {0}$\n{3:23} - {1}$".format(price_raw, price, "Price without discount", "Price with discount"))


print("This program creates a receipt in a cafe")
a = bool(input("Enter 1 or 0 if customer is regular attendant:\n"))
customer = Cafe(a)

b = int(input("Enter number of meals ordered:\n"))
customer.receipt(b)



