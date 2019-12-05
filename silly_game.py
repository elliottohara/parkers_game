command = None
exit_command = 'end'
command_prompt = 'What do you want to do?\n'
goodbye_message = 'Game over!'

rooms = {
    1: dict(Name='Start',
            Description="This is the start. You can go N, S, E or W",
            North=2,
            South=3,
            East=4,
            West=5),
    2: dict(Name='2',
            Description="Ahead of you, you see a hill, to the East a stream.",
            North=6,
            South=1,
            East=7,
            West=5),
    3: dict(Name=3,
            Description="This place is boring",
            North=1,
            South=3,
            East=7,
            West=2),
    4: dict(Name=4,
            Description="This place is awesome.",
            North=1,
            South=4,
            East=4,
            West=1,
            Monster="Dragon"),
    5: dict(Name=5,
            Description="This place is awesome.",
            North=1,
            South=4,
            East=4,
            West=1),
    6: dict(Name=6,
            Description="You're on a hill. How freekin awesome!!! If you go west you die. You'll probably die anyway though",
            North=None,
            South=2,
            East=8,
            West=9,
            ),
    7: dict(Name=6,
            Description="Slash. You drowned. You're dead",
            North=None,
            South=None,
            East=None,
            West=None,
            End=True
            ),
    8: dict(Name=6,
            Description="You fell down the hill and broke your neck. You're not dead, but you're paralized and can't do anything so the game is over",
            North=None,
            South=None,
            East=None,
            West=None,
            End=True
            ),
    9: dict(Name=6,
            Description="Well, that was stupid. Told ya so!",
            North=None,
            South=None,
            East=None,
            West=None,
            End=True
            ),

}

monsters = {
    "Dragon": {
        "Name": "Big Mean Dragon",
        "Description": "A big firebreathing dragon"
    }
}

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
