def ProzentwertRechnen():
	Kapital = float(input("Geben Sie Grundwert an: "))
	Prozentsatz = float(input("Geben Sie Prozentsatz an: "))
	Zw = float(Prozentsatz * Grundwert)
	if zinsen == "ja":
		for l in range(0,12):
			l += 1
			Zinswert = Zw / 12 * l
			print(l, Zinswert)

while True:
    ProzentwertRechnen()
    print("------------------")
