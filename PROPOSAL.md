# PROJECT PROPOSAL: ENHANCEMENT OF THE UNIVERSITY OF ABRA (UA) WEBSITE

**Student / Proponent:** [Your Name / Student ID]  
**Course & Year:** BS Information Technology / Computer Science  
**Subject:** Web Systems and Technologies  
**Target Website:** University of Abra (Formerly ASIST) — [https://asist.edu.ph/](https://asist.edu.ph/)  
**Legal Basis:** Republic Act No. 11574  
**Project Location:** `C:\Users\ASUS\.gemini\antigravity\scratch\ua_enhancement_website`  

---

## 1. PROJECT TITLE
**"UAbra Web Portal: An Enhanced, Mobile-Responsive School Website and Online Admission System for the University of Abra"**

---

## 2. BACKGROUND & REASON FOR CHOOSING THE UA WEBSITE
The **University of Abra (UA)**, formerly known as the *Abra State Institute of Sciences and Technology (ASIST)*, is the premier state university in Abra. Under **Republic Act No. 11574**, the institution was officially converted into a university, expanding its services across three campuses:
* **Lagangilang Main Campus:** Agriculture, Forestry, Computing Sciences, and Teacher Education.
* **Bangued Campus:** Civil, Electrical, and Mechanical Engineering, Industrial Technology, and Arts & Sciences.
* **La Paz Campus:** Agricultural Technology and Extension.

While the university has achieved university status, its official website ([asist.edu.ph](https://asist.edu.ph/)) still uses an older template that has several limitations for modern users.

---

## 3. PROBLEMS IDENTIFIED IN THE CURRENT WEBSITE (`asist.edu.ph`)
1. **Outdated Design & Layout:** The current site uses a dated layout with inconsistent colors that does not properly reflect its new identity as a state university.
2. **Poor Mobile Responsiveness:** Navigating courses and tables on smartphone screens is difficult, and elements often overflow or break.
3. **No Online Admission System:** Prospective high school graduates cannot apply online; they still have to visit the campus registrar or download manual forms.
4. **No Status Tracking:** Applicants have no digital way to check whether their entrance exam schedule has been released or if their application is approved.
5. **Disconnected Student Portal:** Links to the Student Information & Accounting System (SIAS) are broken or lead to external unstyled pages without easy mobile grade and clearance viewing.
6. **Difficult Course Browsing:** Courses offered across the three separate campuses (Lagangilang, Bangued, La Paz) are mixed together without simple campus filters.

---

## 4. PROPOSED ENHANCEMENTS & KEY FEATURES
To solve these problems, this project created an enhanced website with the following student-friendly features:

1. **Clean School Theme (Green & Gold):** Designed with the official colors of the University of Abra (Forest Green `#0d5c3a` and Gold `#f4c430`) with a clean, readable layout.
2. **Mobile-Friendly Navigation:** Clean responsive navigation bar that adapts smoothly to mobile phones, laptops, and tablets.
3. **Integrated Student Portal (SIAS):** A student self-service portal where enrolled students can log in to check their enrolled subjects, midterm grades, semestral GWA (Dean's List honors), online clearance status, and download their Certificate of Registration (COR).
4. **Online Admission Application:** An easy-to-use registration form where incoming students can submit their details, chosen campus, preferred course, and GPA.
5. **Automatic Reference Number Generation:** Immediately gives each applicant an official reference number (e.g., `UA-2026-101`) upon submission.
6. **Real-Time Application Status Tracker:** Students simply enter their reference number on the `/status` page to see if they are *Pending Review*, *Qualified for Exam*, or *Admitted*.
7. **Campus Course Filter:** A clean dropdown filter allowing students to easily see which courses belong to Lagangilang, Bangued, or La Paz.
8. **Free Higher Education (RA 10931) Notices:** Clear reminders for students that tuition is 100% free.
9. **Simple Evaluator/Admin Page:** A clean `/admin` page where teachers or admissions staff can see the list of applicants and update their status and remarks.

---

## 5. TOOLS AND TECHNOLOGIES USED
As instructed for this project:
* **Backend:** Python 3 with the **Flask framework** (`app.py`) for routing and form handling.
* **Database:** **SQLite** (`database.py` / `ua_school.db`) — lightweight, reliable, zero-configuration, and easy to explain.
* **Frontend:** Standard **HTML5** and custom **CSS3** (`style.css`), fully responsive without relying on heavy corporate frameworks.

---

## 6. PROJECT FILE STRUCTURE
```
ua_enhancement_website/
├── app.py                # Main Flask script with all web routes
├── database.py           # SQLite setup, tables, and sample data
├── PROPOSAL.md           # This proposal document
├── README.md             # Run instructions & Defense guide
├── static/
│   ├── css/
│   │   └── style.css     # Clean CSS with UA Green & Gold colors
│   └── images/
│       └── ua_logo.svg   # Official seal of the University of Abra
└── templates/
    ├── base.html         # Master layout (header, nav, footer)
    ├── index.html        # Homepage (hero banner, quick stats, featured courses)
    ├── about.html        # History of ASIST to UA, Vision, Mission, NEW ASIST values
    ├── courses.html      # Course list with campus filter dropdown
    ├── portal_login.html # Student Portal login screen
    ├── portal.html       # Enrolled student dashboard (grades, subjects, clearance, COR)
    ├── apply.html        # Online admission form
    ├── application_success.html # Confirmation & printable slip
    ├── status.html       # Search applicant status
    ├── news.html         # Campus news & announcements
    ├── contact.html      # Campus hotlines & message form
    └── admin.html        # Simple admin table to view/update applicants
```

---

## 7. ORAL DEFENSE / PRESENTATION CHEAT SHEET

When your professor asks you questions during your presentation, use these simple, direct answers:

* **"What is inside the Student Portal?"**  
  * *Answer:* "Sir/Ma'am, in the Student Portal (`/portal`), an enrolled student logs in to view their profile, currently enrolled subjects, units, instructors, midterm grades, and their semestral GWA. It also displays their online clearance status (Library, Cashier, Registrar) and allows them to download their Certificate of Registration (COR)."

* **"Why did you pick the University of Abra website?"**  
  * *Answer:* "Sir/Ma'am, the University of Abra was recently converted from ASIST under Republic Act No. 11574. Its current site (`asist.edu.ph`) lacks mobile responsiveness and has no online admission form, so I wanted to enhance it to help incoming students apply and check their status easily."

* **"Why did you use Python Flask?"**  
  * *Answer:* "Flask was one of the approved tools in our instructions. It is lightweight, beginner-friendly, and very straightforward for handling routes, HTTP GET/POST requests, and connecting forms to SQLite."

* **"How does your database work?"**  
  * *Answer:* "I used SQLite with Python's built-in `sqlite3` library in `database.py`. It has simple tables: `students` and `student_grades` for the portal, `programs` for courses, `applicants` for admissions, `announcements` for news, and `inquiries` for messages."

* **"How does the admission application work?"**  
  * *Answer:* "When the applicant fills out the form in `apply.html`, Flask receives the POST data in `app.py`. It generates a unique reference number (e.g., `UA-2026-101`), inserts the record into SQLite, and redirects to `application_success.html`. The student can then check their status on `status.html` anytime."
