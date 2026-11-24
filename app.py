
import streamlit as st
import pandas as pd

from database import (
    ajouter_depense,
    recuperer_depenses,
    supprimer_depense
)

# Familles déjà créées en interne
familles = {
    "Ace/Seb/Arthur/Jeanne": 4,
    "Monique/JY": 2,
    "Béné/Gaël/Garance/Mattéo": 4,
    "JP/Lulu": 2,
    "Youn/Natacha/Lou/Nina": 2,
    "Alan/Julie/Camille/Liam": 3,
    "Christiane/Philipe": 2,
    "Anaïs/Charles/Swann": 2,
    "Quentin/Camille": 2
}


# Titre de l'application
st.title("🎄 Dépenses de Noël")

# --------------------------------
# AJOUTER UNE DÉPENSE
# --------------------------------

st.subheader("Ajouter une dépense")

titre = st.text_input("Intitulé de la dépense")

famille = st.selectbox(
    "Famille ayant payé",
    familles.keys(),
    index=None,
    placeholder="Choisir une famille"
)

montant = st.number_input(
    "Montant (€)",
    min_value=0.01,
    step=1.0
)

date_depense = st.date_input(
    "Date de la dépense",
    value=None,
    format="DD/MM/YYYY"
)

if st.button("Ajouter la dépense"):

    if titre.strip() and famille is not None else "":

        ajouter_depense(titre, montant, famille, date_depense)

        st.success("Dépense ajoutée !")

        st.rerun()

    else:
        st.error("Veuillez renseigner un intitulé.")


# --------------------------------
# AFFICHER LES DÉPENSES
# --------------------------------

st.subheader("Liste des dépenses")

# Récupérer les dépenses depuis SQLite
depenses = recuperer_depenses()

# Transformer les données en tableau
donnees = []

for depense in depenses:
    donnees.append({
        "Titre": depense["description"],
        "Famille": depense["famille"],
        "Montant (€)": float(depense["montant"]),
        "Date": depense["date_depense"] or ""
    })

# Créer le DataFrame
df = pd.DataFrame(donnees)

# Afficher le tableau
st.dataframe(df, use_container_width=True)


# --------------------------------
# SUPPRIMER UNE DÉPENSE
# --------------------------------

st.subheader("Supprimer une dépense")

for depense in depenses:

    col1, col2 = st.columns([4, 1])

    with col1:
        st.write(
            f'{depense["description"]} - '
            f'{float(depense["montant"]):.2f} € - '
            f'{depense["famille"]} - '
            f'{depense["date_depense"]}' if depense["date_depense"] is not None
        )

    with col2:
        if st.button("Supprimer", key=f'supprimer_{depense["id"]}'):

            supprimer_depense(depense["id"])

            st.success("Dépense supprimée !")

            st.rerun()
