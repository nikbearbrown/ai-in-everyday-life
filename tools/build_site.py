#!/usr/bin/env python3
"""Build the workshop site into docs/ (GitHub Pages). SEIS brand: a unit of the Northeastern brand.

Brand laws used (brutalist.art/brands/seis.md, brands/neu.md): white ground, NU black ink, NU Red #C8102E as
emphasis only, neutral #545454 secondary, hairline #E3E3E3, Lato throughout with regular-weight sentence-case
headings, no gradients, no drop shadows, red on every page, SEIS lockup with clear space, real finished
pictures. Run from the repo root: python3 tools/build_site.py
"""
from pathlib import Path
import html

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
REPO = "https://github.com/nikbearbrown/ai-in-everyday-life"
BLOB = REPO + "/blob/main/"

CSS = """
@font-face{font-family:Lato;src:url(%(p)sassets/fonts/Lato-Regular.ttf) format('truetype');font-weight:400;font-display:swap}
@font-face{font-family:Lato;src:url(%(p)sassets/fonts/Lato-Bold.ttf) format('truetype');font-weight:700;font-display:swap}
:root{--red:#C8102E;--ink:#000;--ground:#fff;--neutral:#545454;--line:#E3E3E3}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%%}
body{margin:0;background:var(--ground);color:var(--ink);font:400 18px/1.55 Lato,'Helvetica Neue',Arial,sans-serif}
a{color:var(--ink);text-decoration:underline;text-underline-offset:3px;text-decoration-thickness:1px}
a:hover,a:focus{color:var(--red)}
.skip{position:absolute;left:-999px;top:0;background:var(--ink);color:#fff;padding:8px 12px}
.skip:focus{left:8px;top:8px;z-index:10}
header.top{border-bottom:4px solid var(--red)}
.bar{max-width:1080px;margin:0 auto;padding:20px 16px 16px;display:flex;flex-wrap:wrap;gap:16px 32px;align-items:center;justify-content:space-between}
.bar img{display:block;height:56px;width:auto}
nav a{margin-right:20px;font-size:16px;text-decoration:none;border-bottom:1px solid transparent}
nav a:hover,nav a[aria-current]{border-bottom-color:var(--red);color:var(--ink)}
main{max-width:1080px;margin:0 auto;padding:40px 16px 64px}
h1,h2,h3{font-weight:400;line-height:1.15;margin:0}
h1{font-size:clamp(34px,5.6vw,58px);margin-bottom:20px}
h2{font-size:clamp(26px,3.6vw,36px);margin:56px 0 16px;padding-top:24px;border-top:1px solid var(--line)}
h3{font-size:22px;margin:0 0 8px}
p{margin:0 0 16px;max-width:68ch}
.lede{font-size:clamp(20px,2.4vw,24px);color:var(--ink);max-width:60ch}
.small{font-size:15px;color:var(--neutral)}
.rule{width:64px;height:4px;background:var(--red);margin:0 0 24px}
.hour{list-style:none;margin:0;padding:0;border-top:1px solid var(--line)}
.hour li{display:grid;grid-template-columns:96px 1fr;gap:16px;padding:14px 0;border-bottom:1px solid var(--line)}
.hour b{font-weight:700}
.hour .t{color:var(--red);font-weight:700}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:24px;margin-top:24px}
.card{border:1px solid var(--line);display:flex;flex-direction:column;text-decoration:none}
.card:hover{border-color:var(--red);color:var(--ink)}
.card img{display:block;width:100%%;aspect-ratio:16/9;object-fit:cover;border-bottom:1px solid var(--line)}
.card div{padding:16px 16px 20px}
.card p{margin:0;font-size:16px;color:var(--neutral)}
.card .go{display:inline-block;margin-top:12px;color:var(--ink);font-weight:700;border-bottom:2px solid var(--red)}
figure{margin:24px 0}
figure img{display:block;width:100%%;max-width:900px;border:1px solid var(--line)}
figcaption{font-size:15px;color:var(--neutral);margin-top:8px;max-width:68ch}
.moves{counter-reset:m;list-style:none;padding:0;margin:0}
.moves li{counter-increment:m;padding:16px 0 16px 48px;position:relative;border-bottom:1px solid var(--line)}
.moves li::before{content:counter(m);position:absolute;left:0;top:14px;width:32px;height:32px;border:2px solid var(--red);color:var(--red);font-weight:700;text-align:center;line-height:28px}
.moves b{font-weight:700}
.note{border-left:4px solid var(--red);padding:4px 0 4px 16px;margin:24px 0;max-width:68ch}
.btn{display:inline-block;background:var(--red);color:#fff;text-decoration:none;padding:12px 20px;font-weight:700;margin:8px 12px 8px 0}
.btn:hover,.btn:focus{background:var(--ink);color:#fff}
.btn.alt{background:#fff;color:var(--ink);border:2px solid var(--ink)}
.btn.alt:hover{border-color:var(--red);color:var(--red);background:#fff}
ul.plain{margin:0 0 16px;padding-left:20px;max-width:68ch}
ul.plain li{margin-bottom:8px}
footer{border-top:1px solid var(--line)}
footer .in{max-width:1080px;margin:0 auto;padding:24px 16px 40px;display:flex;flex-wrap:wrap;gap:16px 32px;align-items:center;justify-content:space-between;font-size:15px;color:var(--neutral)}
footer img{height:36px;width:auto;display:block}
@media(max-width:600px){body{font-size:17px}.hour li{grid-template-columns:72px 1fr}main{padding-top:28px}}
"""


