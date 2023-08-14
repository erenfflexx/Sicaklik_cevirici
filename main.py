print("-" * 30)
print("1- Celcius - Fahrenhayt")
print("2- Fahrenhayt - Celcius")
print("-" * 30)

seçim = input("seçiminiz (1/2): ")

if seçim == "1":
    print("\n# celcius - fahrenhayt")
    celsius = float(input("Dönüştürülecek celcius: "))
    fahrenheit = (celsius * 1.8) + 32
    print("{} derece celcius eşittir {}  fahrenheit derece.".format(celsius, fahrenheit))
elif seçim == "2":
    print("\n# Fahrenhayt - celcius")
    fahrenheit = float(input("dönüştürülecek fahrenhayt: "))
    celsius = (fahrenheit - 32) / 1.8
    print("{} derece fahrenhayt eşittir {} celcius derece.".format(fahrenheit, celsius)
