recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}

class SandwichMachine:

    def init(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        out_of_stock = ""
        for ingredient, amount in ingredients.items():
            if self.machine_resources.get(ingredient, 0) < amount:
                out_of_stock += ingredient.capitalize() + ', '
        return out_of_stock[0:-2] if out_of_stock else False

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print('Please insert coins.')
        dollars = int(input('How many dollars?: '))
        half_dollars = int(input('How many half dollars?: '))
        quarters = int(input('How many quarters?: '))
        nickels = int(input('How many nickels?: '))
        return dollars + half_dollars * 0.5 + quarters * 0.25 + nickels * 0.05

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        return coins >= cost

    def make_sandwich(self, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for ingredient, amount in order_ingredients.items():
            self.machine_resources[ingredient] -= amount
           
machine = SandwichMachine()
machine.init(resources)           
           
def main():
    print('What would you like? (small/ medium/ large/ off/ report)')
    input_size = input()
    if input_size.strip() not in ['small', 'medium', 'large', 'off', 'report']:
        print('Invalid option, please try again.')
        main()
    elif input_size == 'off':
        print('Shutting down...')
        exit()
    elif input_size == 'report':
        print(f'Bread: {machine.machine_resources["bread"]} slices \nHam: {machine.machine_resources["ham"]} slices \nCheese: {machine.machine_resources["cheese"]} ounces')
        main()
    recipe = recipes.get(input_size, None)
    if not recipe:
        print('Invalid option, please try again.')
        main()
    if machine.check_resources(recipe['ingredients']):
        print(f'Sorry, there is not enough {machine.check_resources(recipe['ingredients'])}. Please try again later.')
        main()
    coins = machine.process_coins()
    if not machine.transaction_result(coins, recipe['cost']):
        print('Sorry, that is not enough money. Money refunded.')
        main()
    if coins > recipe['cost']:
        print(f'Here is your change: ${coins - recipe["cost"]:.2f}')
    machine.make_sandwich(recipe['ingredients'])
    print(f'Here is your {input_size.strip()} sandwich. Bon appetit!')
    main()
    
main()