def page(title, body, depth=0, current=""):
    p = "../" * depth
    nav = [("index.html", "Today", "today"), ("index.html#hour", "The hour", "hour"),
           ("index.html#choices", "Your choices", "choices"), ("prework.html", "Before you come", "prework"),
           ("coaches.html", "For coaches", "coaches")]
    nav_html = "".join(
        f'<a href="{p}{h}"{" aria-current=page" if k == current else ""}>{html.escape(t)}</a>' for h, t, k in nav)
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="A hands-on workshop: pick one of four builds, make it with Claude, and talk about what you made.">
<style>{CSS % {'p': p}}</style></head><body>
<a class="skip" href="#main">Skip to content</a>
<header class="top"><div class="bar">
<a href="{p}index.html" aria-label="SEIS, Northeastern University, home"><img src="{p}assets/brand/seis-logo.png" alt="Northeastern University, Software Engineering and Information Systems"></a>
<nav aria-label="Main">{nav_html}</nav></div></header>
<main id="main">
{body}
</main>
<footer><div class="in"><div><img src="{p}assets/brand/seis-button-logo.jpg" alt="SEIS"></div>
<div>AI in Everyday Life. A hands-on workshop. Materials are free to use and adapt (CC BY 4.0).<br>
<a href="{REPO}">All the materials on GitHub</a></div></div></footer>
</body></html>"""


TRACKS = [
    dict(slug="agent", name="An assistant that stops and asks", img="inbox-copilot-test-run.jpg",
         alt="A test run of the email assistant: two drafted replies and four emails flagged for a human",
         make="An email assistant for a small club you invent. You paste in an email. It summarizes it, drafts a short reply using only your club's own notes, and then stops so a person can approve it. Anything risky it flags for a human.",
         fun="Invent any organization: a community garden, a film society, a pet-sitting group, a board-game café. Decide what your assistant must never answer. Then write the emails most likely to trick it.",
         opens="The Claude app, in a new chat. Your club's notes in a short document.",
         moves=[("Look", "Read the sample club and the six test emails. Which ones should the assistant refuse to answer?"),
                ("Spec it", "Write what the assistant must match, may decide, and must stop and ask about. Write each stop as a rule someone else could test. Then write your prediction: for each test email, draft or flag?"),
                ("Build", "Paste your spec and your club's notes into Claude. Paste the emails one at a time."),
                ("Catch", "Compare what it did with your predictions. Write two emails of your own to break it. Find one real failure and fix the instructions, not just the answer."),
                ("Ledger", "Write down what the AI did, what you checked, who signs, and what you did not check.")],
         bring="The email that broke it, the rule you added, and one thing you would still not let it do.",
         pack="kits/agent/PACK.md"),
    dict(slug="game", name="A game's feel is a few numbers", img="game-complete.jpg",
         alt="The Course complete screen of a small platformer starring the Claude mascot",
         make="A changed version of a small platformer game starring the Claude mascot. A handful of numbers decide how it feels. You change them, run the game, and find out whether the level can still be finished.",
         fun="Make the jump floaty like the moon, the runner fast, or the character heavy. Then change the level itself: move the tokens, add a gap, change how the bugs move.",
         opens="The Godot game engine (free) on your group's laptop, with the game open, and the Claude app.",
         moves=[("Look", "Play the game for two minutes. What would you change?"),
                ("Spec it", "Pick one feel. Write what must stay the same (the controls, the goal) and what you may change. Then write your prediction: how will it feel, and can the level still be finished?"),
                ("Build", "Give Claude the small file with the numbers and your request. Paste its answer in and press play."),
                ("Catch", "Watch someone from another group play without speaking. Where do they stop or fall? Was the level still finishable, as you predicted?"),
                ("Ledger", "Write down what the AI did, what you checked, who signs, and what you did not check.")],
         bring="What the other player did that you did not expect, and whether it was fun.",
         pack="kits/game/PACK.md"),
    dict(slug="ship", name="Make your own spaceship", img="ship-palette-variants.jpg",
         alt="Four versions of the same cartoon spaceship in different color schemes",
         make="A cartoon spaceship, built in Blender by a script from one settings file. The ship you start with is only a default. Change its colors, its proportions and its emblem, or ask Claude to build a completely different spaceship.",
         fun="A beach brand, a hospital night shift, a robotics club, a band, a bakery. Keep the ship or invent a new one: different shape, different engines, anything. The moves stay the same; the ship does not have to.",
         opens="Blender (free) on your group's laptop, the ship folder, and the Claude app.",
         moves=[("Look", "Open the picture of the starting ship and find the colors in the settings file."),
                ("Spec it", "Write who your ship is for and how it should feel. Say what must stay and what may change. Then write your prediction: which parts will this change affect, and which will it leave alone?"),
                ("Build", "Ask Claude for a new colors block, paste it in, and press the rebuild button. About twenty seconds."),
                ("Catch", "Check your list of predicted changes. Look at the ship from the other side. Is every color a real color code? Is the emblem right on both sides?"),
                ("Ledger", "Write down what the AI did, what you checked, who signs, and what you did not check.")],
         bring="The thing you only noticed by looking at it from the other side.",
         pack="kits/3d/PACK.md"),
    dict(slug="web", name="Your own journey game", img="first-year-game-running.jpg",
         alt="A browser game about a first year at university, showing credits, motivation, sleep and money",
         make="A small journey game that runs in your web browser from one file. It starts as a classic trail game. You turn it into your own journey, change its numbers, and test whether it is fair.",
         fun="A food truck season, a band on tour, a colony on Mars, a club's year. Decide what counts as winning, because the game only knows the rules you chose.",
         opens="A web browser and the Claude app. The game's files in one folder.",
         moves=[("Look", "Play the starting game for a few minutes. What is the goal, and what can go wrong?"),
                ("Spec it", "Pick your journey, your supplies and one new feature. Say what must stay working. Then write your prediction: will the game get easier or harder, and how often will a player win?"),
                ("Build", "Paste the game's files into Claude with your request. Save its files and reload the page."),
                ("Catch", "Compare with your prediction. Click every button. Win once and lose once. Look for numbers below zero and words that still belong to the old theme."),
                ("Ledger", "Write down what the AI did, what you checked, who signs, and what you did not check.")],
         bring="What your game rewards, and whether that is what you meant it to teach.",
         pack="kits/app/PACK.md"),
]


def moves_html(moves):
    return '<ol class="moves">' + "".join(
        f"<li><b>{html.escape(a)}.</b> {html.escape(b)}</li>" for a, b in moves) + "</ol>"


def build():
    DOCS.mkdir(exist_ok=True)
    (DOCS / "tracks").mkdir(exist_ok=True)
    cards = "".join(
        f'<a class="card" href="tracks/{t["slug"]}.html"><img src="assets/img/{t["img"]}" alt="{html.escape(t["alt"])}">'
        f'<div><h3>{html.escape(t["name"])}</h3><p>{html.escape(t["make"].split(". ")[0])}.</p>'
        f'<span class="go">See this one</span></div></a>' for t in TRACKS)
    index = f"""
