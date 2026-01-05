init python:
    #Data for endings
    if persistent.endings is None:
        persistent.endings = set()
    

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
image bg operating = "operating_room.jpg"
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

label nurse_encounter:
    scene bg hallway
    with fade

    show nurse lily concerned at slightRight
    show mikey normal at slightLeft
    
    nurse "What are you doing out here alone at this time of night?"

if found_key:
        mikey "I found something strange in the doctor's office. A file about me with old dates and a key."
        nurse "That's not possible. You just arrived here a few days ago. Let me see that."
        "Her hannds tremble as she takes the file from me."
        nurse "This... this can't be... there must be some mistake."
        $ trust_doctor -= 10
else:
        mikey "I heard voices. This place doesn't feel right."
        nurse "You must be imagining things. It must be the medication."


menu:
    "Ask about Dr. Yeager":
        mikey "What can you tell me about Dr. Yeager?"
        nurse "He is the head physician here. He is very dedicated to his work."
        nurse "But sometimes, he is too dedicated. He can be... intense."
        mikey "what do you mean by intense?"
        nurse"Nothing, forget i said anything."
        $ sanity -= 15

    "Ask to call family":
        mikey "Can you help me contact my family?"
        nurse "I am sorry but the phones are down right now due to the storm outside."
        nurse "But don't worry you can try to call them in the morning."
        "Her answer feels rehearsed."

        nurse "Now please, go back to your room for your own good."
        jump basement_choice

label return_room:
    scene bg patient_room
    with fade

    show mikey normal at center

    "back in my room, the feeling of being watched intensifies."
    play sound heartbeat

    "My heart is racing. I need to calm down."
    "The walls seems to be... breathing."

    voice "You can't hide from them. They are coming for you."

menu:
    "look out the window":
        scene bg window
        with dissolve
        "The window looks out into a dark, stormy night."
        "lightning flashes, illuminating the garden below. A figure stands there, motionless."
        "wait is that... me?"
        $ sanity -= 25
        jump nightmare_sequence

    "Check the door":
        "The door is locked from the outside."
        "scratches on the inside of the door"
        "How long have I been in here?"
        $sanity -= 20
        jump basement_choice

label basement_choice:
    scene bg hallway
    with fade

    "the hallway seems longer than before."
    "All signs point towards the basement. At the end of the hall, the basement door looms."

    play sound whisper
    voice "The truth lies below."

menu:
    "Go to the basement" if found_key or sanity < 70:
        jump basement_explore 

    "Return to room":
        jump safe_ending

    "Confront Dr. Yeager":
        jump doctor_confrontation

label basement_explore:
    $ saw_basement = True
    scene bg basement
    with fade

    play music horror loop

    "The basement is cold. The air smells of antiseptic and something else...."
    "Something metallic."

    show mikey shocked at center
    
    mikey "What is this place?"

    "Medical equipment, but old really old and rusty. Like from another era."
    "Files. So many files, all filled with patient photos that look terrified"

    "A journal lies open on the desk:"

    center "Day 127: Subject shows increased resistance. The serum needs some adjustments."
    center "Day 132: Memories are returning. Must increase serum dosage."
    center "Day 146: He asked about his family today. Had to adminster a shock treatment."

    mikey "No.... this can't be..."

    show dr yeager angry at slightLeft
    with moveinright

    play sound door_creak

    doctor "I'm disappointed, Mikey. You were not supposed to see all of this."

    mikey "what have you done to me?"

    doctor "We are helping you. Your mind was fractured in the car accident."
    doctor "We are putting you back together. Better. Stronger."

    menu:   
        "Try to escape":
            jump escape_attempt
        "Ask why":
            jump ask_why
        "Attack the doctor":
            jump violent_ending

label nightmare_sequence:
    scene black
    with dissolve

    play music tense

    "Everything goes dark."
    "Voices overlap, screaming, pleading..."

    voice "Don't trust them"
    voice "You've been here before!"
    voice "Wake up! WAKE UP!."

    scene bg operating
    with fade

    "A bright light. Surgical toolse."
    "Strapped to a table. Dr. yeager leaning over me."

    doctor "The procedure is almost complete. Just a bit longer..."

    menu:
        "Screm for help":
            voice "NO ONE CAN HEAR YOU"
            jump bad_ending

        "Foucus on a memory":
            "My daughter's laugh. Her birthday party. The cake..."
            "REAL. That memory is REAL."
            $ sanity += 30
        
