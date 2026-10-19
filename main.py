#Tuples and List in Python
from pyscript import display, document


def checkname(e):
    document.getElementById('output').innerHTML = " "
    club_applicant = str(document.getElementById('firstname').value)
    club_applicant1 = str(document.getElementById('lastname').value)

    input = str(club_applicant) + " " + str(club_applicant1)
    inputlast = input.title()

    allowed_people = ['John Carreon', 'Nathan Bautista', 'Jaden Galvez', 'Chester Roxas']
    applicant_checker = inputlast in allowed_people
    display_message = (f'Sorry {inputlast}, you are not included in the Rainbow Catering Club', f'Congratulations {inputlast}, you are part of the Rainbow Catering Club!')

    display(display_message[applicant_checker], target='output')