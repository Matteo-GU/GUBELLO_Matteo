print("Saisir un jour : ")
jour=input()

print("Saisir une heure : ")
heure=input()

print("Saisir une minute : ")
minute=input()

minute = int(minute)
minute = minute + 60*int(heure) + 1440*int(jour)
print(f"Il y a eu {minute} minutes depuis le début du mois")