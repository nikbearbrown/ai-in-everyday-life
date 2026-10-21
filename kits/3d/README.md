# Kit: the Blender ship (3D model)

## Executive summary

**What this is.** A cartoon delivery spaceship that is **built entirely by a script in Blender**, from one settings file (`params.json`). Your group makes a variant by editing the settings: new colors, one new proportion. After each change a one-click script rebuilds the ship and shows a picture in about 20 seconds. **Why it works for an hour.** A simple AI only has to edit a few lines of a settings file, not model anything. **Status.** The rebuild loop was run and tested once, by Claude, on one Mac with Blender 5.1.2. It has not been tried with Muse, Grok or Codex, or with students.

## The kit is not in this repository

- **The ship folder** (the script, the settings, the logo images, the rebuild button) is a variant of a model that Grok Bot built, in the course repo. It is a copyrighted character design, and the school-logo variant uses a university's marks, so the folder is not published here. The facilitator supplies it from their own files, for classroom use. The unmodified base model, by Grok Bot, is public in the course repo: <https://github.com/nikbearbrown/csye-7270-building-virtual-environments> (the `blender/planet-express-ship-grok` folder).
- **Blender** is free from blender.org. It is a large download. Install it on the coach's laptop before the day, and write down the version you tested.

## What is in the ship folder

| File | What it does |
|---|---|
| `build.command` | Double-click it. It rebuilds the ship from the settings and opens a picture. About 11 seconds in testing |
| `scripts/params.json` | The settings. The `colors` block changes the hull, fin, wings, trim and stripe |
| `scripts/build_pe.py` | The script that builds the ship. Nobody needs to edit it |
| `scripts/final.py` | Renders pictures and exports a 3D file |
| `scripts/logo.png`, `scripts/logo_m.png` | The logo for the right and left faces of the fin. They are not copies: one is the logo mirrored, the other turned 180 degrees |
| `README.md` | What was done and what was not |

## The settings the group changes

In `params.json`, the colors block names each part's color and glossiness, for example the hull, the dark parts (fin, wings, legs), the trim, the stripe and the glass. Each entry is a color code and a number. A group can also change one proportion, found in the same file.

## Starter prompt

> Here is the colors block of a settings file for a 3D model, in JSON: [paste]. I want a variant for [who it is for], and it should feel [two or three words]. Give me a new colors block with the same names and the same structure, using real hex color codes. Change nothing else. Tell me what each color is for.

## Things to catch

A color code that is not a color. Invalid JSON (a missing comma). A palette that does not match the brief. A change on one side of the ship that does not show on the other. A logo that changed on only one side of the fin.

## Limits

The ship's shape is the original model's. A group changes how it looks, not how it is built. The tested loop used one AI; do not claim any other AI can do it until it has been tried. The logo swap needs an image tool to make the mirrored copy, so it is a coach stretch, not a group task.

## Optional stretch: the real 3D-print parts

[`reference-viewer.html`](reference-viewer.html) is a tested one-page viewer for a set of 26 STL part files of a 3D-printable version of the same ship. The files are not included (their license is unknown). It was tested once on one machine. It is for a coach who wants a group to compare the AI's variant against real parts.
