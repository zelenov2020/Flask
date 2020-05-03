from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def start():
    return '''<h3>Миссия Колонизация Марса</h3>'''

@app.route('/index')
def index():
    return '''И на Марсе будут яблони цвести!'''

@app.route('/promotion')
def promotion():
    return '''<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
                <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script>
                <div class="container">Человечество вырастает из детства.</div>
                <div class="container">Человечеству мала одна планета.</div>
                <div class="container"> Мы сделаем обитаемыми безжизненные пока планеты.</div>
                <div class="container">И начнем с Марса!</div>
                <div class="container">Присоединяйся!</div>'''
@app.route('/image_mars')
def image_mars():
    return '''<h1>Жди нас, Марс!</h1>
                <img src="{}" alt="здесь должна была быть картинка, но не нашлась"><br>
                Вот она какая, красная планета!                
                '''.format(url_for('static', filename='img/mars.jpg'))

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')