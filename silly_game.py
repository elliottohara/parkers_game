from map import rooms, monsters

command = None
exit_command = 'end'
command_prompt = 'What do you want to do?\n'
goodbye_message = 'Game over!'

if __name__ == '__main__':
    current_room = rooms.get(1)

    while command != exit_command and current_room is not None:
        print(current_room['Description'])
        monster = current_room.get('Monster')
        if monster is not None:
            m = monsters.get(monster)
            print('Monster Alert: ' + m.get('Name'))
            print(m.get('Description'))

        if current_room.get('End'):
            break
        command = input(command_prompt)

        new_room = rooms.get(current_room[command], None)
        current_room = new_room

    print(goodbye_message)
