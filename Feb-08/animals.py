class Fly:
    speed = 0
    def say(self, speed):
        self.speed = speed
    
    def fly(self, distance):
        time = distance // self.speed
        print(f"Пролетели {distance} за {time} секунд")


class Dog:
    name = ''
    
    def __init__(self, name) -> None:
        self.name = name

    def say(self):
        print('Wooooooooooooooof!')

    def catch(self, something):
        print(f"Пес {self.name} поймал {something}")

class  DogoFly (Fly, Dog):
    def __init__(self, speed, name):
        super(Fly, self).__init__(speed)
        super(Fly, self).__init__(name)

    def say(self):
        # return super().say()
        pass

wonder = DogoFly(24, 'Adolf Hitler')
wonder.say()
wonder.fly(350)
wonder.catch('зигу')