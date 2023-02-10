import csv


def generate_dict_foods(data, person):
    dict_food = {}
    for name, food, _ in data:
        if name == person:
            if food not in dict_food:
                dict_food[food] = 1
            else:
                dict_food[food] += 1
    return dict_food


def find_most_common_food(data, person):
    dict_food = generate_dict_foods(data, person)

    most_order_amout = 0
    most_order_food = ''
    for food, amount in dict_food.items():
        if amount >= most_order_amout:
            most_order_amout = amount
            most_order_food = food
    return most_order_food


def get_never_ask_food_by_person(data, person):
    all_foods = {food for _, food, _ in data}
    all_person_food = {food for name, food, _ in data if name == person}
    return all_foods.difference(all_person_food)


def get_never_went_by_person(data, person):
    all_days = {day for _, _, day in data}
    all_person_day = {day for name, _, day in data if name == person}
    return all_days.difference(all_person_day)


def analyze_log(path_to_file):
    if not path_to_file.endswith('.csv'):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        with open(path_to_file, encoding="utf-8") as file:
            file_info = list(csv.reader(file, delimiter=",", quotechar='"'))

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

    else:
        maria_eats = find_most_common_food(file_info, 'maria')
        arnaldo_food = generate_dict_foods(file_info, 'arnaldo')['hamburguer']
        joao_never_ask = get_never_ask_food_by_person(file_info, 'joao')
        joao_never_went = get_never_went_by_person(file_info, 'joao')

        result = [
            f'{maria_eats}\n',
            f'{arnaldo_food}\n',
            f'{joao_never_ask}\n',
            f'{joao_never_went}\n',
        ]

        with open('data/mkt_campaign.txt', mode='w') as file_txt:
            file_txt.write(''.join(result))
