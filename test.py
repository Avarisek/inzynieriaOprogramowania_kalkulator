def hello(name):
	return "Hello "+str(name)


print("Tutaj bedziemy powodwoac konflikt")

def dodaj(a,b):
	wynik=float(a)+float(b)
	return wynik

pierwsza=input()
druga=input()

print(dodaj(pierwsza,druga))


