# Print the main menu and instructions
def show_instructions():
    print("Defeating Dracula Text Adventure Game")
    print("Collect 6 items to win the game, or be turned into a vampire minion.")
    print("Move commands: go South, go North, go East, go West, or exit to exit the game.")
    print("Add to Inventory: get 'item name'")


# Define an inventory
# A dictionary linking the rooms
def main():
    rooms = {
        'Foyer': {'South': 'Study', 'North': 'Dining Room', 'East': 'Torture Chamber', 'West': 'Utility Room'},
        'Study': {'North': 'Foyer', 'East': 'Library', 'item': 'Holy Water Canteen'},
        'Library': {'West': 'Study', 'item': 'Bible'},
        'Utility Room': {'East': 'Foyer', 'item': 'UV Flashlight'},
        'Dining Room': {'South': 'Foyer', 'East': 'Kitchen', 'item': 'Cross'},
        'Kitchen': {'West': 'Dining Room', 'item': 'Garlic Necklace'},
        'Torture Chamber': {'West': 'Foyer', 'North': 'Tower', 'item': 'Wooden Stake'},
        'Tower': {'South': 'Torture Chamber', 'Villain': 'Dracula!'}
    }

    # Start the player in the Foyer
    location = 'Foyer'

    # List of the inventory items as they are picked up in each room
    inventory_items = []

    # Game Loop
    while True:
        print(f"You are in the {location}\nInventory: {inventory_items}\n{'-' * 20}")
        if 'item' in rooms[location].keys():
            item = rooms[location]['item']
            if item not in inventory_items:
                print(f'You see a {item}')
        if 'Villain' in rooms[location].keys():
            if len(inventory_items) < 6:
                print('You are now a vampire minion.\nYou lose!')
                quit()
            else:
                print('You have saved humanity.\nYOU WIN!')
                break
        player_move = input('Enter your move:')

        next_move = player_move.split()

        action = next_move[0].title()

        if len(next_move) > 1:
            item = next_move[1:]
            direction = next_move[1].title()

            item = ' '.join(item).title()

        # Moving between the rooms
        if action == 'Go':
            try:
                location = rooms[location][direction]
            except:
                print(f'You cant go that way\nTry again')
        elif action == 'Get':
            try:
                if item == rooms[location]['item']:
                    if item not in inventory_items:
                        inventory_items.append(rooms[location]['item'])
                        print(f'{item} retrieved')
                    else:
                        print(f'You already have {item}')
            except:
                print('Cant find {item}')
        elif action == 'Exit':
            print('Thank you for playing.\n Goodbye')
            break
        else:
            print('Invalid command')


show_instructions()
main()
