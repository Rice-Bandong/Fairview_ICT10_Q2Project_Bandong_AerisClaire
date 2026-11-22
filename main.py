from pyscript import document

# Hide all sections and unhighlight all navigation buttons before showing the chosen page
def hide_pages():
    document.getElementById("section-creator").classList.add("d-none")
    document.getElementById("section-sw1").classList.add("d-none")
    document.getElementById("section-drill").classList.add("d-none")
    document.getElementById("section-skills").classList.add("d-none")
    document.getElementById("section-exit").classList.add("d-none")

    document.getElementById("tab-creator").classList.remove("active")
    document.getElementById("tab-sw1").classList.remove("active")
    document.getElementById("tab-drill").classList.remove("active")
    document.getElementById("tab-skills").classList.remove("active")

# Show the Meet the Creator homepage
def show_creator(event):
    hide_pages()
    document.getElementById("section-creator").classList.remove("d-none")
    document.getElementById("tab-creator").classList.add("active")

# Show Seatwork 1 (Glee Club Verification System)
def show_sw1(event):
    hide_pages()
    document.getElementById("section-sw1").classList.remove("d-none")
    document.getElementById("tab-sw1").classList.add("active")

# Show Drill #2 (Set Operators)
def show_drill(event):
    hide_pages()
    document.getElementById("section-drill").classList.remove("d-none")
    document.getElementById("tab-drill").classList.add("active")

# Show Skills Test (Non-Metal Elements Finder)
def show_skills(event):
    hide_pages()
    document.getElementById("section-skills").classList.remove("d-none")
    document.getElementById("tab-skills").classList.add("active")

# Show the thank-you screen when the Exit button is clicked
def exit_website(event):
    hide_pages()
    document.getElementById("section-exit").classList.remove("d-none")

# Official list of Glee Club members used to check candidates
members = [
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
    "Nica Gabriela Crispino"
]

def check_candidate(event):
    # Read first and last name from input fields and remove extra spaces
    first = document.getElementById("first_name").value.strip()
    last = document.getElementById("last_name").value.strip()
    full_name = f"{first} {last}".strip()

    # Check if the entered name is in the members list (True or False)
    is_in_list = full_name in members

    # Choose the output message based on membership status
    output_messages = {
        True: f"Congratulations {full_name}! You are now part of the Glee Club!",
        False: f"Sorry {full_name}, your name is not on the Glee Club roster.",
    }

    # Display the result in #result_area
    document.getElementById("result_area").innerText = output_messages[is_in_list]


# Sets of members grouped by grade level (sets automatically avoid duplicates)
grade8 = {'Jordin San Juan', 'Elina Elysse Padre', 'Savanah Fugueroa'}
grade9 = {'Franshellyahna Pilao', 'Kyrie Cerise Funtanilla', 'Antoinette Caleigh Garcia', 'Julianna Omaking'}
grade10 = {'Aeris Bandong', 'Vyelle Mikayla Bunag', 'Gavin Ghonn Taguiga', 'Hans Arada'}
grade11 = {'Alexi Villanueva', 'Dannielle Luna Dimasuhid', 'Ebtisam A. Al Hazmi', 'Marley Summer Reyes Manese', 'Queeny Haraj Guilas Ramos'}
grade12 = {'Maia Isabelle Fabro', 'Erin Mandapat', 'Maria Elisha Padre', 'Nica Gabriela Crispino'}

def add_member(event):
    # Get new member's first and last name from the inputs
    first_name = document.getElementById('fname').value.strip()
    last_name = document.getElementById('lname').value.strip()
    full_new_name = f"{first_name} {last_name}".strip()

    # Create a new set only if a name was typed; otherwise use an empty set
    new_member = {full_new_name} if full_new_name else set()

    # Combine all grade sets and the new member set using set union (|)
    all_members = grade8 | grade9 | grade10 | grade11 | grade12 | new_member

    # Sort names alphabetically and join them with line breaks for HTML display
    members_list = "<br>".join(sorted(all_members))
    total_members = len(all_members)

    # Show the full member list and total count in #output1
    document.getElementById('output1').innerHTML = f"ALL MEMBERS:<br>{members_list}<br><br>TOTAL MEMBERS: {total_members}"

def search_element(event):
    # Dictionary mapping element symbols to (Element Name, Atomic Number, Atomic Mass)
    non_metals = {
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
        "Rn": ("Radon", "86", "222")
    }

    # Read & trim the symbol typed by the user
    raw_input = document.getElementById("Element1").value.strip()

    # Normalize casing so inputs like "h", "H", "cl", or "CL" match dictionary keys
    if raw_input in non_metals:
        symbol = raw_input
    elif raw_input.capitalize() in non_metals:
        symbol = raw_input.capitalize()
    elif raw_input.upper() in non_metals:
        symbol = raw_input.upper()
    else:
        symbol = raw_input

    # Look up the symbol using .get() with a fallback tuple if not found
    result = non_metals.get(symbol, ("Element not found", "-", "-"))
    output_div = document.getElementById("output")

    # Display an error alert if missing, or show the element's details
    if result[0] == "Element not found":
        output_div.innerHTML = """
            <div class="alert alert-danger mb-0 py-2 px-3 border-0 small">
                Element does not exist in the non-metals list.
            </div>
        """
    else:
        output_div.innerHTML = f"""
            <div class="row g-2 font-monospace small">
                <div class="col-6"><strong>Symbol:</strong> {symbol}</div>
                <div class="col-6"><strong>Element:</strong> {result[0]}</div>
                <div class="col-6"><strong>Atomic No:</strong> {result[1]}</div>
                <div class="col-6"><strong>Atomic Mass:</strong> {result[2]}</div>
            </div>
        """