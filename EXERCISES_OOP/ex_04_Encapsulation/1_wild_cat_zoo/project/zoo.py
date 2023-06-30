from project.animal import Animal
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.vet import Vet
from project.caretaker import Caretaker
from project.lion import Lion
from project.tiger import Tiger
from project.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price: float):  #
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"

        if self.__budget < price:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price

        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity == len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    # def fire_worker(self, worker_name: str):
    #     try:
    #         worker = next(filter(lambda w: w.name == worker_name, self.workers))
    #     except StopIteration:
    #         return f"There is no {worker_name} in the zoo"
    #     self.workers.remove(worker)
    #     return f"{worker_name} fired successfully"

    def pay_workers(self):
        workers_salary = sum(w.salary for w in self.workers)
        if self.__budget >= workers_salary:
            self.__budget -= workers_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        animals_cost = sum(a.money_for_care for a in self.animals)
        if self.__budget >= animals_cost:
            self.__budget -= animals_cost
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"

        lions = [repr(a) for a in self.animals if isinstance(a, Lion)]
        result += f"----- {len(lions)} Lions:\n" + '\n'.join(lions) + "\n"

        tigers = [repr(a) for a in self.animals if isinstance(a, Tiger)]
        result += f"----- {len(tigers)} Tigers:\n" + '\n'.join(tigers) + "\n"

        cheetahs = [repr(a) for a in self.animals if isinstance(a, Cheetah)]
        result += f"----- {len(cheetahs)} Cheetahs:\n" + '\n'.join(cheetahs)
        return result


    # def animals_status(self):
    #     lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
    #     tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
    #     cheetahs = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]
    #
    #     # lions = filter(lambda a: a.__class__.__name__ == "Lion", self.animals)
    #     # tigers = filter(lambda a: a.__class__.__name__ == "Tiger", self.animals)
    #     # cheetah = filter(lambda a: a.__class__.__name__ == "Cheetah", self.animals)
    #
    #     combined_animals = []
    #     for animal in self.animals:
    #         if animal.__class__.__name__ == "Lion" or animal.__class__.__name__ == "Tiger" or animal.__class__.__name__ == "Cheetah":
    #             combined_animals.append(animal)
    #     result = [
    #         f"You have {len(self.animals)} animals",
    #         f"----- {len(lions)} Lions: "
    #     ]
    #     result.extend(lions)
    #
    #     result.append(f"----- {len(tigers)} Tigers:")
    #     result.extend(tigers)
    #
    #     result.append(f"----- {len(cheetahs)} Cheetahs:")
    #     result.extend(cheetahs)
    #
    #     return "\n".join(str(x) for x in result)

    # def workers_status(self):
    #
    #     result = f"You have {len(self.workers)} workers\n"
    #
    #     keepers = [repr(k) for k in self.workers if isinstance(k, Keeper)]
    #     result += f"----- {len(keepers)} Keepers:\n" + "\n".join(keepers) + "\n"
    #
    #     caretakers = [repr(c) for c in self.workers if isinstance(c, Caretaker)]
    #     result += f"----- {len(caretakers)} Caretaker:\n" + "\n".join(caretakers) + "\n"
    #
    #     vets = [repr(v) for v in self.workers if isinstance(v, Vet)]
    #     result += f"----- {len(vets)} Vet:\n" + "\n".join(vets)
    #     return result


    def workers_status(self):
        info = {
            "Keeper": [],
            "Caretaker": [],
            "Vet": [],
        }
        [info[w.__class__.__name__].append(str(w)) for w in self.workers]

        result = [
            f"You have {len(self.workers)} workers",
            f"----- {len(info['Keeper'])} Keepers:",
            *info["Keeper"],
            f"----- {len(info['Caretaker'])} Caretakers:",
            *info["Caretaker"],
            f"----- {len(info['Vet'])} Vets:",
            *info["Vet"],
        ]

        return "\n".join(result)


