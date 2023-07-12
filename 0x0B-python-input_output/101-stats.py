#!/usr/bin/python3
import sys

def print_stats(total_size, status_codes):
    print("File size: {}".format(total_size))
    sorted_status_codes = sorted(status_codes.items())
    for code, count in sorted_status_codes:
        print("{}: {}".format(code, count))

total_size = 0
status_codes = {}

try:
    line_count = 0
    for line in sys.stdin:
        line_count += 1
        elements = line.split()
        if len(elements) >= 7:
            size = int(elements[-1])
            status_code = elements[-2]
            total_size += size
            status_codes[status_code] = status_codes.get(status_code, 0) + 1

        if line_count % 10 == 0:
            print_stats(total_size, status_codes)

except KeyboardInterrupt:
    print_stats(total_size, status_codes)
    raise
