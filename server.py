from flask import Flask,render_template,request,redirect
import csv

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:pagename>')
def about(pagename):
    return render_template(pagename)    

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_myform():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)  # (or) write_to_file(data)
            return redirect('thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'Something went wrong. Try later...'

def write_to_file(data):
    with open('database.txt', mode='a') as myfile:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = myfile.write(f'\n{email}  {subject}  {message}')

def write_to_csv(data):
    with open('database.csv','a', newline='') as myfile2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(myfile2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])