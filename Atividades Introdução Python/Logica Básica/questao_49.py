hora_inicio = int(input('digite a hora do inicio da experiencia: '))
minutos_inicio = int(input('digite os minutos do inicio da experiencia: '))
segundos_inicio = int(input('digite os segundos do inicio da experiencia: '))

hora_duracao = int(input('digite as horas da duracao da experiencia: '))
minutos_duracao = int(input('digite os minutos da duracao da experiencia: '))
segundos_duracao = int(input('digite os segundos da duracao da experiencia: '))

hora_inicio = hora_inicio + hora_duracao

minutos_inicio = minutos_inicio + minutos_duracao

while minutos_inicio >= 60:
    minutos_inicio = minutos_inicio - 60
    hora_inicio+=1

segundos_inicio = segundos_inicio + segundos_duracao

while segundos_inicio >= 60:
    segundos_inicio = segundos_inicio-60
    minutos_inicio +=1

print(f"{hora_inicio}h {minutos_inicio}min {segundos_inicio}s")