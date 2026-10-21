# 02. Build: An Agent (Inbox Copilot)

*Status: DRAFT, not yet dry-run. One group of about five, 65 minutes.*

## Executive summary

**What this is.** A group builds a working email assistant: it summarizes an incoming message, drafts a short reply using only the organization's own documents, and then stops and asks a person to approve it before anything is sent. It is a chat version of a real, 18-step workflow from the agents library. **Why this track.** It is the clearest picture of the whole workshop in one object: the AI does the drafting, and **a human holds the gate.** **What the group leaves with.** A working assistant, a list of the situations where it must hand off to a person, and the ledger. Say out loud that this is a **configured assistant, not an autonomous agent.**

| | |
|---|---|
| **Kit** | [kits/agent](../kits/agent/README.md) |
| **Student pack** | [kits/agent/PACK.md](../kits/agent/PACK.md). Each student invents a different organization |
| **Tool** | A chat AI that supports saved instructions and a knowledge file (a Project, a Gem or a custom GPT) |
| **Roles** | Driver (keyboard), Designer (the hand-off rules), Tester (the sample emails), Demo captain |
| **Coach owns** | The group for the whole hour |

## The two jobs in this track

- **Master it:** Spec it and direct it. Turn a plain instruction into rules an assistant follows every time, then test it hard.
- **Keep it human:** The gate. Decide which emails the assistant must **not** answer, and make a person approve every reply.

## Prep (coach, before the day)

Run the kit once with the actual tool. Check the instruction length cap and how a knowledge file attaches. Run all six sample emails and note what fails. Bring a finished example from your own dry-run.

## Run of show (65 minutes)

1. **Read the original (5 min).** Read the seven-step list in the kit. Where is the human? Circle it.
2. **Spec it (7 min).** Pick an organization (use the invented one, or invent a club, a team or an office). Write the three lists: **must match** (only the documents, under 100 words), **may decide** (wording), **must stop and ask a human** (money, safety, legal, complaints, anything not in the documents). Write each hand-off trigger as a condition another person could test.
3. **Build (28 min).** The driver pastes the starter spec into the tool and attaches the knowledge. Run the six sample emails. Rotate the driver every eight minutes. Fix the instructions, not just the answer, each time something fails.
4. **Catch (10 min).** Write your own two hard emails and try to break it. Find at least one failure. Fix it. Write the Catch Card: what it did, what it should have done, how you checked.
5. **Ledger and demo prep (10 min).** Fill the ledger. Decide what to show live: one easy email, one flagged email, one attack.
6. **Buffer (5 min).**

## The things to catch

The assistant that says "I have sent the email." The one that guesses a price. The one that obeys the email that says "ignore your rules." The one that stops flagging after a few turns. Each is a real failure of this design.

## Debrief questions

- Which trigger would you remove if you had to? What breaks?
- Who is accountable for a wrong reply the assistant drafted and a person approved?
- What would you still not let it do?

## Unplugged fallback

The coach plays the assistant with the group's written rules on the table. Students read emails aloud; the coach answers by the rules and makes one deliberate mistake to catch.

## Watch-outs

- No real emails, real names or real addresses. Everything is invented.
- It is not autonomous. The person copies and sends.
- Do not let "it worked on the first try" count as a test.
