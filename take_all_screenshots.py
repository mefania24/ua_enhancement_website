import os
import time
import shutil
import threading
import subprocess
from app import app

PROJECT_SCREENSHOTS = r"C:\Users\ASUS\.gemini\antigravity\scratch\ua_enhancement_website\screenshots"
ARTIFACT_SCREENSHOTS = r"C:\Users\ASUS\.gemini\antigravity\brain\9614cd06-b6dd-4721-b78c-34dc4cdc7afe\screenshots"
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PORT = 5055
BASE_URL = f"http://127.0.0.1:{PORT}"

def run_server():
    app.run(port=PORT, debug=False, use_reloader=False)

def capture(url, filename, window_size="1280,850"):
    dest1 = os.path.join(PROJECT_SCREENSHOTS, filename)
    dest2 = os.path.join(ARTIFACT_SCREENSHOTS, filename)
    
    cmd = [
        CHROME_PATH,
        "--headless",
        "--disable-gpu",
        f"--window-size={window_size}",
        f"--screenshot={dest1}",
        url
    ]
    subprocess.run(cmd, check=True)
    shutil.copy2(dest1, dest2)
    print(f"Captured: {filename} from {url}")

def main():
    # Start Flask server in background thread
    t = threading.Thread(target=run_server, daemon=True)
    t.start()
    time.sleep(2)  # Give server time to bind

    pages = [
        ("/", "01_homepage.png", "1280,950"),
        ("/about", "02_about_page.png", "1280,950"),
        ("/courses", "03_courses_catalog.png", "1280,950"),
        ("/courses?campus=Bangued", "04_courses_filtered_bangued.png", "1280,850"),
        ("/apply", "05_online_admission_form.png", "1280,950"),
        ("/apply/success/UA-2026-101", "06_admission_confirmation_slip.png", "1280,900"),
        ("/status", "07_admission_status_tracker.png", "1280,850"),
        ("/portal", "08_student_portal_login.png", "1280,800"),
        ("/portal/demo", "09_student_portal_dashboard.png", "1280,1050"),
        ("/news", "10_campus_news.png", "1280,850"),
        ("/contact", "11_contact_us.png", "1280,900"),
        ("/admin", "12_admin_evaluator_view.png", "1280,950")
    ]

    for path, filename, size in pages:
        full_url = BASE_URL + path
        capture(full_url, filename, size)
        time.sleep(0.5)

    print("\nALL 12 PAGE SCREENSHOTS GENERATED AND COPIED SUCCESSFULLY!")

if __name__ == "__main__":
    main()
