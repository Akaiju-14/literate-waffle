from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/toupper', methods=['GET', 'POST'])
def toupper():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('toupper.html', result=result)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/triangle', methods=['GET', 'POST'])
def triangle():
    result = None
    if request.method == 'POST':
        input_base = (request.form.get('inputBase', ''))
        input_height = (request.form.get('inputHeight', ''))
        result = (int(input_base)*int(input_height))/2
    return render_template('triangle.html', result=result)

@app.route('/circle', methods=['GET', 'POST'])
def circle():
    result = None
    if request.method == "POST":
        input_radius = (int(request.form.get('inputCircle', '')))
        result = (3.14)*(int(input_radius)**2)
    return render_template('circle.html', result=result)


if __name__ == "__main__":
    app.run(debug=True)
