#region Characters
define Vicky = Character("Vicky", color = "#008080")
define Ger = Character("Gertrude", color = "#00cdcd")
define mysGer = Character("???", color = "#00cdcd")
define mysDad = Character("???", color = "#00b3b3")
define Hustace = Character("Hustace", color = "#00b3b3")
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
image Chicken = "/images/backgrounds/showchicken.png"
image Cornhole = "/images/backgrounds/cornholing.png"
image TractorPull = "/images/backgrounds/tractor pulling.png"
image NightWoods = "/images/backgrounds/woodsnight.png"
image Confession = "/images/backgrounds/confession.png"
image Kissy = "/images/backgrounds/kissykissy.png"
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
image vickyAnnoyedLeft = "/images/art/FoxGal/left annoyed.png"
image vickySlyRight = "/images/art/FoxGal/right sly.png"
image vickyFairExcited = "/images/art/FoxGal/right mid excited.png"
image vickyFairFlirt = "/images/art/FoxGal/right mid flirt.png"
image vickyFairStandard = "/images/art/FoxGal/right mid standard.png"
image vickyFairSmile = "/images/art/FoxGal/right mid warmsmile.png"
image vickyFairPensive = "/images/art/FoxGal/right mid pensive.png"
image vickyFairEmbarrassed = "/images/art/FoxGal/right mid embarrassed.png"
image chonkyVickyStandard = "/images/art/FoxGal/chonky vicki standard.png"
image chonkyVickySmile = "/images/art/FoxGal/chonky vicki happy smile.png"
image chonkyVickyShy = "/images/art/FoxGal/chonky vicki shy.png"
image chonkyVickySurprise = "/images/art/FoxGal/chonky vicki surprised.png"
image vickyHoneyDrink = "/images/art/FoxGal/drinkin honey.png"
image vickyTummy = "/images/art/FoxGal/tummy.png"
image vickyandhustace = "/images/backgrounds/vicky and hustace.png"

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
image hustaceAngryFlip = Transform("/images/art/Hustace/Huebert angry Posehalf.png", xzoom=-1) 
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
    call part1 from _call_part1
    #region Bounce code
    #something at bounce with dissolve
    transform bounce:
        pause .15
        yoffset 0
        easeout .08 yoffset 12
        easein .08 yoffset 0
        easeout .08 yoffset 6
        easein .08 yoffset 0
        yoffset 0
#endregion

