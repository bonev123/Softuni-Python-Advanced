from Encapsulation_exer_01_Wild_cat_zoo.caretaker import Caretaker
from Encapsulation_exer_01_Wild_cat_zoo.cheetah import Cheetah
from Encapsulation_exer_01_Wild_cat_zoo.keeper import Keeper
from Encapsulation_exer_01_Wild_cat_zoo.lion import Lion
from Encapsulation_exer_01_Wild_cat_zoo.tiger import Tiger
from Encapsulation_exer_01_Wild_cat_zoo.vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) < self.__animal_capacity and self.__budget >= price:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {type(animal).__name__} added to the zoo"
        elif len(self.animals) < self.__animal_capacity and not self.__budget >= price:
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salary = 0
        for worker in self.workers:
            total_salary += worker.salary
        if total_salary <= self.__budget:
            self.__budget -= total_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        money_to_tend = sum(map(lambda animal: animal.money_for_care, self.animals))
        if self.__budget >= money_to_tend:
            self.__budget -= money_to_tend
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        lion_count = 0
        lion_info = []
        for animal in self.animals:
            if type(animal) == Lion:
                lion_count += 1
                lion_info.append(repr(animal))

        tiger_count = 0
        tiger_info = []
        for animal in self.animals:
            if type(animal) == Tiger:
                tiger_count += 1
                tiger_info.append(repr(animal))

        cheetah_count = 0
        cheetah_info = []
        for animal in self.animals:
            if type(animal) == Cheetah:
                cheetah_count += 1
                cheetah_info.append(repr(animal))
        result += f"----- {lion_count} Lions:\n"
        lion_result = "\n".join(lion_info)
        result += lion_result + '\n'

        result += f"----- {tiger_count} Tigers:\n"
        tiger_result = "\n".join(tiger_info)
        result += tiger_result + '\n'

        result += f"----- {cheetah_count} Cheetahs:\n"
        cheetah_result = "\n".join(cheetah_info)
        result += cheetah_result

        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        keeper_count = 0
        keeper_info = []
        for worker in self.workers:
            if type(worker) == Keeper:
                keeper_count += 1
                keeper_info.append(repr(worker))
        caretaker_count = 0
        caretaker_info = []
        for worker in self.workers:
            if type(worker) == Caretaker:
                caretaker_count += 1
                caretaker_info.append(repr(worker))

        vet_count = 0
        vet_info = []
        for worker in self.workers:
            if type(worker) == Vet:
                vet_count += 1
                vet_info.append(repr(worker))

        result += f"----- {keeper_count} Keepers:\n"
        keeper_result = "\n".join(keeper_info)
        result += keeper_result + '\n'

        result += f"----- {caretaker_count} Caretakers:\n"
        caretaker_result = "\n".join(caretaker_info)
        result += caretaker_result + '\n'

        result += f"----- {vet_count} Vets:\n"
        vet_result = "\n".join(vet_info)
        result += vet_result

        return result




