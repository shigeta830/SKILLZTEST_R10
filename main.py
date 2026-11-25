from pyscript import document, when

MEMBERS = ["bong bong marcos", "ethan de leon", "spider man", "jose rizal", "ibbara"]

@when("click", "#check_btn")
def check_name(event):
    first = document.getElementById("first_name").value.strip()
    last = document.getElementById("last_name").value.strip()
    full_name = f"{first} {last}".strip()

    if full_name.lower() in MEMBERS:
        document.getElementById("result").innerHTML = f"Welcome, {full_name}!"
    else:
        document.getElementById("result").innerHTML = f"{full_name} is not on the list."
