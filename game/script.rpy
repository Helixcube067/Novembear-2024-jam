#region Characters
define Vicky = Character("Vicky", color = "#df1d1d")
define Ger = Character("Gertrude", color = "#6b5050ff")
define mysGer = Character("???", color = "#6b5050ff")
define mysDad = Character("???", color = "#bd400fff")
define Hustace = Character("Hustace", color = "#bd400fff")
#endregion

#region backgrounds
image gertyShop = "/images/backgrounds/gerty's shop.png"
image carSceneLooking = "/images/backgrounds/pickup background2.png"
image carSceneGertyTalking = "/images/backgrounds/pickupbackground3.png"
image carSceneVickyTalking = "/images/backgrounds/pickupvickymouthopen.png"
image carSceneNobodyTalking = "/images/backgrounds/pickupgertymouthclosed.png"
image jailScene = "/images/backgrounds/jail.png"
image noSignal = "/images/backgrounds/no signal.png"
image partyScene = "/images/backgrounds/partyscene.png"
image townSquare = "/images/backgrounds/Town Square2.png"
image partyPolice = "/images/backgrounds/partyscenepolice.png"
image woodsScene = "/images/backgrounds/woods.png"
image bearDadFirstScene = "/images/backgrounds/beardad first good lookwip.jpg"
image Fairground = "/images/backgrounds/Fairground.png"
image VickysRoom = "/images/backgrounds/Vicki's room.png"
image vicNhu = "/images/backgrounds/vicky and hustace.png"

#endregion

#region images
#Gertrude
image gerPic = "images/art/Gertrude/Gertrude Standard Pose no leg.png"
image gerLaugh = "images/art/Gertrude/Gertrude laughPose no leg.png"
image gerAngry = "images/art/Gertrude/Gertrude angryPose no leg.png"

#Vicky
image vickyStandard = "/images/art/FoxGal/right standard.png"
image vickyStandardFlipped = "/images/art/FoxGal/left standard.png"
image vickyAnnoyedRight = "/images/art/FoxGal/right annoyed.png"
image vickySlyRight = "/images/art/FoxGal/left annoyed.png"
image vickyFairExcited = "/images/art/FoxGal/right mid excited.png"
image vickyFairFlirt = "/images/art/FoxGal/right mid flirt.png"
image vickyFairStandard = "/images/art/FoxGal/right mid standard.png"
image vickyFairSmile= "/images/art/FoxGal/right mid warmsmile.png"
image chonkyVickyStandard= "/images/art/FoxGal/chonky vicki standard.png"
image chonkyVickySmile = "/images/art/FoxGal/chonky vicki standard.png"
image chonkyVickyShy = "/images/art/FoxGal/chonky vicki shy.png"
image chonkyVickySurprise = "/images/art/FoxGal/chonky vicki shy.png"
image vickyHoneyDrink = "/images/art/FoxGal/drinkin honey.png"
image vickyTummy = "/images/art/FoxGal/tummy.png"

#Hustace
image hustaceStandard = "/images/art/Hustace/Hustace Standard Posehalf.png"
image hustaceLaugh = "/images/art/Hustace/Huebert laugh Posehalf.png"
image hustaceAngry = "/images/art/Hustace/Huebert angry Posehalf.png"
image hustaceSad = "/images/art/Hustace/Huebert sadge Posehalf.png"
image hustaceFairStandard = "/images/art/Hustace/Fairhustandard.png"
image hustaceFairSad = "/images/art/Hustace/FairHuSad.png"
image hustaceFairAngry = "/images/art/Hustace/FairHuAngry.png"
image hustaceFairLaugh = "/images/art/Hustace/Fair HuLaugh.png"
image hustaceFairShy = "/images/art/Hustace/Huebert shy Posehalfno axe.png"
image hustaceStandardFlipped = "/images/art/Hustace/Hustace Standard Posehalf Flipped.png"
#endregion

label splashscreen:
    scene black
    with Pause(1)
    show text "This game contains material only suited for adults 18+ and over. \nIf you are under 18 please click off now." with dissolve
    with Pause(3.5)
    hide text with dissolve
    with Pause(1)
    return

label start:
    #region Bounce code
    #something at bounce with dissolve
    transform bounce:
        pause .15
        yoffset 0
        easein .175 yoffset -10
        easeout .175 yoffset 0
        easein .175 yoffset -4
        easeout .175 yoffset 0
        yoffset 0
#endregion
    #shake code here
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)
    menu:
        "Skip to part 3?"
        "Yes":
            stop music fadeout 1.0
            jump part3
        "No":
            call part1 from _call_part1
    #call part1 from _call_part1
    scene black
    with fade
    "And thanks all! Thanks for reading everybody! This was made for the Novembear 2024 Jam!"
    "Here's a link to our lovely artist Danji! 
    \n{a=https://danji-isthmus.itch.io/}Itchio{/a} | {a=https://bsky.app/profile/danjiisthmus.bsky.social}Bluesky{/a} | {a=https://www.furaffinity.net/user/danji-isthmus}FurAffinity{/a}"
    "And I'm helix I'm the programmer! Heres where can check me out here: {a=https://helixcube.itch.io}Itchio{/a} | {a=https://bsky.app/profile/helixcube.bsky.social}Bluesky{/a}"
    return
