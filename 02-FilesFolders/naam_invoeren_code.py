import os

mapnaam = ""

lengte_mapnaam = 0

while lengte_mapnaam == 0:
    mapnaam=input("welke naam wilt u aan deze map geven?")

    lengte_mapnaam = len(mapnaam)

    if lengte_mapnaam > 0:
        os.mkdir(mapnaam)

    else:
        print ("geef een naam op.")


print ("de map "+ mapnaam + " is aangemaakt.")
