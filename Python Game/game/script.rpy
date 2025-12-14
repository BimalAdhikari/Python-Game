# The script of the game goes in this file.


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_school

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Oreki casual at left with dissolve

    # These display lines of dialogue.

    Oreki "Hi my name is Oreki welcome to our school!"

    show Eileen casual at right with moveinright

    Eileen "You've created a new Ren'Py game."

    Eileen  "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
