def ProzentwertRechnen():
	Grundwert = float(input("Geben Sie Grundwert an: "))
	Prozentsatz = float(input("Geben Sie Prozentsatz an: "))
	Prozentwert = float(Prozentsatz * Grundwert / 100)
	print("Prozentwert: ", Prozentwert)
	print("Grundwert plus Prozentwert : ", Grundwert + Prozentwert)
	print("Grundwert minus Prozentwert: ", Grundwert - Prozentwert)



def ProzentsatzRechnen():
	Grundwert = float(input("Geben Sie Grundwert an: "))
	Prozentwert = float(input("Geben Sie Prozentwert an: "))
	Prozentsatz = float(Prozentwert / Grundwert * 100)
	print("Prozentsatz: ", Prozentsatz)
	print("Grundwert + Prozentwert = ", Grundwert + Prozentwert)
	print("Grundwert - Prozentwert = ", Grundwert - Prozentwert)


def GrundWertRechnen():
	Prozentwert = float(input("Geben Sie Prozentwert an: "))
	Prozentsatz = float(input("Geben Sie Prozentsatz an: "))
	print("Grundwert: ", Prozentwert / Prozentsatz * 100)

x = input ("Wollen Sie Prozentwert, Grundwert oder Prozentsatz?\n")
if x == "Prozentwert":
	while True:	
		ProzentwertRechnen()
elif x == "Prozentsatz":
	while True:
		ProzentsatzRechnen()
else:
	while True:
		GrundWertRechnen()


