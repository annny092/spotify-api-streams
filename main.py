import handlers.totphandler as totphand
from classes.playlist import Playlist as plabj
import json

obj = plabj(106) ##CHANGE: total number of songs in playlist
savedStreams = obj.get_streams()

songs = {
    'Total': 0,
    'Lead': 0,
    'F*CK LOVE': 0,
    'THE FIRST TIME': 0,
    'blank': '',
    'Blessings': '0',
    'Let Her Go': '0',
    'Diva (feat. Lil Tecca)': '0',
    'Addison Rae': '0',
    'Costa Rica (feat. The Kid LAROI) - Remix': '0',
    'Go Dumb (feat. blackbear, The Kid LAROI and Bankrol Hayden)': '0',
    'Fade Away': '0',
    'Hate The Other Side (with Marshmello & The Kid Laroi)': '0',
    'BOOTY CALL (skit)': '0',
    'MAYBE': '0',
    'WRONG (feat. Lil Mosey)': '0',
    'I WISH': '0',
    'NOT FAIR (feat. Corbin)': '0',
    'BATHROOM (skit)': '0',
    'GO (feat. Juice WRLD)': '0',
    'TELL ME WHY': '0',
    'SAME THING': '0',
    'NEW GUY (skit)': '0',
    'ERASE U': '0',
    'RUNNING': '0',
    'WISH YOU WELL (skit)': '0',
    'NEED YOU MOST (So Sick)': '0',
    'SELFISH': '0',
    'Speak (feat. The Kid Laroi)': '0',
    'HELL BENT (with The Kid LAROI)': '0',
    'My City': '0',
    'PIKACHU': '0',
    'SO DONE': '0',
    'TRAGIC (feat. Youngboy Never Broke Again & Internet Money)': '0',
    'ALWAYS DO': '0',
    'FEEL SOMETHING (feat. Marshmello)': '0',
    'F*CK YOU, GOODBYE (feat. Machine Gun Kelly)': '0',
    'WITHOUT YOU': '0',
    'Reminds Me Of You': '0',
    'idk why': '0',
    'Unstable (feat. The Kid LAROI)': '0',
    'WITHOUT YOU - Spotify Singles': '0',
    'Shot For Me - Spotify Singles': '0',
    'WITHOUT YOU (with Miley Cyrus)': '0',
    'No Return (with The Kid LAROI & Lil Durk)': '0',
    'You Can\'t': '0',
    'OVER YOU': '0',
    'NOT SOBER (feat. Polo G & Stunna Gambino)': '0',
    'STAY (with Justin Bieber)': '0',
    'SAME ENERGY': '0',
    'DON\'T LEAVE ME (feat. G Herbo & Lil Durk)': '0',
    'BAD NEWS': '0',
    'STILL CHOSE YOU (feat. Mustard)': '0',
    'I DON\'T KNOW': '0',
    'ABOUT YOU': '0',
    'LONELY AND F*CKED UP': '0',
    'SITUATION': '0',
    'ATTENTION': '0',
    'BEST FOR ME': '0',
    'Wasting Angels (with The Kid LAROI)': '0',
    'Paris to Tokyo': '0',
    'Burning Up (feat. The Kid LAROI)': '0',
    'I Can\'t Go Back To The Way It Was (Intro)': '0',
    'KIDS ARE GROWING UP (PART 1)': '0',
    'I GUESS IT\'S LOVE?': '0',
    'What You Say (feat. Post Malone & The Kid LAROI)': '0',
    '2 Grown (feat. The Kid LAROI)': '0',
    'Forever & Again (From Barbie The Album)': '0',
    'Wind (feat. The Kid LAROI)': '0',
    'SORRY': '0',
    'BLEED': '0',
    'I THOUGHT THAT I NEEDED YOU': '0',
    'WHERE DO YOU SLEEP?': '0',
    'TOO MUCH': '0',
    'TEAR ME APART': '0',
    'STRANGERS (Interlude)': '0',
    'NIGHTS LIKE THIS': '0',
    'WHAT\'S THE MOVE? (feat. Future and BabyDrill)': '0',
    'STRANGERS PT 2 (Interlude)': '0',
    'CALL ME INSTEAD (feat. Youngboy Never Broke Again & Robert Glasper)': '0',
    'DESERVE YOU': '0',
    'WHAT WENT WRONG???': '0',
    'THE LINE (feat. d4vd)': '0',
    'WHAT JUST HAPPENED': '0',
    'YOU': '0',
    'LOVE AGAIN': '0',
    'WHERE DOES YOUR SPIRIT GO?': '0',
    'YOU NEVER FORGET YOUR FIRST TIME...': '0',
    'KIDS ARE GROWING UP': '0',
    'alright (feat. The Kid LAROI)': '0',
    'This My Life (with Lil Tecca, The Kid LAROI & Lil Skies)': '0',
    'Still Yours (From The Doc)': '0',
    'BABY I\'M BACK': '0',
    'STICK WITH ME': '0',
    'PICK SIDES': '0',
    'NIGHTS LIKE THIS PT 2': '0',
    'HATRED': '0',
    'GIRLS': '0',
    'THOUSAND MILES': '0',
    'HEAVEN': '0',
    'Rain Fallin (feat. The Kid LAROI)': '0', 
    'BABY I\'M BACK - Remix': '0',
    'APEROL SPRITZ': '0',
    'SLOW IT DOWN': '0',
    'Goodbye': '0',
    'I know love (feat. The Kid LAROI)': '0',
    'ALL I WANT IS YOU': '0',
    'Distant Strangers (feat. The Kid LAROI & Imogen Heap)': '0',
    'HOW DOES IT FEEL?': '0',
    'HOT GIRL PROBLEMS': '0', 
    'Lost (feat. The Kid LAROI)': '0'
}

