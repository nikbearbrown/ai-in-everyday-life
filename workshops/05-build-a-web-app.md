# 05. Build: A Web App (Oregon Trail)

*Status: DRAFT, not yet dry-run. One group of about five, 65 minutes.*

## Executive summary

**What this is.** A group opens a small Oregon Trail remake that runs in a web browser from one file, and changes it with an AI into a journey of their own: a road trip, a first year at university, a startup, a trip to Mars. They add a feature, play it to the end, and test whether it is fair. **Why this track.** It is the easiest to start and the easiest to see working. It also shows something only a human decides: **what the game counts as success, and what counts as a loss.** **What the group leaves with.** A playable web app on a laptop, a test log, and a note on what "fair" meant to them.

| | |
|---|---|
| **Kit** | [kits/app](../kits/app/README.md) |
| **Student pack** | [kits/app/PACK.md](../kits/app/PACK.md). Each student picks a different journey and numbers |
| **Tool** | A web browser and an AI chat |
| **Roles** | Driver (keyboard), Designer (the new journey), Tester (plays), Demo captain |

## The two jobs in this track

- **Master it:** Direct it. Paste a whole small program, ask for a precise change, and run it.
- **Keep it human:** The rules of the world are a human choice. What you count, what you reward and what you punish say what you value.

## Prep (coach, before the day)

Download the game. Open `index.html`. Play to the end. Read the files in `js/` and find where the events and the resources are defined. Make one change with the AI end to end. Bring a finished example.

## Run of show (65 minutes)

1. **Play it (5 min).** Everyone plays two minutes. What is the goal? What can go wrong? Who decides?
2. **Spec it (7 min).** Pick the new journey, the new resources, and one new feature from the kit. Write the three lists: **must keep** (it must still run as one file, the turn structure), **may change** (names, events, numbers), **must ask me** (the win and lose conditions).
3. **Build (28 min).** The driver pastes the game into the AI with the starter prompt, saves the new files, and reloads the page. Rotate the driver every eight minutes. Run after every change.
4. **Catch (10 min).** Click every button. Win once. Lose once. Reload. Look for "undefined," numbers that go negative, a loss that the player could not have avoided. Fix one. Write the Catch Card.
5. **Ledger and demo prep (10 min).** Fill the ledger. Decide what to show live.
6. **Buffer (5 min).**

## The things to catch

A resource that goes below zero. A button that does nothing. A trip you cannot lose. A trip you cannot win. An event that fires every turn. A reskin that quietly kept the old theme in some text.

## Debrief questions

- What does your game reward? Is that what you meant to teach?
- What would a stranger find unfair?
- Which rule did you choose, and which did the AI choose?

## Unplugged fallback

Everything runs offline once downloaded. If the AI chat fails, change the numbers in `Constants.js` by hand and see what happens.

## Watch-outs

- Keep the MIT license file with the code.
- Make up the data. No real names, no real places a person could be harmed by.
- Nothing saves anywhere but that one browser.