<div class="rule"></div>
<h1>What are we doing today?</h1>
<p class="lede">For the next hour, you and a small group will make something real with Claude. You choose what. At the end, each group shows what it made, and then we talk about it.</p>
<p>The world has changed: the first draft of almost anything now costs nothing. So today is about two things. Getting good at using the tools. And keeping the parts only a person can do: choosing the right problem, noticing a wrong answer, and putting your name on the result.</p>
<p><a class="btn" href="#choices">Your four choices</a><a class="btn alt" href="prework.html">Before you come</a></p>

<h2 id="hour">The hour</h2>
<p>This is the two-hour plan: a short start, then the hour of building, then the demos and the talk. Your session may be shorter; the moves stay the same.</p>
<ul class="hour">
<li><span class="t">20 min</span><div><b>Start.</b> A student builds something live, we try to catch the AI being wrong, and you see a finished example of each choice.</div></li>
<li><span class="t">5 min</span><div><b>Choose.</b> Pick one of the four builds. Groups of about five.</div></li>
<li><span class="t">65 min</span><div><b>Make it.</b> Five moves: look, spec it, build, catch, ledger. One person types, the group directs, and you swap every eight minutes.</div></li>
<li><span class="t">20 min</span><div><b>Show it.</b> Each group starts with what it caught, then runs what it made, live, and reads its ledger.</div></li>
<li><span class="t">10 min</span><div><b>Talk.</b> What did you make? What surprised you? What would you do next?</div></li>
</ul>

