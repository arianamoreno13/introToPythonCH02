#!/usr/bin/env python3

"""Importing hw_05_module"""
import hw_05_module

# print food menu
print(hw_05_module.show_food_menu())
# save costumers food menu choice
food_choice = hw_05_module.get_user_choice()
# print drink menu
print(hw_05_module.show_drink_menu())
# save costumers drink menu choice
drink_choice = hw_05_module.get_user_choice()
# print dessert menu
print(hw_05_module.show_dessert_menu())
# save costumers dessert menu choice
dessert_choice = hw_05_module.get_user_choice()
# calculate total price
total_price = hw_05_module.get_total_price(food_choice, drink_choice, dessert_choice)
print(total_price)
# print total price
print(hw_05_module.print_total_price(total_price))
