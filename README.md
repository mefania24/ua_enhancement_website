# University of Abra (UA) School Website Enhancement

**Student Project Submission**  
Individual Project for Web Development / Web Systems and Technologies  
Reference Site: [https://asist.edu.ph/](https://asist.edu.ph/) (University of Abra, formerly ASIST)

---

## 💻 How to Run the Website

### Step 1: Open Terminal / Command Prompt
Open PowerShell or Command Prompt on your computer.

### Step 2: Navigate to Project Folder
```powershell
cd "C:\Users\ASUS\.gemini\antigravity\scratch\ua_enhancement_website"
```

### Step 3: Run Flask
```powershell
python app.py
```

### Step 4: Open in Your Browser
Go to:
**`http://127.0.0.1:5000`**

---

## 🎓 Where is the Student Portal?

The **Student Portal (SIAS)** is located right on the navigation bar or by going directly to:
👉 **`http://127.0.0.1:5000/portal`**

### How to Test / Demonstrate the Student Portal:
1. Go to `http://127.0.0.1:5000/portal`.
2. Click the yellow button: **"👉 1-Click Demo Login (Maria Santos - BSIT)"**  
   *(Or type Student ID: `2023-0145` and Password: `student123`).*
3. Once logged in, the portal displays:
   * **Student Profile:** Student ID, full name, year level, campus, and degree.
   * **Grades & Subjects:** Real table showing enrolled subjects (e.g. *Web Systems, Database, Mobile App Development*), grades, units, and instructors.
   * **Semestral GWA:** `1.38` (Dean's List honors).
   * **Tuition Balance:** `₱0.00` (Free Higher Education under RA 10931).
   * **Online Clearance:** Real-time clearance status from the Library, Cashier, Guidance, Dean, and Registrar.
   * **Printable Grade Slip:** A print button to print or save as PDF.
   * **Downloadable Forms:** Certificate of Registration (COR), TOR request form, and Student Handbook.

---

## 📌 Complete List of Pages to Show Your Professor

1. **Homepage (`/`)**  
   * Shows the official University of Abra branding (Green & Gold), hero banner, quick facts, featured courses, and campus news.
2. **About UA (`/about`)**  
   * Explains the conversion from ASIST to University of Abra under RA 11574, official Vision, Mission, and the **NEW ASIST** Core Values.
3. **Courses & Campuses (`/courses`)**  
   * Shows degree programs with an interactive dropdown to filter by **Lagangilang Main**, **Bangued**, or **La Paz** campus.
4. **Student Portal SIAS (`/portal`)**  
   * Enrolled student portal with grades, subjects, GWA, clearance, and COR.
5. **Online Admission Form (`/apply`)**  
   * Online application form that generates an official Reference Number (e.g. `UA-2026-101`) and printable confirmation slip.
6. **Check Application Status (`/status`)**  
   * Enter the reference number (test with `UA-2026-101` or `UA-2026-102`) to track evaluation and exam schedules.
7. **Admin View (`/admin`)**  
   * Admissions evaluator table where you can view student applications and change their status or remarks.
8. **Contact Us (`/contact`)**  
   * Shows campus addresses, contact hotlines, and a working inquiry form.

---

## 🗄️ Database Information

* File: `ua_school.db` (SQLite)
* Helper script: `database.py`
* Tables:
  * `students` (Student portal user accounts)
  * `student_grades` (Enrolled subjects and semestral grades)
  * `programs` (List of degrees, departments, campuses)
  * `applicants` (Submitted student admission forms and evaluation statuses)
  * `announcements` (Campus news bulletins)
  * `inquiries` (Messages sent from the Contact page)

---

## 📄 Proposal & Defense Notes
See [PROPOSAL.md](PROPOSAL.md) for the complete student proposal and the oral defense Q&A guide.
