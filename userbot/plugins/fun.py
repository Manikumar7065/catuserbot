"""COMMAND : `.runs` , `.metoo` , `.rape` , `.insult` , `.pro`, `.noob`, `.maaki` , `.gey`, `.chase`, `.hii` `.abuse` , `.abusehin`
Other emoticons commands
`.abusewaving`, `.abusewtf`, `.abuselove`, `.abuseconfused`, `.abusedead`, `.abusesad`, `.abusedog`
`.abuse` <any word>

"""

from telethon import events
import random, re
from uniborg.util import admin_cmd

METOOSTR = [
    "`Me too thanks`",
    "`Haha yes, me too`",
    "`Same lol`",
    "`Me irl`",
    "`Same here`",
    "`Haha yes`",
    "`Same pinch bsdk`",
]
NOOBSTR = [
    "`You Noob don't mess with Me!`",
    "`Noob Boi trying to be Famous Lol`",
    "`Some Nibbas need to open their small minds instead of their Big Mouths`",
    "`Ah! you don't me, stay away Noob`",
    "`I only talk with Pros. You better go away!`",
    "`Itna bada Noobda dekhlia ab to marna hoga`",
    "`You're a Noob and You won't get that !`",
]
RUNSREACTS = [
    "`Runs to Thanos`",
    "`Runs to Modiji For Achey Din`",
    "`Runs far, far away from earth`",
    "`Running faster than usian bolt coz I'mma Bot`",
    "`Runs to Marie`",
    "`This Group is too cancerous to deal with.`",
    "`Cya bois`",
    "`I am a mad person. Plox Ban me.`",
    "`I go away`",
    "`I am just walking off, coz me is too fat.`",
    "`I Fugged off!`",
    "`Will run for chocolate.`",
    "`I run because I really like food.`",
    "`Running...\nbecause dieting is not an option.`",
    "`Wicked fast runnah`",
    "`If you wanna catch me, you got to be fast...\nIf you wanna stay with me, you got to be good...\nBut if you wanna pass me...\nYou've got to be kidding.`",
    "`Anyone can run a hundred meters, it's the next forty-two thousand and two hundred that count.`",
    "`Why are all these people following me?`",
    "`Are the kids still chasing me?`",
    "`Running a marathon...there's an app for that.`",
]
RAPE_STRINGS = [
     "`Rape Done Drink The Cum`",
     "`The user has been successfully raped`",
     "`Dekho Bhaiyya esa hai! Izzat bachailo apni warna Gaand maar lenge tumhari`",
     "`Relax your Rear, ders nothing to fear,The Rape train is finally here`",
     "`Rape coming... Raped! haha 😆`",
     "`Kitni baar Rape krvyega mujhse?`",
     "`Don't rape too much BOSSdk, else problem....`",
     "`Rape krdunga pata bhi nahi chalega`"
     "`Lodu Andha hai kya Yaha tera rape ho raha hai aur tu abhi tak yahi gaand mara raha hai lulz`",
] 
CHASE_STR = [
    "Where do you think you're going?",
    "Huh? what? did they get away?",
    "ZZzzZZzz... Huh? what? oh, just them again, nevermind.",
    "Get back here!",
    "Not so fast...",
    "Look out for the wall!",
    "Don't leave me alone with them!!",
    "You run, you die.",
    "Jokes on you, I'm everywhere",
    "You're gonna regret that...",
    "You could also try /kickme, I hear that's fun.",
    "Go bother someone else, no-one here cares.",
    "You can run, but you can't hide.",
    "Is that all you've got?",
    "I'm behind you...",
    "You've got company!",
    "We can do this the easy way, or the hard way.",
    "You just don't get it, do you?",
    "Yeah, you better run!",
    "Please, remind me how much I care?",
    "I'd run faster if I were you.",
    "That's definitely the droid we're looking for.",
    "May the odds be ever in your favour.",
    "Famous last words.",
    "And they disappeared forever, never to be seen again.",
    "\"Oh, look at me! I'm so cool, I can run from a bot!\" - this person",
    "Yeah yeah, just tap /kickme already.",
    "Here, take this ring and head to Mordor while you're at it.",
    "Legend has it, they're still running...",
    "Unlike Harry Potter, your parents can't protect you from me.",
    "Fear leads to anger. Anger leads to hate. Hate leads to suffering. If you keep running in fear, you might "
    "be the next Vader.",
    "Multiple calculations later, I have decided my interest in your shenanigans is exactly 0.",
    "Legend has it, they're still running.",
    "Keep it up, not sure we want you here anyway.",
    "You're a wiza- Oh. Wait. You're not Harry, keep moving.",
    "NO RUNNING IN THE HALLWAYS!",
    "Hasta la vista, baby.",
    "Who let the dogs out?",
    "It's funny, because no one cares.",
    "Ah, what a waste. I liked that one.",
    "Frankly, my dear, I don't give a damn.",
    "My milkshake brings all the boys to yard... So run faster!",
    "You can't HANDLE the truth!",
    "A long time ago, in a galaxy far far away... Someone would've cared about that. Not anymore though.",
    "Hey, look at them! They're running from the inevitable banhammer... Cute.",
    "Han shot first. So will I.",
    "What are you running after, a white rabbit?",
    "As The Doctor would say... RUN!",
]
HELLOSTR = [
    "Hi !",
    "‘Ello, gov'nor!",
    "What’s crackin’?",
    "‘Sup, homeslice?",
    "Howdy, howdy ,howdy!",
    "Hello, who's there, I'm talking.",
    "You know who this is.",
    "Yo!",
    "Whaddup.",
    "Greetings and salutations!",
    "Hello, sunshine!",
    "Hey, howdy, hi!",
    "What’s kickin’, little chicken?",
    "Peek-a-boo!",
    "Howdy-doody!",
    "Hey there, freshman!",
    "I come in peace!",
    "Ahoy, matey!",
    "Hiya!",
]
ABUSE_STRINGS = [
       "`Madharchod`",
	   "`Gaandu`",
	   "`Chutiya he rah jaye ga`",
	   "`Ja be Gaandu`",
	   "`Ma ka Bhodsa madharchod`",
	   "`mml`",
	   "`You MotherFukcer`",
           "`You Betichod`",
           "`you are lodu no.1`"
	   "`Muh Me Lega Bhosdike ?`"
           "`Taare hai Asmaan me very very bright jaat na jla bskd dekh le apni hight.`",
        "`Zindagi ki na toote lari iski lulli hoti nhi khadi`",
        "`Kbhi kbhi meri dil me khyaal ata hai ayse chutiyo ko kon paida kr jata hai😂.`",
        "`Saawan ka mahina pawan kare shor jake gand mara bskd kahi aur.`", 
        "`Dil ke armaa ansuon me beh jaye tum bskd ke chutiye hi reh gye.`",
        "`Ishq Se Tabiyat Ne Zeest Ka Mazaa aya maine is lodu ko randi khane me paya.`",
        "`Mirza galib ki yeh khani hai tu bhosdika hai yeh sab ki jubani hai.`",
	"`Mashoor Rand, Ne Arz Kiya Hai. Aane Wale Aate Hai, Jaane Wale Jaate Hai. Yaade Bas Unki Reh Jaati Hai, Jo G**Nd Sujaa Ke Jaate Hai`",
        "`Pani kam hai matke me gand marlunga jhatke me.`",
        "`Aand kitne bhi bade ho, lund ke niche hi rehte hai`",
        "`Tum Ameer hum gareeb hum jhopdiwale Tum bhosiwale`",
        "`Sisi Bhari Gulab ki padi palang ke pass chodne wale chod gye ab q baitha udaas`",
        "`Phuloo Ka Raja Gulaab Kaato me Rehta hai Jeewan ka Nirmata jaato me rehta hai😂`",
        "`Chude hue maal ko yaad mt krna Jo Chut na de usse kabhi friyad mt karna jise chudna hai wo chud ke rhegi bekar me muth maar ke apni jindagi barbaad mt krna`",
        "`Gand mare gandu Chut mare Chutiya Sabse accha mutti 2 mint me chutti😛`",
        "`Marzi Ka Sex Pap Nahi Hota.. Piche Se Dalne Wala Kabhi Baap Nahi Hota.. Condom Zarur Lagana Mere Dost Qki.. Sex K Waqt Popat Ke Pass Dimag Nahi Hota.`",
        "`Uss Ne Hothon Se Chhu Kar Lowd* Pe Nasha Kar Diya; Lu*D Ki Baat To Aur Thi, Uss Ne To Jhato* Ko Bhi Khada Kar Diya!`",
        "`Mashoor Rand, Ne Arz Kiya Hai. Aane Wale Aate Hai, Jaane Wale Jaate Hai. Yaade Bas Unki Reh Jaati Hai, Jo G**Nd Sujaa Ke Jaate Hai`",
     "`Pani kam hai matkey me ga*d mardunga teri ek jatke me`",
     "`Aand kitne bhi bade ho, lund ke niche hi rehte hai`",
     "`Tum Ameer hum gareeb hum jhopdiwale Tum bhosiwale`",
     "`Sisi Bhari Gulab ki padi palang ke pass chodne wale chod gye ab q baitha udaas`",
     "`Phuloo Ka Raja Gulaab Kaato me Rehta hai Jeewan ka Nirmata jaato me rehta hai😂`",
     "`Chude hue maal ko yaad mt krna Jo Chut na de usse kabhi friyad mt karna jise chudna hai wo chud ke rhegi bekar me muth maar ke apni jindagi barbaad mt krna`",
     "`Gand mare gandu Chut mare Chutiya Sabse accha mutti 2 mint me chutti😛`",
     "`Marzi Ka Sex Pap Nahi Hota.. Piche Se Dalne Wala Kabhi Baap Nahi Hota.. Condom Zarur Lagana Mere Dost Qki.. Sex K Waqt Popat Ke Pass Dimag Nahi Hota.`",
     "`Uss Ne Hothon Se Chhu Kar Lowd* Pe Nasha Kar Diya; Lu*D Ki Baat To Aur Thi, Uss Ne To Jhato* Ko Bhi Khada Kar Diya!`",
     "`Taare hai Asmaan me very very bright jhaat na jla bsdk dekh le apni height.`",
     "`jindagi ki na toote lari iski lulli hoti nhi khadi`",
     "`Kbhi kbhi meri dil me khyaal ata hai ayse chutiyo ko kon paida kr jata hai😂.`",
     "`Saawan ka mahina pawan kare shor jake gand mara bskd kahi aur.`", 
     "`Dil ke armaa ansuon me beh jaye tum bskd ke chutiye hi reh gye.`",
     "`Ishq Se Tabiyat Ne Zeest Ka Mazaa aya maine is lodu ko randi khane me paya.`",
     "`Mirza galib ki yeh khani hai tu bhosdika hai yeh sab ki jubani hai.`",
     "`It's better to let someone think you are an Idiot than to open your mouth and prove it.`",
   "`Talking to a liberal is like trying to explain social media to a 70 years old`",
   "`CHAND PE HAI APUN LAWDE.`",
   "`Pehle main tereko chakna dega, fir daru pilayega, fir jab aap dimag se nahi L*nd se sochoge, tab bolega..`",
   "`Pardhan mantri se number liya, parliament apne ;__; baap ka hai...`",
   "`Cachaa Ooo bhosdi wale Chacha`",
   "`Aaisi Londiya Chodiye, L*nd Ka Aapa Khoye, Auro Se Chudi Na Ho, Biwi Wo Hi Hoye`",
   "`Nachoo Bhosdike Nachoo`",
   "`Jinda toh Jhaat ke Baal bhi hai`",
]
GEY_STRINGS = [
     "`you gey bsdk`",
     "`you gey`",
     "`you gey in the house`",
     "`you chakka`",
     "`you gey gey gey gey gey gey gey gey`",
     "`you gey go away`",
     "`Such Gay personality !`",
     "`Me chakko se baat nhi krta`",
     "`There is no difference between You and Manjul Khattar`",
]
PRO_STRINGS = [
     "`This gey is pro as phack.`",
     "`Pros here -_- Time to Leave`",
     "`Proness Level: 6969696969`",
     "`Itna pro banda dekhlia bc, ab to marna hoga.`",
     "`U iz pro but i iz ur DAD, KeK`",
     "`What are you Bsdk? Human or Gawd(+_+)`",
     "`Aye pro,ek baat yaad rakhna, Agar Bharosa khud par ho to ksi ki chut tumhari kamzori nahi bnskti.`",
     "`I smell a Pro Guy around me!`",
     "`You're as pro as Durov`",
]
INSULT_STRINGS = [ 
    "`Owww ... Such a stupid idiot.`",
    "`BC.. Gaand na fulao, maa chod denge tumhari`",
    "`Don't drink and type.`",
    "`I think you should go home or better a mental asylum.`",
    "`Command not found. Just like your brain.`",
    "`Bot rule 544 section 9 prevents me from replying to stupid humans like you.`",
    "`Sorry, we do not sell brains.`",
    "`Believe me you are not normal.`",
    "`I bet your brain feels as good as new, seeing that you never use it.`",
    "`If I wanted to kill myself I'd climb your ego and jump to your IQ.`",
    "`You didn't evolve from apes, they evolved from you.`",
    "`What language are you speaking? Cause it sounds like bullshit.`",
    "`You are proof that evolution CAN go in reverse.`",
    "`I would ask you how old you are but I know you can't count that high.`",
    "`As an outsider, what do you think of the human race?`",
    "`Ordinarily people live and learn. You just live.`",
    "`Keep talking, someday you'll say something intelligent!.......(I doubt it though)`",
    "`Everyone has the right to be stupid but you are abusing the privilege.`",
    "`I'm sorry I hurt your feelings when I called you stupid. I thought you already knew that.`",
    "`You should try tasting cyanide.`",
    "`You should try sleeping forever.`",
    "`Pick up a gun and shoot yourself.`",
    "`Try bathing with Hydrochloric Acid instead of water.`",
    "`Go Green! Stop inhaling Oxygen.`",
    "`God was searching for you. You should leave to meet him.`",
    "`You should Volunteer for target in an firing range.`",
    "`Try playing catch and throw with RDX its fun.`",
    "`People like you are the reason we have middle fingers.`",
    "`When your mom dropped you off at the school, she got a ticket for littering.`",
    "`You’re so ugly that when you cry, the tears roll down the back of your head…just to avoid your face.`",
    "`If you’re talking behind my back then you’re in a perfect position to kiss my a**!.`",
    "`Do you realize you are making a fool of yourself? Apparently not.`",
    "`Zombies eat brains... you're safe.`",
    "`I'm not saying you're stupid, I'm just saying you've got bad luck when it comes to thinking.`",
    "`Brains aren't everything. In your case they're nothing.`",
    "`I don't know what makes you so stupid, but it really works.`",
    "`Alas! Your neurotransmitters are no more working.`",
    "`Are you crazy you fool.`",
    "`Shock me, say something intelligent.`",
    "`Your enzymes are meant to digest rat poison.`",
    "`You could make a world record by jumping from a plane without parachute.`",
    "`Stop talking BS and jump in front of a running bullet train.`",
    "`Try this: if you hold your breath underwater for an hour, you can then hold it forever.`",
    "`God was searching for you. You should leave to meet him.`",
    "`Give your 100%. Now, go donate blood.`",
    "`Try jumping from a hundred story building but you can do it only once.`",
    "`You should donate your brain seeing that you never used it.`",
    "`Volunteer for target in an firing range.`",
    "`Head shots are fun. Get yourself one.`",
    "`You should try swimming with great white sharks.`",
    "`You should paint yourself red and run in a bull marathon.`",
    "`You can stay underwater for the rest of your life without coming back up.`",
    "`How about you stop breathing for like 1 day? That'll be great.`",
    "`Try provoking a tiger while you both are in a cage.`",
    "`Have you tried shooting yourself as high as 100m using a canon.`",
    "`You should try holding TNT in your mouth and igniting it.`",
    "`Try playing catch and throw with RDX its fun.`",
    "`I heard phogine is poisonous but i guess you wont mind inhaling it for fun.`",
    "`Launch yourself into outer space while forgetting oxygen on Earth.`",
    "`You should try playing snake and ladders, with real snakes and no ladders.`",
    "`Dance naked on a couple of HT wires.`",
    "`Active Volcano is the best swimming pool for you.`",
    "`You should try hot bath in a volcano.`",
    "`Try to spend one day in a coffin and it will be yours forever.`",
    "`Hit Uranium with a slow moving neutron in your presence. It will be a worthwhile experience.`",
    "`You can be the first person to step on sun. Have a try.`",
]
# ===========================================
                          