albums = {
    'F*CK LOVE': [
       'BOOTY CALL (skit)',
        'MAYBE',
        'WRONG (feat. Lil Mosey)',
        'I WISH',
        'NOT FAIR (feat. Corbin)',
        'BATHROOM (skit)',
        'GO (feat. Juice WRLD)',
        'TELL ME WHY',
        'SAME THING',
        'NEW GUY (skit)',
        'ERASE U',
        'RUNNING',
        'WISH YOU WELL (skit)',
        'NEED YOU MOST (So Sick)',
        'SELFISH', 
        'PIKACHU',
        'SO DONE',
        'TRAGIC (feat. Youngboy Never Broke Again & Internet Money)',
        'ALWAYS DO',
        'FEEL SOMETHING (feat. Marshmello)',
        'F*CK YOU, GOODBYE (feat. Machine Gun Kelly)',
        'WITHOUT YOU',
        'OVER YOU',
        'NOT SOBER (feat. Polo G & Stunna Gambino)',
        'STAY (with Justin Bieber)',
        'SAME ENERGY',
        'DON\'T LEAVE ME (feat. G Herbo & Lil Durk)',
        'BAD NEWS',
        'STILL CHOSE YOU (feat. Mustard)',
        'I DON\'T KNOW',
        'ABOUT YOU',
        'LONELY AND F*CKED UP',
        'SITUATION',
        'ATTENTION',
        'BEST FOR ME'
    ],
    "THE FIRST TIME":[
        'SORRY',
        'BLEED',
        'I THOUGHT THAT I NEEDED YOU',
        'WHERE DO YOU SLEEP?',
        'TOO MUCH',
        'TEAR ME APART',
        'STRANGERS (Interlude)',
        'NIGHTS LIKE THIS',
        'WHAT\'S THE MOVE? (feat. Future and BabyDrill)',
        'STRANGERS PT 2 (Interlude)',
        'CALL ME INSTEAD (feat. Youngboy Never Broke Again & Robert Glasper)',
        'DESERVE YOU',
        'WHAT WENT WRONG???',
        'THE LINE (feat. d4vd)',
        'WHAT JUST HAPPENED',
        'YOU',
        'LOVE AGAIN',
        'WHERE DOES YOUR SPIRIT GO?',
        'YOU NEVER FORGET YOUR FIRST TIME...',
        'KIDS ARE GROWING UP',
        'BABY I\'M BACK',
        'STICK WITH ME',
        'PICK SIDES',
        'NIGHTS LIKE THIS PT 2',
        'HATRED',
        'GIRLS',
        'THOUSAND MILES',
        'HEAVEN'
    ]
}

features = [
    'Costa Rica (feat. The Kid LAROI) - Remix',
    'Go Dumb (feat. blackbear, The Kid LAROI and Bankrol Hayden)',
    'Hate The Other Side (with Marshmello & The Kid Laroi)',
    'Speak (feat. The Kid Laroi)',
    'HELL BENT (with The Kid LAROI)',
    'idk why',
    'Unstable (feat. The Kid LAROI)',
    'No Return (with The Kid LAROI & Lil Durk)',
    'You Can\'t',
    'Wasting Angels (with The Kid LAROI)',
    'Burning Up (feat. The Kid LAROI)',
    'What You Say (feat. Post Malone & The Kid LAROI)',
    '2 Grown (feat. The Kid LAROI)',
    'Wind (feat. The Kid LAROI)',
    'alright (feat. The Kid LAROI)',
    'This My Life (with Lil Tecca, The Kid LAROI & Lil Skies)',
    'Rain Fallin (feat. The Kid LAROI)',
    'I know love (feat. The Kid LAROI)',
    'Distant Strangers (feat. The Kid LAROI & Imogen Heap)',
    'Lost (feat. The Kid LAROI)'
]

def get_all_streams():
    global songs
    global savedStreams
    savedStreams = savedStreams["data"]["playlistV2"]["content"]["items"]
    for song in savedStreams:
        song = song["itemV2"]["data"]
        songs[song["name"]] = song["playcount"]

def album():
    for x in list(songs.values())[5:]:
        songs["Total"] = songs["Total"] + int(x)

    songs['Lead'] = songs['Total']
    for x in features:
        songs['Lead'] = songs['Lead'] - int(songs[x])

    for x, y in albums.items():
        for yy in y:
            songs[x] = songs[x] + int(songs[yy])
            
get_all_streams()
album()

for x in songs.values():
    print(x)
