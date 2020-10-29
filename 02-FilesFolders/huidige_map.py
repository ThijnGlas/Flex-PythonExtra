
import os


werkmap = os.getcwd()


print("De huidige map is: " + werkmap)

os.mkdir("Een nieuwe map")

os.mkdir("eigen gemaakte map")

mapnaam = input("Welke naam wil je voor de map? ")


lengte_mapnaam = len(mapnaam)
if lengte_mapnaam > 0:
    os.mkdir(mapnaam)
    print("De map " + mapnaam + " is gemaakt.")
else:
    print("Je hebt geen naam ingevoerd")
    
mapnaam = ""


lengte_mapnaam = 0


while lengte_mapnaam == 0:
    
    mapnaam = input("Welke naam wil je voor de map? ")

    
    lengte_mapnaam = len(mapnaam)

    
    if lengte_mapnaam > 0:
        os.mkdir(mapnaam)
    else:
       
        print("Je hebt geen naam ingevoerd")


print("De map " + mapnaam + " is gemaakt.")
