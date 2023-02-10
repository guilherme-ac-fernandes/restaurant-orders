import random


class TrackOrders:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def add_new_order(self, customer, order, day):
        self._data.append([customer, order, day])

    def generate_foods_dict(self, customer):
        dict_food = {}
        for name, food, _ in self._data:
            if name == customer:
                if food not in dict_food:
                    dict_food[food] = 1
                else:
                    dict_food[food] += 1
        return dict_food

    def get_most_ordered_dish_per_customer(self, customer):
        dict_food = self.generate_foods_dict(customer)

        most_order_amout = 0
        most_order_food = ''
        for food, amount in dict_food.items():
            if amount >= most_order_amout:
                most_order_amout = amount
                most_order_food = food
        return most_order_food

    def get_all_foods(self):
        return {food for _, food, _ in self._data}

    def get_never_ordered_per_customer(self, customer):
        all_foods = self.get_all_foods()
        all_person_food = {food
                           for name, food, _ in self._data
                           if name == customer}
        return all_foods.difference(all_person_food)

    def get_all_days(self):
        return {day for _, _, day in self._data}

    def get_days_never_visited_per_customer(self, customer):
        all_days = self.get_all_days()
        all_person_day = {day
                          for name, _, day in self._data
                          if name == customer}
        return all_days.difference(all_person_day)

    def get_busiest_day(self):
        dict_days = {}
        for _, _, day in self._data:
            if day not in dict_days:
                dict_days[day] = 1
            else:
                dict_days[day] += 1

        most_busiest_amout = 0
        most_busiest_day = ''
        for day, amount in dict_days.items():
            if amount >= most_busiest_amout:
                most_busiest_amout = amount
                most_busiest_day = day
        return most_busiest_day

    def get_least_busy_day(self):
        dict_days = {}
        for _, _, day in self._data:
            if day not in dict_days:
                dict_days[day] = 1
            else:
                dict_days[day] += 1

        # Seleção de uma chave aleatória proveniente da Solução
        # proveniente do Stack OverFlow
        # source: https://stackoverflow.com/questions/4859292/h
        # ow-to-get-a-random-value-from-dictionary
        random_item = random.choice(list(dict_days.items()))
        least_busy_day, least_busy_amout = random_item
        for day, amount in dict_days.items():
            if amount < least_busy_amout:
                least_busy_amout = amount
                least_busy_day = day
        return least_busy_day
