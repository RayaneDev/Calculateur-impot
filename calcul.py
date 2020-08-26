salaire = int(input('Salaire annuel net : '))
en_couple = str(input('En couple ? (O pour oui et N pour non) : '))
nb_enfants = int(input('Nombre d\'enfants ? :'))

def calc_impot (salaire, reste=salaire, impot=0, quotients=1, b=1) : 

    if (b < 5) : 
        tranches = [10064, 15595, 47710, 84437, 157806]
        impositions = [0, 0.11, 0.3, 0.41, 0.45]

        if (b == 1 and (nb_enfants > 0 or en_couple == "O")) : 
            quotients = quotients + nb_enfants * 0.5
            if (en_couple == "O") : 
                quotients = quotients + 1 

            salaire = salaire / quotients 
            reste = salaire

        nouveau_reste = reste - tranches[b-1]

        if (nouveau_reste > 0) : 
            impot = impot + tranches[b-1] * impositions[b - 1]
            print ("Vous payez", impot, "€ pour la tranche numéro", b,".")
            b = b + 1
            calc_impot(salaire, nouveau_reste, impot, quotients, b)
        else : 
            impot = (impot + reste * impositions[b - 1]) * quotients 
            print("Votre impôt s'élève à", impot, "€.")

            return impot
            
calc_impot(salaire)