<h2 id="choices">Choose one of four</h2>
<p>Each group makes one of these. They are different on purpose. None is the main one.</p>
<div class="grid">{cards}</div>

<h2>Make it your own</h2>
<p>Whatever you pick, the version we show you is only a default. Build a completely different spaceship. Make a game about something you care about. Invent an assistant for a club that does not exist. The five moves stay the same, and everything else is yours. Have fun with it.</p>
<figure><img src="assets/img/ship-front34.jpg" alt="A cartoon spaceship in red, black and white"><figcaption>One ship, from the starting build. Four groups will make four very different ones.</figcaption></figure>

<h2>What happens at the end</h2>
<ul class="plain">
<li>Each group gets four minutes. It starts with what it caught: one thing the AI got wrong and how you found it. Then it runs its build, live, and reads its one-page ledger.</li>
<li>The ledger has four parts: what the AI did, what you checked and how, what a person decided and signs, and one honest line about what you did not check.</li>
<li>Then we close in two parts: each person says one thing they would trust the AI with and one thing they would not, and after a short break there is information about graduate study at SEIS.</li>
<li>You leave with your build and the materials to make more.</li>
</ul>
<p class="note">This workshop has not been run with students yet. The builds were tested by running them, not by people using them. If something breaks, that is useful, and we want to hear about it.</p>
"""
    (DOCS / "index.html").write_text(page("AI in Everyday Life: a hands-on workshop", index, 0, "today"))

    for t in TRACKS:
        body = f"""
