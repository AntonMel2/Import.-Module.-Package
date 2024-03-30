from application import salary
from application.db import people
from time import sleep
from tqdm import tqdm
import datetime

dt_now = datetime.datetime.now()
print(dt_now)

for i in tqdm(range(100), ncols=80, ascii=True, desc='Total'):
    sleep(0.1)

if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()