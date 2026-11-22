from flask import Flask, render_template, request, redirect, url_for, flash, session
import random
from database import get_db, init_db

app = Flask(__name__)
app.secret_key = 'ua-student-project-secret-key'

# Initialize database on startup
init_db()

# ---------------------------------------------
# 1. HOMEPAGE
# ---------------------------------------------
@app.route('/')
def index():
    conn = get_db()
    announcements = conn.execute('SELECT * FROM announcements ORDER BY id DESC LIMIT 3').fetchall()
    featured_courses = conn.execute('SELECT * FROM programs LIMIT 4').fetchall()
    conn.close()
    return render_template('index.html', announcements=announcements, courses=featured_courses)

# ---------------------------------------------
# 2. ABOUT PAGE (Vision, Mission, Core Values, History)
# ---------------------------------------------
@app.route('/about')
def about():
    return render_template('about.html')

# ---------------------------------------------
# 3. COURSES / ACADEMIC PROGRAMS
# ---------------------------------------------
@app.route('/courses')
def courses():
    campus_filter = request.args.get('campus', 'All')
    conn = get_db()
    
    if campus_filter != 'All':
        programs = conn.execute('SELECT * FROM programs WHERE campus LIKE ?', (f'%{campus_filter}%',)).fetchall()
    else:
        programs = conn.execute('SELECT * FROM programs').fetchall()
        
    conn.close()
    return render_template('courses.html', programs=programs, selected_campus=campus_filter)

# ---------------------------------------------
# 4. ONLINE ADMISSION APPLICATION
# ---------------------------------------------
@app.route('/apply', methods=['GET', 'POST'])
def apply():
    conn = get_db()
    
    if request.method == 'POST':
        fullname = request.form.get('fullname')
        email = request.form.get('email')
        contact = request.form.get('contact')
        campus = request.form.get('campus')
        course = request.form.get('course')
        prev_school = request.form.get('prev_school')
        average = request.form.get('average')

        # Simple random applicant reference number (e.g. UA-2026-482)
        random_id = random.randint(100, 999)
        ref_number = f"UA-2026-{random_id}"

        conn.execute('''
            INSERT INTO applicants (ref_number, fullname, email, contact, campus, course, prev_school, average, status, remarks)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'Pending Review', 'Application submitted. Documents under evaluation.')
        ''', (ref_number, fullname, email, contact, campus, course, prev_school, average))
        conn.commit()
        conn.close()

        flash('Your admission application has been successfully submitted!', 'success')
        return redirect(url_for('application_success', ref_number=ref_number))

    # For GET: load list of courses for the dropdown
    programs = conn.execute('SELECT title, campus FROM programs ORDER BY campus, title').fetchall()
    conn.close()
    return render_template('apply.html', programs=programs)

# ---------------------------------------------
# 5. APPLICATION SUCCESS / CONFIRMATION
# ---------------------------------------------
@app.route('/apply/success/<ref_number>')
def application_success(ref_number):
    conn = get_db()
    applicant = conn.execute('SELECT * FROM applicants WHERE ref_number = ?', (ref_number,)).fetchone()
    conn.close()
    if not applicant:
        flash('Applicant record not found.', 'danger')
        return redirect(url_for('apply'))
    return render_template('application_success.html', applicant=applicant)

# ---------------------------------------------
# 6. APPLICATION STATUS TRACKER
# ---------------------------------------------
@app.route('/status', methods=['GET', 'POST'])
def status():
    applicant = None
    searched = False
    
    if request.method == 'POST':
        ref_number = request.form.get('ref_number', '').strip()
        searched = True
        if ref_number:
            conn = get_db()
            applicant = conn.execute('SELECT * FROM applicants WHERE ref_number = ?', (ref_number,)).fetchone()
            conn.close()
            if not applicant:
                flash(f'No record found for Reference Number: {ref_number}', 'warning')

    return render_template('status.html', applicant=applicant, searched=searched)

# ---------------------------------------------
# 7. STUDENT PORTAL (SIAS - Enrolled Students)
# ---------------------------------------------
@app.route('/portal')
def portal():
    student_id = session.get('student_id')
    if not student_id:
        return render_template('portal_login.html')
    
    conn = get_db()
    student = conn.execute('SELECT * FROM students WHERE student_id = ?', (student_id,)).fetchone()
    grades = conn.execute('SELECT * FROM student_grades WHERE student_id = ?', (student_id,)).fetchall()
    conn.close()
    
    if not student:
        session.pop('student_id', None)
        return redirect(url_for('portal'))
        
    return render_template('portal.html', student=student, grades=grades)

@app.route('/portal/login', methods=['POST'])
def portal_login():
    student_id = request.form.get('student_id', '').strip()
    password = request.form.get('password', '').strip()

    conn = get_db()
    student = conn.execute('SELECT * FROM students WHERE student_id = ? AND password = ?', (student_id, password)).fetchone()
    conn.close()

    if student:
        session['student_id'] = student['student_id']
        flash(f'Welcome back, {student["fullname"]}!', 'success')
        return redirect(url_for('portal'))
    else:
        flash('Invalid Student ID or Password. (Demo account: 2023-0145 / student123)', 'danger')
        return redirect(url_for('portal'))

@app.route('/portal/demo')
def portal_demo():
    session['student_id'] = '2023-0145'
    flash('Logged in with Demo Student account (Maria Clarisse Santos)!', 'success')
    return redirect(url_for('portal'))

@app.route('/portal/logout')
def portal_logout():
    session.pop('student_id', None)
    flash('You have been logged out of the Student Portal.', 'success')
    return redirect(url_for('portal'))

# ---------------------------------------------
# 8. CAMPUS NEWS & ANNOUNCEMENTS
# ---------------------------------------------
@app.route('/news')
def news():
    conn = get_db()
    items = conn.execute('SELECT * FROM announcements ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('news.html', announcements=items)

# ---------------------------------------------
# 9. CONTACT US & DIRECTORY
# ---------------------------------------------
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        conn = get_db()
        conn.execute('INSERT INTO inquiries (name, email, subject, message) VALUES (?, ?, ?, ?)',
                     (name, email, subject, message))
        conn.commit()
        conn.close()

        flash('Thank you! Your message has been sent to the University of Abra.', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html')

# ---------------------------------------------
# 10. SIMPLE ADMIN PAGE (View / Update Applicants)
# ---------------------------------------------
@app.route('/admin')
def admin():
    conn = get_db()
    applicants = conn.execute('SELECT * FROM applicants ORDER BY id DESC').fetchall()
    inquiries = conn.execute('SELECT * FROM inquiries ORDER BY id DESC').fetchall()
    total_applicants = len(applicants)
    conn.close()
    return render_template('admin.html', applicants=applicants, inquiries=inquiries, total_applicants=total_applicants)

@app.route('/admin/update/<int:id>', methods=['POST'])
def admin_update(id):
    new_status = request.form.get('status')
    remarks = request.form.get('remarks')
    
    conn = get_db()
    conn.execute('UPDATE applicants SET status = ?, remarks = ? WHERE id = ?', (new_status, remarks, id))
    conn.commit()
    conn.close()
    
    flash('Applicant status updated successfully!', 'success')
    return redirect(url_for('admin'))

if __name__ == '__main__':
    print("==================================================")
    print("University of Abra (UA) School Website Enhancement")
    print("Running on http://127.0.0.1:5000")
    print("Student Portal: http://127.0.0.1:5000/portal")
    print("==================================================")
    app.run(debug=True, port=5000)
