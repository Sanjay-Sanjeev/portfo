from flask import Flask, render_template,request, url_for, redirect #render_template allows to render html files passed
import csv
app = Flask(__name__) #__name__ returns main as this is the main function


@app.route("/")
def my_home():
    return  render_template('index.html')

@app.route('/<string:pagename>')
def dynamic_page(pagename):
    return  render_template(pagename)

def write_to_text(data):
    with open('./webserver/database.txt', mode='a') as my_file:
        email = data['email']
        subject = data['subject']
        message = data['message']
        print(email + "," + subject + "," + message + "\n")
        text = my_file.write(email + "," + subject + "," + message + "\n")

def write_to_csv(data):
    with open('./webserver/database.csv', mode='a', newline='') as my_file_csv:
        email = data['email']
        subject = data['subject']
        message = data['message']
        print(email + "," + subject + "," + message + "\n")
        csv_out = csv.writer(my_file_csv, delimiter=',' , quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_out.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            #write_to_text(data)
            write_to_csv(data)
        except:
            return 'Something went wrong!'
        return redirect('/thankyou.html')
    else:
        return 'something wrong'





#python -m venv webserver
#webserver\Scripts\activate
#set FLASK_APP=server
#set FLASK_ENV=development

#pip freeze > requirements.txt #to get the installed packages in the venv
