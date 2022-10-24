weight=int(input('Weight: '))
measurement=input( '(L)bs or (K)g: ')
if measurement.lower()== "L":
    converted= weight*0.4550
    print(f"You are {converted} kilos")
else:
    converted = weight//0.45
    print(f"You are {converted}")
