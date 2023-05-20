# Task 1 Positional, Keyword and Default arguments

tables = {
  1: ['Jiho', False],
  2: [],
  3: [],
  4: [],
  5: [],
  6: [],
  7: [],
}
print(tables)

def assign_table(table_number, name, vip_status = False):
  tables.update({table_number:[name, vip_status]})


assign_table(6, "Yoni", False)
assign_table(table_number = 3, name = "Martha", vip_status = True)
assign_table(4, "Karla")
print(tables)


# Task 2 *args (name of the parameter after * sign allows to pass any number of parameters)

def print_order(*order_items):
  print(order_items)

print_order('Orange Juice', 'Apple Juice', 'Scrambled Eggs', 'Pancakes')



