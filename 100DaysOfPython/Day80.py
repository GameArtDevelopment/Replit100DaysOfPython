from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Retrieve the values from the form
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Perform your login logic here (e.g., check if the username, email, and password are valid)

        # Return a success message or redirect to another page
        return 'Login successful!'
    
    # Render the login template for GET requests
    return render_template('Day80.html')

if __name__ == '__main__':
    app.run()
