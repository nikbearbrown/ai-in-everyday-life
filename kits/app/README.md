# Kit: the Oregon Trail remake (web app)

## Executive summary

**What this is.** A small text-adventure game, a remake of the classic *Oregon Trail*, written in plain HTML, CSS and JavaScript. It runs by opening one file in a browser. Your group changes it with an AI into a new journey, with new events, new resources and a new feature. **Why it works for an hour.** The whole game is seven small files (about 17 KB of code), so you can paste all of it into an AI chat. **Status.** Not run as a workshop yet. Someone needs to open it in a browser and play it through once before the day.

## Get it

- Repository: <https://github.com/nsafai/Oregon-Trail-Game> (a third-party remake, MIT license, copyright 2019 Mitchell). Use **Code, Download ZIP**.
- To run: unzip, then double-click `index.html`. No install, no server, no Wi-Fi once downloaded.
- To edit: the game logic is in `js/` (`Caravan.js`, `Constants.js`, `Event.js`, `Game.js`, `Init.js`, `UI.js`). The README says the original tutorial code had bugs that were fixed, so expect rough edges. That is a feature for this workshop.
- MIT requires the license notice to stay with the code. Keep the `LICENSE` file in your folder.

## Build menu (pick one for the hour)

1. **A new journey.** Reskin the whole game: a road trip, a first year at university, a startup's first year, a trip to Mars. Change the resources (food and oxen become budget, sleep, battery), the places and the events.
2. **A new feature.** Add a high-score board (saved in the browser), a travel log, a difficulty setting, or a "rest day" action.
3. **Make it fair.** Play ten turns. Can you win? Can you lose through no fault of your own? Change the numbers until it is fair, and say what "fair" means.

## Starter prompt

> Here is a small JavaScript game, Oregon Trail style: [paste index.html and the files in js/]. Change it into [new journey]. Keep it working as plain HTML and JavaScript with no libraries. Tell me which files you changed and give me each complete file.

## Test list ("click every button")

Open the game fresh. Play a full game. Click every button. Win once. Lose once. Reload the page. Does a saved score survive? Does anything say "undefined" or "NaN"? Does a resource go negative?

## Limits

No accounts, no shared score board between players, and nothing is saved except in that one browser. Everything is made up; use no real personal data.
