# # codinng: utf-8

# #Avant toute chose, je dois d'abord importer les différents modules nécessaires à la lecture d'un API (et création d'un ficher csv)

# import json
# import csv
# import requests 

# #Je dois créer la variable qui contiendra le fichier csv par la suite 

# fichier = "lobying.csv"

# #Je crée la variable qui contient l'url de l'API des lobyings 

# url = "http://jhroy.ca/uqam/lobby.json"

# #Je dois maintenant créer mon entête pour m'identifier lorsque j'irai chercher dans l'url des informations 

# entete = {
#     "User-Agent":"Clémence Bouquerod - +33647021901 - Je réalise un devoir pour un cours de journalisme de données"
#     # "From":"clemence.bouquerod@iscpalyon.net"
# }

# #J'ai du mettre le "from" en commentaire parce que cela me dit qu'il y a une erreur de syntaxe au niveau des deux points.... j'ai tout essayé pour le faire marcher mais rien n'y fais...J'ai preféré ne pas perdre trop de temps avec ce souci qui m'a déjà fait perdre une bonne demi-heure 
# #J'utilise le .get avec l'url et mes entêtes pour aller faire la requete et aller chercher des infos dans l'API

# req = requests.get(url,headers=entete)

# #Je vérifie si l'accès m'est accordé

# print(req)

# #Je crée une condition qui ne fera fonctionner le programme que si la réponse à ma demande d'accès est 200 (comme vu en cours)
# #Puis, je continue le programme en créant une variable qui va traiter le contenu de ma variable req avec le module json 

# # if req.status_code != 200:
# #     print("L'accès n'est pas autorisé")
# # else:
# #     test = req.json()
#     #Je vérifie que ça fonctionne : 
#     # print(test) cela fonctionne, mais comme prévu, c'est illisible 
#     #Je vais réduire ma recherche et mon print 
#     # print(test["registre"][O][2]) Cela me dit que le 0 n'est pas défini....
# #Je me rend compte que si je veux réduire les possibilités aux lobbying climatiques, je dois changer de conditions : 

# #Je dois aussi créer la variable créée précedemment ici. 

# test = req.json()

# # print(test) J'ai testé et cela fonctionne

# # if req.status_code == 200:
# #     print("L'accès est autorisé")
# #     #Je teste. Cela fonctionne. J'écris la suite 
# # elif test["registre"][1]["objet"] == "limat":
# #     print(test)
# #Cette façon de faire ne fonctionne pas. Je viens de penser qu'on pouvait créer une variable pour justement avoir tous ces lobbyings climatiques

# # test2 = test["registre"][1]["objet"] == "limat"
# # print(test2)
# #Cela ne fonctionne pas comme ça 

# if req.status_code != 200:
#     print("L'accès n'est pas autorisé")
# else:
#     objet = test["registre"][1]["objet"] == "limat"
#     objet2 = test["registre"][1]["objet_autre"] == "limat" 
#     print(objet, objet2)
    #Je ne comprend pas vraiment pas pourquoi, mais voilà ce que ça me dit : "TypeError: list indices must be integers or slices, not str"  Je ne sais pas comment transformer du str en integer ou slices (je ne l'ai pas dans mon cours et ne trouve pas sur internet)

#Après ne pas avoir trouvé réponses à mes questions, j'ai décidé de continuer comme si cela allait marcher, pour vous montrer ce que je pensais faire à la base. Je suis quand même très déçue de ne pas pouvoir tester
#Je repars de 0. 

import json
import csv
import requests 

fichier = "lobying.csv"

url = "http://jhroy.ca/uqam/lobby.json"

entete = {
    "User-Agent":"Clémence Bouquerod - +33647021901 - Je réalise un devoir pour un cours de journalisme de données"
    # "From":"clemence.bouquerod@iscpalyon.net" Ca ne marche toujours pas ### ICI, IL FALLAIT SIMPLEMENT TERMINER LA LIGNE PRÉCÉDENTE PAR UNE VIRGULE :)
}

req = requests.get(url,headers=entete)

# print(req)

test = req.json()
liste = [] #J'ouvre une liste où tous les résultats iront dedans

if req.status_code != 200:
    print("L'accès n'est pas autorisé")
else:
    climat = []
    climat2 = test["registre"][1]["objet"] == "limat" ### ÇA NE MARCHE PAS PCQ ICI, TU NE REGARDES QUE DANS LE 1ER DES 72000 ÉLÉMENTS DE LA LISTE QUI EST LA VALEUR DE LA CLÉ "REGISTRE"...
    climat3 = test["registre"][1]["objet_autre"] == "limat"
    climat.append(climat2)
    climat.append(climat3)
    # print(climat, climat2) # C'est pour vérifier si ça marche (non, mais je ne trouve pas pourquoi)
    nom = climat["registre"][0]["fr_client_org_corp_nm"] 
    nom2 = climat["registre"][0]["en_client_org_corp_nm"] 
    code = climat["registre"][0]["client_org_corp_num"] 
    date = climat["registre"][0]["date_comm"]
    objet = climat["registre"][1]["objet"]
    objet2 = climat["registre"][1]["objet_autre"]
    agence = climat["registre"][2]["institution"] #Cela me dit le problème "pylint(invalide-sequence-index)" pour les 7 dernières lignes + "list indices must be integers or slices, not str" pour la ligne 98
    liste.append(nom)
    liste.append(nom2)
    liste.append(code)
    liste.append(date)
    liste.append(objet)
    liste.append(objet2)
    liste.append(agence) #J'ai rentré dans ma liste toutes les variables qu'on recherchait
    print(liste)

    dead = open(fichier, "a") #Le a c'est pour écrire dans le fichier en "append". Là j'a tout bêtement suivi ce qu'on a fait la semaine dernière pour écrire le fichier csv
    obies = csv.writer(dead)
    obies.writerow(liste)

print(req)

#Je ne sais pas pourquoi il y a eu le souci. Mais ce qui est sur, c'est que je me suis trompée à la ligne 98... J'ai eu beau me creuser la tête et chercher à faire autrement, je n'ai pensé à aucun code qui me permettrait de faire ce que je voulais faire... c'est à dire ne regarder que les lignes qui parlent de climat 
#Le problème, c'est le côté "str" que je ne comprend vraiment pas. Je pense que même ceux-ci "pylint(invalide-sequence-index)" viennent de ce problème initial, car sur internet les deux problèmes ont un rapport
