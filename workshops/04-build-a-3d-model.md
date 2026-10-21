# 04. Build: A 3D Model (the Delivery Ship)

*Status: DRAFT. A reference viewer was built and tested once; nobody has run this as a workshop. One group of about five, 65 minutes.*

## Executive summary

**What this is.** A group has an AI build a web page that loads the 26 real part files of a 3D-printable cartoon delivery spaceship, then explores it: switch parts on and off, explode it apart, read each part's size. Then they compare the real geometry to AI-generated pictures of the same ship and find what the pictures got wrong. **Why this track.** It is the most visual and the most fun, and it shows the central skill plainly: **the pictures look right and are not the real thing, and you can find that out because you have the real files.** **What the group leaves with.** A working 3D viewer, a list of what the AI pictures invented, and a ledger.

| | |
|---|---|
| **Kit** | [kits/3d](../kits/3d/README.md) |
| **Tool** | The STL files on the coach's laptop, the AI-generated pictures, a browser, and an AI chat |
| **Roles** | Driver (keyboard), Reader (the file list and the pictures), Checker (compares pictures to parts), Demo captain |

## The two jobs in this track

- **Master it:** Spec it and direct it. Describe a tool precisely enough that the AI builds it in one go, then fix what is wrong.
- **Keep it human:** Compare the AI's pictures and claims to the real files. Decide where parts go. Say what is verified and what is not.

## Prep (coach, before the day)

Copy the STL folder to the laptop. Confirm where the files came from and that classroom use is fine; they are not in the public repository. Run the starter prompt once with your tool, and record what it got wrong. Open the result, choose all the files, and check it works on the real Wi-Fi. Look at [the reference viewer](../kits/3d/reference-viewer.html) but do not show it to the group. Bring a finished example.

## Run of show (65 minutes)

1. **Look (5 min).** Show the AI pictures. Sort them into front, side, top and back. List the parts you can see: body, stripe, windows, dome, tail fin, side fins, engine.
2. **Read the file list (7 min).** Look at the 26 file names. Which things in the pictures have a file? Which files have no picture? What does that tell you?
3. **Spec it (5 min).** Three lists for the viewer: **must do** (load the files from the computer, show every part, switch parts on and off), **may decide** (colors, controls), **must ask me** (units, where parts go).
4. **Build (28 min).** The driver sends the starter prompt. Open the page. Choose the STL files. Rotate it. Rotate the driver every eight minutes. Fix one thing at a time and reload.
5. **Catch (10 min).** Compare the pictures to the real parts. Find two things the pictures got wrong. Check the AI's claim about units and sizes against the file names and the sizes shown. Write the Catch Card.
6. **Ledger and demo prep (10 min).** Fill the ledger. Include one line: **what the viewer is not** (a viewer, not an assembled model). Stretch if there is time: add sliders to move a part and assemble the wings by eye.

## The things to catch

A picture that shows a part with no file. A part with no picture. A units claim with no evidence. A hull that sits upright because the file is laid out for printing. Wings and landing gear sitting off to one side. A reversed logo.

## Debrief questions

- Which was more reliable, the pictures or the files? How do you know?
- What did the AI assume when it built the page? How would you have found out?
- Where did you decide something the AI could not?

## Unplugged fallback

If the AI chat or the page fails, print the file list and the pictures and do the comparison on paper: which parts exist, which do not, and a guess at where each part goes. Name what you did not get to run.

## Watch-outs

- The files are classroom-only and not in the public repository.
- The pictures are AI-generated. Do not call them photos or official reference.
- The page needs the internet to load the 3D code. Test before the day.
