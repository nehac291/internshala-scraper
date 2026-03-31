# Internshala Internship Scraper
This project is a Python-based web scraper that attempts to extract internship listings from Internshala.

## Objective
The goal of this project is to understand web scraping concepts and extract useful data such as internship titles and company names from a website.

## Technologies Used
- Python
- Playwright (for dynamic web scraping)
- CSV (for data storage)

## Features
- Opens Internshala website using browser automation
- Attempts to extract internship titles and company names
- Stores the extracted data into a CSV file

## How It Works
- Playwright is used to open and render the Internshala website
- The script waits for the page to load completely
- It tries to locate internship cards and extract relevant data
- The data is then saved into `internships.csv`

## Challenges Faced
Internshala is a dynamic website and uses JavaScript to load content. It may also have anti-scraping mechanisms, which can sometimes result in empty data extraction.

## Learning Outcomes
- Learned difference between static and dynamic web scraping
- Gained experience with Playwright for browser automation
- Understood challenges of scraping real-world websites

# Note
Due to dynamic rendering and possible anti-scraping restrictions, the output may vary.

## Output
The extracted data is stored in:
