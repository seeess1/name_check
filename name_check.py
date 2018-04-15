"""
TODO:

How to output data as csv file?

How to load a csv file with multiple columns and only take names from
the first column?
"""

"""
You can use this program to check a list of names in a csv file
to make sure they are the names of people and not the names of
companies or other entities.

In its current form this program is only able to check a csv file that
has one column of full names. Names must either be in first name,
last name order or first, middle, then last name. It cannot check for names
that are ordered last name, then first name.

You will need to have a csv of names you want to check saved as "my_csv.csv"
within the same directory as this file.

The lists of common first and last names were compiled and published by
Quiet Affiliate Marketing at https://bit.ly/1AXeqFx.
"""

import re
import csv

"""
Create sets that will hold common first names, common last names, and the
names in your csv.
"""

temp_first_names = set()
first_names = set()
temp_last_names = set()
last_names = set()
temp_my_csv = set()
my_csv = set()

"""
Open all three csv files and add them to the sets just created.
"""

# Common first names csv
f = open('first_names.csv', 'rU')
reader1 = csv.reader(f, dialect=csv.excel_tab)
for name in reader1:
    temp_first_names.add(name[0])

for name in temp_first_names:
    name = name.lower()
    first_names.add(name)

# Common last names csv
f = open('last_names.csv', 'rU')
reader2 = csv.reader(f, dialect=csv.excel_tab)
for name in reader2:
    temp_last_names.add(name[0])

for name in temp_last_names:
    name = name.lower()
    last_names.add(name)

# Your csv
f = open('my_csv.csv', 'rU')
reader3 = csv.reader(f, dialect=csv.excel_tab)
for name in reader3:
    temp_my_csv.add(name[0])

for name in temp_my_csv:
    name = name.lower()
    my_csv.add(name)

"""
Name check function
"""
def name_check(contributor):
    # Check name for symbols
    str_contributor = str(contributor)
    str_no_space = str_contributor.replace(" ", "")
    if str_no_space.isalpha() == False:
        print(str_contributor + ": may be a company because " \
        "name contains symbols")
        return("")
        # Stop check b/c "&" or other characters suggests company, not person

    # Split name into first, middle, and last names
    contributor = re.split('\s+', str_contributor)
    if (len(contributor) < 2) or (len(contributor) > 3):
    	print(str_contributor + ": too many or too few names " \
        "- needs more research")
        return("")
        # Program is only equiped to check first, middle, and last names

    # Simple first and last name check
    elif len(contributor) == 2:
        first = contributor[0]
        last = contributor[1]
        if first not in first_names:
            print(str_contributor + ": may be a company because first name " \
            "is not commmon")
            return("")
        elif last not in last_names:
            print(str_contributor + ": may be a company because last name " \
            "is not common")
            return("")
        else:
            print(str_contributor + ": it's a person!")
            return("")

    # Check first, last, and middle names
    else:
        first = contributor[0]
        middle = contributor[1]
        last = contributor[2]
        if first not in first_names:
            print(str_contributor + ": may be a company because first name " \
            "is not common")
            return("")
        elif last not in last_names:
            print(str_contributor + ": may be a company because last name " \
            "is not common")
            return("")
        elif middle not in first_names and (len(middle) != 1):
            print(str_contributor + ": may be a company because middle name " \
            "is not common")
            return("")
        else:
            print(str_contributor + ": it's a person!")
            return("")

# Print the results to the terminal window
for name in my_csv:
    print(name_check(name))

exit(0)
