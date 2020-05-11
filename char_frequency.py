from collections import Counter as cr
from datetime import datetime as dtm
import logging as lg
lg.basicConfig(level=lg.DEBUG)

start = dtm.now()

input_string = input("enter a string to calculate: ")

frequency_per_char = cr(input_string)
first_most_common_element = cr(frequency_per_char).most_common(1)
my_sorted = sorted(frequency_per_char)

lg.debug("Frequency is: " + str(frequency_per_char))
lg.debug(first_most_common_element)
lg.debug(my_sorted)
end = dtm.now()
lg.debug('Durata - {}'.format(end - start))
