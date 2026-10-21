# Kit: the approval-gated email agent

## Executive summary

**What this is.** A real, moderately complex agent design, rebuilt as a configured AI assistant. An incoming email goes in. The agent summarizes it, writes a short reply using only the organization's own documents, and then **stops and asks a person to approve or reject the draft before anything is sent.** Your group builds a working version for an invented organization. **Why this agent.** It is useful for anyone who runs a club, a team or a small business. It has several steps, not one. And its most important feature is the human gate in the middle, which is exactly what the workshop teaches. **Status.** The original design is a collected workflow that has not been run in our tests. The chat version here has not been run as a workshop yet.

## Where it comes from

The original is the workflow *AI Email processing autoresponder with approval (Yes/No)*, in the agents library at bearbrown.co/agents (slug `approval-gated-email`). It was collected from the public n8n workflow collection by Zie619 (MIT license; attribution is kept with the workflow). It has 18 nodes. The agents library marks it "source available, not runtime tested."

What the original does, in order:

1. **Receive** a new email.
2. **Convert** it to clean text so the AI reads it better.
3. **Summarize** it.
4. **Look up** the organization's own documents (a knowledge base).
5. **Write** a reply of no more than 100 words, in a professional tone, from those documents.
6. **Send the draft to a human** with a Yes / No button.
7. **If Yes,** send it. **If No,** go back and write it again.

## What a chat assistant can and cannot do

A configured chat assistant cannot read your inbox or send email. It can do steps 3 to 7 as a conversation: you paste in an email, it summarizes, drafts, and then waits for you to say **APPROVE** or **REVISE**. Say this out loud: *it is a configured assistant, not an autonomous agent. The "sending" is you, copying the draft into your email.*

## What is in this kit

| File | What it is |
|---|---|
| `starter-spec.md` | The instructions to paste into the assistant (a Claude Project, a Gemini Gem, or a custom GPT) |
| `club-knowledge.md` | The invented organization's documents, to upload or paste as the assistant's knowledge |
| `sample-emails.md` | Six test emails, including the hard ones |

## Before the day

Run it yourself once with the tool you will use on the day. Check how long the instructions can be (some tools cap the instruction box). Confirm the knowledge file uploads or pastes cleanly. Note anything that surprises you.

## Limits

Everything about the organization is invented. Never paste real emails, names or addresses.
