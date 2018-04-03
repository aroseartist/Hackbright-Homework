"""
Prints out all the melons in our inventory
"""

from melons import melons


def print_melon_info(melon_file):

    for melon, details in melon_data.items():
        print melon.upper()

    for melon_keys, melon_values in melon_data.items():
        print "%s: %d" % (melon_keys, melon_values)

print_melon_info(melons)
