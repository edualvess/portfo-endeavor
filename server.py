from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


# home page router function
@app.route('/')
def root():
    return render_template('index.html')


# page router function
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# csv file writing for persistent form data
def write_csv_file(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


# app collecting form data and submitting to file
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_csv_file(data)
        except:
            return 'Failed to save submitted form, please try again'

        return redirect('/thankyou.html')

    else:
        return "Unable to submit form data, please try again later"
