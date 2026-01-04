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

    $ saw_basement = False
    $ talked_to_nurse = False
    $ found_key = False
    $ trust_doctor = 0
    $ sanity = 100

"welcome to Haunted Asylum visual novel."

play music ambient loop
scene black
with fade

"My head is pounding and I don't remember how I got here."
"Where am I?"
"The last thing I remember is..... the car accident..."

scene bg patient_room
with dissolve

show mikey shocked at slightLeft
with dissolve

mikey "Ugh.... what happened to me?"
"i am in a hospital room. The room is dimly lit, only some light coming through the window."
"something feels off... about this place."

play sound door_creak

"the door creaks open slowly."

show dr yeager normal at slightRight
with moveinright

"Ah you're finally awake. Good."
"I am Dr. Yeager. You've have been in an accident."

mikey "What... what kind of accident?"

doctor "A severe car accident. You have been unconscious for couple of days now."

show mikey normal at slightLeft

mikey "Three days? My family ... do they know I'm here?"

doctor "Yes they do and they are very worried about you."
"But right now, you need to focus on getting some rest."

menu:
    "Ask about leaving the hospital":
        mikey "when can I leave this place?"
        doctor "Well, hopefully soon once there are no complications."
        $ trust_doctor -= 5
        show dr yeager smile at slightRight
        doctor "But for now. Try to get some sleep."

    "Ask about injuries":
        mikey "What are my injuries?"
        doctor "You have a minor concussion, some bruises you were lucky."
        mikey "It doesn't feel like a minor concussion..."
        doctor "That's normal. The mind plays tricks on you sometimes during recovery."
        $ trust_doctor += 5

hide dr yeager
with moveoutright

"Doctor Yeager leaves the room closing the doors behind him."
"Something feels off about him..."

play sound whisper
voice "Get out."

show mikey scared at center
with dissolve

mikey "who's there?"
"who said that?"
"The voice seems to come from inside my head."

scene bg hallway
with fade

"I decide to get up and explore. The hallway is dimly lit and eerily quiet."
"Clock ticks loudly somewhere in the distance. It's shows 2:00 AM."
"No nurses at the station. No sounds expect..."

play sound footsteps

"Footsteps echoing from the end of the hall."
"someone is coming."

menu:
    "Hide in the nearby room":
        jump hide_in_room
        
    "Continue down the hall":
        jump continue_hall

    "Return to your room":
        jump return_room

label hide_in_room:
    scene bg office
    with fade

    play sound door_creak

    "I slip into the nearby doctor's office and close the doors behind me."
    "Paperwork scattered everywhere. Medical journals, patient files and prescriptions."

    show mikey normal at slightLeft
    with dissolve

    mikey "What's this?"
    "A file with my name on it. It's bigger than it should be."
    "Dates going back several months before the accident. Test results, Observations..."
    "How is this possible?"

    play sound scratch

    voice "They are watching you."

    mikey "This doesn't make any sense..."
    "I just got here a few days ago..."

    "A key falls out of the file."
    $ found_key = True

    "I take the key and quietly leave the office."

    jump nurse_encounter

label continue_hall:
    scene bg hallway
    with dissolve

    show mikey scared at center

    mikey "Is someone there?"

    show nurse lily normal at slightRight
    with dissolve

    nurse "You shouldn't be out of your room this time of night."

    mikey "I... I couldn't get some sleep."

    nurse "I am nurse Lily. Let me help you get back to your room."

menu:
    "Go with Nurse Lily":
        mikey "You're right. I think i really should get some rest."
        nurse "That's a good idea. The nights can be quite unsettling here."
        $ talked_to_nurse = True
        jump return_room

    "Ask about the hospital":
        mikey "This place feels strange and where is everyone?"
        nurse "This hospital is a private facility. Not many patients stay here overnight."
        mikey "Why is that?"
        nurse "Please don't worry about it. Just come with me."
        $ sanity -= 10
        jump nurse_encounter






