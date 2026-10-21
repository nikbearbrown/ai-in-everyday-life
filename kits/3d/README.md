# Kit: the delivery ship (3D model)

## Executive summary

**What this is.** A 3D-printable model of a teal cartoon delivery spaceship (the Planet Express ship from *Futurama*), supplied as 26 separate part files (STL, the format 3D printers use), plus a set of AI-generated reference pictures of the ship. Your group has an AI build a viewer in a web page that loads the real parts, lets you switch parts on and off, explode the ship apart and read each part's size, and then compares the real geometry to the AI pictures to find what the pictures got wrong. **Why it works for an hour.** The parts are real and named (hull, wings, dome, turret, nozzle, windows, logos), the ship is instantly recognizable, and the files are *print parts, not an assembled ship*, so there is a real puzzle in figuring out where things go. **Status.** One reference viewer was built and tested once; nobody has run this as a workshop.

## The files are not in this repository

- **The 26 STL files** are a designer's 3D-print model (the files are named "GOODesign"). The license is unknown, so they are not included. The facilitator copies the folder to the laptop from their own files. Confirm the license and where it came from before the day, and keep it classroom-only.
- **The reference pictures** are AI-generated (made with an image generator and then transformed). They are **not** ground truth. That is the point of the track: the pictures are fluent, and the files are real.

## What the files are (from the one inspection so far)

- **26 files, about 35 MB, about 737,000 triangles.** A modern laptop loads them in well under a second.
- **Named parts:** Hull_Front, Hull_Rear, Wing_Left, Wing_Right, Wing_Top, Dome, Turret_A and B, Nozzle_A and B, Window, Window_Frame, Cargo_A and B, Landing_Gear, Stair_A and B, Logo_A, B and C, Ring, Red_Parts, Silver_Parts_A and B, and covers.
- **Not an assembled ship.** The hull halves and most body parts sit around the origin, but the wings, landing gear and silver parts are laid out off to the side, the way they sit on a print bed. Putting the ship together is part of the job.
- **Units are not labeled.** The sizes look like millimeters (hull front plus rear is about 51 × 137 × 90), but nothing in the files says so. Treat any AI statement of units as a claim to check.

## What the group needs

- The STL folder on the coach's laptop, and the AI-generated pictures printed or on a screen.
- A laptop with an AI chat and a web browser.
- Wi-Fi while the page loads (the 3D code comes from a CDN). Test this on the real network, and decide how to run it offline.

## Method

1. **Look.** Sort the AI pictures into front, side, top and back views. List the parts you can see.
2. **Read the file list.** Which parts exist as files? Which things in the pictures have no part? Which parts have no picture?
3. **Spec the viewer.** Write three lists: what it must do (load the chosen files from the computer, show every part, let you switch parts on and off), what the AI may decide (colors, layout, controls), and what it must ask about (units, where parts go).
4. **Build.** Ask the AI for one HTML file. Open it, choose the STL files, and look.
5. **Catch.** Compare the AI pictures to the real parts. Find at least two things the pictures got wrong. Check the AI's claims about units and sizes against the file.
6. **Stretch.** Add a way to move a part (sliders for x, y, z) and assemble the wings and landing gear by eye. That decision is yours, and the pictures that guide it are themselves AI-made.

## Starter prompt

> I have 26 STL files of a 3D-printable spaceship, with names like Hull_Front, Wing_Left, Dome and Nozzle_A. Write ONE HTML file that lets me choose the .stl files from my computer and shows them together in a 3D scene I can rotate. Use three.js version 0.160.0 from the jsdelivr CDN with an import map, plus STLLoader and OrbitControls from its addons. Set the camera up-axis to Z. Give each part a color based on its name, a checkbox to show or hide it, and its size next to its name. Add an Explode slider and a Reset view button. The files must stay on my computer. At the end, tell me what you assumed about the units.

## Things to catch

A picture that shows a part the files do not have. A part the files have that no picture shows. A size the AI quoted that does not match the part. A units claim with no evidence. A logo that is flipped or reversed. A hull that is upright, because it is laid out for printing.

## Limits

A viewer, not a modeling tool. It shows geometry; it does not repair or edit it. Big files can be slow on a weak laptop.

## Coach reference

[`reference-viewer.html`](reference-viewer.html) is one finished viewer built to this prompt. Do not show it to the group before they have built their own.
