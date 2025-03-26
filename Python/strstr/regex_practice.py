import re


def search_email():
    lines = read_file('email.txt')
    pattern = '[.A-Za-z0-9]+@[.A-Za-z0-9]+'
    return use_regex(lines, [pattern])


def search_dates():
    lines = read_file('dates.txt')
    pattern1 = '[0-9]+\/[0-9]+\/[0-9]+'
    pattern2 = '[0-9]+-[0-9]+-[0-9]+'
    pattern3 = '[A-Za-z]+ [0-9]+, [0-9]+'
    return use_regex(lines, [pattern1, pattern2, pattern3])


def search_phones():
    lines = read_file('phones.txt')
    pattern = '(\(|\+|)([0-9]+)(\)|)(.)([0-9].+)'
    return use_regex(lines, [pattern])


def search_urls():
    lines = read_file('urls.txt')
    pattern = '(http|https|ftp)([^ ]+)'
    return use_regex(lines, [pattern])


def search_color_codes():
    lines = read_file('color_codes.txt')
    pattern = '(#)([A-Za-z0-9]+)'
    return use_regex(lines, [pattern])


def use_regex(lines, patterns):
    results = []
    for line in lines:
        for pattern in patterns:
            result = re.findall(pattern, line)
            if len(result) > 0:
                for r in result:
                    results.append(''.join(r))
    return results


def read_file(filename):
    lines = []
    with open(filename, 'r') as reader:
        for line in reader:
            line = line.strip()
            if line == "":
                continue
            lines.append(line)
    return lines
