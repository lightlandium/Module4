class MyDict:
    def __init__(self):
        self._keys = []
        self._values = []

    def _find_key(self, key):
        """Возвращает индекс ключа или -1, если ключ не найден."""
        try:
            return self._keys.index(key)
        except ValueError:
            return -1

    def __setitem__(self, key, value):
        idx = self._find_key(key)
        if idx != -1:
            self._values[idx] = value
        else:
            self._keys.append(key)
            self._values.append(value)

    def __getitem__(self, key):
        idx = self._find_key(key)
        if idx == -1:
            raise KeyError(key)
        return self._values[idx]

    def __delitem__(self, key):
        idx = self._find_key(key)
        if idx == -1:
            raise KeyError(key)
        del self._keys[idx]
        del self._values[idx]

    def __contains__(self, key):
        return self._find_key(key) != -1

    def keys(self):
        return self._keys.copy()

    def values(self):
        return self._values.copy()

    def items(self):
        return [(self._keys[i], self._values[i]) for i in range(len(self._keys))]

    def __str__(self):
        items = ', '.join(f"{repr(k)}: {repr(v)}" for k, v in self.items())
        return '{' + items + '}'


# Пример использования:
my_dict = MyDict()
my_dict['name'] = 'Alice'
my_dict['age'] = 30
print(my_dict['name'])  # Вернет 'Alice'
print('city' in my_dict)  # Вернет False
del my_dict['age']
print(my_dict.keys())  # Вернет ['name']
print(my_dict.values())  # Вернет ['Alice']