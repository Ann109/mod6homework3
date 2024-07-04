class Horse:
    def __init__(self):
        self.x_distance = 0  #- пройденный путь.
        self.sound = 'frrr'  #- звук, который издаёт лошадь.
        super().__init__()
    def run(self, dx):
        self.x_distance += dx
        return self.x_distance


class Eagle:
    def __init__(self):
        self.y_distance = 0  #-высота полёта
        self.sound = 'I train, eat, sleep, and repeat'  #-звук, который издаёт орёл(отсылка)

    def fly(self, dy):  #где dy - изменение дистанции, увеличивает y_distance на dy.
        self.y_distance += dy
        return self.y_distance


class Pegasus(Horse, Eagle):
    def move(self, dx, dy):  #где dx и dy изменения дистанции. В этом методе должны запускаться наследованные методы run и fly соответственно.
        return (self.run(dx), self.fly(dy))
    def get_pos(self):  #возвращает текущее положение пегаса в виде кортежа - (x_distance, y_distance) в том же порядке.
        self.pos = (self.x_distance, self.y_distance)
        return self.pos
    def voice(self):  #- который печатает значение унаследованного атрибута sound.
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()