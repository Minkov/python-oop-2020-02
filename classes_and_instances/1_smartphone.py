class Smartphone:
    apps = []

    def __init__(self, memory):
        self.memory = memory
        self.memory_taken = 0
        self.is_on = False
        # self.apps = []

    def power(self):
        self.is_on = not self.is_on

    def install(self, app, app_memory):
        if not self.is_on:
            return f'Turn on your phone to install {app}'

        memory_left = self.memory - self.memory_taken
        if memory_left < app_memory:
            return f'Not enough memory to install {app}'

        self.apps.append(app)
        self.memory_taken += app_memory
        return f'Installing {app}'

    def install2(self, app, app_memory):
        if self.is_on:
            memory_left = self.memory - self.memory_taken
            if memory_left < app_memory:
                return f'Not enough memory to install {app}'
            else:
                self.apps.append(app)
                self.memory_taken += app_memory
                return f'Installing {app}'
        else:
            return f'Turn on your phone to install {app}'

    def status(self):
        total_apps_count = len(self.apps)
        memory_left = self.memory - self.memory_taken
        return f'Total apps: {total_apps_count}. Memory left: {memory_left}'


samsung = Smartphone(32)
iphone = Smartphone(16)

print(samsung.status())
print(iphone.status())

iphone.power()
iphone.install('fb', 1)

print(samsung.status())
print(iphone.status())
print(Smartphone.apps)


class Smartphone2:
    memory = int
