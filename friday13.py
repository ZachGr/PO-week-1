import datetime
def has_friday_13(month, year):
    month = str(month)
    year = str(year)
    if datetime.datetime.strptime('13 '+' '+month+' '+year,'%d %m %Y').weekday()==4:
        print('True')
    else:
        print('False')


has_friday_13(3, 2020)

has_friday_13(10, 2017)

has_friday_13(1, 1985)