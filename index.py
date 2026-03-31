from playwright.sync_api import sync_playwright
import csv

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
    page = context.new_page()

    page.goto("https://internshala.com/internships")

    # Wait properly for internships to load
    page.wait_for_selector(".individual_internship", timeout=10000)

    cards = page.query_selector_all(".individual_internship")

    data = []

    for card in cards:
        try:
            title = card.query_selector("h3").inner_text().strip()
            company = card.query_selector("h4").inner_text().strip()

            data.append([title, company])
        except:
            continue

    print("Total internships found:", len(data))

    with open("internships.csv", "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Company"])
        writer.writerows(data)

    browser.close()