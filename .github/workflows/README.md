# Future GitHub Actions Ideas

No live paid AI workflow is included in this MVP.

This folder explains possible future workflows only.

## Manual lesson draft workflow

A future manual workflow could let the teacher click a button in GitHub Actions and generate lesson page drafts from `lessons-data.json`.

Important safety step: generated drafts should open as a pull request, not publish directly.

## Scheduled weekly revision generation

A future scheduled workflow could prepare weekly revision drafts every week.

Important safety step: drafts must wait for teacher review before students see them.

## Google Sheets integration

A future workflow could read lesson planning rows from a private Google Sheet.

The public GitHub repository should not contain student names, emails, grades, private submissions, or full textbook content.

## Teacher approval before publishing

The safest workflow is:

1. Teacher updates lesson plan.
2. Automation creates draft pages.
3. Teacher reviews accuracy and copyright safety.
4. Teacher merges the pull request.
5. GitHub Pages publishes the approved site.
