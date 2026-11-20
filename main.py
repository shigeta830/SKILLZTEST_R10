 from pyscript import display, document, when

non_metal = {
    "H": ("Hydrogen", "1", "1.008"),
    "He": ("Helium", "2", "4.003"),
    "C": ("Carbon", "6", "12.011"),
    "N": ("Nitrogen", "7", "14.007"),
    "O": ("Oxygen", "8", "15.999"),
    "F": ("Fluorine", "9", "18.998"),
    "Ne": ("Neon", "10", "20.180"),
    "P": ("Phosphorus", "15", "30.974"),
    "S": ("Sulfur", "16", "32.06"),
    "Cl": ("Chlorine", "17", "35.45"),
    "Ar": ("Argon", "18", "39.948"),
    "Se": ("Selenium", "34", "78.971"),
    "Br": ("Bromine", "35", "79.904"),
    "Kr": ("Krypton", "36", "83.798"),
    "I": ("Iodine", "53", "126.90"),
    "Xe": ("Xenon", "54", "131.29"),
    "Rn": ("Radon", "86", "222")
}

# Tells you immediately when Python is ready!
document.getElementById('Result').innerHTML = "Ready! Enter a symbol above."

@when("click", "#search_btn")
def show_element(e):
    document.getElementById('Result').innerHTML = " "
    element1 = document.getElementById('element_input').value.strip().title()

    name, atomic_num, atomic_mass = non_metal.get(
        element1,
        ("Element not found", " ", " ")
    )

    document.getElementById('Result').innerHTML = f"""
    <b>Symbol:</b> {element1} <br>
    <b>Element:</b> {name} <br>
    <b>Atomic Number:</b> {atomic_num} <br>
    <b>Atomic Mass:</b> {atomic_mass}
    """
