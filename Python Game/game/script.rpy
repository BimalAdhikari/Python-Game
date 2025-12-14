# The script of the game goes in this file.


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_school

    show Eileen casual at right with moveinright
    Eileen "hi there! what's your name?"
    show Oreki casual at left with moveinleft
    menu:
        "my name is Oreki":
            Eileen"Thats what i thought!"
        "my name is ken":
            Eileen"oh! my bad i thouht you were oreki"

        "say nothing":
            jump say_nothing
    
    Oreki "what's your name?"
    Eileen "my name is Eileen. nice to meet you!"


    # This ends the game.

    return

label say_nothing:
    Eileen "oh... okay then i must be going."
    return