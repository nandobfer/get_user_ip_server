from flask import Flask, request, url_for, redirect, render_template, request
app = Flask(__name__)


def getData():
    with open('data.txt', 'r') as file:
        users = file.read().split('\n')
        file.close()
    return users


@app.route('/connect/', methods=['GET'])
def connect():
    global users
    user = request.args.get('user')
    data = (user, request.remote_addr)
    if not str(data) in users:
        users.append(data)
        with open('data.txt', 'a') as file:
            file.write(str(data)+'\n')
            file.close()
        users = getData()
        return str(data)
    else:
        return 'user already connected'


if __name__ == '__main__':
    users = getData()
    app.run(debug=True, host="0.0.0.0", port="5000")
