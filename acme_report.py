"""
Generate random products and print a summary of them
should have two functions:
generate_products(): generates (default 30) products randomly and returns them
as a list
inventory_report(): takes a list of products and prints a "nice" summary
"""
import random
from acme import Product

adj_list = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
noun_list = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):

    products = []

    for i in range(num_products):
        r_name = (random.choice(adj_list) + ' ' + random.choice(noun_list))
        products.append(Product(r_name))
        products[i].price = random.randint(5, 101)
        products[i].weight = random.randint(5, 101)
        products[i].flammability = random.uniform(0.0, 2.5)
    return products

    # OLD CODE
    # Product.name = (random.choice(adj_list) +
    #                             random.choice(noun_list))
    # Product.price = random.randint(5, 101)
    # Product.weight = random.randint(5, 101)
    # Product.flammability = random.uniform(0.0, 2.5)
    # for i in range(30):
    #     product_list[i].name = (random.choice(adj_list) +
    #                             random.choice(noun_list))
    #     product_list[i].price = random.randint(5, 101)
    #     product_list[i].weight = random.randint(5, 101)
    #     product_list[i].flammability = random.uniform(0.0, 2.5)


def inventory_report(products):
    # Print report including unique product names, average price, average weight
    # and average flammability, to be initialized on run

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    tot_weight = 0
    tot_price = 0
    tot_flam = 0
    tot_unique = 0
    unique = True
    for i in range(len(products)):
        tot_weight += products[i].weight
        tot_price += products[i].price
        tot_flam += products[i].flammability
        for j in range(len(products)):
            if (products[i].name == products[j].name):
                unique = False
        if unique:
            tot_unique += 1
        else:
            unique = True
    print('Unique product names: ', tot_unique)
    print('Average price: ', (tot_price / len(products)))
    print('Average weight: ', (tot_weight / len(products)))
    print('Average flammability: ', (tot_flam / len(products)))


if __name__ == '__main__':
    inventory_report(generate_products())
