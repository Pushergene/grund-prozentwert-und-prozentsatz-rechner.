def ProzentwertRechnen():
	Grundwert = float(input("Geben Sie Grundwert an: "))
	Prozentsatz = float(input("Geben Sie Prozentsatz an: "))
	Prozentwert = float(Prozentsatz * Grundwert // 100)
	print('----------------------')
	print("Prozentwert: ", Prozentwert)
	print("Grundwert plus Prozentwert : ", Grundwert + Prozentwert)
	print("Grundwert minus Prozentwert: ", Grundwert - Prozentwert)
	print('----------------------')
	zinsen = str(input("zinsen?"))
	if zinsen == "ja":
		for l in range(0,12):
			l += 1
			Zinswert = Prozentwert / 12 * l
			print(l, Zinswert)

def ProzentsatzRechnen():
	Grundwert = float(input("Geben Sie Grundwert an: "))
	Prozentwert = float(input("Geben Sie Prozentwert an: "))
	Prozentsatz = float(Prozentwert / Grundwert * 100)
	print("Prozentsatz: ", Prozentsatz)
	print('')
	print("Grundwert + Prozentwert = ", Grundwert + Prozentwert)
	print('')
	print("Grundwert - Prozentwert = ", Grundwert - Prozentwert)
	print('')


def GrundWertRechnen():
	Prozentwert = float(input("Geben Sie Prozentwert an: "))
	Prozentsatz = float(input("Geben Sie Prozentsatz an: "))
	print('')
	print("Grundwert: ", Prozentwert // Prozentsatz * 100)
	
while True:
  x = input ("Wollen Sie Prozentwert, Grundwert oder Prozentsatz?\n")
  if x == "pw":	
    ProzentwertRechnen()
  elif x == "ps":
    ProzentsatzRechnen()
  elif x == "gw":
    GrundWertRechnen()
  print("------------------")