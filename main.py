from pyscript import display, document #type: ignore

nonmetals = { #Dictionary
    "H": ("Hydrogen", 1, 1.008),
    "He": ("Helium", 2, 4.0026),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999), 
    "F": ("Fluorine", 9, 18.998),
    "Ne": ("Neon", 10, 20.180),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.06),
    "Cl": ("Chlorine", 17, 35.45),
    "Ar": ("Argon", 18, 39.948),
    "Se": ("Selenium", 34, 78.971),
    "Br": ("Bromine", 35, 79.904),
    "Kr": ("Krypton", 36, 83.798),
    "I": ("Iodine", 53, 126.90),
    "Xe": ("Xenon", 54, 131.29),
    "Rn": ("Radon", 86, 222),
}

def element_Checker(e): # I got help from Google Search with this
    document.getElementById('result').innerHTML = ""

    element1 = document.getElementById("Element").value.strip().title()
    elname, number, mass = nonmetals.get(element1, ("Element not found", "-", "-")
    )

    document.getElementById('result').innerHTML = f"""
    <b>Symbol:</b> {element1} <br>
    <b>Element:</b> {elname} <br>
    <b>Atomic Number:</b> {number} <br>
    <b>Atomic Mass:</b> {mass}
    """


def candidate_checker(e): 
    club_members = ["angelica delrosario", "river datiles", "aaron deguzman", "kyle delacalzada", "millicent meneses", "gilliah tabaldo", "alexandra uaje"]

    f_name = document.getElementById('first_name').value
    l_name = document.getElementById('last_name').value
    candidate = f_name + ' ' + l_name
    member_checker = candidate.lower() in club_members 

    messages = (
        f'Sorry {candidate}, your name is not on the list' ,
        f'Congratulations {candidate}, you are part of the Marching Band!' 
    )

    document.getElementById('result').innerHTML = messages[member_checker]

