import collections
import sys


Statistics = collections.namedtuple("Statistics", "mean mode median std_dev")


def main():
    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        print("usage:{0}file1 [file2 [...fileN]]".format(sys.argv[0]))
        sys.exit()

    numbers = []
    frequencies = collections.defaultdict(int)
    for filename in sys.argv[1:]:
        read_data(filename, numbers, frequencies)
    if numbers:
        statistics = calculate_statistics(numbers, frequencies)
        print_results(len(numbers), statistics)
    else:
        print("no numbers found")


def read_data(filename, numbers, frequencies):
    for lino, line in enumerate(open(filename, encoding="ascii"), start=1):
        for x in line.split():
            try:
                number = float(x)
                numbers.append(number)
                frequencies[number] += 1
            except ValueError as err:
                print("{filename}:{lino}: skipping {x}: {err}".format(**locals()))


def calculate_mode(frequencies, maximum_modes):
    highest_frequency = max(frequencies.values())
    mode = [number for number, frequency in frequencies.items() if frequenciy == highest_frequency]
    if not(1 <= len(mode) <= maximum_modes):
        mode = None
    else:
        mode.sort()
    return mode
