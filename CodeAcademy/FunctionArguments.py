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

# Task 3 working with *args

tables = {
  1: {
    'name': 'Jiho',
    'vip_status': False,
    'order': 'Orange Juice, Apple Juice'
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}
print(tables)

def assign_table(table_number, name, vip_status=False):
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = ''

def assign_and_print_order(table_number, *order_items):
  tables[table_number]['order'] = order_items
  for item in order_items:
    return(item)


assign_table(2, "Arwa", True)
assign_and_print_order(2, 'Steak', 'Seabass', 'Wine Bottle')

print(tables)


