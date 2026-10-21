# AI in Everyday Life: workshop materials

## Executive summary

**What this is.** The complete materials for a hands-on workshop called **AI in Everyday Life: Solving Real-World Problems Through Innovation**. It is a workshop, and this repository is where the materials live so anyone can download and run it. It was designed for about 20 undergraduates from mixed technical and non-technical backgrounds, taught by graduate students. Students do not write code by hand: the AI writes it, and the students direct, run and check it. It was first prepared for a visit to the Northeastern University Information Systems department (SEIS) on November 6, 2026.

**Why use it.** The world has changed. AI now produces a first draft of almost anything in seconds, and students are graduating into that. So the workshop teaches two things together and refuses to teach one without the other:

1. **Master the tools.** Spec it, direct it, check it, chain it. Students keep their hands on the keyboard.
2. **Keep what is irreducibly human.** Notice the right problem, smell a wrong answer, be with people, decide together, own the consequence.

**What you get.** A short intro, then four hands-on builds of about an hour each: an **email agent** that drafts replies but stops for a person's approval, a **game** (the Claude Jumpman platformer, in Godot), a **3D model** (a new variant of a Blender-built cartoon ship, made by editing its settings), and a **web app** (an Oregon Trail remake). Plus a demo round, a close, a run of show for 90 minutes, 2 hours or a half day, and a guide for the people who coach. Starter files are in [kits/](kits/).

**Status.** These are drafts. No workshop has been run with a live audience yet. Expect to adapt them, and please tell us what breaks.

## What the finished builds look like

| Agent | Game |
|---|---|
| ![Email assistant test run](images/agent/inbox-copilot-test-run.jpg) | ![Platformer, course complete](images/game/game-complete.jpg) |
| **3D model** | **Web app** |
| ![Ship variants](images/3d/ship-palette-variants.jpg) | ![First-year game running](images/app/first-year-game-running.jpg) |

These are real outputs: the platformer is a screen from the game itself; the ship, the web game and the assistant test were made and checked in testing. See "What has been tested" below for exactly what that means.

## How to use this

1. Read [THE-THROUGH-LINE.md](THE-THROUGH-LINE.md). It is the idea behind everything.
2. Pick a length in [RUN-OF-SHOW.md](RUN-OF-SHOW.md).
3. Send students [PRE-WORK.md](PRE-WORK.md): each makes a free AI account ahead of time.
4. Give each coach [FACILITATOR-GUIDE.md](FACILITATOR-GUIDE.md) and their track. Each track has a one-page student pack in [kits/](kits/).
5. Have each coach run their build once, on the real laptop, before the real session.

**To download:** use the green **Code** button, then **Download ZIP**, or clone the repository.

## The workshops

| # | Workshop | What it is |
|---|---|---|
| [01](workshops/01-intro-the-world-has-changed.md) | Intro: The World Has Changed | A live build, a catch round, the two hands |
| [02](workshops/02-build-an-agent.md) | Build: An Agent | Email assistant with a human approval gate |
| [03](workshops/03-build-a-game.md) | Build: A Game | Change the Claude Jumpman platformer |
| [04](workshops/04-build-a-3d-model.md) | Build: A 3D Model | Make a variant of a Blender-built ship |
| [05](workshops/05-build-a-web-app.md) | Build: A Web App | Remake Oregon Trail as your own journey |
| [06](workshops/06-the-ledger-and-the-demos.md) | The Driver's Ledger and the Demos | One-page record and a live demo round |
| [07](workshops/07-close-your-next-step.md) | Close: Your Next Step | Graduate study in information systems |

## What has been tested

Not with students and not with the free plan. As a rough stand-in, a small Claude model (Haiku), given only the starter material, was tried on four tracks, and Claude checked its output. These are single runs, not guarantees.

- **Agent:** answered the two easy emails from the knowledge sheet and flagged all four hard ones (refund, injury, out-of-scope request, an attack email). It never claimed to have sent anything. All six emails were in one prompt, which may have helped it.
- **3D (Blender):** wrote three valid color blocks that matched their briefs. All three rendered correctly. The Northeastern seal stayed on the fin in each, because only colors were changed.
- **3D (parts viewer):** wrote a one-page viewer that loaded all 26 part files, with correct sizes and no console errors.
- **Web app:** reskinned the game into a first year at university and added a saved high score. It started, ran events and a shop with no console errors. Nobody played a full game.
- **Game (Godot):** only an automatic start-up check with changed numbers. No person played it.

## Notes

- The ideas are teaching lenses from the author's courses and writing. They are not research findings, and the materials quote no statistics.
- Any program facts in the close (workshop 07) must be confirmed with your own program office. The repo invents none.
- The 3D track's ship folder is a variant of a copyrighted character design and is not in this repository. The Oregon Trail code is a third-party MIT project, linked and not copied. The Claude Jumpman game is linked, and its repository carries no license file yet.
- Facilitators appear by first name and last initial only. No students are ever named.

## License

Creative Commons Attribution 4.0 (CC BY 4.0). Use it, adapt it, share it, and credit Nik Bear Brown.
