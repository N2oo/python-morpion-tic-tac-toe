import re


class Player:
    def __init__(self):
        pseudo: str = input("Quel est votre pseudo ? ")
        saisie_symbole: str = "XXXX"
        while len(saisie_symbole) != 1:
            saisie_symbole = str(input("{}, quel est votre symbole ? (pas plus de 1 charactère ni un chiffre) ".format(pseudo)))
            result = re.match('\d',saisie_symbole)
            if result:
                print("Veuillez ne pas saisir de chiffres")
                saisie_symbole =  "123455667"
                continue
        self.symbole: str = saisie_symbole
        self.pseudo: str = pseudo
        # demander la saisie utilisateur

    def __eq__(self, other):
        if isinstance(other, Player):
            if other.symbole == self.symbole and other.pseudo == self.pseudo:
                print("Attention le symbole et le pseudo sont les mêmes pour les deux joueurs")
                return True
            elif other.symbole == self.symbole:
                print("Attention le symbole est le même choisi par les joueurs")
                return True
            elif other.pseudo == self.pseudo:
                print("Attention les pseudos chosis sont identiques")
                return True
        return False

    def __str__(self):
        return "{} ({})".format(self.pseudo,self.symbole)

    def play(self):
        while True:
            case_selectionnee = input("{}, Veuillez saisir à quel endroit vous souhaitez jouer (tapez le numéro de la case) : ".format(self))
            result = re.match("^[1-9]$",case_selectionnee)
            if result:
                return case_selectionnee
            print("Veuillez saisir une position parmi celles disponibles, et comprises entre 1 et 9")
