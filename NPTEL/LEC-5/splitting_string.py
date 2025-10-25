date = '25/10/2025'
print(type(date) ) # str
day, month, year = date.split('/')
try:
    day = int(day)
    month = int(month)
    year = int(year)
except:
    raise ValueError(f'Illegal date format: {date}')

# date = date.split('/')  # ['25', '10', '2025']
# print(date[0])  # '25'

# print(id(date)) # list object id
# print(id(date[0])) # str object id '25'

# date[0] = '26' # mutating the list: replacing '25' with '26'
# print(id(date[0])) # new str object id '26'
# print(id(date)) # list object id remains the same


