import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_padding(cell, top=120, bottom=120, left=180, right=180):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def create_document():
    doc = docx.Document()

    # Page setup - 0.75 in margins
    for section in doc.sections:
        section.top_margin = Inches(0.75)
        section.bottom_margin = Inches(0.75)
        section.left_margin = Inches(0.75)
        section.right_margin = Inches(0.75)
        
        # Header & Footer
        header = section.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("University of Abra (UA) • System Documentation & Enhancement Manual")
        hrun.font.name = "Calibri"
        hrun.font.size = Pt(8.5)
        hrun.font.italic = True
        hrun.font.color.rgb = RGBColor(120, 120, 120)

        footer = section.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        frun = fp.add_run("Republic Act No. 11574 | Web Systems and Technologies | Final Project")
        frun.font.name = "Calibri"
        frun.font.size = Pt(8.5)
        frun.font.color.rgb = RGBColor(140, 140, 140)

    # Styles & Colors
    GREEN = RGBColor(13, 92, 58)      # #0D5C3A
    GOLD = RGBColor(190, 140, 20)     # #BE8C14
    DARK = RGBColor(40, 44, 52)       # #282C34
    GRAY = RGBColor(90, 95, 105)

    # ----------------------------------------------------
    # COVER / HEADER TITLE
    # ----------------------------------------------------
    title_p = doc.add_paragraph()
    title_p.paragraph_format.space_before = Pt(10)
    title_p.paragraph_format.space_after = Pt(4)
    run_inst = title_p.add_run("UNIVERSITY OF ABRA\n")
    run_inst.font.name = "Calibri"
    run_inst.font.size = Pt(22)
    run_inst.font.bold = True
    run_inst.font.color.rgb = GREEN

    run_sub = title_p.add_run("OFFICIAL WEB SYSTEM ENHANCEMENT & MODERNIZATION PROJECT\n")
    run_sub.font.name = "Calibri"
    run_sub.font.size = Pt(13)
    run_sub.font.bold = True
    run_sub.font.color.rgb = GOLD

    run_charter = title_p.add_run("Converting ASIST to University of Abra under Republic Act No. 11574")
    run_charter.font.name = "Calibri"
    run_charter.font.size = Pt(10)
    run_charter.font.italic = True
    run_charter.font.color.rgb = GRAY

    # Metadata Table
    meta_table = doc.add_table(rows=5, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_table.autofit = False

    meta_data = [
        ("Subject / Course:", "Web Systems and Technologies"),
        ("Project Scope:", "Comprehensive School Website Enhancement & Full System Modernization"),
        ("Original Live Site:", "https://asist.edu.ph/ (Abra State Institute of Sciences and Technology)"),
        ("Governing Mandate:", "Republic Act No. 11574 (Charter of the University of Abra)"),
        ("Technology Stack:", "Python 3 (Flask Framework) + SQLite3 Relational Database + HTML5 / CSS3 / JS")
    ]

    for i, (label, val) in enumerate(meta_data):
        row = meta_table.rows[i]
        
        c0 = row.cells[0]
        c0.width = Inches(1.8)
        set_cell_background(c0, "0D5C3A")
        set_cell_padding(c0, 60, 60, 100, 100)
        p0 = c0.paragraphs[0]
        p0.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r0 = p0.add_run(label)
        r0.font.name = "Calibri"
        r0.font.size = Pt(9.5)
        r0.font.bold = True
        r0.font.color.rgb = RGBColor(255, 255, 255)

        c1 = row.cells[1]
        c1.width = Inches(5.2)
        set_cell_background(c1, "F4F8F5" if i % 2 == 0 else "FFFFFF")
        set_cell_padding(c1, 60, 60, 120, 120)
        p1 = c1.paragraphs[0]
        r1 = p1.add_run(val)
        r1.font.name = "Calibri"
        r1.font.size = Pt(9.5)
        r1.font.color.rgb = DARK

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # ----------------------------------------------------
    # SECTION 1: EXECUTIVE SUMMARY
    # ----------------------------------------------------
    h1 = doc.add_heading(level=1)
    r = h1.add_run("1. Executive Summary & Purpose of Enhancement")
    r.font.name = "Calibri"
    r.font.color.rgb = GREEN

    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_after = Pt(6)
    p.add_run(
        "The University of Abra (UA), originally established as the Abra State Institute of Sciences and Technology (ASIST), "
        "is the sole state higher education institution in the province of Abra, officially converted into a university under "
        "Republic Act No. 11574. Despite its vital educational mandate across its three campuses (Lagangilang Main, Bangued, and La Paz), "
        "the institution's legacy website (asist.edu.ph) suffered from critical technical deficiencies:\n"
    )

    bullets = [
        ("Outdated & Broken Mobile Responsiveness: ", "The legacy website utilizes fixed-width tables and legacy CSS that break completely on mobile devices and tablets."),
        ("Zero Online Admission Capabilities: ", "Prospective students had to travel in person to the registrar in Abra or download manual paper PDF forms, resulting in heavy logistical friction."),
        ("No Application Status Tracking: ", "Applicants had no digital mechanism to track their evaluation status, entrance examination schedules, or test room assignments."),
        ("Broken Student Information System (SIAS) Links: ", "Portal navigation led to broken external links or unencrypted raw IP addresses that discouraged student usage."),
        ("Unstructured Course Directory: ", "Programs across all three campuses were lumped into static lists without filtering, making it confusing to identify campus program locations.")
    ]
    for b_title, b_desc in bullets:
        bp = doc.add_paragraph(style='List Bullet')
        bp.paragraph_format.space_after = Pt(3)
        bp.paragraph_format.line_spacing = 1.15
        r_bt = bp.add_run(b_title)
        r_bt.font.name = "Calibri"
        r_bt.font.bold = True
        r_bt.font.color.rgb = GREEN
        r_bd = bp.add_run(b_desc)
        r_bd.font.name = "Calibri"

    p2 = doc.add_paragraph()
    p2.paragraph_format.line_spacing = 1.15
    p2.paragraph_format.space_before = Pt(4)
    p2.paragraph_format.space_after = Pt(12)
    p2.add_run(
        "This project delivers an end-to-end, modern, secure, and mobile-responsive web portal built with Python (Flask) and SQLite3, "
        "incorporating the official University Forest Green (#0D5C3A) and Gold (#F4C430) visual identity, a self-service admission application workflow, "
        "a live reference status tracker, a functional student academic dashboard with GWA calculation, and an administrative evaluator console."
    )

    # ----------------------------------------------------
    # SECTION 2: PAGE-BY-PAGE DOCUMENTATION
    # ----------------------------------------------------
    h2 = doc.add_heading(level=1)
    r2 = h2.add_run("2. Comprehensive Page-by-Page Documentation & Enhancements")
    r2.font.name = "Calibri"
    r2.font.color.rgb = GREEN

    pages = [
        {
            "num": 1,
            "title": "Homepage (Central University Gateway)",
            "route": "http://127.0.0.1:5000/",
            "template": "templates/index.html",
            "method": "GET",
            "controller": "index() in app.py",
            "db": "announcements, programs",
            "image": "screenshots/01_homepage.png",
            "about": (
                "The Homepage is the primary digital front-door of the University of Abra. It introduces prospective students, "
                "enrolled scholars, faculty, alumni, and community stakeholders to the university. The page features the official "
                "university header bar with the UA vector seal, a Republic Act No. 11574 announcement strip, an engaging hero banner "
                "with immediate call-to-action buttons, key institutional statistic callouts (3 campuses, ₱0 tuition under RA 10931, "
                "and board passing rates), a preview of featured academic programs, and a live campus news feed."
            ),
            "limitations": (
                "The original live website (asist.edu.ph) featured a dated, cluttered layout with low-contrast typography, fixed-width "
                "desktop tables that overflowed screens on smartphones, and no visual hierarchy. Vital institutional announcements and "
                "admission deadlines were buried deep in obscure menus without clear action buttons to guide users."
            ),
            "enhancements": [
                "Official Institutional Branding: Designed with official Forest Green (#0D5C3A) and Gold (#F4C430) theme, official vector seal, and RA 11574 banner.",
                "Action-Driven Hero Banner: Implemented prominent direct-action buttons: 'Apply Online', 'Explore Courses', and 'Check Status'.",
                "High-Visibility Institutional Statistics: Prominently highlights key university milestones: 3 Campuses (Lagangilang, Bangued, La Paz), 100% Free Tuition guarantee (RA 10931), and top licensure board passing records.",
                "Dynamic Featured Programs: Directly queries the SQLite database to showcase premier degree offerings with one-click direct application links.",
                "Real-Time Announcements Stream: Displays the latest official notices and academic calendar reminders dynamically from the announcements table.",
                "Fluid Mobile Responsiveness: Uses CSS Grid and Flexbox to guarantee an optimal reading experience across smartphones, tablets, laptops, and desktop displays."
            ]
        },
        {
            "num": 2,
            "title": "About the University (History, Campuses & Values)",
            "route": "http://127.0.0.1:5000/about",
            "template": "templates/about.html",
            "method": "GET",
            "controller": "about() in app.py",
            "db": "Static / Institutional Charter Reference",
            "image": "screenshots/02_about_page.png",
            "about": (
                "The About page serves as the official institutional profile of the University of Abra. It documents the historical "
                "transition from ASIST to university status under Republic Act No. 11574, provides an authoritative role breakdown of the "
                "three campuses, articulates the university's Vision and Mission statements, and presents the official NEW ASIST core values."
            ),
            "limitations": (
                "On the original website, historical documents were fragmented across broken links and downloadable PDFs. Institutional "
                "vision and core values were buried in dense, unformatted paragraphs without clear distinction between the specialized roles "
                "of the Lagangilang Main, Bangued, and La Paz campuses."
            ),
            "enhancements": [
                "Statutory Transition Overview: Prominently details the legislative conversion from ASIST to the University of Abra under Republic Act No. 11574.",
                "Multi-Campus Structural Delineation: Clearly outlines the distinct academic thrust of each campus:\n  • Lagangilang Main: Administrative seat, Smart Agriculture, Forestry, Teacher Education, and Computing Sciences.\n  • Bangued Campus: Urban engineering and technology powerhouse (Civil, Mechanical, Electrical Engineering, and BIT).\n  • La Paz Campus: Agro-industrial technology, extension farm laboratories, and rural community training.",
                "Styled Vision & Mission Callouts: High-contrast callout containers with green accent borders for maximum readability and prestige.",
                "Interactive NEW ASIST Core Values Grid: An 8-pillar visual grid detailing Nobility, Entrepreneurship, Wisdom, Action, Sincerity, Integrity, Service, and Teamwork."
            ]
        },
        {
            "num": 3,
            "title": "Courses & Academic Programs Catalog",
            "route": "http://127.0.0.1:5000/courses",
            "template": "templates/courses.html",
            "method": "GET",
            "controller": "courses() in app.py",
            "db": "programs table (SELECT * FROM programs)",
            "image": "screenshots/03_courses_catalog.png",
            "about": (
                "The Courses & Programs Catalog provides an exhaustive, centralized directory of all undergraduate and technical degree "
                "programs offered by the University of Abra. Each program card clearly specifies the course code, full degree title, "
                "administering college/department, duration (4 Years), campus location, and tuition-free coverage."
            ),
            "limitations": (
                "The legacy website presented academic offerings in static, unstyled HTML tables where degrees across all three campuses "
                "were lumped together without campus filtering, leaving prospective students confused about where specific programs were located."
            ),
            "enhancements": [
                "Modern Card-Based Grid: Replaced cramped tabular listings with responsive course cards highlighting course codes (BSIT, BSA, BSCE, BSED, etc.).",
                "Campus Badges: Distinct colored badges indicate whether the program is offered at Lagangilang Main, Bangued, or La Paz.",
                "Republic Act No. 10931 Zero-Tuition Guarantee: Prominently badges all qualified undergraduate programs as 100% Free Tuition.",
                "Integrated 'Apply Online' CTA: Direct button on every card linking directly into the online admission form with program intent."
            ]
        },
        {
            "num": 4,
            "title": "Courses Filtered by Campus (Interactive Filtering)",
            "route": "http://127.0.0.1:5000/courses?campus=Bangued",
            "template": "templates/courses.html",
            "method": "GET (with query parameter)",
            "controller": "courses() in app.py",
            "db": "programs table (SELECT * FROM programs WHERE campus LIKE ?)",
            "image": "screenshots/04_courses_filtered_bangued.png",
            "about": (
                "Demonstrates the dynamic campus filtering capability in action. When a prospective student selects a specific campus "
                "(e.g., 'Bangued Campus') from the dropdown selector, the system immediately filters the catalog to display only programs "
                "hosted at that campus."
            ),
            "limitations": (
                "The original website had zero dynamic filtering capability. Users had to manually read through pages of text or cross-check "
                "unorganized PDF brochures to determine program locations."
            ),
            "enhancements": [
                "Dynamic Server-Side Query Execution: Selecting a campus sends a clean URL query (?campus=Bangued) executing parameterized SQL in SQLite.",
                "Instant Visual Refinement: Immediately isolates Bangued-specific programs such as BS Civil Engineering, BS Mechanical Engineering, BS Electrical Engineering, and Bachelor of Industrial Technology.",
                "Filter State Persistence: The dropdown menu automatically preserves the selected option so the user retains browsing context."
            ]
        },
        {
            "num": 5,
            "title": "Online Admission Application Form",
            "route": "http://127.0.0.1:5000/apply",
            "template": "templates/apply.html",
            "method": "GET, POST",
            "controller": "apply() in app.py",
            "db": "programs (for dropdown) and applicants (INSERT)",
            "image": "screenshots/05_online_admission_form.png",
            "about": (
                "A 100% paperless digital admission application portal for senior high school graduates and transfer students. "
                "Applicants can select their preferred campus and degree program, enter their personal and contact information, "
                "declare their previous school attended, and submit their general average (GPA) online."
            ),
            "limitations": (
                "The live website asist.edu.ph completely lacked an online admission system. Applicants were forced to travel physically "
                "to the registrar's office in Lagangilang or Bangued, leading to high transportation costs, manual encoding errors, "
                "long queues, and barriers for applicants living in remote Abra municipalities or other provinces."
            ),
            "enhancements": [
                "100% Paperless Online Registration: Accessible anytime, anywhere from mobile phones, tablets, or computers.",
                "Structured Validation Fields: Captures complete legal name, valid email, mobile number, campus choice, program choice, school attended, and GPA average.",
                "Dynamic Database-Populated Program Dropdown: The program selection options are dynamically queried from the programs table, preventing invalid selections.",
                "Automated Reference Issuance: On submission, Flask generates a unique Admission Reference Number (e.g., UA-2026-482) and persists the record into SQLite."
            ]
        },
        {
            "num": 6,
            "title": "Application Confirmation & Printable Slip",
            "route": "http://127.0.0.1:5000/apply/success/<ref_number>",
            "template": "templates/application_success.html",
            "method": "GET",
            "controller": "application_success(ref_number) in app.py",
            "db": "applicants table (SELECT * WHERE ref_number = ?)",
            "image": "screenshots/06_admission_confirmation_slip.png",
            "about": (
                "Provides formal digital confirmation immediately after an application is submitted. It presents the applicant's official "
                "Admission Reference Number (ARN), recaps their chosen campus and program, and provides a printable confirmation slip."
            ),
            "limitations": (
                "Previously, applicants received no digital receipt or verifiable tracking number; paper documents were frequently mislaid, "
                "and students had no tangible proof of timely application submission."
            ),
            "enhancements": [
                "Prominent Reference Number (ARN) Callout: Displays the unique tracking code in a large, dashed callout box for easy notation.",
                "Applicant Dossier Summary: Recaps applicant name, selected course, campus assignment, contact number, and initial 'Pending Review' status.",
                "One-Click Printable Slip: Features an integrated 'Print Confirmation' button triggering window.print() formatted cleanly for physical printing or saving as a PDF.",
                "Next-Step Instructions: Clearly informs the applicant to save their ARN and prepare required physical documents for exam day."
            ]
        },
        {
            "num": 7,
            "title": "Admission Status Tracker",
            "route": "http://127.0.0.1:5000/status",
            "template": "templates/status.html",
            "method": "GET, POST",
            "controller": "status() in app.py",
            "db": "applicants table (SELECT * WHERE ref_number = ?)",
            "image": "screenshots/07_admission_status_tracker.png",
            "about": (
                "A self-service application inquiry portal where candidates can check their real-time evaluation status, examination schedule, "
                "and room assignment by simply inputting their Admission Reference Number."
            ),
            "limitations": (
                "On the legacy website, applicants had no way to verify their status online. They were required to make long-distance phone calls "
                "or physically travel to campus bulletin boards to check printed sheets of qualified applicants."
            ),
            "enhancements": [
                "Instant Reference Search: Simple, responsive search bar allowing instant record lookup via the applicant's ARN.",
                "Color-Coded Status Badges: Distinct visual indicators: Yellow ('Pending Review'), Blue ('Qualified for Exam'), and Green ('Admitted').",
                "Evaluator Remarks Container: Displays evaluator instructions such as testing dates, designated exam room (e.g., 'Room 204, IT Building'), and documents to bring.",
                "Sample Demo Reference Codes: Built-in clickable sample reference codes to allow fast, seamless demonstration during academic evaluation."
            ]
        },
        {
            "num": 8,
            "title": "Student Portal Login (SIAS Authentication)",
            "route": "http://127.0.0.1:5000/portal",
            "template": "templates/portal_login.html",
            "method": "GET, POST (/portal/login)",
            "controller": "portal() / portal_login() in app.py",
            "db": "students table (SELECT * WHERE student_id = ? AND password = ?)",
            "image": "screenshots/08_student_portal_login.png",
            "about": (
                "The secure authentication gateway for enrolled students accessing the Student Information and Accounting System (SIAS). "
                "Provides encrypted credential verification and session initiation."
            ),
            "limitations": (
                "Links to the student portal on asist.edu.ph were frequently broken, directed to unencrypted raw IP addresses, and lacked mobile "
                "optimization, often triggering browser security warnings."
            ),
            "enhancements": [
                "Unified Institutional Design: Consistent University Green/Gold branding with institutional security notices.",
                "Session-Based Security: Employs secure Flask sessions to safeguard student personal and academic data.",
                "1-Click Demo Login: Built-in evaluator button allowing instant login as sample student 'Maria Clarisse Santos (BSIT)' without manual typing during defenses."
            ]
        },
        {
            "num": 9,
            "title": "Student Portal Dashboard (Academic Self-Service)",
            "route": "http://127.0.0.1:5000/portal",
            "template": "templates/portal.html",
            "method": "GET (Authenticated Session)",
            "controller": "portal() in app.py",
            "db": "students, student_grades",
            "image": "screenshots/09_student_portal_dashboard.png",
            "about": (
                "The comprehensive self-service academic dashboard for enrolled students. Displays the student's profile, academic standing, "
                "General Weighted Average (GWA), zero-tuition balance under RA 10931, enrolled subjects with midterm grades, multi-department "
                "clearance checklist, and downloadable academic records."
            ),
            "limitations": (
                "The existing SIAS interface was dated, desktop-only, lacked semestral GWA honors metrics, had no multi-department online "
                "clearance tracking, and provided no online document downloading."
            ),
            "enhancements": [
                "Student Profile Header: Displays student avatar, full name, ID number (2023-0145), degree program, campus, and year standing.",
                "Semestral GWA & Honors Badge: Automatically displays calculated GWA (1.38) with an official 'Dean's List' honor badge.",
                "Zero Tuition Balance Badge: Clearly displays ₱0.00 Outstanding Balance under RA 10931 Free Higher Education Act.",
                "Enrolled Subjects & Grades Table: Displays active semester subjects (IT 311, IT 312, IT 313, IT 314, GE 8, PE 4) with unit weights, instructors, and midterm grades.",
                "Multi-Office Clearance Tracker: Live clearance status across 5 offices: Library, Cashier, Guidance, College Dean, and University Registrar.",
                "Direct Document Downloads: One-click downloads for Certificate of Registration (COR), TOR Request Slip, and Student Handbook.",
                "Print Grade Slip: Integrated button to print or export the official grade summary directly to PDF."
            ]
        },
        {
            "num": 10,
            "title": "Campus News & Bulletins Board",
            "route": "http://127.0.0.1:5000/news",
            "template": "templates/news.html",
            "method": "GET",
            "controller": "news() in app.py",
            "db": "announcements table (SELECT * ORDER BY id DESC)",
            "image": "screenshots/10_campus_news.png",
            "about": (
                "The official university news and press release board. Communicates institutional achievements, academic announcements, "
                "university charter milestones, and administrative advisories."
            ),
            "limitations": (
                "Announcements on the original website were rarely categorized, lacked dates, and mixed internal administrative memoranda with "
                "public news in plain unformatted text."
            ),
            "enhancements": [
                "Card-Based News Architecture: Modern cards featuring category badges (Admissions, Academic Excellence, Campus Update), posting dates, and summaries.",
                "Statutory Milestones Highlight: Spotlights major institutional advancements including RA 11574 university conversion and 100% board passing achievements.",
                "Database-Driven Publishing: Dynamically queried from the SQLite announcements table."
            ]
        },
        {
            "num": 11,
            "title": "Contact Us & Multi-Campus Directory",
            "route": "http://127.0.0.1:5000/contact",
            "template": "templates/contact.html",
            "method": "GET, POST",
            "controller": "contact() in app.py",
            "db": "inquiries table (INSERT INTO inquiries)",
            "image": "screenshots/11_contact_us.png",
            "about": (
                "Provides verified contact information for all three university campuses and an interactive citizen inquiry form "
                "for students, parents, and community members."
            ),
            "limitations": (
                "The old site listed only an outdated landline number, lacked physical address clarity for the three distinct campuses, and "
                "had no interactive messaging form, forcing users to use third-party email clients."
            ),
            "enhancements": [
                "Comprehensive 3-Campus Directory: Detailed physical addresses, active telephone hotlines, and office hours for Lagangilang Main, Bangued Campus, and La Paz Campus.",
                "Working Interactive Message Form: Allows users to submit their Name, Email, Subject, and Inquiry directly on the website.",
                "Database Persistence: Form submissions are stored in the inquiries database table, and users receive an immediate on-screen confirmation banner."
            ]
        },
        {
            "num": 12,
            "title": "Admin & Evaluator Management Console",
            "route": "http://127.0.0.1:5000/admin",
            "template": "templates/admin.html",
            "method": "GET, POST (/admin/update/<id>)",
            "controller": "admin() / admin_update() in app.py",
            "db": "applicants, inquiries",
            "image": "screenshots/12_admin_evaluator_view.png",
            "about": (
                "The administrative backend console for university admissions evaluators and registrars to review incoming online applications, "
                "update evaluation statuses, assign entrance examination rooms, and view public inquiries."
            ),
            "limitations": (
                "The university previously possessed no online application management system; staff had to record paper forms into disconnected "
                "spreadsheets or paper logbooks, leading to lost records and processing delays."
            ),
            "enhancements": [
                "Real-Time Application Metric: Displays live counter of total registered applicant volume.",
                "Applicant Management Dossier Table: Lists reference numbers, applicant names, selected courses, campus assignments, and GPA.",
                "Inline Status & Remarks Editor: Evaluators can select a new evaluation status ('Pending Review', 'Qualified for Exam', 'Admitted'), enter custom instructions (e.g., testing room assignment), and click 'Save' to commit updates directly to SQLite.",
                "Citizen Feedback Audit Stream: Lists all inquiries submitted via the Contact page with sender details and timestamps for administrative follow-up."
            ]
        }
    ]

    for p_info in pages:
        doc.add_page_break()

        # Page Heading
        ph = doc.add_heading(level=2)
        r_ph = ph.add_run(f"PAGE {p_info['num']}: {p_info['title'].upper()}")
        r_ph.font.name = "Calibri"
        r_ph.font.size = Pt(14)
        r_ph.font.bold = True
        r_ph.font.color.rgb = GREEN

        # Spec Table
        spec_table = doc.add_table(rows=4, cols=2)
        spec_table.alignment = WD_TABLE_ALIGNMENT.CENTER
        spec_table.autofit = False

        specs = [
            ("URL Route:", p_info["route"]),
            ("Template & Methods:", f"{p_info['template']}  |  HTTP: {p_info['method']}"),
            ("Controller Function:", p_info["controller"]),
            ("Database Interaction:", p_info["db"])
        ]

        for r_idx, (k, v) in enumerate(specs):
            row = spec_table.rows[r_idx]
            c0 = row.cells[0]
            c0.width = Inches(1.8)
            set_cell_background(c0, "0D5C3A")
            set_cell_padding(c0, 40, 40, 100, 100)
            p0 = c0.paragraphs[0]
            r0 = p0.add_run(k)
            r0.font.name = "Calibri"
            r0.font.size = Pt(9)
            r0.font.bold = True
            r0.font.color.rgb = RGBColor(255, 255, 255)

            c1 = row.cells[1]
            c1.width = Inches(5.2)
            set_cell_background(c1, "F4F8F5" if r_idx % 2 == 0 else "FFFFFF")
            set_cell_padding(c1, 40, 40, 100, 100)
            p1 = c1.paragraphs[0]
            r1 = p1.add_run(v)
            r1.font.name = "Calibri"
            r1.font.size = Pt(9)
            r1.font.color.rgb = DARK

        doc.add_paragraph().paragraph_format.space_after = Pt(6)

        # Screenshot Picture
        img_path = p_info["image"]
        if os.path.exists(img_path):
            pic_p = doc.add_paragraph()
            pic_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            pic_p.paragraph_format.space_before = Pt(4)
            pic_p.paragraph_format.space_after = Pt(2)
            pic_run = pic_p.add_run()
            pic_run.add_picture(img_path, width=Inches(6.2))

            cap_p = doc.add_paragraph()
            cap_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            cap_p.paragraph_format.space_after = Pt(8)
            cap_run = cap_p.add_run(f"Figure {p_info['num']}: Actual System Screenshot — {p_info['title']}")
            cap_run.font.name = "Calibri"
            cap_run.font.size = Pt(9)
            cap_run.font.italic = True
            cap_run.font.color.rgb = GRAY

        # Section: About the Page
        ab_h = doc.add_paragraph()
        ab_h.paragraph_format.space_before = Pt(4)
        ab_h.paragraph_format.space_after = Pt(2)
        r_abh = ab_h.add_run("ABOUT & FUNCTIONALITY OF THIS PAGE:")
        r_abh.font.name = "Calibri"
        r_abh.font.size = Pt(10.5)
        r_abh.font.bold = True
        r_abh.font.color.rgb = GREEN

        ab_p = doc.add_paragraph()
        ab_p.paragraph_format.line_spacing = 1.15
        ab_p.paragraph_format.space_after = Pt(6)
        r_abp = ab_p.add_run(p_info["about"])
        r_abp.font.name = "Calibri"
        r_abp.font.size = Pt(10)

        # Section: Limitations of Original Website
        lim_h = doc.add_paragraph()
        lim_h.paragraph_format.space_before = Pt(4)
        lim_h.paragraph_format.space_after = Pt(2)
        r_limh = lim_h.add_run("LIMITATIONS OF THE ORIGINAL WEBSITE (asist.edu.ph):")
        r_limh.font.name = "Calibri"
        r_limh.font.size = Pt(10.5)
        r_limh.font.bold = True
        r_limh.font.color.rgb = RGBColor(160, 40, 40) # Crimson

        lim_p = doc.add_paragraph()
        lim_p.paragraph_format.line_spacing = 1.15
        lim_p.paragraph_format.space_after = Pt(6)
        r_limp = lim_p.add_run(p_info["limitations"])
        r_limp.font.name = "Calibri"
        r_limp.font.size = Pt(10)

        # Section: Enhancements Implemented
        enh_h = doc.add_paragraph()
        enh_h.paragraph_format.space_before = Pt(4)
        enh_h.paragraph_format.space_after = Pt(2)
        r_enhh = enh_h.add_run("ENHANCEMENTS & MODERNIZATION IMPLEMENTED:")
        r_enhh.font.name = "Calibri"
        r_enhh.font.size = Pt(10.5)
        r_enhh.font.bold = True
        r_enhh.font.color.rgb = GREEN

        for enh in p_info["enhancements"]:
            ep = doc.add_paragraph(style='List Bullet')
            ep.paragraph_format.space_after = Pt(2.5)
            ep.paragraph_format.line_spacing = 1.15
            
            if ":" in enh:
                e_title, e_desc = enh.split(":", 1)
                r_et = ep.add_run(e_title + ": ")
                r_et.font.name = "Calibri"
                r_et.font.size = Pt(10)
                r_et.font.bold = True
                r_et.font.color.rgb = GREEN
                
                r_ed = ep.add_run(e_desc)
                r_ed.font.name = "Calibri"
                r_ed.font.size = Pt(10)
            else:
                r_e = ep.add_run(enh)
                r_e.font.name = "Calibri"
                r_e.font.size = Pt(10)

    # ----------------------------------------------------
    # SECTION 3: SUMMARY COMPARISON MATRIX
    # ----------------------------------------------------
    doc.add_page_break()
    h3 = doc.add_heading(level=1)
    r3 = h3.add_run("3. Summary Matrix: Original Website vs. Enhanced Solution")
    r3.font.name = "Calibri"
    r3.font.color.rgb = GREEN

    matrix_table = doc.add_table(rows=9, cols=3)
    matrix_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    matrix_table.autofit = False

    matrix_headers = ["System Module / Page", "Original Website (asist.edu.ph)", "Our Enhanced UA Solution"]
    for c_idx, h_text in enumerate(matrix_headers):
        cell = matrix_table.rows[0].cells[c_idx]
        set_cell_background(cell, "0D5C3A")
        set_cell_padding(cell, 80, 80, 100, 100)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h_text)
        r.font.name = "Calibri"
        r.font.size = Pt(10)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    matrix_rows = [
        ("Visual Identity & Branding", "Dated layout, low contrast, no official RA 11574 university branding.", "Official UA Forest Green (#0D5C3A) & Gold (#F4C430), vector seal, and statutory charter banner."),
        ("Mobile Responsiveness", "Non-responsive fixed tables; breaks heavily on smartphones.", "100% fluid responsive layout across mobile, tablet, and desktop screens."),
        ("Academic Programs", "Static unorganized HTML tables mixing all campuses together.", "Interactive card grid with dynamic campus filter (?campus=Bangued)."),
        ("Admissions System", "Completely absent; manual in-person travel or paper PDF forms only.", "100% paperless online admission form with instant automated ARN issuance."),
        ("Application Slip", "None; students received no digital proof of application submission.", "Digital confirmation slip with printable format (window.print()) for exam day."),
        ("Application Tracker", "In-person bulletin board inquiry or landline phone calls only.", "Real-time online status lookup by reference number with room assignment notices."),
        ("Student SIAS Portal", "Broken external links, unencrypted raw IP addresses, security alerts.", "Integrated self-service portal with grades, GWA (1.38), Dean's list badge, and online clearance."),
        ("Admissions Admin", "Offline paper binders, manual registry books, slow evaluation.", "Web-based admin console to view, evaluate, and update applicant statuses in real time.")
    ]

    widths = [Inches(1.8), Inches(2.6), Inches(2.6)]

    for r_idx, (mod, old, new) in enumerate(matrix_rows, start=1):
        row = matrix_table.rows[r_idx]
        bg_col = "F4F8F5" if r_idx % 2 == 1 else "FFFFFF"

        for c_idx, text in enumerate([mod, old, new]):
            cell = row.cells[c_idx]
            cell.width = widths[c_idx]
            set_cell_background(cell, bg_col)
            set_cell_padding(cell, 60, 60, 100, 100)
            p = cell.paragraphs[0]
            r = p.add_run(text)
            r.font.name = "Calibri"
            r.font.size = Pt(9.5)
            if c_idx == 0:
                r.font.bold = True
                r.font.color.rgb = GREEN
            elif c_idx == 1:
                r.font.color.rgb = RGBColor(140, 40, 40)
            else:
                r.font.color.rgb = DARK

    # ----------------------------------------------------
    # SECTION 4: DATABASE ARCHITECTURE
    # ----------------------------------------------------
    doc.add_page_break()
    h4 = doc.add_heading(level=1)
    r4 = h4.add_run("4. Database Architecture & Data Dictionary (ua_school.db)")
    r4.font.name = "Calibri"
    r4.font.color.rgb = GREEN

    db_p = doc.add_paragraph()
    db_p.paragraph_format.line_spacing = 1.15
    db_p.paragraph_format.space_after = Pt(8)
    db_p.add_run(
        "The system utilizes an embedded SQLite3 relational database (ua_school.db) managed through database.py. "
        "The relational schema supports modular scalability, normalized academic records, and transactional integrity:"
    )

    db_tables = [
        ("1. programs (Academic Offerings Catalog)", [
            ("id", "INTEGER", "Primary Key, Autoincrement"),
            ("code", "TEXT", "Short degree code (e.g., 'BSIT', 'BSCE', 'BSA')"),
            ("title", "TEXT", "Full degree program title"),
            ("campus", "TEXT", "Campus location (Lagangilang, Bangued, La Paz)"),
            ("department", "TEXT", "College department in charge"),
            ("years", "TEXT", "Program duration (e.g., '4 Years')"),
            ("description", "TEXT", "Curricular description and career prospects")
        ]),
        ("2. applicants (Admission Applications)", [
            ("id", "INTEGER", "Primary Key, Autoincrement"),
            ("ref_number", "TEXT", "Unique tracking reference (e.g., 'UA-2026-482')"),
            ("fullname", "TEXT", "Applicant complete legal name"),
            ("email", "TEXT", "Applicant contact email"),
            ("contact", "TEXT", "Mobile contact phone number"),
            ("campus", "TEXT", "Selected campus"),
            ("course", "TEXT", "Preferred degree program"),
            ("prev_school", "TEXT", "Previous senior high school / college"),
            ("average", "TEXT", "General Weighted Average (GPA)"),
            ("status", "TEXT", "Evaluation status ('Pending Review', 'Qualified for Exam', 'Admitted')"),
            ("remarks", "TEXT", "Registrar evaluator notes & exam room assignments")
        ]),
        ("3. students (Enrolled Student Accounts)", [
            ("id", "INTEGER", "Primary Key, Autoincrement"),
            ("student_id", "TEXT", "Unique student ID number (e.g., '2023-0145')"),
            ("password", "TEXT", "Account password"),
            ("fullname", "TEXT", "Enrolled student full name"),
            ("course", "TEXT", "Degree program"),
            ("campus", "TEXT", "Campus affiliation"),
            ("year_level", "TEXT", "Current academic standing"),
            ("gwa", "TEXT", "Cumulative General Weighted Average (e.g., '1.38')")
        ]),
        ("4. student_grades (Enrolled Subject Grades)", [
            ("id", "INTEGER", "Primary Key, Autoincrement"),
            ("student_id", "TEXT", "Foreign key referencing students.student_id"),
            ("subject_code", "TEXT", "Curriculum course code (e.g., 'IT 311')"),
            ("subject_title", "TEXT", "Descriptive title of subject"),
            ("units", "INTEGER", "Unit credit weight"),
            ("grade", "TEXT", "Midterm semestral grade (e.g., '1.25')"),
            ("instructor", "TEXT", "Assigned faculty instructor")
        ]),
        ("5. announcements (Campus News Bulletins)", [
            ("id", "INTEGER", "Primary Key, Autoincrement"),
            ("title", "TEXT", "Announcement headline"),
            ("date_posted", "TEXT", "Publication date string"),
            ("category", "TEXT", "Category tag ('Admissions', 'Academic', 'Updates')"),
            ("content", "TEXT", "Complete article body text")
        ]),
        ("6. inquiries (Public Citizen Feedback)", [
            ("id", "INTEGER", "Primary Key, Autoincrement"),
            ("name", "TEXT", "Inquiring citizen name"),
            ("email", "TEXT", "Contact email"),
            ("subject", "TEXT", "Subject line"),
            ("message", "TEXT", "Complete message inquiry body")
        ])
    ]

    for tbl_name, fields in db_tables:
        th = doc.add_paragraph()
        th.paragraph_format.space_before = Pt(6)
        th.paragraph_format.space_after = Pt(2)
        r_th = th.add_run(tbl_name)
        r_th.font.name = "Calibri"
        r_th.font.size = Pt(11)
        r_th.font.bold = True
        r_th.font.color.rgb = GREEN

        tbl = doc.add_table(rows=len(fields) + 1, cols=3)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False

        headers = ["Column Name", "Data Type", "Description / Constraints"]
        for ci, ht in enumerate(headers):
            cell = tbl.rows[0].cells[ci]
            set_cell_background(cell, "0D5C3A")
            set_cell_padding(cell, 40, 40, 80, 80)
            p = cell.paragraphs[0]
            r = p.add_run(ht)
            r.font.name = "Calibri"
            r.font.size = Pt(9)
            r.font.bold = True
            r.font.color.rgb = RGBColor(255, 255, 255)

        w = [Inches(1.8), Inches(1.2), Inches(4.0)]
        for ri, (col_name, col_type, col_desc) in enumerate(fields, start=1):
            row = tbl.rows[ri]
            bg_c = "F4F8F5" if ri % 2 == 1 else "FFFFFF"
            for ci, val in enumerate([col_name, col_type, col_desc]):
                cell = row.cells[ci]
                cell.width = w[ci]
                set_cell_background(cell, bg_c)
                set_cell_padding(cell, 30, 30, 80, 80)
                p = cell.paragraphs[0]
                r = p.add_run(val)
                r.font.name = "Calibri"
                r.font.size = Pt(8.5)
                if ci == 0:
                    r.font.bold = True
                    r.font.color.rgb = GREEN

    # ----------------------------------------------------
    # SECTION 5: ORAL DEFENSE PRESENTATION SCRIPT
    # ----------------------------------------------------
    doc.add_page_break()
    h5 = doc.add_heading(level=1)
    r5 = h5.add_run("5. Oral Defense Presentation Guide & Talking Points")
    r5.font.name = "Calibri"
    r5.font.color.rgb = GREEN

    script_intro = doc.add_paragraph()
    script_intro.paragraph_format.line_spacing = 1.15
    script_intro.paragraph_format.space_after = Pt(8)
    script_intro.add_run(
        "Use this structured script when demonstrating the project to your professor and panel evaluators:\n"
    )

    scripts = [
        ("Step 1: Introduction & Project Mandate",
         "\"Good day, Sir/Ma'am! My project is an individual comprehensive enhancement of the official website of the University of Abra (UA), "
         "formerly ASIST, established under Republic Act No. 11574. I chose to enhance the live site at asist.edu.ph because an audit revealed "
         "that it was non-responsive on smartphones and completely lacked an online admission system, leaving applicants with no way to apply or check results online.\""),
        
        ("Step 2: Demonstrating Branding & Course Filtering",
         "\"First, I modernized the visual branding using the official University Forest Green and Gold color palette. On the Courses catalog, "
         "I created an interactive campus filter dropdown. Selecting 'Bangued Campus' instantly queries SQLite and isolates their engineering programs "
         "(Civil, Mechanical, and Electrical Engineering), solving the long-standing problem of applicants not knowing which campus offers which degree.\""),
        
        ("Step 3: Demonstrating the Online Admission Flow",
         "\"Second, on the Admission page (/apply), I implemented a 100% paperless registration form. When an applicant submits their credentials, "
         "the Flask backend automatically generates a unique tracking number, such as UA-2026-482, and displays an official confirmation slip with a "
         "one-click Print button for exam day. The applicant can then track their live evaluation status and exam room assignment on /status.\""),
         
        ("Step 4: Demonstrating the Student Portal (SIAS)",
         "\"Third, on /portal, I created an integrated student self-service portal. Using the 1-click demo login, we can view real enrolled subjects, "
         "midterm grades, a computed GWA of 1.38 with a Dean's List honor badge, zero-tuition balance under RA 10931, and a 5-office clearance tracker.\""),
         
        ("Step 5: Demonstrating the Admin Evaluator Console",
         "\"Finally, on /admin, admissions officers can view all applicants in real time, change an applicant's status to 'Qualified for Exam', "
         "input their test room number, and save changes to SQLite instantly, completing a fully integrated university web system.\"")
    ]

    for s_step, s_text in scripts:
        sp_title = doc.add_paragraph()
        sp_title.paragraph_format.space_before = Pt(6)
        sp_title.paragraph_format.space_after = Pt(2)
        r_st = sp_title.add_run(s_step)
        r_st.font.name = "Calibri"
        r_st.font.size = Pt(10.5)
        r_st.font.bold = True
        r_st.font.color.rgb = GREEN

        sp_body = doc.add_paragraph()
        sp_body.paragraph_format.line_spacing = 1.15
        sp_body.paragraph_format.left_indent = Inches(0.25)
        sp_body.paragraph_format.space_after = Pt(6)
        r_sb = sp_body.add_run(s_text)
        r_sb.font.name = "Calibri"
        r_sb.font.size = Pt(9.5)
        r_sb.font.italic = True
        r_sb.font.color.rgb = DARK

    # Save Word Document
    output_docx = "UA_System_Documentation_and_Enhancements.docx"
    doc.save(output_docx)
    print(f"Successfully generated Word Document: {output_docx}")

if __name__ == '__main__':
    create_document()
