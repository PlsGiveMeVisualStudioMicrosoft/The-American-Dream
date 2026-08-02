# The American Dream — Interactive Core (drop-in)

Adds Congress + tribes, a legitimacy meter, three decision minigames, a scoreboard,
and the interactive events. Unzip **into your mod's root** so the folders merge.

```
common/scripted_effects/USA_ad_politics.txt      Congress, tribes, legitimacy
common/scripted_effects/USA_ad_iran.txt          Iran attrition clock + effects
common/scripted_effects/USA_ad_cheat.txt         midterm + election cheat effects
common/decisions/categories/USA_ad_categories.txt   4 categories (3 minigames + scoreboard)
common/decisions/USA_ad_iran_decisions.txt
common/decisions/USA_ad_midterm_decisions.txt
common/decisions/USA_ad_election_decisions.txt
common/decisions/USA_ad_scoreboard.txt           the Washington scoreboard readout
common/on_actions/USA_ad_on_actions.txt          lazy-init + monthly Iran tick + daily recalc
events/USA_ad_events.txt                          the handoff / choice / payoff events (usa_ad)
localisation/english/USA_ad_l_english.yml         all names, tooltips, and the [?var] readouts
```

**Dependencies (must already be installed):** the approval/chaos machinery
(`USA_apr_add`, `USA_chaos_add`, `USA_apr_shutdown`) and the chaos leash
(`USA_chaos_collapse`). This layer calls them; it doesn't re-ship them.

## What changed in this pass (the bug fixes)

1. **Every story beat fires exactly once, from the tree — never on a date.**
   All `usa_ad` events are `is_triggered_only = yes` + `fire_only_once = yes`. In the
   events tool project, the 16 dated duplicates (the collapse, the Rout, the stolen
   midterms, the 22nd, etc.) are set to **triggered-only** so they no longer auto-fire.
   That's what stops "the collapse declared on 9 Nov before you did anything."
2. **Choices are events that complete a focus.** A parent focus fires a choice event
   whose options `complete_national_focus` the chosen branch; the branches are
   `available = { always = no }`, so only the event completes them.
3. **De-duplicated.** Removed the duplicate "The Rout" focus and the redundant
   Purge/Flood fork. The Rout now comes only from the Iran clock.
4. **Real bug fixed:** the focus tool does **not** export the apr/chaos `vars`, so the
   focus mood changes are now written into the `completion_reward` instead.

## The flow (focus → event → focus / minigame)

| Focus | fires | then |
|---|---|---|
| **Liberation Day** | `usa_ad.61` | option completes **Befriend Europe** *or* **Tarrif the World** |
| **The Iran Ultimatum** | `usa_ad.1` → `USA_ad_iran_arm` | opens **The Iran Front**; the monthly clock fires **The Rout** (`usa_ad.10`) once, sets `usa_iran_lost` |
| **Boots on the Ground** | — | escalates the clock (faster Rout) while the war is active |
| **Question the Count** | `usa_ad.30` → `USA_ad_mid_open` | opens **The Midterms**; *Certify* → `usa_ad.62` completes **Blatant Steal**/**Quiet Steal** (sets `usa_stole_midterms`); *Let Them Count* → `usa_ad.21` (`usa_lost_house`) |
| **Suppress the Vote** | `usa_ad.50` → `USA_ad_steal_open` | opens **The 2028 Election**; *Declare Victory* → `usa_ad.63` completes **Brazen Fraud**/**Quiet Rigging** → that focus triggers **THE COLLAPSE** (`usa_ad.40`, `USA_chaos_collapse`) |

**Gated focuses** (require a prior outcome): *The Rout Fallout*, *Purge of the Pentagon*,
*Bring the Troops Home* → `usa_iran_lost`; *The Stolen Midterms*, *Reinterpret the 22nd*,
*Declare Candidacy* → `usa_stole_midterms`; *Declare Victory — THE COLLAPSE* → `usa_collapse_triggered`.
(On the honest midterms path the third-term branch stays closed — that's the fork.)

## The scoreboard & readouts

Open the new **Washington Scoreboard** decision category any time: four display-only
"decisions" whose loc shows the live numbers via `[?variable]` — House, Senate, the
overlapping tribes, legitimacy, approval and chaos. Each minigame category also has a
status readout at the top (Iran progress, cheat banked vs. threshold, legitimacy).

## Tuning

- Iran pace: `usa_iran_intensity` baseline 14 (`USA_ad_iran.txt`) → Rout ~7 months after arming.
- Certify needs `usa_midterm_cheat ≥ 5`; Declare Victory needs `usa_steal_cheat ≥ 6`.
- Legitimacy < 30 → `usa_low_legitimacy`.
- Icons/pictures are generic placeholders — swap freely.

## `[BUILD]` — the big effects left for you (marked, never attempted)

Search `[BUILD]` in the scripts/JSONs. The main ones: **THE COLLAPSE** (release the
West-Coast + blue-state bloc, `start_civil_war`, scale by legitimacy) on the Brazen/Quiet
focus reward; the **real Iran withdrawal** on the Rout; the **impeachment branch** on the
honest-midterms path; **Maduro captured**; **Greenland/Panama**; state releases when
`usa_low_legitimacy` sets.
