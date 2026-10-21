# Kit: the starship plans (3D model)

## Executive summary

**What this is.** A set of 2D engineering plans of a famous fictional starship (the original Enterprise, top, side, front and cutaway views). Your group builds a rotatable 3D model of it in a web browser from those plans, using an AI to write the code. **Why it works for an hour.** The ship is built from simple shapes (a saucer disc, a neck, a hull cylinder, two engine pods on pylons), the plans show every proportion, and everyone recognizes the result. **Status.** Not run as a workshop yet.

## The plans are not in this repository

The plans are copyrighted franchise material. This repository does not include them. The facilitator brings a printed copy and a screen copy from their own files, for classroom use only. **Do not post the plans or the model's images publicly.** The model is a classroom study, not a product.

The author's local copy (14 images, about 450 pixels wide, poster plus 13 sheets) is small. A larger scan would make the measuring step easier. Ask the author whether one exists.

## What the group needs

- A printed plan, a ruler, a pencil.
- A laptop with an AI chat that accepts a photo of a plan, and a web browser.
- Wi-Fi while building (the 3D library loads from the internet). To run offline afterward, save the library file next to the page. Test this before the day.

## Method

1. **Measure from the plan.** On the top view, measure the saucer diameter and call it **1.0**. Measure everything else against it: ship length, hull diameter, nacelle length, pylon length, saucer thickness from the side view. Write the numbers on the plan.
2. **Spec the model.** List the parts and their proportions. Write three lists: what the model must match, what the AI may decide, and what it must ask about.
3. **Build.** Ask the AI for one HTML file with a rotatable 3D scene using the numbers and the photo.
4. **Compare.** Hold the model next to the plan. Find where the AI invented a proportion.

## Starter prompt

> Here is a photo of the top and side views of a starship, and my measurements, with the saucer diameter as 1.0: [your numbers]. Write ONE HTML file using three.js from a CDN, with OrbitControls so I can rotate it. Build the saucer, the neck, the secondary hull, the two engine pods and their pylons from simple shapes, to those proportions. At the end, list every proportion you invented that I did not give you.

## Limits

A scene built from simple shapes, not a sculpted model. It will look like a toy. That is fine, and it is the point of comparing it to the plan.
