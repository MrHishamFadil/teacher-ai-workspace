# Automation Preparation

This folder is only a safe preparation area for future automation.

The current MVP does not:

- Call any paid AI API.
- Send emails.
- Collect student submissions.
- Store student personal data.
- Publish content without teacher review.

## Current scripts

The scripts in `automation/scripts` read `lessons-data.json` and print a clear plan of what could be generated later.

They are beginner-safe placeholders. Running them will not change the website.

## Future idea

Later, a teacher could keep lesson plans in Google Sheets. A GitHub Actions workflow could read the plan, create draft lesson pages, and ask the teacher to review them before publishing.

## Safety rule

Book PDFs and textbook pages must stay outside the public repository. Use them only as private teacher reference material when you are allowed to do so. Publish original explanations, worksheets, and revision tasks.
