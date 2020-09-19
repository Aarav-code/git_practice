
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming",
                  "alarmed", "out of control", "help", "unhappy", "bad", 
                  "upset", "awful", "broken", "damage", "damaging", "dismal",
                  "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
censor = "learning algorithms"
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her",
                     "herself"]


def censor_email1(email1):
    new_mail = []
    if censor in email1:
        new_mail = email1.replace("learning algorithms", "*******")
    return new_mail


def censor_email2(email2):
    new_mail = []
    for num in range(len(proprietary_terms)):
        if proprietary_terms[num] in email2:
            new_mail = email2.replace(proprietary_terms[num], "********")
            email2 = new_mail
    return new_mail


def censor_email3(email3):
    i = 0
    new_mail = []
    for num in range(len(negative_words)):
        if negative_words[num] in email3:
            i += 1
            if i > 2:
                new_mail = email3.replace(negative_words[num], "********")
                email3 = new_mail
    return censor_email2(new_mail)


print(censor_email3(email_three))
