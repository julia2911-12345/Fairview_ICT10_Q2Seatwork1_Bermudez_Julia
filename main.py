from pyscript import document

#list of members in the dance club
club_members = [
    "GEORGINA FLORENCE BANAL",
    "GEORGINA MANDY LAINE CAJANDING",
    "JILLIAN MAIA EUSEBIO",
    "JULIA BERMUDEZ",
    "KHLOE GUTIERREZ",
    "MARC CATU",
    "SAMANTHA BAUTISTA",
    "STEPHANIE TAMBIO",
    "VIKTOR PEÑA",
    "ALEYNAH CASSEDINE REDILLAS",
    "AUDREY TAN",
    "CHELSI SIBAL",
    "CHLOE ADLAWAN",
    "DANIELLE SANDOVAL",
    "ELEAZAR SALUDEZ",
    "ELISHA ANNE O. IGLOSO",
    "ENZO JOSH MACARANAS"
]


# function for checking if name is in the list of members
def check_candidate(e):

    # calls first name and last name
    first_name = document.getElementById("first_name").value
    last_name = document.getElementById("last_name").value

    # combines first name and last name, converting it to uppercase to compare it the list
    full_name = first_name + " " + last_name
    full_name = full_name.upper()

    # checks if fullname is in the list, true or false
    is_member = full_name in club_members

    messages = {
        True: "Congratulations " + full_name.title() +
              "! You are now part of the Dance Club.",

        False: "Sorry " + full_name.title() +
               ", your name is not on the list."
    }

    #gets result from dict then displays it in the result div
    result = messages[is_member]

    document.getElementById("result").innerHTML = result