import requests
from bs4 import BeautifulSoup
from fakeperson import Person

url = 'https://www.fakenamegenerator.com/gen-random-us-us.php'
headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36 OPR/67.0.3575.137"
    }
people = []

for i in range(10):
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, 'lxml')

    fullName = soup.find('h3').text
    firstName = fullName.split(' ')[0]
    LastName = fullName.split(' ')[2]
    middleIntial = fullName.split(' ')[1].split('.')[0]

    address = soup.find('div', {'class': 'adr'})
    address = str(address).split('<br/>')
    addressLine1 = address[0].split('>\n')[1].strip()
    city = address[1].split(',')[0]
    state = address[1].split(',')[1].strip().split(' ')[0]
    zip = address[1].split(',')[1].split(' ')[2]

    dd = soup.find_all('dd')
    maidenName = dd[0].text
    ssn = dd[1].text.split(' ')[0]
    latitude = dd[2].text.split(',')[0]
    longitude = dd[2].text.split(',')[1].strip()
    phoneNumber = dd[3].text
    countryCode = dd[4].text
    birthday = dd[5].text
    age = dd[6].text.split(' ')[0]
    zodiac = dd[7].text
    email = dd[8].text.split(' ')[0]
    username = dd[9].text
    password = dd[10].text
    website = dd[11].text
    useragent = dd[12].text
    mastercard = dd[13].text
    expires = dd[14].text
    cvc = dd[15].text
    company = dd[16].text
    occupation = dd[17].text
    height = dd[18].text
    weight = dd[19].text
    bloodType = dd[20].text
    upsTrackingNumber = dd[21].text
    westernUnionMTCN = dd[22].text
    moneyGramMTCN = dd[23].text
    people.append(Person(firstName, LastName, middleIntial, addressLine1, city, state, zip, maidenName, ssn, latitude, longitude, phoneNumber, countryCode, birthday, age, zodiac, email, username, password, website, useragent, mastercard, expires, cvc, company, occupation, height, weight, bloodType, upsTrackingNumber, westernUnionMTCN, moneyGramMTCN))

for person in people:
    print (person.firstName)