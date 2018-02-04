from player import Player
import gamemap

def play():
    print("understand.")
    player = Player()
    while True:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        action_input= get_player_command()
        if action_input in ["n","N","North","north"]:
            player.move_north()
        elif action_input in ["s","S","South","south"]:
            player.move_south()
        elif action_input in ["w","W","West","west"]:
            player.move_west()
        elif action_input in ["e","E","East","east"]:
            player.move_east()
        elif action_input in ['i', 'I', 'inventory']:
            player.print_inventory()
        else:
            print("#h!ST%)A{!Y#! %A&b(*WA&##Y$!r#@ ")

def get_player_command():
    return input('Action: ')


play()
