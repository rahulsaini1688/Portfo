from flask import Flask, render_template, request, redirect
import csv
import random
app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/password',methods = ['POST','GET'])
def password():
	if request.method == "POST":
		length = int(request.form.get("length"))
		numbers_required = request.form.get("numbers")
		special_required = request.form.get("special_chars")
		
	return render_template('password.html',password= random_password_generator(length,numbers_required,special_required))


@app.route('/<string:page_name>')
def page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods = ['POST','GET'])
def submit():

	if request.method == "POST":
		
		submitted_data_dict = request.form.to_dict()
		write_to_csv(submitted_data_dict)

		return redirect('/thankyou.html')

	else:
		return 'something went wrong'

def write_to_txt(submitted_data_dict):
	with open("E:\Learning\Python\webserver\submitted_data.txt",'a') as database_text:
		email = submitted_data_dict['email']
		subject = submitted_data_dict['subject']
		message = submitted_data_dict['message']
		database_text.write(f'\n{email},{subject},{message}')
		

def write_to_csv(submitted_data_dict):
	try:
		with open("submitted_data.csv",newline = '',mode ='a') as database_csv:
			database_csv_writer = csv.writer(database_csv,delimiter =',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

			email = submitted_data_dict['email']
			subject = submitted_data_dict['subject']
			message = submitted_data_dict['message']
			database_csv_writer.writerow([email,subject,message])
			print("Data saved into database")
	except :
		print('Data not saved into database')

def random_password_generator(length,numbers_required,special_required):
	characters = list('abcdefghijklmnopqrstuvwxyz')
	numbers = list('0123456789')
	special = list('!@#$%^&*()')

	
	if numbers_required:
		characters.extend(numbers)
	if special_required:
		characters.extend(special)

	password = ''
	for x in range(length):
		password += random.choice(characters)

	return password



