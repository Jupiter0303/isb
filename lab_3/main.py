import argparse
from scenarios import Scenario


def main():
    """
        Главная функция программы. Реализует парсинг аргументов командной строки,
         на основе которых запускает тот или иной сюжет гибридного шифрования
        :return:
        """
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-gen', '--generation', help='Запуск режима генерации ключей', action='store_true')
    group.add_argument('-enc', '--encryption', help='Запуск режима шифрования', action='store_true')
    group.add_argument('-dec', '--decryption', help='Запуск режима дешифрования', action='store_true')

    args = parser.parse_args()
    status = False
    if args.generation:
        status = Scenario.generate_keys()
    elif args.encryption:
        status = Scenario.encrypt_data()
    elif args.decryption:
        status = Scenario.decrypt_data()
    else:
        print("Была выбрана неизвестная операция")

    if status:
        print("Операция успешно завершилась")
    else:
        print("Операция завершилась с ошибкой")

    return 0


if __name__ == '__main__':
    main()
