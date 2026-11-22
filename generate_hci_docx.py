import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_padding(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def generate_hci_doc():
    doc = docx.Document()

    # Set 0.75 in margins
    for sec in doc.sections:
        sec.top_margin = Inches(0.75)
        sec.bottom_margin = Inches(0.75)
        sec.left_margin = Inches(0.75)
        sec.right_margin = Inches(0.75)

        # Header & Footer
        hp = sec.header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("Human-Computer Interaction (HCI) • University of Abra Website Enhancement")
        hrun.font.name = "Calibri"
        hrun.font.size = Pt(8.5)
        hrun.font.italic = True
        hrun.font.color.rgb = RGBColor(120, 120, 120)

        fp = sec.footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        frun = fp.add_run("HCI Project: System Usability & Interface Enhancement Report")
        frun.font.name = "Calibri"
        frun.font.size = Pt(8.5)
        frun.font.color.rgb = RGBColor(140, 140, 140)

    # Theme colors
    GREEN = RGBColor(13, 92, 58)    # #0D5C3A
    GOLD = RGBColor(185, 135, 15)   # #B9870F
    DARK = RGBColor(35, 40, 48)     # #232830
    GRAY = RGBColor(90, 95, 105)

    # --------------------------------------------------------
    # TITLE & COURSE HEADER
    # --------------------------------------------------------
    title_p = doc.add_paragraph()
    title_p.paragraph_format.space_before = Pt(8)
    title_p.paragraph_format.space_after = Pt(2)
    
    r_crs = title_p.add_run("COURSE: HUMAN-COMPUTER INTERACTION (HCI)\n")
    r_crs.font.name = "Calibri"
    r_crs.font.size = Pt(13)
    r_crs.font.bold = True
    r_crs.font.color.rgb = GOLD

    r_main = title_p.add_run("University of Abra (UA) Website Interface & Usability Enhancement\n")
    r_main.font.name = "Calibri"
    r_main.font.size = Pt(20)
    r_main.font.bold = True
    r_main.font.color.rgb = GREEN

    r_sub = title_p.add_run("Comprehensive Page-by-Page Screenshot Portfolio and UI/UX Enhancement Breakdown")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(10.5)
    r_sub.font.italic = True
    r_sub.font.color.rgb = GRAY

    # Meta Table
    tbl = doc.add_table(rows=4, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False

    meta = [
        ("Course / Subject:", "Human-Computer Interaction (HCI)"),
        ("Project Title:", "University of Abra (UA) School Website Enhancement & UX Redesign"),
        ("Original Website Evaluated:", "https://asist.edu.ph/ (Abra State Institute of Sciences and Technology)"),
        ("Core HCI Objectives:", "Usability Enhancement, Visual Hierarchy, Mobile Responsiveness, Reduced Cognitive Load, Self-Service Workflows")
    ]

    for idx, (label, val) in enumerate(meta):
        row = tbl.rows[idx]
        c0 = row.cells[0]
        c0.width = Inches(2.2)
        set_cell_background(c0, "0D5C3A")
        set_cell_padding(c0, 50, 50, 80, 80)
        p0 = c0.paragraphs[0]
        r0 = p0.add_run(label)
        r0.font.name = "Calibri"
        r0.font.size = Pt(9.5)
        r0.font.bold = True
        r0.font.color.rgb = RGBColor(255, 255, 255)

        c1 = row.cells[1]
        c1.width = Inches(4.8)
        set_cell_background(c1, "F4F8F5" if idx % 2 == 0 else "FFFFFF")
        set_cell_padding(c1, 50, 50, 100, 100)
        p1 = c1.paragraphs[0]
        r1 = p1.add_run(val)
        r1.font.name = "Calibri"
        r1.font.size = Pt(9.5)
        r1.font.color.rgb = DARK

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # --------------------------------------------------------
    # 12 PAGES DATA
    # --------------------------------------------------------
    pages_data = [
        {
            "num": 1,
            "title": "Homepage (Primary Digital Gateway)",
            "image": "screenshots/01_homepage.png",
            "about": "The homepage serves as the primary digital front-door and welcoming landing page for prospective students, current enrollees, faculty, and stakeholders of the University of Abra.",
            "enhancement": (
                "From a Human-Computer Interaction perspective, the original website (asist.edu.ph) was cluttered, non-responsive, "
                "and overwhelmed visitors with dense, unorganized text that violated basic visual hierarchy principles. In this enhanced version, "
                "I introduced a clean, modern aesthetic utilizing the university’s official Forest Green (#0D5C3A) and Gold (#F4C430) branding. "
                "I created a prominent Hero Section featuring three clear, high-contrast Call-to-Action (CTA) buttons ('Apply Online', 'Explore Courses', "
                "and 'Check Status') to significantly reduce cognitive friction and streamline user navigation. I also integrated quick-glance statistic "
                "cards (highlighting the 3 campuses, ₱0 tuition fee under RA 10931, and top licensure passing rates) and a dynamic campus announcement feed, "
                "all designed with a fully fluid, mobile-first responsive layout that adapts seamlessly across smartphones, tablets, and desktop displays."
            )
        },
        {
            "num": 2,
            "title": "About the University (History, Campuses & Values)",
            "image": "screenshots/02_about_page.png",
            "about": "This page communicates the institutional profile of the university, detailing its transition under Republic Act No. 11574, campus specializations, official Vision, Mission, and the NEW ASIST Core Values.",
            "enhancement": (
                "On the original website, institutional background was buried inside fragmented text blocks and hard-to-find PDF downloads, "
                "creating severe usability barriers for users seeking basic school information. To resolve this, I restructured the entire content "
                "architecture into an intuitive, modular layout with distinct visual callouts. I clearly separated the unique specializations of the "
                "three campuses (Lagangilang Main for smart agriculture and computing, Bangued for engineering, and La Paz for agro-technology) "
                "so visitors can easily understand their distinct academic thrusts. Furthermore, the Vision, Mission, and the 8 core values "
                "(Nobility, Entrepreneurship, Wisdom, Action, Sincerity, Integrity, Service, Teamwork) were organized into a high-contrast two-column "
                "card grid, enhancing scannability, legibility, and overall visual balance."
            )
        },
        {
            "num": 3,
            "title": "Courses & Academic Programs Catalog",
            "image": "screenshots/03_courses_catalog.png",
            "about": "The Courses Catalog provides an exhaustive directory of all undergraduate and technical degree programs offered across the university.",
            "enhancement": (
                "The legacy website displayed academic programs in long, static HTML tables that lumped all degrees together regardless of campus, "
                "making it frustrating and confusing for applicants to determine where a course was actually held. In this enhancement, I transitioned "
                "the layout into an interactive card-based catalog adhering to modern UI design standards. Each card highlights the program code "
                "(BSIT, BSA, BSCE, BSED), official title, college department, 4-year duration, and a green badge emphasizing the RA 10931 Free Higher "
                "Education coverage. Most importantly, each card incorporates a colored campus location tag and a direct 'Apply Online' button, "
                "establishing a direct, intuitive user flow from course exploration to application."
            )
        },
        {
            "num": 4,
            "title": "Courses Filtered by Campus (Interactive Filtering)",
            "image": "screenshots/04_courses_filtered_bangued.png",
            "about": "Demonstrates the dynamic campus filtering mechanism, showing degree offerings filtered specifically for the Bangued Campus.",
            "enhancement": (
                "In the original system, users had zero ability to filter or search for courses by location, forcing them to manually read through "
                "irrelevant degree lists. To enhance user control and efficiency—a core HCI heuristic—I designed an interactive campus filter dropdown. "
                "When a user selects 'Bangued Campus', the interface dynamically refreshes to display only the relevant engineering and industrial technology "
                "degrees (such as Civil, Mechanical, and Electrical Engineering). The dropdown automatically preserves the user's selected state, "
                "providing immediate visual feedback and drastically cutting the interaction time required for applicants to find programs available in their local municipality."
            )
        },
        {
            "num": 5,
            "title": "Online Admission Application Form",
            "image": "screenshots/05_online_admission_form.png",
            "about": "A paperless digital admission application portal where incoming high school graduates and transferees can apply for enrollment online.",
            "enhancement": (
                "The original website completely lacked any digital application mechanism, forcing applicants to travel in person to the registrar "
                "in Abra or deal with manual paper forms—a major friction point that caused long queues and excluded distant applicants. I designed "
                "an intuitive, user-friendly digital application form with clear input grouping, high-contrast labels, and built-in validation. "
                "The degree selection dropdown dynamically syncs with the university database to prevent invalid course choices. The form follows "
                "clean form-design best practices with ample spacing, accessible input fields, and an inviting submit button that simplifies the entire enrollment journey."
            )
        },
        {
            "num": 6,
            "title": "Application Confirmation & Printable Slip",
            "image": "screenshots/06_admission_confirmation_slip.png",
            "about": "The digital confirmation receipt page displayed immediately after an applicant successfully submits their online admission form.",
            "enhancement": (
                "In Human-Computer Interaction, immediate system feedback is critical for establishing user confidence and trust. The old system provided "
                "no digital confirmation whatsoever. In this enhancement, upon form submission, the system instantly generates an official Admission Reference "
                "Number (ARN) displayed prominently inside an eye-catching dashed container. It summarizes the applicant's submitted information and provides "
                "clear instructions for entrance examination day. Additionally, I added a prominent one-click 'Print Confirmation' button that triggers a "
                "clean print-optimized layout, allowing applicants to print their slip or save it as a PDF without any cluttered browser elements."
            )
        },
        {
            "num": 7,
            "title": "Admission Status Tracker",
            "image": "screenshots/07_admission_status_tracker.png",
            "about": "A self-service inquiry tool that allows applicants to check their evaluation progress and examination schedule using their reference number.",
            "enhancement": (
                "Previously, applicants had to repeatedly phone registrar landlines or travel to physical bulletin boards to know if their applications "
                "were approved. To satisfy the HCI principle of 'Visibility of System Status', I built an online tracker where applicants simply enter "
                "their reference number to view real-time results. The system communicates status through clear, color-coded status badges (Yellow for "
                "'Pending Review', Blue for 'Qualified for Exam', and Green for 'Admitted'), paired with an official remarks box containing personalized "
                "evaluator instructions such as the assigned testing room and exam date. I also included clickable demo sample codes to allow effortless "
                "testing during usability reviews."
            )
        },
        {
            "num": 8,
            "title": "Student Portal Login (SIAS)",
            "image": "screenshots/08_student_portal_login.png",
            "about": "The security gateway for enrolled students to access their Student Information and Accounting System (SIAS) accounts.",
            "enhancement": (
                "On the old website, links to the student portal were often broken or pointed to intimidating raw IP addresses without proper SSL branding, "
                "confusing students and raising security concerns. In this enhanced version, I designed a cohesive institutional login portal styled "
                "with the official university logo, comforting green background accents, and clear form fields for Student ID and Password. To make "
                "usability evaluation and live demonstrations effortless, I added a '1-Click Demo Login' button that instantly signs in as sample "
                "student Maria Clarisse Santos, eliminating typing errors and allowing instant evaluation of the internal portal."
            )
        },
        {
            "num": 9,
            "title": "Student Portal Dashboard (Academic Self-Service)",
            "image": "screenshots/09_student_portal_dashboard.png",
            "about": "The academic self-service portal for enrolled students, featuring profile info, enrolled subjects, midterm grades, semestral GWA, clearance checklist, and document downloads.",
            "enhancement": (
                "The original SIAS was a dated, desktop-only system with cluttered tables, poor font scaling on mobile devices, and zero visual distinction "
                "for student accomplishments. In this enhancement, I transformed the portal into a modern dashboard that presents student data through clean "
                "visual hierarchy: an avatar profile header, an automated Semestral GWA indicator (1.38) with a prestigious 'Dean's List' honor badge, "
                "and a reassuring ₱0.00 tuition balance under RA 10931. I organized grades into an easily readable table with clear color badges, "
                "incorporated an interactive 5-office clearance progress checklist, and added instant download buttons for the Certificate of Registration (COR) "
                "and student handbook, drastically improving student satisfaction and self-service efficiency."
            )
        },
        {
            "num": 10,
            "title": "Campus News & Bulletins Board",
            "image": "screenshots/10_campus_news.png",
            "about": "The official announcements and university press releases board keeping students, faculty, and the public informed.",
            "enhancement": (
                "The legacy website’s news section suffered from information overload, presenting announcements as plain, unformatted walls of text "
                "without category tags or publication dates. For this enhancement, I implemented a card-based visual layout where each bulletin is neatly "
                "packaged with a category tag (Admissions, Academic, Campus Update), posting date, and concise summary. Important institutional achievements—such "
                "as the RA 11574 university transition and 100% board passing rates—are given visual prominence, making it effortless for visitors to scan, "
                "digest, and stay updated on university developments."
            )
        },
        {
            "num": 11,
            "title": "Contact Us & Campus Directory",
            "image": "screenshots/11_contact_us.png",
            "about": "The contact information directory for all three campuses and an interactive public inquiry and feedback form.",
            "enhancement": (
                "The old contact page listed only a single general telephone number that was frequently unattended, and offered no interactive messaging "
                "capability, forcing visitors to open third-party email clients. To improve user communication and accessibility, I organized a comprehensive "
                "directory detailing the physical addresses and active hotlines for the Lagangilang Main, Bangued, and La Paz campuses. Beside the directory, "
                "I created a responsive web contact form where users can directly submit inquiries with immediate on-screen visual confirmation, significantly "
                "lowering communication barriers for remote students and parents."
            )
        },
        {
            "num": 12,
            "title": "Admissions Admin & Evaluator Console",
            "image": "screenshots/12_admin_evaluator_view.png",
            "about": "The administrative dashboard for admissions officers and faculty to evaluate applications, update statuses, assign exam rooms, and review citizen inquiries.",
            "enhancement": (
                "From an HCI administrative workflow perspective, the university previously had no centralized web interface to manage applicant submissions, "
                "forcing evaluators to manually record paper applications into offline notebooks or disjointed spreadsheets. I designed an intuitive "
                "back-office dashboard featuring an instant application volume counter, a scannable applicant dossier table, and an inline status updater. "
                "Evaluators can effortlessly select an applicant's new status from a dropdown, type test room instructions, and save changes with a single click, "
                "providing immediate database synchronization and streamlining administrative decision-making."
            )
        }
    ]

    for item in pages_data:
        doc.add_page_break()

        # Section Header
        h = doc.add_heading(level=1)
        r_h = h.add_run(f"PAGE {item['num']}: {item['title'].upper()}")
        r_h.font.name = "Calibri"
        r_h.font.size = Pt(14)
        r_h.font.bold = True
        r_h.font.color.rgb = GREEN

        # Insert Picture
        img_p = item["image"]
        if os.path.exists(img_p):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(4)
            p_img.paragraph_format.space_after = Pt(2)
            run_img = p_img.add_run()
            run_img.add_picture(img_p, width=Inches(6.2))

            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_after = Pt(10)
            run_cap = p_cap.add_run(f"Figure {item['num']}: {item['title']} Interface")
            run_cap.font.name = "Calibri"
            run_cap.font.size = Pt(9)
            run_cap.font.italic = True
            run_cap.font.color.rgb = GRAY

        # About the Page Box
        t_about = doc.add_table(rows=1, cols=1)
        t_about.alignment = WD_TABLE_ALIGNMENT.CENTER
        t_about.autofit = False
        cell_about = t_about.rows[0].cells[0]
        cell_about.width = Inches(7.0)
        set_cell_background(cell_about, "F4F8F5")
        set_cell_padding(cell_about, 80, 80, 120, 120)
        p_ab = cell_about.paragraphs[0]
        p_ab.paragraph_format.space_after = Pt(0)
        p_ab.paragraph_format.line_spacing = 1.15
        r_abt_label = p_ab.add_run("About This Page: ")
        r_abt_label.font.name = "Calibri"
        r_abt_label.font.size = Pt(10)
        r_abt_label.font.bold = True
        r_abt_label.font.color.rgb = GREEN

        r_abt_txt = p_ab.add_run(item["about"])
        r_abt_txt.font.name = "Calibri"
        r_abt_txt.font.size = Pt(10)
        r_abt_txt.font.color.rgb = DARK

        doc.add_paragraph().paragraph_format.space_after = Pt(6)

        # Enhancement Paragraph
        p_enh_head = doc.add_paragraph()
        p_enh_head.paragraph_format.space_before = Pt(4)
        p_enh_head.paragraph_format.space_after = Pt(2)
        r_eh = p_enh_head.add_run("HCI & Usability Enhancements Implemented:")
        r_eh.font.name = "Calibri"
        r_eh.font.size = Pt(11)
        r_eh.font.bold = True
        r_eh.font.color.rgb = GREEN

        p_enh = doc.add_paragraph()
        p_enh.paragraph_format.line_spacing = 1.2
        p_enh.paragraph_format.space_after = Pt(8)
        r_ep = p_enh.add_run(item["enhancement"])
        r_ep.font.name = "Calibri"
        r_ep.font.size = Pt(10)
        r_ep.font.color.rgb = DARK

    # Save to HCI docx
    output_filename = "HCI_UA_Website_Enhancements.docx"
    doc.save(output_filename)
    print(f"Successfully generated {output_filename}")

if __name__ == '__main__':
    generate_hci_doc()
