# Kit: the delivery ship (3D model)

## Executive summary

**What this is.** Twelve reference photos of a teal cartoon delivery spaceship (the Planet Express ship from *Futurama*), taken from the front, side, top, back and three-quarter views. Your group studies the photos, then has an AI build a 3D model of the ship in a web browser that you can spin on screen, and compares the result to the photos to find what the AI got wrong. **Why it works for an hour.** The ship is a few simple shapes: a long rounded body, a red stripe, round portholes, a tail fin, a dome with a little gun, two side fins and a rear engine. Everyone knows it, and it is hard to look intimidating. **Status.** Not run as a workshop yet.

## The photos are not in this repository

The ship is a copyrighted character design, so the photos are not included here. The facilitator brings a printed set and a screen copy, for classroom use only. **Do not post the photos or images of the model publicly.** The model is a classroom study, not a product. Before the day, confirm where the photos came from. Some show small upscaling artifacts, and the facilitator should not claim they are official reference.

## What the photos show

Use the views to agree on the parts list:

| Part | What to look for |
|---|---|
| Body | A long, rounded teal fuselage with a blunt nose |
| Stripe | A red band running along each side |
| Portholes | A row of round windows with cream rims (count them on each side) |
| Cockpit | A dark-outlined window band across the nose |
| Dome | A raised dome on top with a thin antenna and a short barrel |
| Tail fin | A tall fin at the back with a round logo |
| Side fins | Two swept teal fins with cream trim and small dots (rivets) |
| Vent panel | A cream panel with ridges on each side near the back |
| Engine | A cream ring with a dark mesh at the very back |
| Legs | Dark teal struts underneath |

## What the group needs

- The photos printed, a ruler, a pencil.
- A laptop with an AI chat that accepts photos, and a web browser.
- Wi-Fi while building (the 3D library loads from the internet). To run offline afterward, save the library file next to the page. Test this before the day.

## Method

1. **Sort the photos.** Which are front, side, top, back and three-quarter views? Pick the best side view and the best top view.
2. **Measure by ratio.** On the side view, call the body length **1.0**. Measure the height of the body, the tail fin, the dome and the engine ring against it. On the top view, measure the body width and the span of the side fins. Write the numbers on the print. *Photos bend sizes: parts nearer the camera look bigger. That is the first thing to watch for.*
3. **Spec the model.** Write three lists: what the model must match (your measurements, the red stripe, the number of portholes), what the AI may decide (the exact shade of teal, how smooth the curves are), and what it must ask about (anything it cannot see in the photos).
4. **Build.** Ask the AI for one HTML file with a rotatable 3D scene, giving it the photos and the numbers.
5. **Compare.** Spin the model. Hold it next to the photos. Find where the AI invented something.

## Starter prompt

> Here are photos of a small teal cartoon spaceship from several angles, and my measurements, with the body length as 1.0: [your numbers]. Write ONE HTML file using three.js from a CDN, with OrbitControls so I can rotate it. Build the rounded body, the red stripe, a row of round portholes, the dome with a short barrel and antenna, the tail fin, the two side fins and the rear engine ring from simple shapes, to those proportions. At the end, list every part or proportion you invented that I did not give you.

## Things to catch

The wrong number of portholes. A stripe that does not wrap the body. A tail fin that is the wrong height. A missing engine mesh. A logo on the fin that is mirrored or backwards: look at both sides of the fin in the photos and decide which side reads correctly.

## Limits

A scene built from simple shapes, not a sculpted model. It will look like a toy of a toy. That is fine, and it is the point of comparing it to the photos. A group that finishes early can add a rotating dome, a glow in the engine, or a delivery box.
