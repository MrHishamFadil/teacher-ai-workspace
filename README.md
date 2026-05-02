# Smart Path Study Hub

Smart Path Study Hub is a simple educational website for Grade 3, Grade 4, Grade 5, and Grade 6 students.

It is designed for a teacher with limited coding experience who wants a low-cost study hub that can be hosted for free on GitHub Pages.

## What this project does now

- Shows a clean home page for the study hub.
- Organizes content by grade, unit, and lesson.
- Includes one complete sample Grade 5 lesson.
- Includes one sample weekly revision page.
- Includes a writing practice page.
- Uses original placeholder content only.
- Uses static HTML, CSS, JavaScript, and JSON.
- Includes beginner-safe automation preparation notes.

## What this project does not do yet

- It does not use a paid backend.
- It does not use a database.
- It does not have a login system.
- It does not collect student personal data.
- It does not send emails.
- It does not call paid AI APIs.
- It does not publish copied textbook pages.

## How to enable GitHub Pages

1. Open the repository on GitHub.
2. Click **Settings**.
3. Click **Pages** in the left menu.
4. Under **Build and deployment**, choose **Deploy from a branch**.
5. Choose the `main` branch.
6. Choose the `/root` folder.
7. Click **Save**.
8. Wait a few minutes for GitHub to publish the website.

After GitHub Pages is enabled, GitHub will show you the website link.

## How to preview the site on your computer

Open `index.html` in your browser.

You can also use a simple local server later, but it is not required for this MVP.

## How to add a new lesson manually

The easiest beginner method:

1. Copy an existing lesson file, for example `grades/grade-5/unit-1/lesson-1.html`.
2. Paste it into the correct grade and unit folder.
3. Rename the file, for example `lesson-2.html`.
4. Open the file and update the title, objectives, vocabulary, grammar, explanation, practice questions, and parent note.
5. Add a link to the new lesson from the grade page.
6. Update `lessons-data.json` with the new lesson information.

Important: write original content in your own words. Do not copy textbook pages.

## How to add a YouTube video

1. Find a video you are allowed to share.
2. Click **Share** on YouTube.
3. Click **Embed**.
4. Copy the embed code.
5. Replace the video placeholder in the lesson page.

If you are not sure whether a video is allowed, link to it instead of copying or downloading it.

## How to add a worksheet link

1. Create an original worksheet.
2. Upload it somewhere safe, such as Google Drive.
3. Set the sharing permission carefully.
4. Copy the share link.
5. Replace the worksheet placeholder link in the lesson page.

Do not upload worksheets that include copied textbook pages.

## How to update `lessons-data.json`

`lessons-data.json` is a list of lesson information. Each lesson has:

- `id`
- `grade`
- `unit`
- `lessonNumber`
- `title`
- `objectives`
- `vocabulary`
- `grammarFocus`
- `videoUrl`
- `worksheetUrl`
- `quizUrl`
- `status`
- `pagePath`

When you add a new lesson page, add a matching lesson object to this file.

## Suggested teacher content workflow

1. Choose the grade and unit.
2. Write lesson objectives.
3. Draft an original teacher explanation.
4. Add vocabulary and grammar focus.
5. Create original practice questions.
6. Add a worksheet link if ready.
7. Add a video link if ready.
8. Review everything as the teacher.
9. Publish only after checking copyright and student safety.

## Copyright safety rules

- Do not upload full textbook PDFs.
- Do not copy textbook pages.
- Do not copy answer keys from books.
- Use original explanations.
- Use curriculum-aligned but original worksheets.
- Keep book PDFs outside this public GitHub repository.
- Use any local book PDFs only as private teacher reference material if you are allowed to use them.

## Student privacy rules

- Do not publish student names.
- Do not publish student emails.
- Do not publish student grades or private feedback.
- Do not publish student writing submissions.
- Keep student data outside this public GitHub repository.

## Future automation roadmap

### Phase 1: Static study hub

Build and review the manual website structure.

### Phase 2: Add real teacher-reviewed lessons

Replace placeholder content with original teacher-reviewed lessons.

### Phase 3: Connect Google Sheets as content planner

Use a private spreadsheet to plan lessons, vocabulary, videos, worksheets, and review status.

### Phase 4: Use GitHub Actions to generate draft lesson pages

Automation can create draft pages, but the teacher should review before publishing.

### Phase 5: Add student writing feedback workflow using Google Forms and Sheets

Students submit writing through a private form. The public website should not collect personal data.

### Phase 6: Add teacher approval before sending feedback

AI can draft feedback, but the teacher approves it before students receive it.

### Phase 7: Consider n8n or VPS only after the workflow proves valuable

Do not pay for extra infrastructure until the manual workflow is useful.

### Phase 8: Monetization options

Possible future options include worksheet packs, revision sessions, premium resources, or school licensing.

## Current file structure

```text
index.html
styles.css
script.js
lessons-data.json
about.html
writing-practice.html
grades/
  grade-3/
  grade-4/
  grade-5/
  grade-6/
automation/
  prompts/
  scripts/
.github/
  workflows/
```
