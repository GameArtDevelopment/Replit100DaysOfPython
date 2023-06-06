from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def verification_form():
    if request.method == 'POST':
        name = request.form.get('name')
        color = request.form.get('color')
        animal = request.form.get('animal')

        # Perform the verification checks here
        if name and color == 'blue' and animal == 'lion':
            verification_status = 'Human verified!'
        else:
            verification_status = 'Failed to verify as human.'

        return render_template('result.html', status=verification_status)

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
