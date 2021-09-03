import re


with open(input('File name: ')) as file:
    fr = file.read()
"""
> fr
3
  /\\
 /  \\
1
 ----
|    |
|    |
 ----
2
  ||
--||--
  ||
0
"""

# Separate the drawing fragments away from the numbers
regex_lego = r"[^0-9\n]+[^0-9]+" # Expression test-> regexr.com/64uqi
lego = re.findall(regex_lego, fr)

"""
> lego[0]
  /\\
 /  \\

> lego[1]
 ----
|    |
|    |
 ----

> lego[2]
  ||
--||--
  ||
"""

# Get those numbers
regex_order = r"[0-9]"
order = re.findall(regex_order, fr)
"""
> order
['3', '1', '2', '0']
"""

# zip order and lego together   -order_fragment = list(zip(order, lego))
order_lego = list(zip(order, lego))
"""
> order_lego[0]
('3', /\\
     /  \\ )

> order_lego[1]
('1', ----
     |    |
     |    |
      ---- )

> order_lego[2]
('2',  ||
     --||--
       || )
"""

# Function that returns the first value of the list/tuple/iterable
def first_index(lst):
  return lst[0]

# Sort order_lego by first value
ordered_lego = sorted(order_lego,
                      key=first_index)
"""
> ordered_lego[0]
('1', ----
     |    |
     |    |
      ---- )


> ordered_lego[1]
('2',  ||
     --||--
       || )

> ordered_lego[2]

('3', /\\
     /  \\ )
"""

# Join the drawing fragments into 1 string
print_list = []
for order_num, drawing in ordered_lego:
  print_list.append(drawing)
  
print_string = "".join(print_list)
"""
> print_string
 ----
|    |
|    |
 ----
  ||
--||--
  ||
  /\\
 /  \\
"""


# Print the drawing
print(print_string)
"""
 ----
|    |
|    |
 ----
  ||
--||--
  ||
  /\\
 /  \\
"""
