#region Characters
define Vicky = Character("Vicky", color = "#df1d1d")
define Ger = Character("Gertrude", color = "#6b5050ff")
define mysGer = Character("???", color = "#6b5050ff")
define mysDad = Character("???", color = "#bd400fff")
define Hustace = Character("Hustace", color = "#bd400fff")
#endregion

#region backgrounds
image gertyShop = "/images/backgrounds/gertys_shop.png"
image carScene = "/images/backgrounds/carScene1.jpg"
image carScene2 = "/images/backgrounds/carScene2.jpg"
image carScene3 = "/images/backgrounds/carScene3.jpg"
image carScene4 = "/images/backgrounds/carScene4.jpg"
image jailScene = "/images/backgrounds/jail.jpg"
image noSignal = "/images/backgrounds/no signal.png"
image partyScene = "/images/backgrounds/partyscene.png"
image townSquare = "/images/backgrounds/Town Square.jpg"
image woodsScene = "/images/backgrounds/woods.png"
image bearDadFirstScene = "/images/backgrounds/beardad first good lookwip.jpg"
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

#Hustace
image hustaceStandard = "/images/art/Hustace/Hustace Standard Posehalf.png"
image hustaceLaugh = "/images/art/Hustace/Huebert laugh Posehalf.png"
image hustaceAngry = "/images/art/Hustace/Huebert angry Posehalf.png"
image hustaceSad = "/images/art/Hustace/Huebert sadge Posehalf.png"
#endregion

label splashscreen:
    scene black
    with Pause(1)
    show text "This game contains material only suited for adults 18+ and over. If you are under 18 please click off now." with dissolve
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
    call part1 from _call_part1
    return
