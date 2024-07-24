from random_user_id import generate_random_user_id
def user_id_gen_by_user():
    number_of_character = int(input())
    number_of_id = int(input())
    list_of_id = []
    for i in range(number_of_id):
        list_of_id.append(generate_random_user_id(number_of_character))
    return list_of_id
print(user_id_gen_by_user())