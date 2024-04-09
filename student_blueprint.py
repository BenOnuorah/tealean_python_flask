from flask import Blueprint, render_template, request

from database import connect_db
conn = connect_db()

student_bp=Blueprint("student_blueprint", __name__, static_folder="static", template_folder="templates")

#load form
@student_bp.route('/student') 
def student():
	return render_template('student.html')

#display record
@student_bp.route('/seestudents') 
def seestudents():
	 cursor = conn.cursor() 
	 cursor.execute('SELECT * FROM student')
	 data = cursor.fetchall()
	 return render_template('seestudents.html', students=data)
	 
	 
#process the student add
@student_bp.route('/addstudent', methods=['GET', 'POST']) 
def addstudent(): 
  if request.method == 'POST': 
    surname = request.form['surname'] 
    othernames = request.form['othernames'] 
    address = request.form['address'] 
    
    conn.execute('INSERT INTO student (surname_name,other_name,address_address) VALUES (?,?,?)',(surname, othernames, address)) 
    conn.commit() 
    output="Student record saved"
  return render_template('student.html', msg=output) 