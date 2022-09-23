import os


# check whether there is a ./data/ folder, if not, create one
def check_data_folder():
    if not os.path.exists('data'):
        os.makedirs('data')

# get today's date
def get_date():
    from datetime import date
    today = date.today()
    return today.strftime("%Y-%m-%d")

# read file data/{date}.txt, if there is no such file, create one with content 0
def read(date):
    try:
        with open('data/{0}.txt'.format(date), 'r') as f:
            return f.read()
    except FileNotFoundError:
        with open('data/{0}.txt'.format(date), 'w') as f:
            f.write('0')
        return '0'


def increment():
    date = get_date()
    num = read(date)
    num = int(num) + 1
    # write file to data/{date}.txt
    with open(f'data/{date}.txt', 'w') as f:
        f.write(str(num))
    return num
        

