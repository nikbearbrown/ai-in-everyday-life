# Student pack: your own journey game

## Executive summary

**What this is.** Everything you need to turn a small browser game into your own. The game is a small text adventure where you guide a team along a trail, managing a few supplies, with random events. You use a free AI to change its theme, its numbers and one feature. **It runs from one file in your browser.** **Make yours different.** Each person picks a different journey and numbers, then you play each other's.

## What you have

A folder with `index.html` and a `js` folder. Open `index.html` in a browser to play the original: a startup team growing to 1,000 users, with developers who need food, servers and random events. Your coach also has a finished example that turns it into "your first year at university". A small AI made it from a plain request, so yours is doable.

## Step 1. Pick your journey (one each)

A first year at university (the tested one) · launching a food truck · a band on tour · a colony on Mars · a club's season · your own idea. Decide: what is the goal, what are the three or four supplies, and what are the things that can go wrong?

## Step 2. Pick your numbers

These are in `js/Constants.js`. The first number is the original. Change one or two, then play.

| Setting | What it does | Original | Try |
|---|---|---|---|
| `GAME_SPEED` | Milliseconds per tick (smaller is faster) | 800 | 400 |
| `EVENT_PROBABILITY` | Chance of a random event each tick | 0.15 | 0.3 (more events) or 0.05 (fewer). More events is not automatically harder: in one tested version it made the game easier, so play it and see |
| `DAY_PER_STEP` | How much time passes each tick | 0.2 | 0.4 (shorter game) |
| `FINAL_USERS` | The goal | 1000 | 500 (easier) or 2000 (hard) |

If you rename the supplies, ask the AI to rename them everywhere.

## Step 3. Ask the AI

Open each file, copy everything, and paste all the files into one chat. Then:

> Here is a small JavaScript game in plain HTML and JavaScript: [paste index.html and every file in js/]. Change it into [your journey]. Rename the stats, the places and the events to fit. Keep the same structure and keep it working as plain HTML and JavaScript with no libraries. Give me each file you changed, complete, and tell me which files you changed. Also add a high score saved in the browser.

## Step 4. Save and play

**Predict first.** Before you reload, write down whether you think the game will get easier or harder, and how often a player will win. Then play and compare. In one tested version, more events made the game easier.

Replace the files with the AI's, save, and reload the page. Play a full game.

## Check yourself

- Click every button. Win once and lose once.
- Does any number go negative? Does any text say "undefined" or "NaN"?
- Can the player lose through no fault of their own? Is a win possible?
- Does anything still mention the old theme?
- Reload the page. Does the high score stay?
- Is it fair? Say what "fair" means for your game.

## If it breaks

Open the browser's console (right-click, Inspect, Console), copy the red message, and paste it back with "fix only this."

## Save tokens

Free accounts have limits, and these files are about 17 KB together. Paste them once, then ask for one change at a time. Ask for only the changed file back.
