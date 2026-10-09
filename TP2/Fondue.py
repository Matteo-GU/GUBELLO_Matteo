BASE=4  #indique le nombre de personnes pour laquelle est conçue la recette de base
fromage=800.0 #quantité de fromage en grammes nécessaire pour BASE personnes
eau=2  #quantité d'eau en décilitres nécessaire pour BASE personnes
ail=2 #nombre de gousses d'ail nécessaires pour BASE personnes
pain=400 # quantité de pain en grammes nécessaire pour BASE personnes

nbConvives=int(input("Entrez le nombre de personne(s) conviées à la fondue : "))

fromage=fromage*nbConvives/BASE
eau=eau*nbConvives/BASE
ail=ail*nbConvives/BASE
pain=pain*nbConvives/BASE

print("Pour faire une fondue fribourgeoise pour {} personnes, il vous faut :".format(nbConvives))
print("- {} gr de fromage".format(fromage))
print("- {} dl de eau".format(eau))
print("- {} gousse(s) d'ail".format(eau))
print("- {} gr de pain".format(pain))