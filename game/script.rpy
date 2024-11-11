# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#region Characters
define Vicky = Character("Vicky", color = "#df1d1d")
define Ger = Character("Gertrude", color = "#6b5050ff")
define mysGer = Character("???", color = "#6b5050ff")
#endregion

#region images
#Gertrude
image gerPic = "images/art/Gertrude/Gertrude Standard Pose no leg.png"

#Vicky
image VickyPic = "images/art/FoxGal/Fox Standard Pose facing right no leg750x1000.png"
image VickyPicLegs = "images/art/FoxGal/Fox Standard Pose facing right no leg.png"
image annoyedVicky = "images/art/FoxGal/Fox Annoyed Pose facing right no leg 750x1000.png"
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
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)
    call part1
    return
