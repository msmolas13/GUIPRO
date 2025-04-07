from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

cars = [
    {'id': 1, 'make': 'Toyota', 'model': 'GR Supra', 'year': 2025, 'price': '$56,900'},
    {'id': 2, 'make': 'Honda', 'model': 'Civic', 'year': 2025, 'price': '$28,750'},
    {'id': 3, 'make': 'Ford', 'model': 'Mustang', 'year': 2021, 'price': '$27,000'}
]

inquiries = []

@app.route('/')
def index():
    return render_template('index.html', cars=cars)

@app.route('/inventory')
def inventory():
    return render_template('inventory.html', cars=cars)

# ✅ Allow both GET and POST here
@app.route('/inquire', methods=['GET', 'POST'])
def inquire():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        car_id = int(request.form['car_id'])
        message = request.form['message']

        selected_car = next((car for car in cars if car['id'] == car_id), None)

        inquiries.append({
            'name': name,
            'email': email,
            'car': selected_car,
            'message': message
        })

        return redirect(url_for('inquiries_page'))

    return render_template('inquire.html', cars=cars)

@app.route('/inquiries')
def inquiries_page():
    return render_template('inquiries.html', inquiries=inquiries)

if __name__ == '__main__':
    app.run(debug=True)
