#Создайте класс машина, и несколько экземпляров данного класса с разными атрибутами. Код разметите в гит репозитории и ссылочку мне на него.
class Car:
    wheel = 4
    color = 'green'
    doors = 4
Peugeot = Car()
Peugeot.fogLights = 2
Peugeot.multimediaOld = 1
Lexus = Car()
Lexus.type = 'Сrossover' # седан, универсал, кроссовер, внедорожник и т.д.
Lexus.hoist = 2          # лебёдка
BMW = Car()
BMW.motor = '300 hp'     # 300 лошадиных сил
BMW.antifly = 1          # Антикрыло открывается на скорости

print(Peugeot.color, Peugeot.fogLights, Peugeot.multimediaOld)
print(Lexus.type, Lexus.hoist)
print(BMW.motor, BMW.antifly)