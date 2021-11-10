import random

# assign a random person to each person as a seceret santa
# cannot assign same person

secret_santa_list = []
person_list = ["Ruth", "David", "Gel", "Ciaran", "Bev", "Vince", "Vanessa", "Matt", "Semra"]
assign_person_list = list(person_list)
random.shuffle(assign_person_list)

def assign_person(person):
    last_person = assign_person_list[-1]

    if person != last_person:
        person_dict = {
            person: last_person #: person
        }

        assign_person_list.remove(last_person)
        secret_santa_list.append(person_dict)
    else:
        random.shuffle(assign_person_list)
        assign_person(person)

N = len(person_list)
while N > 0:
    random_person = random.choice(person_list)

    assign_person(random_person)
    person_list.remove(random_person)

    N -= 1

print("Secret Santa List:\n")

for x in secret_santa_list:
    for k, v in x.items():
        print(f"{k}: {v}")