label doctor_confrontation:
    scene bg office
    with fade

    show dr yeager normal at slightRight
    show mikey normal at slightLeft

    mikey "I want answers, Doctor. NOW!!."

    doctor "What would you like to know?"


    menu:
        "Why can't I remember the accident?":
            mikey "Why don't I remember the accident?"
            doctor "Traumatic amnesia. Common in these cases."
            mikey "But I remember other things. Things that shouldn't be possible here."
            $ trust_doctor -= 15

        "Where are the other patients?":
            mikey "This place is empty. Where are the other patients?"
            doctor "Transferred. We're closing this wing."
            "His eye twitches when he says this."
            $ sanity -= 10

    if trust_doctor < -10:
        jump basement_explore
    else:
        doctor "You need to trust me, Mikey. I'm trying to help you."
        jump safe_ending

label awakening:
    scene bg patient_room
    with flash

    show mikey shocked at center

    mikey "It was a dream... but it felt so real."
    
    "Or was it a memory?"

    play sound scratch

    "Scratching from the walls. The same pattern every night."

    voice "Seven scratches... count them..."

    mikey "Seven months. I have been here for seven months now!!"

    jump true_awakening

label true_awakening:
    scene bg operating
    with fade

    "The truth hits me like a physical blow."
    "I am not a patient. I am just a another test subject."
    "An experiment"

    show dr yeager smile at slightRight
    with dissolve

    doctor "Ah, you finally understand. Excellent."
    doctor "The breakthrough always comes when they realize."

    mikey "What are you doing to me?"

    doctor "Exploring the limits of human consciousness. The resilience of memory."
    doctor "you're special, Mikey. You can rebuild yourself from fragments."

    menu:
        "Beg for release":
            mikey "Please, I have a family..."
            doctor "Had. You had a family. The accident was... unfortunate."
            doctor "But your loss is science's gain."

        "Play along":
            mikey "If I am so special, Let me help you."
            doctor "Interesting. Most would beg for mercy."
            jump manipulation_ending

        "Remember your stength":
            mikey "The memories aren't just pain. There is anger too. Power."
            voice "FIGHT BACK!!!"
            jump escape_attempt
    
label escape_attempt:
    scene bg basement
    with hpunch

    play music horror

    "I shove Dr. Yeager, knocking down equipment over."

    show mikey scared at slightLeft
    show dr_yeager_angry at slightRight

    doctor "Security! He's getting away"

    "Footsteps from above. More than one person."

    menu:
        "Hide":
            "I duck behind a old filing cabinet as the guards run past me."
            "Nurse Lily is with them. She looks... different. Angry."
        
            if talked_to_nurse:
                nurse "Find him! The subject can't leave!"
            jump hidden_escape

        "Run upstairs":
            "I sprint up the stairs, taking them two at a time."
            "The door at the top is locked!"
        
            if found_key:
                "The key! It fits!"
                jump freedom_ending
            else:
                "Trapped! The guards catch up..."
                jump captured_ending

label hidden_escape:
    scene bg hallway
    with fade

    "The hallway is clear. For now."
    "Emergency exit sign glows red at the far end."

    play sound footsteps

    "More footsteps. Coming from both directions."

    show nurse lily concerned at slightRight
    with dissolve

    nurse "Mikey! This way, quickly!"

    menu:
        "Trust her":
            mikey "Why should I trust you?"
            nurse "I also want to get out of here. I never agreed to any of this."
            nurse "There is a service elevator. Follow me."
            $ trust_doctor -= 30
            jump ally_escape

        "Run the other way":
            mikey "Stay away from me!!"
            "I run torwards the exit sign."
            jump solo_escape 

