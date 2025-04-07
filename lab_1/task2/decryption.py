from constants import stats, IGNORE_CHAR, EXIT_COMMAND


def create_encrypted_alphabet(data: str) -> list:
    """
    создание алфавита из символов шифротекста
    :param data: исходные зашифрованные данные в виде строки
    :return: список отсортированный по убывающей частоте символа алфавита шифротекста
    """


    sorted_dict = dict()
    encrypted_alphabet = set(data)
    encrypted_alphabet.discard(IGNORE_CHAR)
    data_size = len(data)
    for x in encrypted_alphabet:
        sorted_dict[x] = data.count(x) / data_size
    sorted_dict = dict(sorted(sorted_dict.items(),
                              key=lambda item: item[1],
                              reverse=True)
                       )
    return list(sorted_dict.keys())


def swap(symbol1: str, symbol2: str, key: dict) -> dict:
    """
    обмениваем значения по ключам в словаре(ключу шифротекста)
    :param symbol1:  Первый символ, на который заменяли один символ шифротекста.
    :param symbol2: Второй символ, на который заменяли другой символ шифротекста
    :param key: словарь: ключи - символы шифротекста, значения - символы корректного текста
    :return: измененный ключ-словарь
    """
    swap_keys = list()
    for k in key:
        if key[k] in {symbol1,symbol2}:
            swap_keys.append(k)

        if len(swap_keys) == 2:
            break

    if len(swap_keys) < 2:
        raise ValueError("Ошибка в swap: не найдены все ключи для обмена значениями в словаре")

    key[swap_keys[0]],key[swap_keys[1]] = key[swap_keys[1]],key[swap_keys[0]]
    return key


def decoding(encrypted_data: str, key: dict) -> str:
    """
    создание расшифрованного по ключу шифротекста - конвертирование ключей словаря в значения по ним
    :param encrypted_data: зашифрованная строка
    :param key: словарь: ключи - символы шифротекста, значения - символы корректного текста
    :return: расшифрованная строка
    """
    decrypted_data = list()
    for char in encrypted_data:
        if char in key:
            decrypted_data.append(key[char])
        elif char == IGNORE_CHAR:
            decrypted_data.append(IGNORE_CHAR)
        else:
            raise KeyError(f"Символ {char} отсутствует в словаре key в функции decoding")

    return ''.join(decrypted_data)


def create_key(encrypted_text: str) -> dict:
    """
    создание словаря-ключа для дешифрования текста.
    Сначала используем частотный анализ и формируем словарь на соотношении частот
    алфавитов шифротекста и корректного. Далее вручную исправляем несостыковки
    :param encrypted_text: зашифрованная строка
    :return: ключ-словарь, который сформировали
    """
    encrypted_alphabet = create_encrypted_alphabet(encrypted_text)
    original_alphabet = list(stats.keys())
    print("Формирование ключа:")
    key = dict(zip(encrypted_alphabet,original_alphabet))

    while True:
        print(f"Текущий текст:\n {decoding(encrypted_text,key)}")
        print(f"Текущий ключ:\n {key}")

        choice = input(f"Завершить - {EXIT_COMMAND}, поменять символы по ключам - иначе: ").strip()

        if choice.lower() != 'exit':
            symbol1 = input("1-ый символ: ").strip()
            symbol2 = input("2-ой символ: ").strip()

            while not (symbol1 in original_alphabet and symbol2 in original_alphabet):
                print("Некорректно введенный символ, повторите снова.")
                symbol1 = input("1-ый символ: ").strip()
                symbol2 = input("2-ой символ: ").strip()

            try:
                key = swap(symbol1,symbol2,key)
            except ValueError as ex:
                print(ex)
        else:
            break

    return key

