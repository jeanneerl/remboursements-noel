import sqlite3

# Connexion à la base de données
def connexion():
    return sqlite3.connect("depenses.db")


# Création de la table
def initialiser_base():
    conn = connexion()
    curseur = conn.cursor()

    curseur.execute("""
        CREATE TABLE IF NOT EXISTS depenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            montant REAL NOT NULL,
            famille TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

def ajouter_depense(description, montant, famille):
    conn = connexion()
    curseur = conn.cursor()

    curseur.execute("""
        INSERT INTO depenses (description, montant, famille)
        VALUES (?, ?, ?)
    """, (description, montant, famille))

    conn.commit()
    conn.close()

def recuperer_depenses():
    conn = connexion()
    curseur = conn.cursor()

    curseur.execute("SELECT * FROM depenses")
    depenses = curseur.fetchall()

    conn.close()
    return depenses

def supprimer_depense(id_depense):
    conn = connexion()
    curseur = conn.cursor()

    curseur.execute(
        "DELETE FROM depenses WHERE id = ?",
        (id_depense,)
    )

    conn.commit()
    conn.close()