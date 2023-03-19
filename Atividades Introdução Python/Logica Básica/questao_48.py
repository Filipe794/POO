segundos = int(input("Digite a quantidade de segundos: "))

horas = segundos // 3600
segundos %= 3600

minutos = segundos // 60
segundos %= 60

print(f"{horas}h {minutos}min {segundos}s")
