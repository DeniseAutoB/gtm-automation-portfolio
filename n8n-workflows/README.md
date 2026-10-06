# n8n Automatiion Workflows

**One-line outcome:** [What it does and what it achieves]

## The problem
[Who it's for and what problem it solves, 2-3 sentences]

## What I built
[Short description of the build and the steps in the flow]

**Workflow:** [Trigger] > [Step] > [Step] > [Output]

## Tools used
- [Tool 1]
- [Tool 2]

## Demo
- Loom walkthrough: [link]
- Screenshot: [add image]

## Files in this folder
- [`file-name`](file-name): [what it is]

## Results
[What it produced. If this is sample or test data, say so clearly.]

## What I'd improve
- [Next step or limitation]
- [Next step or limitation]

## Daily Streak Tracker
Runs every night at 9pm (Jamaica time). Checks my builds repo for commits that day, calculates a work streak with one rest day per week, logs it to a Google Sheet, and posts the result to Slack.

Flow: Schedule > GitHub commits > Day summary > Read log > Calculate streak > Log to sheet > Slack

File: [daily-streak-tracker.json](daily-streak-tracker.json)
