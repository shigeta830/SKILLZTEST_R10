from pyscript import document, when

CLUB_MEMBERS = [
    "bong bong marcos",
    "ethan de leon",
    "spider man",
    "jose rizal",
    "ibbara",
]


def set_status(message, state="neutral"):
    box = document.getElementById("result")
    box.className = "status-screen"
    if state == "granted":
        box.classList.add("status-granted")
    elif state == "denied":
        box.classList.add("status-denied")
    box.innerHTML = message


@when("click", "#enter_btn")
def candidate_checker(event):
    f_name = document.getElementById("first_name").value.strip()
    l_name = document.getElementById("last_name").value.strip()
    candidate = f"{f_name} {l_name}".strip()

    if not candidate:
        set_status("WARNING: ENTER PLAYER NAME FIRST.", "denied")
        return

    is_member = candidate.lower() in CLUB_MEMBERS
    if is_member:
        set_status(
            f"ACCESS GRANTED // WELCOME, {candidate.upper()}!",
            "granted",
        )
    else:
        set_status(
            f"ACCESS DENIED // {candidate.upper()} IS NOT ON THE ROSTER.",
            "denied",
        )


@when("click", "#reset_btn")
def reset_menu(event):
    document.getElementById("first_name").value = ""
    document.getElementById("last_name").value = ""
    set_status("AWAITING PLAYER INPUT...", "neutral")


@when("click", ".preset-btn")
def load_preset(event):
    btn = event.currentTarget
    document.getElementById("first_name").value = btn.getAttribute("data-first") or ""
    document.getElementById("last_name").value = btn.getAttribute("data-last") or ""
    candidate_checker(event)
