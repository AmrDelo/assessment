name = input('Enter encoded string ')
person={}

person_list = name.split('0')

person['first_name'] = person_list[0]
person['id'] = person_list[-1]

for i in range(len(person_list)):
    if person_list[i] != '' and person_list[i]!= person_list[0]:
        person['last_name'] = person_list[i]
        break
    else:
        continue

print("Decoded string is:\n",person)