@borg.on(admin_cmd("runs ?(.*)"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(RUNSREACTS) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = RUNSREACTS[bro]
    await event.edit(reply_text)


@borg.on(admin_cmd("metoo ?(.*)"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(METOOSTR) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = METOOSTR[bro]
    await event.edit(reply_text)


@borg.on(admin_cmd("rape ?(.*)"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(RAPE_STRINGS) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = RAPE_STRINGS[bro]
    await event.edit(reply_text)
			  
                          
@borg.on(admin_cmd("insult ?(.*)"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(INSULT_STRINGS) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = INSULT_STRINGS[bro]
    await event.edit(reply_text)
			  
			  
@borg.on(admin_cmd("pro ?(.*)"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(PRO_STRINGS) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = PRO_STRINGS[bro]
    await event.edit(reply_text)
			  
			  
@borg.on(admin_cmd("maaki ?(.*)"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(ABUSE_STRINGS) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = ABUSE_STRINGS[bro]
    await event.edit(reply_text)
			  
			  
@borg.on(admin_cmd("gey ?(.*)"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(GEY_STRINGS) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = GEY_STRINGS[bro]
    await event.edit(reply_text)

@borg.on(admin_cmd("noob ?(.*)"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(NOOBSTR) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = NOOBSTR[bro]
    await event.edit(reply_text)


@borg.on(admin_cmd("hii ?(.*)"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(HELLOSTR) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = HELLOSTR[bro]
    await event.edit(reply_text)

@borg.on(admin_cmd("chase ?(.*)"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(CHASE_STR) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = CHASE_STR[bro]
    await event.edit(reply_text)


@borg.on(events.NewMessage(pattern=r"\.abuse(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str in "hin":
        emoticons = [
            "Maderchod- MOTHERFUCKER",
            "Bhosadike-BORN FROM A ROTTEN PUSSY",
            "Bhen chod-Sister fucker",
            "Bhadhava- Pimp",
            "Bhadhava- Pimp",
            "Chodu- Fucker",
            "Chutiya- Fucker, bastard",
            "Gaand- ASS",
            "Gaandu-Asshole",
"Gadha, Bakland- Idiot",
"Lauda, Lund- Penis, dick, cock",
"Hijra- Gay, Transsexual",
"Kuttiya- Bitch",
"Paad- FART",
"Randi- HOOKER",
"Saala kutta- Bloody dog",
"Saali kutti- Bloody bitch",
"Tatti- Shit",
"Kamina- bastard",
"Chut ke pasine mein talay huye bhajiye- Snack fried in pussy sweat",
"Chut ke dhakkan- Pussy lid",
"Chut ke gulam- Pussy whipped",
"Chutiya ka bheja ghas khane gaya hai- idiot’s brain has gone to eat grass",
"Choot marani ka- Pussy whipped",
"Choot ka baal- Hair of vagina",
"Chipkali ke jhaat ke baal- Lizard’s cunt hairs",
"Chipkali ke jhaat ke paseene- Sweat of Lizard’s pubic hair",
"Chipkali ke gaand ke pasine-  Sweat of a lizard’s ass",
"Chipkali ke chut ke pasine- Sweat of reptiles cunt",
"Chipkali ki bhigi chut- Wet pussy of a wall lizard",
"Chinaal ke gadde ke nipple ke baal ke joon- Prostitute’s breast’s nipple’s hair’s lice",
"Chullu bhar muth mein doob mar-  Drown yourself in a handful of semen",
"Cuntmama- Vaginal uncle",
"Chhed- Vagina,Hole",
"Apni gaand mein muthi daal- Put your fist up your ass",
"Apni lund choos- Go and suck your own dick",
"Apni ma ko ja choos- Go suck your mom",
"Bhen ke laude- Sister’s dick",
"Bhen ke takke: Go and suck your sister’s balls",
"Abla naari tera buble bhaari-  woman, your tits are huge",
"Bhonsri-Waalaa- You fucker",
"Bhadwe ka awlat- Son of a pimp",
"Bhains ki aulad- Son of a buffalo",
"Buddha Khoosat- Old fart",
"Bol teri gand kaise maru- let me know how to fuck you in the ass",
"Bur ki chatani- Ketchup of cunt",
"Chunni- Clit",
"Chinaal- Whore",
"Chudai khana- Whore house",
"Chudan chuda- Fucking games",
"Chut ka pujari- pussy worshipper",
"Chut ka bhoot- Vaginal Ghost",
"Gaand ka makhan- Butter from the ass",
"Gaand main lassan- Garlic in ass",
"Gaand main danda- Stick in ass",
"Gaand main keera- Bug up your ass",
"Gaand mein bambu- A bambooup your ass",
"Gaandfat- Busted ass",
"Pote kitne bhi bade ho, lund ke niche hi rehte hai- However big the balls might be, they have to stay beneath the penis",
"Hazaar lund teri gaand main-Thousand dicks in your ass",
"Jhat ke baal- Pubic hair",
"Jhaant ke pissu- Bug of pubic hair",
"Kadak Mall- Sexy Girl",
"Kali Choot Ke Safaid Jhaat- White hair of a black pussy",
"Khotey ki aulda- Son of donkey",
"Kutte ka awlat- Son of a dog",
"Kutte ki jat- Breed of dog",
"Kutte ke tatte- Dog’s balls",
"Kutte ke poot, teri maa ki choot-  Son of a dog, your mother’s pussy",
"Lavde ke bal- Hair on your penis",
"muh mei lele: Suck my dick",
"Lund Chus: Suck dick",
"Lund Ke Pasine- Sweat of dick",
"Meri Gand Ka Khatmal: Bug of my Ass",
"Moot, Mootna- Piss off",
"Najayaz paidaish- Illegitimately born",
"Randi khana- whore house",
"Sadi hui gaand- Stinking ass",
"Teri gaand main kute ka lund- A dog’s dick in your ass",
"Teri maa ka bhosda- Your mother’s breasts",
"Teri maa ki chut- Your mother’s pussy",
"Tere gaand mein keede paday- May worms infest your ass-hole",
"Ullu ke pathe- Idiot",
        ]
    
    elif input_str in "waving":
        emoticons = [
            "(ノ^∇^)",
            "(;-_-)/",
            "@(o・ェ・)@ノ",
            "ヾ(＾-＾)ノ",
            "ヾ(◍’౪◍)ﾉﾞ♡",
            "(ό‿ὸ)ﾉ",
            "(ヾ(´・ω・｀)",
        ]
    elif input_str in "wtf":
        emoticons = [
            "༎ຶ‿༎ຶ",
            "(‿ˠ‿)",
            "╰U╯☜(◉ɷ◉ )",
            "(;´༎ຶ益༎ຶ)♡",
            "╭∩╮(︶ε︶*)chu",
            "( ＾◡＾)っ (‿|‿)",
        ]
    elif input_str in "love":
        emoticons = [
            "乂❤‿❤乂",
            "(｡♥‿♥｡)",
            "( ͡~ ͜ʖ ͡°)",
            "໒( ♥ ◡ ♥ )७",
            "༼♥ل͜♥༽",
        ]
    elif input_str in "confused":
        emoticons = [
            "(・_・ヾ",
            "｢(ﾟﾍﾟ)",
            "﴾͡๏̯͡๏﴿",
            "(￣■￣;)!?",
            "▐ ˵ ͠° (oo) °͠ ˵ ▐",
            "(-_-)ゞ゛",
        ]
    elif input_str in "dead":
        emoticons = [
            "(✖╭╮✖)",
            "✖‿✖",
            "(+_+)",
            "(✖﹏✖)",
            "∑(✘Д✘๑)",
        ]
    elif input_str in "sad":
        emoticons = [
            "(＠´＿｀＠)",
            "⊙︿⊙",
            "(▰˘︹˘▰)",
            "●︿●",
            "(　´_ﾉ` )",
            "彡(-_-;)彡",
        ]
    elif input_str in "dog":
        emoticons = [
            "-ᄒᴥᄒ-",
            "◖⚆ᴥ⚆◗",
        ]
    else:    
        emoticons = [
            "( ͡° ͜ʖ ͡°)",
            "¯\_(ツ)_/¯",
            "( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)",
            "ʕ•ᴥ•ʔ",
            "(▀ Ĺ̯▀   )",
            "(ง ͠° ͟ل͜ ͡°)ง",
            "༼ つ ◕_◕ ༽つ",
            "ಠ_ಠ",
            "(☞ ͡° ͜ʖ ͡°)☞",
            "¯\_༼ ି ~ ି ༽_/¯",
            "c༼ ͡° ͜ʖ ͡° ༽⊃",
        ]
    index = random.randint(0, len(emoticons))
    output_str = emoticons[index]
    await event.edit(output_str)

