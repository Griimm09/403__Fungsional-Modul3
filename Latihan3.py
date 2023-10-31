data = ['Hello', 3.1, 105, 'Python', 2.7, 737, 'world', 5.5, 'AI', 412]

nilai_float = list(filter(lambda x: isinstance(x, float), data))
nilai_int = list(filter(lambda x: isinstance(x, int), data))
nilai_string = list(filter(lambda x: isinstance(x, str), data))


def map_int(value):
    return {
        'ratusan': (value // 100) % 10,
        'puluhan': (value // 10) % 10,
        'satuan': value % 10
    }


int_mapped = list(map(map_int, nilai_int))

print("Data float:", nilai_float)
print("\nData Int:")
for value in int_mapped:
    print(value)

print("\nData String :")
print(nilai_string)
