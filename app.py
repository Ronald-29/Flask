from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Aquí podrías guardar los datos o enviar un correo
        return f"Gracias {name}, hemos recibido tu mensaje."
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
