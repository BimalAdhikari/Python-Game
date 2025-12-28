define config.name = "Haunted Asylum"
define gui.show_name = True
define config.version = "1.0"
define config.has_sound = True
define config.has_music = True
define config.has_voice = False

#backgrounds
image bg hospital_exterior = "hospital_exterior.jpg"
image bg reception = "reception.jpg"
image bg hallway = "hallway.jpg"
image bg patient_room = "patient_room.jpg"
image bg office = "office.jpg"
image bg basement = "basement.jpg"
image bg operating = "operating.jpg"
image bg window = "window.jpg"

#transformers 
transform slightLeft:
    xalign 0.25
    yalign 1.0

transform slightRight:
    xalign 0.75
    yalign 1.0

transform center:
    xalign 0.5
    yalign 1.0

#music and sounds 
define audio.ambient = "audio/ambient.mp3"
define audio.tense = "audio/tense.mp3"
define audio.horror = "audio/horror.mp3"
define audio.soft = "audio/soft.mp3"
define audio.heartbeat = "audio/heartbeat.mp3"
define audio.door_creak = "audio/door_creak.mp3"
define audio.footsteps = "audio/footsteps.mp3"
define audio.whisper = "audio/whisper.mp3"
define audio.scratch = "audio/scratch.mp3"

#Start of the game
label start:
    play music ambient loop
    with fade

    "My head is pounding and I don't remember how I got here."
    "Where am I?"
    "The last thing I remember is..... the car accident..."

scene bg patient_room
with dissolve


