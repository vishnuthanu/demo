from flask import Flask, request, make_response

app=Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def cookie():
    count = int(request.cookies.get('visi-count',0))
    count += 1
    message = 'We have visited this page' + str(count) + 'time'

    resp=make_response(message)
    resp.set_cookies('visit-count', str(count))
    return resp

    app.run()