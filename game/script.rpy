# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#region Characters
define Vicky = Character("Vicky", color = "#df1d1d")
define Ger = Character("Gertrude", color = "#6b5050ff")
define mysGer = Character("???", color = "#6b5050ff")
#endregion

#region backgrounds
image gertyShop = "/images/backgrounds/gertys_shop.png"
image carScene = "/images/backgrounds/carScene1.jpg"
image carScene2 = "/images/backgrounds/carScene2.jpg"
image carScene3 = "/images/backgrounds/carScene3.jpg"
image carScene4 = "/images/backgrounds/carScene4.jpg"
image jailScene = "/images/backgrounds/jail.jpg"
image noSignal = "/images/backgrounds/no_signal.png"
image partyScene = "/images/backgrounds/partyscene.png"
image townSquare = "/images/backgrounds/Town_Square.jpg"
image woodsScene = "/images/backgrounds/woods.jpg"
#endregion

#region images
#Gertrude
image gerPic = "images/art/Gertrude/Gertrude Standard Pose no leg.png"

#Vicky
image vickyStandard = "/images/art/FoxGal/Fox Standard Pose facing right no leg650.png"
#endregion

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
    call part1
    return
