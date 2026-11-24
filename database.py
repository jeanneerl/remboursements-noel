
import streamlit as st
from supabase import create_client


# Connexion à Supabase
def connexion():
    url = st.secrets["SUPABASE_URL"]
    cle = st.secrets["SUPABASE_KEY"]
    print("URL utilisée :", url)
    return create_client(url, cle)


# Ajouter une dépense
def ajouter_depense(description, montant, famille):
    supabase = connexion()

    supabase.table("depenses").insert({
        "description": description,
        "montant": float(montant),
        "famille": famille
    }).execute()


# Récupérer toutes les dépenses
def recuperer_depenses():
    supabase = connexion()

    resultat = (
        supabase.table("depenses")
        .select("*")
        .order("id")
        .execute()
    )

    return resultat.data


# Supprimer une dépense
def supprimer_depense(id_depense):
    supabase = connexion()

    supabase.table("depenses").delete().eq(
        "id", id_depense
    ).execute()
