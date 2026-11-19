from pyscript import document

# Update status badge once PyScript finishes loading
status_badge = document.getElementById("py-status")
if status_badge:
    status_badge.innerText = "Python Ready"
    status_badge.classList.add("ready")

# Mapping between navigation button IDs and section container IDs
SECTION_TABS = {
    "tab-home": "section-home",
    "tab-elements": "section-elements",
    "tab-club": "section-club",
    "tab-creator": "section-creator",
}

# List of official Glee Club members for Seatwork 1 
OFFICIAL_MEMBERS = [
    "Jordin San Juan",
    "Elina Elysse Padre",
    "Savanah Fugueroa",
    "Franshellyahna Pilao",
    "Kyrie Cerise Funtanilla",
    "Antoinette Caleigh Garcia",
    "Julianna Omaking",
    "Aeris Bandong",
    "Vyelle Mikayla Bunag",
    "Gavin Ghonn Taguiga",
    "Hans Arada",
    "Alexi Villanueva",
    "Dannielle Luna Dimasuhid",
    "Ebtisam A. Al Hazmi",
    "Marley Summer Reyes Manese",
    "Queeny Haraj Guilas Ramos",
    "Maia Isabelle Fabro",
    "Erin Mandapat",
    "Maria Elisha Padre",
    "Nica Gabriela Crispino",
]

# Non-metal elements dictionary: Symbol --> (Name, Atomic Number, Atomic Mass)
NON_METALS = {
    "H": ("Hydrogen", "1", "1.008"),
    "C": ("Carbon", "6", "12.011"),
    "N": ("Nitrogen", "7", "14.007"),
    "O": ("Oxygen", "8", "15.999"),
    "F": ("Fluorine", "9", "18.998"),
    "P": ("Phosphorus", "15", "30.974"),
    "S": ("Sulfur", "16", "32.06"),
    "Cl": ("Chlorine", "17", "35.45"),
    "Se": ("Selenium", "34", "78.971"),
    "Br": ("Bromine", "35", "79.904"),
    "I": ("Iodine", "53", "126.90"),
    "He": ("Helium", "2", "4.0026"),
    "Ne": ("Neon", "10", "20.180"),
    "Ar": ("Argon", "18", "39.95"),
    "Kr": ("Krypton", "36", "83.80"),
    "Xe": ("Xenon", "54", "131.29"),
    "Rn": ("Radon", "86", "222"),
}

# Grade-level member sets for Drill #2
GRADE_8 = {"Jordin San Juan", "Elina Elysse Padre", "Savanah Fugueroa"}
GRADE_9 = {
    "Franshellyahna Pilao",
    "Kyrie Cerise Funtanilla",
    "Antoinette Caleigh Garcia",
    "Julianna Omaking",
}
GRADE_10 = {
    "Aeris Bandong",
    "Vyelle Mikayla Bunag",
    "Gavin Ghonn Taguiga",
    "Hans Arada",
}
GRADE_11 = {
    "Alexi Villanueva",
    "Dannielle Luna Dimasuhid",
    "Ebtisam A. Al Hazmi",
    "Marley Summer Reyes Manese",
    "Queeny Haraj Guilas Ramos",
}
GRADE_12 = {
    "Maia Isabelle Fabro",
    "Erin Mandapat",
    "Maria Elisha Padre",
    "Nica Gabriela Crispino",
}


def switch_section(event):
    """Switch active navigation tab and display the selected showcase section."""
    button = event.currentTarget
    clicked_id = button.id if button else ""

    if clicked_id not in SECTION_TABS:
        return

    for tab_id, section_id in SECTION_TABS.items():
        tab_el = document.getElementById(tab_id)
        section_el = document.getElementById(section_id)
        is_selected = tab_id == clicked_id

        tab_el.classList.toggle("active", is_selected)
        section_el.classList.toggle("d-none", not is_selected)


def check_candidate(event):
    """Verify if a candidate is in the official Glee Club roster (Seatwork 1)."""
    first = document.getElementById("verify-fname").value.strip()
    last = document.getElementById("verify-lname").value.strip()
    output_el = document.getElementById("verify-output")

    full_name = f"{first} {last}".strip()

    if not full_name:
        output_el.innerHTML = (
            '<span class="text-danger fw-bold">'
            "Please enter both first and last name to verify."
            "</span>"
        )
        return

    # Case-insensitive membership check against official list
    normalized_roster = [member.lower() for member in OFFICIAL_MEMBERS]
    is_in_list = full_name.lower() in normalized_roster

    output_messages = {
        True: f"Congratulations {full_name.title()}! You are part of the official Glee Club roster.",
        False: f"Sorry {full_name}, your name is not on the Glee Club roster.",
    }

    output_el.innerHTML = f'<span class="fw-bold">{output_messages[is_in_list]}</span>'


def search_element(event):
    """Search non-metal element details using case-normalized dictionary lookup."""
    raw_symbol = document.getElementById("element-input").value.strip()
    output_el = document.getElementById("element-output")

    # Normalize input to match exact, capitalized, or uppercase keys
    if raw_symbol in NON_METALS:
        symbol = raw_symbol
    elif raw_symbol.capitalize() in NON_METALS:
        symbol = raw_symbol.capitalize()
    elif raw_symbol.upper() in NON_METALS:
        symbol = raw_symbol.upper()
    else:
        symbol = raw_symbol

    name, atomic_num, atomic_mass = NON_METALS.get(
        symbol, ("Element not found", "-", "-")
    )

    if name == "Element not found":
        output_el.innerHTML = (
            '<div class="alert alert-danger mb-0 py-2 px-3 border-0 small">'
            "Element does not exist in the non-metals list."
            "</div>"
        )
    else:
        output_el.innerHTML = (
            "<div class='row g-2 font-monospace small'>"
            f"<div class='col-6'><strong>Symbol:</strong> {symbol}</div>"
            f"<div class='col-6'><strong>Element:</strong> {name}</div>"
            f"<div class='col-6'><strong>Atomic No:</strong> {atomic_num}</div>"
            f"<div class='col-6'><strong>Atomic Mass:</strong> {atomic_mass}</div>"
            "</div>"
        )


def add_member(event):
    """Combine grade sets with set union (|) and optionally add a new member."""
    first_name = document.getElementById("member-fname").value.strip()
    last_name = document.getElementById("member-lname").value.strip()
    output_el = document.getElementById("club-output")

    full_name = f"{first_name} {last_name}".strip()
    new_member_set = {full_name} if full_name else set()

    # Combine all grade-level sets using the union operator 
    all_members = GRADE_8 | GRADE_9 | GRADE_10 | GRADE_11 | GRADE_12 | new_member_set
    sorted_members = sorted(all_members)
    roster_html = "<br>".join(sorted_members)

    output_el.innerHTML = (
        "<div class='small'>"
        "<div><strong>ALL MEMBERS:</strong></div>"
        f"<div class='mt-1'>{roster_html}</div>"
        f"<div class='mt-3'><strong>TOTAL MEMBERS:</strong> {len(all_members)}</div>"
        "</div>"
    )