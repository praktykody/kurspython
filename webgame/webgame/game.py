# zdefiniuj klasę:
class Creatures:
    # konstruktor - domyślne właściwości przy tworzeniu obiektu
    def __init__(self,name):
        self.name = name
        self.id = 1
        self.position = [34,-10,0]
        self.direction = 1
        self.health = 100
        self.maxHealth = 150
        self.sprite = "male_citizen"
        self.type = "player"
        self.text = "siema z django2"
    # odświeżanie postaci, za każdym zapytaniem od klienta (przeglądarki)
    def update(self,controls):
        # drukowanie wciśniętych przycisków
        # print(controls)
        # jeśli kliknięta strzałka w prawo, dodaj pozycję i zmień kierunek
        if(39 in controls):
            self.position[0] += 1
            self.direction = 2
        if(37 in controls):
            self.position[0] -= 1
            self.direction = 3

# lista zawierająca instancje klasy Creatures
creatureList = []
# lista zwierająca dict'y stworzone z instancji Creatures (wysyłane do klienta)
creatureListJSON = []

import json
# funkcja wykonująca się za każdym zapytaniem klienta (przeglądarki)
def manage(request):
    # dane od klienta (nazwa, kliknięte przyciski etc.)
    data = json.loads(request.GET.get('data',''))
    # sprawdź, czy player jest na liście
    isPlayer = False
    for creature in creatureList:
        if data["name"] == creature.name:
            # jeśli jest, wykonaj metodę update 
            # (odśwież playera za każdym zapytaniem z przeglądarki)
            creature.update(data["controls"])
            isPlayer = True
    # jeżeli nie ma takiego playera - dodaj go: 
    if(not isPlayer):
        # stwórz playera z klasy  Creatures
        player = Creatures(data["name"])
        # dodaj go do listy postaci (instancji obiektów)
        creatureList.append(player)
        # dodaj go do listy dict'ów - do informacji wysyłanych do klienta
        creatureListJSON.append(player.__dict__)
    # zwróć listę wysyłaną do klienta
    return creatureListJSON