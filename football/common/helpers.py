from datetime import datetime


def format_date(date):
    arr = date.split('/')
    match_date = date
    if len(arr[2]) == 2:
        match_year = '20' + date[-2:]
        match_date = date[:-2] + match_year

    return datetime.strptime(match_date, '%d/%m/%Y').strftime('%Y-%m-%d')
