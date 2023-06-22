class Smartphone:

    def __init__(self, memory: int):
        self.memory = memory
        self.memory_used = 0
        self.apps = []
        self.is_on = False

    def power(self):
        self.is_on = True

    def install(self, app, app_memory):
        if not self.is_on:
            return f"Turn on your phone to install {app}"
        if self.calc_left_memory() < app_memory:
            return f"Not enough memory to install {app}"

        self.apps.append(app)
        self.memory_used += app_memory
        return f"Installing {app}"

    def status(self):
        total_apps_count = len(self.apps)
        mem_left = self.calc_left_memory()
        return f"Total apps: {total_apps_count}. Memory left: {mem_left}"

    def calc_left_memory(self):
        return self.memory - self.memory_used


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())