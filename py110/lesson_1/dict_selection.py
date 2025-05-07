def select_fruit(my_dictionary):
    transformed_dictionary = {}
    for key, value in my_dictionary.items():
        if value == 'Fruit':
            transformed_dictionary[key] = value

    return transformed_dictionary

produce = {
    'apple': 'Fruit',
    'carrot': 'Vegetable',
    'pear': 'Fruit',
    'broccoli': 'Vegetable',
}

print(select_fruit(produce) == {'apple': 'Fruit', 'pear': 'Fruit'})