def convert_base(numbers, base):
        multiplyer = 1
        total = 0
        for number in reversed(numbers):
                total += number * multiplyer
                multiplyer *= base
        return total


def minimum_seconds(sequence):
        unique_numbers = len(set(sequence))
        min_base = max(unique_numbers, 2)
        numbers = []
        mapping = {sequence[0]: 1}
        if len(sequence) == 1:
            return 1
        if unique_numbers == 1:
            return convert_base([1] * len(sequence), 2)

        next_symbol = [symbol for symbol in sequence if symbol != sequence[0]][0]

        mapping[next_symbol] = 0
        min_number = 2
        for symbol in sequence:
                if symbol not in mapping:
                        mapping[symbol] = min_number
                        min_number += 1
                        numbers.append(mapping[symbol])
                else:
                        numbers.append(mapping[symbol])
        return convert_base(numbers, min_base)


if __name__ == '__main__':
    print(minimum_seconds('cats'))
    print(minimum_seconds('11001001'))
    print(minimum_seconds('zig'))

    lines = []
    with open('python/A-small-practice.in') as f:
        for line in f:
            lines.append(line.strip())
    with open('python/A-small-practice.out', 'w+') as f:
        for i, line in enumerate(lines[1:]):
            f.write("Case #%s: %s\n" % (i + 1, str(minimum_seconds(line))))
