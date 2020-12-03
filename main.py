from flask import Flask, url_for
app = Flask(__name__)


@app.route('/')
def start():
    return '''<h3>Миссия Колонизация Марса</h3>'''

@app.route('/index')
def index():
    return '''И на Марсе будут яблони цвести!'''


@app.route('/promotion_image')
def promotion_image():
    style_file = url_for('static', filename='css/style.css')
    image_file = url_for('static', filename='img/mars.jpg')
    return ''' <!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
                    <link rel="stylesheet" type="text/css" href="{}" />
                    <title>Колонизация</title>
                </head>
                <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{}" alt="здесь должна была быть картинка, но не нашлась"><br>               
                    <div class="alert alert-success alert-dismissible">Человечество вырастает из детства.</div>
                    <div class="alert alert-primary">Человечеству мала одна планета.</div>
                    <div class="alert alert-warning"> Мы сделаем обитаемыми безжизненные пока планеты.</div>
                    <div class="alert alert-primary" role="alert">И начнем с Марса!</div>
                    <div class="alert alert-success">Присоединяйся!</div>
                </body>
                </html>'''.format(style_file, image_file)



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')