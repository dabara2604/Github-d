Co = int(input("¿Qué te queda en pesos?: "))
Pe = int(input("¿Qué te queda en soles?: "))
Br = int(input("¿Qué te queda en reais?: "))
Cod = Co * 0.0578
Ped = Pe * 0.2800
Brd = Br * 0.2140
Usd = Cod + Ped + Brd
print(Usd)