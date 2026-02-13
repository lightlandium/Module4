def eval_rpn(expression: str) -> float:
    """
    Вычисляет значение выражения в обратной польской записи.
    Токены разделяются пробелами. Поддерживаются операторы +, -, *, /.
    """
    stack = []
    operators = {'+', '-', '*', '/'}

    tokens = expression.split()

    for token in tokens:
        if token in operators:
            if len(stack) < 2:
                raise ValueError("Недостаточно операндов для оператора " + token)

            right = stack.pop()
            left = stack.pop()

            if token == '+':
                result = left + right
            elif token == '-':
                result = left - right
            elif token == '*':
                result = left * right
            elif token == '/':
                if right == 0:
                    raise ZeroDivisionError("Деление на ноль")
                result = left / right
            # Помещаем результат в стек
            stack.append(result)
        else:
            try:
                number = float(token)
                if number.is_integer():
                    number = int(number)
                stack.append(number)
            except ValueError:
                raise ValueError(f"Недопустимый токен: {token}")

    # После обработки всех токенов в стеке должен быть ровно один элемент
    if len(stack) != 1:
        raise ValueError("Некорректное выражение: в стеке осталось несколько значений")

    return stack[0]


if __name__ == "__main__":
    # Демонстрация на готовых примерах
    examples = [
        "3 4 +",          # 7
        "3 4 -",          # -1
        "3 4 *",          # 12
        "3 4 /",          # 0.75
        "4 2 * 3 +",      # 11 (4*2 + 3)
        "5 1 2 + 4 * + 3 -",  # (5 + ((1+2)*4)) - 3 = 14
    ]

    print("Проверка примеров:")
    for expr in examples:
        try:
            result = eval_rpn(expr)
            print(f"{expr} = {result}")
        except Exception as e:
            print(f"{expr} -> Ошибка: {e}")

    # Интерактивный ввод
    print("\nВведите выражение в обратной польской записи (токены через пробелы):")
    user_input = input("> ")
    try:
        res = eval_rpn(user_input)
        print(f"Результат: {res}")
    except Exception as e:
        print(f"Ошибка: {e}")