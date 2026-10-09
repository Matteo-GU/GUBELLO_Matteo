print("Saisir les minutes : ")
minute=input()
minute=int(minute)

heure = minute // 60
minute = minute %60

jour = heure // 24
heure = heure %24

print(f"Nous sommes le {jour} à {heure}:{minute}")