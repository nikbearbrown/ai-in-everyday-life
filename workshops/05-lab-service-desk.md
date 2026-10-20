# 05. Lab: Service Desk

*Status: DRAFT, not yet dry-run. Small group, 40 minutes. Topic: AI for business customer service.*

## Executive summary

**What this is.** A group designs a customer-service assistant for a made-up small business and, more importantly, decides **exactly when it must stop and hand the customer to a human.** **Why run it.** Customer service is where most people meet AI every day, and where its failures are felt. The human skill this lab trains is **being with people**: care, trust, and knowing when a person has to take over. The tool skill is **Direct it**: a persona, rules and sample conversations that a bot actually follows. **What the group leaves with.** A written bot spec, sample dialogues (including two handoffs), a list of escalation triggers, a Catch Card, and a Driver's Ledger.

| | |
|---|---|
| **Time** | 40 minutes |
| **Group** | 4 students plus one coach |
| **Materials** | Driver's Canvas, scenario cards (below), one shared laptop with a general-purpose AI |
| **Tech** | Wi-Fi for AI. Paper fallback below. |

## The two jobs in this lab

- **Master it:** Direct it. Give the AI a role, rules and examples, and test it.
- **Keep it human:** Be with people. Decide which moments are the human's. Angry, grieving, confused and high-stakes moments are not for a script.

## Scenario cards (deal one)

A bakery with online orders. A small gym with memberships. A repair shop. A local airline-style travel desk. A student-run ticket sale. Each card lists a business, its three most common questions, and one "bad day" situation.

## Run of show

1. **Meet the customer (6 min). User hat.** Pick one person who calls on a bad day. Write a two-sentence portrait. What do they need *right now*, and what would make it worse?
2. **Spec the bot (8 min). Process hat.** Three lists: **Must match** (the business's real policies, a calm tone), **May decide** (phrasing), **Must stop and ask a human** (refunds above a limit, safety, complaints about a person, anything involving health, legal or money trouble, any customer who is upset after two tries). Write the handoff triggers as *testable conditions*. "If upset" is not testable; "if the customer uses any of these words or repeats the same question twice" is.
3. **Direct it (13 min).** A student drives. Give the AI the spec and ask for a persona plus six sample dialogues: four routine, two that must hand off. Run two of them against your own triggers. Does the bot hand off when it should? Does it *wrongly* hand off? Fix the spec, not just the output.
4. **Catch Card (6 min). Skeptic hat.** Find one place the bot made up a policy, over-promised, or sounded warm while saying nothing. Write what it said, what the business's real rule was, and how you checked.
5. **Driver's Ledger and pitch outline (7 min).** Fill the ledger. The line that matters: *what happens to the customer at the handoff, and who is waiting for them?* A handoff to nobody is a failure.

## Debrief questions

- Where does a bot save a person time? Where does it cost them dignity?
- Which trigger would you remove if you had to pick? What would break?
- Who signs off the refund policy the bot is allowed to quote?

## Unplugged fallback

The coach plays the bot with the group's written spec on the table. Students play customers. Run the two handoff scenes as role-play; the "human" steps in at the triggers.

## Watch-outs

- Real businesses and real customer data are off the table. Everything is made up.
- A bot that says "I understand how frustrating that must be" is simulating care. It is not feeling it. Say that plainly and move on; do not argue philosophy.
- A bot that refuses to ever hand off is not "safe." Find the triggers.
