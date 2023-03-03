from flask import Flask, render_template, url_for, redirect
import requests, json

app = Flask(__name__)

session_id = ""

headers = {
    'accept': 'application/json', 
    'Content-Type': 'application/x-www-form-urlencoded',
}

login_obj = {
    'username': 'nestjs_ts',
    'password': '835374Tejesh',
    'verification_code': '',
    'proxy': '',
    'locale': '',
    'timezone': ''
}

login_url = 'http://139.59.67.152:8000/auth/login'

@app.route('/likes')
def like():
    global session_id
    media_obj = {
        'sessionid':session_id,
        'pk':'3026938334093871756',
        'use_cache':'false'
    }

    media_url = "http://139.59.67.152:8000/media/info"

    x = requests.post(media_url, data = media_obj, headers = headers)
    print(x.status_code, x.text)
    if(x.status_code == 200):
        try:
            data = json.loads(str(x.text))
            print(data['like_count'])
            return str(data['like_count'])
        except:
            print("json file is missing")
            return "json file is missing"

    else:
        print("Session closed. Re-logging in")
        x = requests.post(login_url, data = login_obj, headers = headers)
        print(x.text)
        if(x.status_code == 200):
            session_id = x.text
            print("Successfully logged in")

            return redirect(url_for('like'))
        else:
            print("Error at logging in")
            return "Error at logging in"

if __name__ == '__main__':
    # x = requests.post(login_url, data = login_obj, headers = headers)
    # print(x.text)
    # if(x.status_code == 200):
    #     session_id = x.text
    #     print("Successfully logged in")

    # else:
    #     print("Error at logging in")

    app.run('0.0.0.0', port=5000)
