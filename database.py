import sqlite3
import os

DB_FILE = os.path.join(os.path.dirname(__file__), 'ua_school.db')

def get_db():
    """Connect to SQLite database and return connection with row factory"""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize database tables with sample data"""
    conn = get_db()
    cursor = conn.cursor()

    # Table for Academic Programs / Courses
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS programs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT NOT NULL,
            title TEXT NOT NULL,
            campus TEXT NOT NULL,
            department TEXT NOT NULL,
            years TEXT NOT NULL,
            description TEXT NOT NULL
        )
    ''')

    # Table for Admission Applications
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS applicants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ref_number TEXT UNIQUE NOT NULL,
            fullname TEXT NOT NULL,
            email TEXT NOT NULL,
            contact TEXT NOT NULL,
            campus TEXT NOT NULL,
            course TEXT NOT NULL,
            prev_school TEXT NOT NULL,
            average TEXT NOT NULL,
            status TEXT DEFAULT 'Pending Review',
            remarks TEXT DEFAULT 'Application submitted. Waiting for exam schedule.'
        )
    ''')

    # Table for Announcements / News
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS announcements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            date_posted TEXT NOT NULL,
            category TEXT NOT NULL,
            content TEXT NOT NULL
        )
    ''')

    # Table for Inquiries / Contact
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inquiries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            subject TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')

    # Table for Enrolled Students (Student Portal / SIAS)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            fullname TEXT NOT NULL,
            course TEXT NOT NULL,
            campus TEXT NOT NULL,
            year_level TEXT NOT NULL,
            gwa TEXT NOT NULL
        )
    ''')

    # Table for Student Grades
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS student_grades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL,
            subject_code TEXT NOT NULL,
            subject_title TEXT NOT NULL,
            units INTEGER NOT NULL,
            grade TEXT NOT NULL,
            instructor TEXT NOT NULL
        )
    ''')

    # Populate default courses if empty
    cursor.execute('SELECT COUNT(*) FROM programs')
    if cursor.fetchone()[0] == 0:
        sample_programs = [
            ('BSIT', 'BS Information Technology', 'Lagangilang Campus', 'College of Computing Sciences', '4 Years', 'Focuses on software development, web systems, database design, and computer networking.'),
            ('BSA', 'BS Agriculture', 'Lagangilang Campus', 'College of Agriculture & Forestry', '4 Years', 'Prepares students in crop production, animal science, and sustainable modern farming in Abra.'),
            ('BSF', 'BS Forestry', 'Lagangilang Campus', 'College of Agriculture & Forestry', '4 Years', 'Focuses on forest management, biodiversity conservation, and Cordillera watershed protection.'),
            ('BSED', 'BS Secondary Education', 'Lagangilang Campus', 'College of Teacher Education', '4 Years', 'Trains future high school educators majoring in English, Mathematics, and Science.'),
            ('BSCE', 'BS Civil Engineering', 'Bangued Campus', 'College of Engineering & Technology', '4 Years', 'Specializes in structural engineering, road systems, and disaster-resilient building design.'),
            ('BSME', 'BS Mechanical Engineering', 'Bangued Campus', 'College of Engineering & Technology', '4 Years', 'Covers machine design, power generation, refrigeration, and manufacturing systems.'),
            ('BSEE', 'BS Electrical Engineering', 'Bangued Campus', 'College of Engineering & Technology', '4 Years', 'Focuses on electrical circuits, power plants, renewable energy, and motor controls.'),
            ('BIT', 'Bachelor of Industrial Technology', 'Bangued Campus', 'College of Engineering & Technology', '4 Years', 'Hands-on training in automotive diagnostics, electronics, and culinary management.'),
            ('BAT', 'Bachelor of Agricultural Technology', 'La Paz Campus', 'College of Agriculture', '4 Years', 'Practicum-oriented course focusing on seed production, nursery management, and agribusiness.')
        ]
        cursor.executemany('''
            INSERT INTO programs (code, title, campus, department, years, description)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', sample_programs)

    # Populate default announcements if empty
    cursor.execute('SELECT COUNT(*) FROM announcements')
    if cursor.fetchone()[0] == 0:
        sample_news = [
            ('Online Admissions for AY 2026-2027 Officially Open', 'Nov 15, 2026', 'Admissions', 'Incoming first-year college students and transferees may now submit their admission forms online. Free tuition is provided under RA 10931.'),
            ('University of Abra Achieves 100% Board Passing Rate', 'Nov 10, 2026', 'Academic', 'Congratulations to the graduates of the College of Agriculture and College of Engineering for garnering a 100% passing rate in the PRC board examinations.'),
            ('Smart Campus Upgrade and Library Extension Under RA 11574', 'Nov 05, 2026', 'Campus Update', 'The university administration announces ongoing facility improvements across Lagangilang, Bangued, and La Paz campuses.')
        ]
        cursor.executemany('''
            INSERT INTO announcements (title, date_posted, category, content)
            VALUES (?, ?, ?, ?)
        ''', sample_news)

    # Add sample applicants for easy testing
    cursor.execute('SELECT COUNT(*) FROM applicants')
    if cursor.fetchone()[0] == 0:
        sample_applicants = [
            ('UA-2026-101', 'Juan Dela Cruz', 'juan@gmail.com', '09171234567', 'Bangued Campus', 'BS Civil Engineering', 'Abra High School', '91.5', 'Qualified for Exam', 'Assigned testing room: Bangued Room 204. Date: Dec 5, 2026.'),
            ('UA-2026-102', 'Maria Santos', 'maria@gmail.com', '09289876543', 'Lagangilang Campus', 'BS Information Technology', 'Holy Spirit Academy', '93.0', 'Pending Review', 'Documents are currently being verified by the admissions office.')
        ]
        cursor.executemany('''
            INSERT INTO applicants (ref_number, fullname, email, contact, campus, course, prev_school, average, status, remarks)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', sample_applicants)

    # Add enrolled student demo for Student Portal
    cursor.execute('SELECT COUNT(*) FROM students')
    if cursor.fetchone()[0] == 0:
        cursor.execute('''
            INSERT INTO students (student_id, password, fullname, course, campus, year_level, gwa)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', ('2023-0145', 'student123', 'Maria Clarisse Santos', 'BS Information Technology (BSIT)', 'Lagangilang Main Campus', '3rd Year - 1st Semester', '1.38'))

        sample_grades = [
            ('2023-0145', 'IT 311', 'Web Systems & Technologies 2', 3, '1.25', 'Engr. D. Balolong'),
            ('2023-0145', 'IT 312', 'Database Systems Administration', 3, '1.50', 'Prof. M. Batoon'),
            ('2023-0145', 'IT 313', 'Information Assurance & Security', 3, '1.25', 'Instr. K. Valera'),
            ('2023-0145', 'IT 314', 'Mobile Application Development', 3, '1.50', 'Prof. J. Bringas'),
            ('2023-0145', 'GE 109', 'Life and Works of Jose Rizal', 3, '1.25', 'Dr. S. Bernardez')
        ]
        cursor.executemany('''
            INSERT INTO student_grades (student_id, subject_code, subject_title, units, grade, instructor)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', sample_grades)

    conn.commit()
    conn.close()
    print("Database initialized successfully!")

if __name__ == '__main__':
    init_db()
