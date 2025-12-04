"""
Module proposant des outils pour vérifier si une chaîne est un palindrome.
La normalisation inclut la mise en minuscules, la suppression d'accents
et l’élimination des espaces et de certains signes de ponctuation.
"""
#### Fonction secondaire


def ispalindrome(p):
    """
    Vérifie si une chaîne est un palindrome après normalisation.
    
    La fonction :
    - met la chaîne en minuscules,
    - remplace les caractères accentués,
    - supprime espaces et ponctuation courante,
    - compare la chaîne à son inverse.
    
    Retourne True si la chaîne ainsi traitée est un palindrome.
    """
    p=p.lower()
    table=str.maketrans('éèêëàâäùûüôç','eeeeaaauuuoc'," '!,-:?;.’")
    p=p.translate(table)
    return p == p[::-1]

#### Fonction principale


def main():
    """
    Lance quelques tests de la fonction ispalindrome et affiche les résultats.
    Sert d’exemple d'utilisation du module.
    """
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
