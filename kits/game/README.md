# Kit: the Claude Jumpman (Godot game)

## Executive summary

**What this is.** A small, complete 2D platformer called *Shipping Lane* starring Clawd, the Claude mascot, built in Godot. Your group changes it with an AI, plays it, and shows the result. **Why it works for an hour.** The game is small. The player's jump tuning is a 10-line file, the enemy behavior is one 53-line file, and the entire level is one JSON file, so a group can paste any of them into an AI chat and ask for a change. **Status.** The game was built and tested by its author; human playtesting is still pending, and nobody has run this as a workshop yet.

## Get it

- Repository: <https://github.com/nikbearbrown/walker-claude> (public). Use **Code, Download ZIP**, or clone it.
- Engine: **Godot 4.7.2**, free, from godotengine.org. It is a single app and needs no installer or account. Use that exact version on every laptop.
- Open `godot/project.godot` in the Godot editor, press **F5** to play. Controls: A/D or arrows to move, Space to jump, R to retry, Esc or P to pause.

## The files that matter (all inside `godot/`)

| File | What it controls | Size |
|---|---|---|
| `features/player/tuning.gd` | Jump height, speed, gravity | 10 lines |
| `features/player/player.gd` | How Clawd moves | 93 lines |
| `features/course/bug.gd` | How the bugs (enemies) behave | 53 lines |
| `features/course/token.gd` | Collectible tokens | 26 lines |
| `levels/shipping_lane.json` | The whole level: platforms, gaps, hazards, tokens, enemies, blocks | one file |

## Build menu (pick one for the hour)

1. **Redesign the level.** Change `shipping_lane.json`: add gaps, move platforms, place tokens.
2. **New enemy behavior.** Edit `bug.gd`: faster, patrols farther, jumps.
3. **Re-tune the feel.** Edit `tuning.gd`: floaty or heavy, fast or slow.
4. **New collectible rule.** Edit `token.gd` and the HUD: tokens that give something.

## Starter prompt

> I am editing a small Godot 4.7 platformer written in GDScript. Here is the file: [paste]. I want to change it so that [one sentence]. Give me the complete new file, tell me exactly what you changed and why, and tell me one way it could break.

If Godot shows an error, paste the exact error text back to the AI.

## Browser fallback (if Godot will not run on a laptop)

Paste `levels/shipping_lane.json` and ask: "Build this level as ONE self-contained HTML file with a canvas: arrow keys, space to jump, the platforms, bugs and tokens from the JSON." This is a different game engine, so say so out loud.

## Credits and limits

Starter credit: the Walker Jumpman project. Clawd's character art comes from the author's own character iteration; the repository says human playtesting is pending and the 18-animation gallery is separate from gameplay. The repository does not currently carry a license file. Confirm reuse terms before redistributing the game itself; this workshop only links to it.
