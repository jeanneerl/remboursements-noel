class Famille:
    def __init__(self, nom, nb_parts):
        self.nom = nom
        self.nb_parts = nb_parts
        self.montant_paye = 0

    def ajouter_paiement(self, montant):
        self.montant_paye += montant

    def calculer_part(self, prix_part):
        return self.nb_parts * prix_part

    def calculer_solde(self, prix_part):
        return self.montant_paye - self.calculer_part(prix_part)

class Depense:
    def __init__(self, montant, famille, description):
        self.description = description
        self.montant = montant
        self.famille = famille

class GestionRemboursements:
    def __init__(self):
        self.familles = {}
        self.depenses = []

    def ajouter_famille(self, famille):
        self.familles[famille.nom] = famille

    def ajouter_depense(self, depense):
        self.depenses.append(depense)

    def calculer_total_depenses(self):
        return sum(d.montant for d in self.depenses)

    def calculer_total_parts(self):
        return sum(f.nombre_parts for f in self.familles.values())

    def generer_remboursements(soldes):

      crediteurs = []
      debiteurs = []

      for nom, solde in soldes.items():
        if solde > 0:
            crediteurs.append([nom, solde])

        elif solde < 0:
            debiteurs.append([nom, -solde])

      remboursements = []

      i = 0
      j = 0

      while i < len(debiteurs) and j < len(crediteurs):

        montant = min(debiteurs[i][1], crediteurs[j][1])

        remboursements.append((debiteurs[i][0], crediteurs[j][0], montant))

        debiteurs[i][1] -= montant
        crediteurs[j][1] -= montant

        if debiteurs[i][1] == 0:
            i += 1

        if crediteurs[j][1] == 0:
            j += 1

      return remboursements


anais = Famille("Anaïs/Charles/Swann",2)
ace = Famille("Anne-Céline/Seb/Jeanne/Arthur",4)
monique = Famille("Jean-Yves/Monique",2)
bene = Famille("Béné/Gaël/Garance/Mattéo",4)
youn = Famille("Youenn/Natacha/Lou/Nina",2)
jp = Famille("Jean-Pierre/Lulu",2)
christiane = Famille("Christiane/Philipe",2)
quentin = Famille("Quentin/Camille",2)
alan = Famille("Alan/Julie/Camille/Liam",3)

Depense(1000,ace, "Gîte")
Depense(1000,christiane, "Gîte")
Depense(1000,jp, "Gîte")

