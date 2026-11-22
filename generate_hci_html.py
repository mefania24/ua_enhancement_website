import os

html_code = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HCI: University of Abra Website Enhancement Portfolio</title>
    <style>
        :root {
            --ua-green: #0d5c3a;
            --ua-green-dark: #083c26;
            --ua-gold: #f4c430;
            --text-dark: #1f2937;
            --bg-page: #f8fafc;
            --card-border: #e2e8f0;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            color: var(--text-dark);
            background-color: var(--bg-page);
            line-height: 1.6;
            padding: 24px 0 60px 0;
        }

        .container {
            max-width: 960px;
            margin: 0 auto;
            padding: 0 20px;
        }

        .header-card {
            background: linear-gradient(135deg, var(--ua-green) 0%, var(--ua-green-dark) 100%);
            color: #ffffff;
            padding: 32px 28px;
            border-radius: 12px;
            border-bottom: 5px solid var(--ua-gold);
            margin-bottom: 30px;
            box-shadow: 0 8px 20px rgba(13, 92, 58, 0.2);
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 16px;
        }

        .badge-course {
            background-color: var(--ua-gold);
            color: #000;
            font-weight: 800;
            font-size: 12px;
            padding: 4px 10px;
            border-radius: 4px;
            display: inline-block;
            margin-bottom: 8px;
            letter-spacing: 0.5px;
        }

        .header-title {
            font-size: 24px;
            font-weight: 800;
            margin-bottom: 4px;
        }

        .header-sub {
            font-size: 14px;
            color: #e2e8f0;
        }

        .btn-print {
            background: var(--ua-gold);
            color: #000;
            border: none;
            padding: 10px 18px;
            font-weight: 700;
            font-size: 13.5px;
            border-radius: 6px;
            cursor: pointer;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: all 0.2s ease;
        }

        .btn-print:hover {
            background: #ffd64f;
            transform: translateY(-1px);
        }

        .page-card {
            background: #ffffff;
            border: 1px solid var(--card-border);
            border-radius: 12px;
            padding: 26px;
            margin-bottom: 36px;
            box-shadow: 0 3px 10px rgba(0,0,0,0.04);
            page-break-after: always;
        }

        .page-head {
            border-bottom: 2px solid #f1f5f9;
            padding-bottom: 12px;
            margin-bottom: 18px;
        }

        .page-num {
            color: var(--ua-green);
            font-size: 12px;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .page-title {
            font-size: 20px;
            font-weight: 800;
            color: var(--ua-green);
        }

        .img-container {
            margin: 16px 0;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 12px rgba(0,0,0,0.06);
            background: #000;
        }

        .img-container img {
            width: 100%;
            height: auto;
            display: block;
        }

        .img-cap {
            background: #f8fafc;
            padding: 8px 14px;
            font-size: 12px;
            font-style: italic;
            color: #64748b;
            border-top: 1px solid #e2e8f0;
            text-align: center;
        }

        .about-box {
            background: #f0fdf4;
            border-left: 4px solid var(--ua-green);
            padding: 12px 16px;
            border-radius: 0 6px 6px 0;
            margin-bottom: 16px;
            font-size: 14px;
            color: #14532d;
        }

        .about-box strong {
            color: var(--ua-green);
        }

        .enhancement-box {
            margin-top: 14px;
        }

        .enhancement-head {
            font-size: 14px;
            font-weight: 800;
            text-transform: uppercase;
            color: var(--ua-green);
            letter-spacing: 0.5px;
            margin-bottom: 6px;
        }

        .enhancement-text {
            font-size: 14.5px;
            line-height: 1.65;
            color: #334155;
            text-align: justify;
        }

        @media print {
            body { background: #fff; padding: 0; }
            .container { max-width: 100%; padding: 0; }
            .btn-print { display: none; }
            .header-card { border-radius: 0; box-shadow: none; margin-bottom: 15px; }
            .page-card { border: 1px solid #ddd; box-shadow: none; page-break-after: always; padding: 15px; }
        }
    </style>
</head>
<body>

<div class="container">

    <div class="header-card">
        <div>
            <div class="badge-course">COURSE: HUMAN-COMPUTER INTERACTION (HCI)</div>
            <div class="header-title">University of Abra (UA) Website Enhancement Portfolio</div>
            <div class="header-sub">UI/UX Redesign, Usability Enhancements, and Page-by-Page Visual Portfolio</div>
        </div>
        <div>
            <button onclick="window.print()" class="btn-print">🖨️ Print / Save as PDF</button>
        </div>
    </div>
"""

pages = [
    {
        "num": 1,
        "title": "Homepage (Primary Digital Gateway)",
        "img": "screenshots/01_homepage.png",
        "about": "The homepage serves as the primary digital front-door and welcoming landing page for prospective students, current enrollees, faculty, and stakeholders of the University of Abra.",
        "enh": "From a Human-Computer Interaction perspective, the original website (asist.edu.ph) was cluttered, non-responsive, and overwhelmed visitors with dense, unorganized text that violated basic visual hierarchy principles. In this enhanced version, I introduced a clean, modern aesthetic utilizing the university’s official Forest Green (#0D5C3A) and Gold (#F4C430) branding. I created a prominent Hero Section featuring three clear, high-contrast Call-to-Action (CTA) buttons ('Apply Online', 'Explore Courses', and 'Check Status') to significantly reduce cognitive friction and streamline user navigation. I also integrated quick-glance statistic cards (highlighting the 3 campuses, ₱0 tuition fee under RA 10931, and top licensure passing rates) and a dynamic campus announcement feed, all designed with a fully fluid, mobile-first responsive layout that adapts seamlessly across smartphones, tablets, and desktop displays."
    },
    {
        "num": 2,
        "title": "About the University (History, Campuses & Values)",
        "img": "screenshots/02_about_page.png",
        "about": "This page communicates the institutional profile of the university, detailing its transition under Republic Act No. 11574, campus specializations, official Vision, Mission, and the NEW ASIST Core Values.",
        "enh": "On the original website, institutional background was buried inside fragmented text blocks and hard-to-find PDF downloads, creating severe usability barriers for users seeking basic school information. To resolve this, I restructured the entire content architecture into an intuitive, modular layout with distinct visual callouts. I clearly separated the unique specializations of the three campuses (Lagangilang Main for smart agriculture and computing, Bangued for engineering, and La Paz for agro-technology) so visitors can easily understand their distinct academic thrusts. Furthermore, the Vision, Mission, and the 8 core values (Nobility, Entrepreneurship, Wisdom, Action, Sincerity, Integrity, Service, Teamwork) were organized into a high-contrast two-column card grid, enhancing scannability, legibility, and overall visual balance."
    },
    {
        "num": 3,
        "title": "Courses & Academic Programs Catalog",
        "img": "screenshots/03_courses_catalog.png",
        "about": "The Courses Catalog provides an exhaustive directory of all undergraduate and technical degree programs offered across the university.",
        "enh": "The legacy website displayed academic programs in long, static HTML tables that lumped all degrees together regardless of campus, making it frustrating and confusing for applicants to determine where a course was actually held. In this enhancement, I transitioned the layout into an interactive card-based catalog adhering to modern UI design standards. Each card highlights the program code (BSIT, BSA, BSCE, BSED), official title, college department, 4-year duration, and a green badge emphasizing the RA 10931 Free Higher Education coverage. Most importantly, each card incorporates a colored campus location tag and a direct 'Apply Online' button, establishing a direct, intuitive user flow from course exploration to application."
    },
    {
        "num": 4,
        "title": "Courses Filtered by Campus (Interactive Filtering)",
        "img": "screenshots/04_courses_filtered_bangued.png",
        "about": "Demonstrates the dynamic campus filtering mechanism, showing degree offerings filtered specifically for the Bangued Campus.",
        "enh": "In the original system, users had zero ability to filter or search for courses by location, forcing them to manually read through irrelevant degree lists. To enhance user control and efficiency—a core HCI heuristic—I designed an interactive campus filter dropdown. When a user selects 'Bangued Campus', the interface dynamically refreshes to display only the relevant engineering and industrial technology degrees (such as Civil, Mechanical, and Electrical Engineering). The dropdown automatically preserves the user's selected state, providing immediate visual feedback and drastically cutting the interaction time required for applicants to find programs available in their local municipality."
    },
    {
        "num": 5,
        "title": "Online Admission Application Form",
        "img": "screenshots/05_online_admission_form.png",
        "about": "A paperless digital admission application portal where incoming high school graduates and transferees can apply for enrollment online.",
        "enh": "The original website completely lacked any digital application mechanism, forcing applicants to travel in person to the registrar in Abra or deal with manual paper forms—a major friction point that caused long queues and excluded distant applicants. I designed an intuitive, user-friendly digital application form with clear input grouping, high-contrast labels, and built-in validation. The degree selection dropdown dynamically syncs with the university database to prevent invalid course choices. The form follows clean form-design best practices with ample spacing, accessible input fields, and an inviting submit button that simplifies the entire enrollment journey."
    },
    {
        "num": 6,
        "title": "Application Confirmation & Printable Slip",
        "img": "screenshots/06_admission_confirmation_slip.png",
        "about": "The digital confirmation receipt page displayed immediately after an applicant successfully submits their online admission form.",
        "enh": "In Human-Computer Interaction, immediate system feedback is critical for establishing user confidence and trust. The old system provided no digital confirmation whatsoever. In this enhancement, upon form submission, the system instantly generates an official Admission Reference Number (ARN) displayed prominently inside an eye-catching dashed container. It summarizes the applicant's submitted information and provides clear instructions for entrance examination day. Additionally, I added a prominent one-click 'Print Confirmation' button that triggers a clean print-optimized layout, allowing applicants to print their slip or save it as a PDF without any cluttered browser elements."
    },
    {
        "num": 7,
        "title": "Admission Status Tracker",
        "img": "screenshots/07_admission_status_tracker.png",
        "about": "A self-service inquiry tool that allows applicants to check their evaluation progress and examination schedule using their reference number.",
        "enh": "Previously, applicants had to repeatedly phone registrar landlines or travel to physical bulletin boards to know if their applications were approved. To satisfy the HCI principle of 'Visibility of System Status', I built an online tracker where applicants simply enter their reference number to view real-time results. The system communicates status through clear, color-coded status badges (Yellow for 'Pending Review', Blue for 'Qualified for Exam', and Green for 'Admitted'), paired with an official remarks box containing personalized evaluator instructions such as the assigned testing room and exam date. I also included clickable demo sample codes to allow effortless testing during usability reviews."
    },
    {
        "num": 8,
        "title": "Student Portal Login (SIAS)",
        "img": "screenshots/08_student_portal_login.png",
        "about": "The security gateway for enrolled students to access their Student Information and Accounting System (SIAS) accounts.",
        "enh": "On the old website, links to the student portal were often broken or pointed to intimidating raw IP addresses without proper SSL branding, confusing students and raising security concerns. In this enhanced version, I designed a cohesive institutional login portal styled with the official university logo, comforting green background accents, and clear form fields for Student ID and Password. To make usability evaluation and live demonstrations effortless, I added a '1-Click Demo Login' button that instantly signs in as sample student Maria Clarisse Santos, eliminating typing errors and allowing instant evaluation of the internal portal."
    },
    {
        "num": 9,
        "title": "Student Portal Dashboard (Academic Self-Service)",
        "img": "screenshots/09_student_portal_dashboard.png",
        "about": "The academic self-service portal for enrolled students, featuring profile info, enrolled subjects, midterm grades, semestral GWA, clearance checklist, and document downloads.",
        "enh": "The original SIAS was a dated, desktop-only system with cluttered tables, poor font scaling on mobile devices, and zero visual distinction for student accomplishments. In this enhancement, I transformed the portal into a modern dashboard that presents student data through clean visual hierarchy: an avatar profile header, an automated Semestral GWA indicator (1.38) with a prestigious 'Dean's List' honor badge, and a reassuring ₱0.00 tuition balance under RA 10931. I organized grades into an easily readable table with clear color badges, incorporated an interactive 5-office clearance progress checklist, and added instant download buttons for the Certificate of Registration (COR) and student handbook, drastically improving student satisfaction and self-service efficiency."
    },
    {
        "num": 10,
        "title": "Campus News & Bulletins Board",
        "img": "screenshots/10_campus_news.png",
        "about": "The official announcements and university press releases board keeping students, faculty, and the public informed.",
        "enh": "The legacy website’s news section suffered from information overload, presenting announcements as plain, unformatted walls of text without category tags or publication dates. For this enhancement, I implemented a card-based visual layout where each bulletin is neatly packaged with a category tag (Admissions, Academic, Campus Update), posting date, and concise summary. Important institutional achievements—such as the RA 11574 university transition and 100% board passing rates—are given visual prominence, making it effortless for visitors to scan, digest, and stay updated on university developments."
    },
    {
        "num": 11,
        "title": "Contact Us & Campus Directory",
        "img": "screenshots/11_contact_us.png",
        "about": "The contact information directory for all three campuses and an interactive public inquiry and feedback form.",
        "enh": "The old contact page listed only a single general telephone number that was frequently unattended, and offered no interactive messaging capability, forcing visitors to open third-party email clients. To improve user communication and accessibility, I organized a comprehensive directory detailing the physical addresses and active hotlines for the Lagangilang Main, Bangued, and La Paz campuses. Beside the directory, I created a responsive web contact form where users can directly submit inquiries with immediate on-screen visual confirmation, significantly lowering communication barriers for remote students and parents."
    },
    {
        "num": 12,
        "title": "Admissions Admin & Evaluator Console",
        "img": "screenshots/12_admin_evaluator_view.png",
        "about": "The administrative dashboard for admissions officers and faculty to evaluate applications, update statuses, assign exam rooms, and review citizen inquiries.",
        "enh": "From an HCI administrative workflow perspective, the university previously had no centralized web interface to manage applicant submissions, forcing evaluators to manually record paper applications into offline notebooks or disjointed spreadsheets. I designed an intuitive back-office dashboard featuring an instant application volume counter, a scannable applicant dossier table, and an inline status updater. Evaluators can effortlessly select an applicant's new status from a dropdown, type test room instructions, and save changes with a single click, providing immediate database synchronization and streamlining administrative decision-making."
    }
]

for p in pages:
    html_code += f"""
    <div class="page-card">
        <div class="page-head">
            <div class="page-num">PAGE 0{p['num']}</div>
            <div class="page-title">{p['title']}</div>
        </div>

        <div class="img-container">
            <img src="{p['img']}" alt="{p['title']} Picture">
            <div class="img-cap">Figure {p['num']}: Actual Interface Picture — {p['title']}</div>
        </div>

        <div class="about-box">
            <strong>About This Page:</strong> {p['about']}
        </div>

        <div class="enhancement-box">
            <div class="enhancement-head">HCI & Usability Enhancements Done:</div>
            <p class="enhancement-text">{p['enh']}</p>
        </div>
    </div>
    """

html_code += """
</div>
</body>
</html>
"""

with open("HCI_UA_Website_Enhancements.html", "w", encoding="utf-8") as f:
    f.write(html_code)

print("Generated HCI_UA_Website_Enhancements.html successfully")
