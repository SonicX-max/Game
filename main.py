from abc import ABC, abstractmethod


# Абстрактный класс Weapon
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def name(self):
        pass


# Класс меча (Sword)
class Sword(Weapon):
    def attack(self):
        return "удар мечом"

    def name(self):
        return "Меч"


# Класс лука (Bow)
class Bow(Weapon):
    def attack(self):
        return "выстрел из лука"

    def name(self):
        return "Лук"


# Класс для пользовательского оружия
class CustomWeapon(Weapon):
    def __init__(self, name, action):
        self._name = name
        self._action = action

    def attack(self):
        return f"{self._action}"

    def name(self):
        return self._name


# Класс бойца
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None  # Поле для хранения оружия

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {weapon.name()}.")

    def attack(self, monster):
        if self.weapon is None:
            print(f"{self.name} не вооружен!")
        else:
            print(f"{self.name} наносит {self.weapon.attack()}.")
            monster.take_damage()


# Класс монстра
class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self):
        self.health -= 1
        if self.health <= 0:
            print(f"{self.name} побежден!")
        else:
            print(f"У {self.name} осталось {self.health} жизней.")


# Функция выбора оружия
def choose_weapon(custom_weapons):
    print("Выберите оружие:")
    print("1. Меч")
    print("2. Лук")
    print("3. Добавить новое оружие")

    choice = input("Введите номер оружия: ")

    if choice == '1':
        return Sword()
    elif choice == '2':
        return Bow()
    elif choice == '3':
        new_weapon_name = input("Введите название нового оружия: ")
        new_weapon_action = input("Введите действие оружия: ")
        new_weapon = CustomWeapon(new_weapon_name, new_weapon_action)
        custom_weapons.append(new_weapon)
        print(f"Новое оружие '{new_weapon_name}' добавлено!")
        return new_weapon
    else:
        print("Неверный выбор, попробуйте снова.")
        return choose_weapon(custom_weapons)


# Основная функция для демонстрации игры
def main():
    # Создаем бойца и монстра
    fighter = Fighter("Боец")
    monster = Monster("Монстр", 1)  # Монстр с 1 жизнью
    custom_weapons = []  # Список для хранения пользовательских видов оружия

    # Выбор оружия для бойца
    weapon = choose_weapon(custom_weapons)
    fighter.change_weapon(weapon)

    # Демонстрация боя
    fighter.attack(monster)

    # Проверка: хотите ли вы поменять оружие и снова сразиться
    while True:
        choice = input("Хотите поменять оружие? (да/нет): ").strip().lower()
        if choice == 'да':
            weapon = choose_weapon(custom_weapons)
            fighter.change_weapon(weapon)
            monster = Monster("Монстр", 1)  # Создаем нового монстра
            fighter.attack(monster)
        elif choice == 'нет':
            print("Игра завершена.")
            break
        else:
            print("Неверный ввод, попробуйте снова.")


if __name__ == "__main__":
    main()

