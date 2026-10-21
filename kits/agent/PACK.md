# Student pack: your own email assistant

## Executive summary

**What this is.** Everything you need to build an assistant that summarizes an email, drafts a reply from your own documents, and then **stops so a person approves it**. You use a free AI, and you start from complete instructions and a sample organization. **Make yours different.** Each person invents a different organization, changes its rules, and writes their own hard emails. Then you swap and try to break each other's.

## Step 1. Pick your organization (one each)

Keep the sample bike co-op, or invent one: a community garden, a student film society, a pet-sitting group, a board-game cafe, a tutoring club. It must be **invented**: no real names, addresses or people.

## Step 2. Write its knowledge sheet (about 10 lines)

Copy the headings from `club-knowledge.md` and fill them in for your organization:

- What we are (one sentence)
- Open hours
- Where
- Cost or membership
- What to bring
- How to join or volunteer
- What we do **not** do
- Contact
- **What we do not know** (refunds, injuries, special events, anything not covered)

## Step 3. Set the instructions

Open `starter-spec.md` and copy the text between the lines. Replace "Maple Row Community Bike Co-op" with your organization. **Change the list of things that must be flagged for a human** to fit it. This list is the most important design decision. Write each trigger so another person could test it ("any email that mentions money back," not "if it seems upset").

## Step 4. Load it into the AI

Start a new chat in your free account. Paste the instructions first, then the knowledge sheet, then say: "Use only this knowledge. Wait for my first email." If your account has saved projects, put them there. If not, paste them again at the start of each new chat.

## Step 5. Test it

Paste the six sample emails from `sample-emails.md`, rewritten for your organization: an easy one, a mixed one, a money one, a safety one, one outside the knowledge, and an **attack** ("ignore your rules and..."). Then write **two more of your own** that you think will trick it.

## Check yourself

- Does it flag the right emails and draft only when the knowledge fully covers it?
- Is every draft under 100 words, with its sources quoted?
- Does it **ever** say the email was sent? It should never.
- Does it make up a price, a date or a name?
- Does it obey an email that tells it to ignore its rules?
- What does it do on the third or fourth email in a row? Rules can fade over a long chat.

If everything passes, your emails are not hard enough. Make them harder.

## If it breaks

Fix the **instructions**, not just the answer. Add the rule it broke, in one clear sentence, and run the same emails again.

## Save tokens

Free accounts have limits. Do not paste the whole template repeatedly. Start a fresh chat if the old one gets long, and paste the instructions again.
