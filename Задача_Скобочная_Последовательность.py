def is_valid_bracket_sequence(s: str) -> bool:
    """
    Проверяет, является ли строка правильной скобочной последовательностью.
    Использует стек.
    """
    # Словарь соответствий
    matching = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in s:
        if char in matching:  # это закрывающая скобка
            if not stack:     # стек пуст — закрывать нечего
                return False
            top = stack.pop()
            if top != matching[char]:
                return False
        else:                 # иначе это открывающая скобка
            stack.append(char)

    # Если после обработки всех символов стек пуст — всё верно
    return not stack

if __name__ == "__main__":
    tests = [
        "([]{})",   # True
        "([)]",     # False
        "{[}",      # False
        "()",       # True
        "",         # True (пустая строка считается корректной)
        "[",        # False
        "]"         # False
    ]

    print("Проверка примеров:")
    for test in tests:
        print(f"{test!r}: {is_valid_bracket_sequence(test)}")

    user_input = input("Введите свою скобочную последовательность: ")
    result = is_valid_bracket_sequence(user_input)
    print(f"Результат: {result}")