<div class="rule"></div>
<p class="small"><a href="../index.html#choices">All four choices</a></p>
<h1>{html.escape(t['name'])}</h1>
<p class="lede">{html.escape(t['make'])}</p>
<figure><img src="../assets/img/{t['img']}" alt="{html.escape(t['alt'])}"><figcaption>This is what the finished build looks like. Yours will be different.</figcaption></figure>
<h2>What to have open</h2><p>{html.escape(t['opens'])}</p>
<h2>The hour, in five moves</h2>
{moves_html(t['moves'])}
<h2>Make it yours</h2><p>{html.escape(t['fun'])}</p>
<h2>Bring this to the talk</h2><p>{html.escape(t['bring'])}</p>
<p><a class="btn" href="{BLOB}{t['pack']}">Open the one-page pack</a><a class="btn alt" href="../index.html#choices">Back to the choices</a></p>
<p class="note">Nobody has run this build with students yet. It was tested by running it, and where a small AI model did the work, the pack says so.</p>
"""
        (DOCS / "tracks" / f"{t['slug']}.html").write_text(page(t["name"], body, 1, "choices"))

    pre = """
<div class="rule"></div>
<h1>Before you come</h1>
<p class="lede">One short task, about five minutes, so we can start building right away.</p>
<ol class="moves">
<li><b>Make a free Claude account.</b> Use your own email. Accounts are for adults, so check the sign-up terms. Free accounts have usage limits that reset after a few hours, and what the free plan includes can change, so look at what yours has.</li>
<li><b>Test it.</b> Send one message, for example: "In two sentences, what does a spaceship's tail fin do in a cartoon?" Check that it answers.</li>
<li><b>Bring a laptop</b> with a modern web browser, and its charger. If you cannot bring one, tell the organizers ahead of time.</li>
<li><b>Tell the organizers which build you would like,</b> in order: an email assistant, a game, a spaceship, or a journey game. You may not get your first choice.</li>
</ol>
<h2>Rules for using the AI</h2>
<ul class="plain">
<li>Never put personal information into it: no real names of other people, no student IDs, no addresses, no health information.</li>
<li>Paste only what you need. Free accounts have limits, and short, specific messages go further.</li>
<li>Everything you build is invented. No real people, no real emails.</li>
</ul>
<h2>If you cannot make an account</h2>
<p>Tell the organizers before the day. Your group can share an account, and you will still do the building.</p>
"""
    (DOCS / "prework.html").write_text(page("Before you come", pre, 0, "prework"))

    co = f"""
<div class="rule"></div>
<h1>For coaches</h1>
<p class="lede">You are coaching one group of about five through one build. You do not need to live-code, and nobody will ask you to. The guide is the script.</p>
<ul class="plain">
<li>Follow the five moves and keep time: look, spec it, build, catch, ledger.</li>
<li>Show the finished picture first. Every track guide opens with one.</li>
<li>Students type; you do not. Swap the driver every eight minutes.</li>
<li>Ask the question rather than typing the answer: "What would you tell the AI?" "What does the error say?"</li>
<li>If something breaks and you do not know why, say so, paste the exact error into Claude together, and read the answer aloud. That is the skill you are teaching.</li>
<li>This is a draft, and you are free to change anything you think is better. Run your build first, then improve it.</li>
</ul>
<p><a class="btn" href="{BLOB}FACILITATOR-GUIDE.md">Facilitator guide</a><a class="btn alt" href="{BLOB}RUN-OF-SHOW.md">Run of show</a><a class="btn alt" href="{BLOB}THE-THROUGH-LINE.md">The idea behind it</a></p>
<h2>Each track</h2>
<ul class="plain">
<li><a href="{BLOB}workshops/02-build-an-agent.md">The email assistant</a></li>
<li><a href="{BLOB}workshops/03-build-a-game.md">The platformer</a></li>
<li><a href="{BLOB}workshops/04-build-a-3d-model.md">The spaceship</a></li>
<li><a href="{BLOB}workshops/05-build-a-web-app.md">The journey game</a></li>
</ul>
<p class="note">Run each build once, on the real laptop with the real AI, before the day. Without that, nobody knows whether it fits in an hour.</p>
"""
    (DOCS / "coaches.html").write_text(page("For coaches", co, 0, "coaches"))
    (DOCS / ".nojekyll").write_text("")
    print("built", len(list(DOCS.rglob("*.html"))), "pages")


if __name__ == "__main__":
    build()
