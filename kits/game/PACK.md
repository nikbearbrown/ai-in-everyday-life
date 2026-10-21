# Student pack: your own version of the game

## Executive summary

**What this is.** Everything you need to change how the platformer *feels*, by editing a handful of numbers, and then to try a bigger change. Your coach has Godot open on the laptop. You ask a free AI for the new numbers, paste them into one small file, and press play. **Make yours different.** Each person picks a different "feel" below, then you swap and play each other's.

## Step 1. Pick your feel (one each)

The file is `godot/features/player/tuning.gd`. These are the numbers. Every value was kept to the same names and structure. **A quick automatic start-up check ran without errors with the Moon-jump numbers and a speed of 220. No person has played any of these, so some may make the level impossible. That is a good thing to find.**

| Number | What it does | Original | Moon jump | Sprinter | Heavy |
|---|---|---|---|---|---|
| `speed` | Top running speed | 160 | 160 | 220 | 130 |
| `jump_velocity` | How hard the jump launches (more negative is higher) | -320 | -420 | -320 | -420 |
| `gravity` | How fast you fall | 960 | 480 | 960 | 1400 |
| `acceleration` | How fast you reach top speed | 1280 | 1280 | 1800 | 900 |

Leave `deceleration`, `terminal_velocity`, `coyote_ticks` and `buffer_ticks` alone for now.

**What was tested (by a script, not a person).** The project's own route test finishes the level on the original numbers and on the Heavy numbers. On the **Moon jump** numbers it fails: the scripted jump no longer lands in a 64-pixel gap, around the middle of the level. That does not prove the level is impossible. A search over other takeoff points found some that do finish it at moon numbers. And jump -420 with the *original* gravity sails over the flag. Some of the project's older unit tests also fail on moon numbers, because they were written for the original feel. So a changed feel can break a level even when the game starts without errors. Whether it is fun is still a question only a player can answer.

## Step 2. Ask the AI

> This is a small Godot 4.7 file in GDScript, for how a platformer character moves: [paste tuning.gd]. I want it to feel like [Moon jump / Sprinter / Heavy / your idea]. Give me the complete new file with the same variable names and types. Change only the numbers. Then tell me in one sentence what each change does to the game.

## Step 3. Apply and play

Replace the contents of `tuning.gd` with the AI's file, save, and press **F5** in Godot. Play for one minute. If Godot shows an error, copy it exactly and paste it back to the AI.

## Step 4. A bigger change (if you finish)

The whole level is `godot/levels/shipping_lane.json`. It holds the platforms, the gaps, 24 tokens and 4 bugs. Ask your AI for one change, such as moving tokens or adding a platform over a gap, and paste the file back. Change one thing at a time.

## Check yourself

- Can the game still be finished? Try to reach the flag.
- Did the AI change only what you asked?
- Watch someone from another group play. Where do they die? Where do they stop? What did they try that you did not expect?

## If it breaks

Paste the exact error back and say "fix only this." Or put the original number back.

## Save tokens

Free accounts have limits. Paste only the one small file you are changing.
