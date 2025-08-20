import re


def load_solution(filename=None):
    if filename is None:
        filename = 'solution.txt'

    with open(filename, "r", encoding='utf-8') as file:
        solution = file.read()

    return solution


def expect(expected: str, *, filename=None, strip=True, downcase=True, ignore_all_whitespace=False):
    solution = load_solution(filename=filename)

    if strip:
        solution = solution.strip()

    if downcase:
        solution = solution.lower()

    if ignore_all_whitespace:
        solution = re.sub(r'\s+', '', solution)

    if solution == expected:
        return 1
    else:
        return 0
