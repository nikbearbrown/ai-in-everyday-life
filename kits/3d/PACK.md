# Student pack: your own ship

## Executive summary

**What this is.** Everything you need to make your own version of the cartoon ship. Your coach has the ship folder. You change a few numbers and colors, a script rebuilds the ship, and you see it in about 20 seconds. **Why it is easy.** The ship is built from one settings file. You never model anything. You tell a free AI what you want, paste its answer into the file, and press a button. **Make yours different.** Each person in the group picks a different theme, palette and tweak, then you line the ships up.

## Pick your theme (one each)

Beach brand · night-shift hospital team · robotics club · your own idea (a band, a bakery, a sports team, a made-up company).

## Step 1. Colors

Tested palettes (these built and rendered correctly). Paste one into the `colors` block of `params.json`, or ask your AI for a new one:

- **Beach:** hull `#1FB6C1`, fin `#0E6E7A`, trim `#FFF6E5`, accent `#E9C98F`, stripe `#FF6B4A`, portholes `#FFE08A`, glass `#9ADBEB`, dome `#F5B841`, dark `#1B2A44`, engine `#2E2E2E`.
- **Night shift:** hull `#8FB7B0`, fin `#4A5D6B`, trim `#EEF1F0`, accent `#CFC8BC`, stripe `#A87F7A`, portholes `#D9E0E3`, glass `#B8CAD2`, dome `#C5D3DA`, dark `#2A3136`, engine `#3A3F43`.
- **Green and gold:** hull `#0B6E3B`, fin `#053B22`, trim `#F7F3E3`, accent `#C9A227`, stripe `#FFC72C`, portholes `#D8DED9`, glass `#A8C8B8`, dome `#C9D6CF`, dark `#151A17`, engine `#0E1210`.

Each color in the file is written as `["#hexcode", glossiness]`, for example `["#1FB6C1", 0.35]`. Keep the structure exactly.

**Prompt to paste into your AI:**

> Here is the colors block of a settings file for a 3D model, in JSON: [paste the block]. I want a ship for [your theme], and it should feel [two or three words]. Give me a new colors block with the same names and the same structure, using real six-digit hex codes. Change nothing else. Tell me what each color is for.

## Step 2. One number

Pick one. Each of these was tested and the ship still built. The first number is the original.

| Setting (in `params.json`) | Original | Try |
|---|---|---|
| `turret` → `ant_h` (antenna height) | 0.85 | 2.0 |
| `turret` → `gun` → `len` (gun length) | 0.75 | 1.4 |
| `turret` → `dome_r` (dome size) | 0.27 | 0.4 |
| `engine` → `n_pods` (engine pods) | 12 | 6 |
| `fin` → `thick` (fin thickness) | 0.16 | 0.4 |

Change **one number at a time** and rebuild, so you know which change did what.

## Step 3. Logo (optional)

The `logos` folder has three plain emblems: star, wave and bolt. Copy **both** `logo.png` and `logo_m.png` from one folder over the two in `scripts`. Copying only one changes only one side of the fin: the other side keeps the old logo. If your theme uses a real school's or company's marks, ask your coach first.

## Step 4. Build and look

**Predict first.** Before you press the button, write down which parts of the ship your change will affect and which it will leave alone. After the picture opens, check your list: did anything change that you did not expect?

Double-click `build.command`. After about 20 seconds a picture opens. Open the side view and the fin as well: the front can look right while the back is wrong.

## Check yourself

- Is every color a real hex code (a `#` and six letters or numbers)?
- Is the file still valid? One missing comma breaks it.
- Does the picture match the words you gave? ("Calm" should not come back neon.)
- Did the AI change only what you asked?
- Does the emblem read correctly from both sides?

## If it breaks

Paste the exact error from `scripts/build.log` back to your AI and say "fix only this." Or undo your last change and try again.

## Save tokens

Free accounts have limits. Paste only the colors block, not the whole file. Do not re-paste what the AI already has.
