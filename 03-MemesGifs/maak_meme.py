from PIL import Image, ImageFont, ImageDraw


achtergrond = Image.open("meme_background.jpg")

breedte = achtergrond.width
hoogte = achtergrond.height

print("De afbeelding is " + str(breedte) + " pixels breed en " + str(hoogte) + " pixels hoog")

lettertype = ImageFont.truetype("impact.ttf", 20)

tekengebied = ImageDraw.Draw(achtergrond)

tekst = "teenage mutant/nninja turtles"
tekengebied.multiline_text((10,10), tekst, font=lettertype, fill=(0,0,0))

tekst_breedte, tekst_hoogte = tekengebied.textsize(tekst, font=lettertype)
print("tekstbreedte=" + str(tekst_breedte) + ", tekst_hoogte=" + str(tekst_hoogte))

tekst_x = (breedte - tekst_breedte) / 2
tekst_y = (hoogte - tekst_hoogte) / 2

tekengebied.multiline_text((tekst_x, tekst_y), tekst, font=lettertype, fill=(0,0,0))
tekengebied.multiline_text((tekst_x-2, tekst_y-2), tekst, font=lettertype, fill=(255,255,255))

achtergrond.show()

achtergrond.save("meme_met_tekst.jpg")