#endings
label safe_ending:
    scene bg patient_room
    with fade  

    play music soft loop

    "I decide to trust Dr. Yeager. Maybe he is really trying to help."
    "The treatment continues. The memories fade."
    "Sometimes I wake up screaming, but I can't remember why."
    "Dr. Yeager says that's progress."

    scene black
    with dissolve

    centered "ENDING: COMPLIANT PATIENT"
    centered "you chose to trust the system."
    centered "The nightmares continue, but at least they are familiar."

    $ persistent.endings.add("safe") 
    jump endings_screen

label tragic_ending:
    scene bg operating
    with fade

    play music horror loop

    "Dr. yeager increases the dosage. The world goes soft at the edges."
    "My family's faces they fade away. Their voices fade away."
    "The last thing I hear before complete darkness:"

    doctor "Facinating. Complete memory wipe in 3 seconds."

    scene black 
    with dissolve

    centered "ENDING: BlANK SLATE"
    centered "Your past is erased."
    centered "You future belongs to the doctor now"

    $persistent.endings.add("tragic")
    jump endings_screen

label freedom_ending:
    scene bg hospital_exterior
    with fade 

    play music soft loop

    "The key turns. The door opens to a cool night air"
    "I run through the woods, branches tearing my clothes apart."
    "Behind me, the hospital grows smaller"
    "Ahead of me, lights. A small town."
    "I don't know what's real anymore, but I'm finally free."

    scene black
    with dissolve

    $ persistent.endings.add("freedom")
    jump endings_screen

label captured_ending:
    scene bg basement
    with fade

    "Strong hands grab me. Needles pierce my skin."
    doctor "sigh. We will have to start over."
    "The world dissolves into chemicals and pain."

    scene black 
    with dissolve

    centered "ENDING: RECAPTURED"
    centered "The experiment continues."
    centered "There are no more escape attempts."

    $ persistent.endings.add("captured")
    jump endings_screen

label ally_endings:
    scene bg hospital_exterior
    with fade 

    "Nurse Lily leads me through the hidden passages."
    "She has a car waiting. We drive in silence."
    nurse "I'm sorry for everything."
    "The sun is rising. For the first time in months. I feel hope."

    scene black
    with dissolve

    centered "ENDING: UNLIKELY ALLY"
    centered "You trusted when you should't have."
    centered "Sometime, it pays off."

    $ persistent.endings.add("ally")
    jump endings_screen

label violent_ending:
    scene bg basement
    with hpunch

    play sound horror

    "Rage takes over. I grab the surgical instrument."
    "Dr. yeager does't scream. He just looks... dissapointed."
    "The security arrives too late."
    "But now there's blood on your hands. So much blood!!"

    scene black
    with dissolve

    centered "ENDING: BECOMING THE MONSTER"
    centered "You fought fire with fire."
    centered "Now you burn with them."

    $ persistent.endings.add("violent")
    jump endings_screen

label manipulation_ending:
    scene bg office
    with fade 

    "I become Dr. yeager's assistant."
    "At first, I pretend. Then I start to understand."
    "The beauty of breaking minds to rebuild them."
    "New patients arrive. I help them with their... treatment."

    scene black 
    with dissolve

    centered "ENDING: THE APPRENTICE"
    centered "If you can't them..."
    centered "Join them. Then surpass them."

    $ persistent.endings.add("manipulation")
    jump endings_screen

label bad_ending:
    scene bg operating
    with fade

    play sound horror

    "My screams echo in the empty room."
    "No one comes. No one ever comes."
    "Dr. yeager smiles as he adjusts the dials."

    doctor "The screaming phase. It means we are close to a breakthrough."
    doctor "Don't worry. Soon you won't remember how to scream at all."

    "The world fades to white. Then to nothing."
    "The last thing I feel is cold metal against my skin."
    
    scene black
    with dissolve

    centered "ENDING: LOST VOICE"
    centered "You screamed into the void."
    centered "The void didn't answer."

    $ persistent.endings.add("bad")
    jump endings_screen


label endings_screen:
    scene black
    with dissolve

    "You have unlocked one ending. There are a total of 9 endings."

    menu:
        "Play again to discover more endings":
            jump start
        "Quit game":
            return

#THE END





  

            







