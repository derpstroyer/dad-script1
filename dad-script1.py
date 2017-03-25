from bs4 import BeautifulSoup
import requests
import twilio
import time
import datetime

today = datetime.date.today()
while True:
    while today == datetime.date.today():
        url = "http://www.nasdaq.com/symbol/exls"

        r = requests.get(url)
        r.raise_for_status()

        soup = BeautifulSoup(r.text, 'html.parser')

        elem = soup.find('div', {'id':'qwidget_netchange'})
        elem_up = soup.find('div', {'class':'qwidget-cents qwidget-Green'})
        elem_dwn = soup.find('div', {'class':'qwidget-cents qwidget-Red'})

        if not elem_dwn:
            x = 0
            raw_num = elem.text
            if raw_num == 'unch':
                pass
            num = float(raw_num)
            while x == 0:
                if num > 0.005:
                    username = 'ACa0a692ebfb58c431597f503662481c20'  # account sid
                    password = 'ba8b3ee2ba0ba09646da1d97701cf777'  # auth token

                    num_to_txt = '+18606140816'
                    twilio_num = '+18607852138'

                    message_body = ('The EXL stock has raised by: ' + str(num))

                    base_url = 'https://api.twilio.com/2010-04-01/Accounts'
                    message_url = base_url + '/' + username + '/Messages'

                    auth_cred = (username, password)
                    post_data = {
                        "From": twilio_num,
                        "To": num_to_txt,
                        "Body": message_body,
                    }
                    r = requests.post(message_url, data=post_data, auth=auth_cred)
                    x = 1
                    while today == datetime.date.today():
                        time.sleep(1000)
                    if today != datetime.date.today():
                        today = datetime.date.today()
                        pass
                    pass

        else:
            x = 0
            raw_num = elem.text
            if raw_num == 'unch':
                pass
            else:
                num = float(raw_num)
            while x == 0:
                if num > 0.005:
                    username = 'ACa0a692ebfb58c431597f503662481c20'  # account sid
                    password = 'ba8b3ee2ba0ba09646da1d97701cf777'  # auth token

                    num_to_txt = '+18606140816'
                    twilio_num = '+18607852138'

                    message_body = ('The EXL stock has lowered by: ' + str(num))
                    print(message_body)

                    base_url = 'https://api.twilio.com/2010-04-01/Accounts'
                    message_url = base_url + '/' + username + '/Messages'

                    auth_cred = (username, password)
                    post_data = {
                        "From": twilio_num,
                        "To": num_to_txt,
                        "Body": message_body,
                    }
                    r = requests.post(message_url, data=post_data, auth=auth_cred)
                    x = 1
                    while today == datetime.date.today():
                        time.sleep(1000)
                    if today != datetime.date.today():
                        today = datetime.date.today()
                        pass
                    pass

                else:
                    time.sleep(1000)
                    pass
        pass
