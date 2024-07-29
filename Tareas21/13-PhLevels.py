pH = int(input("Enter a pH value(0-14): "))
if pH > 7:
  print("Basico")
elif pH < 7:
  print("Acido")
else:
  print("Neutral")
  