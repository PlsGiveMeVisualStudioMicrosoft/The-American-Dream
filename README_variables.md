# USA approval tracking system

Makes `aproval_rate` follow a scripted historical curve while still letting
decisions and events move it, then hands off cleanly to the 2028 collapse.

## Install

Drop `common/`, `interface/` and `localisation/` into the mod root and merge.
Two files intentionally overwrite what you already have:

- `common/on_actions/USA_trump_inauguration_on_actions.txt` — your original,
  with the two `set_variable` lines swapped for `USA_apr_arm_system = yes`
- `common/decisions/simp_propoganda_decisions.txt` — poster 1 now calls the
  helper effect instead of writing to `aproval_rate` directly

Nothing else touches your existing files. `simp_propoganda.gui`,
`simp_propoganda_scripted_gui.txt` and the sprite definitions are unchanged.

## The one file you edit

`common/scripted_effects/USA_approval_00_tuning.txt` holds every number: the
band, the pull strength, the modifier scales, the chaos creep rates, the six
tier thresholds, and the 48-month target curve. Everything else is machinery.

## How the leash works

Each month, in order:

1. **Band** — approval is hard-clamped to within `usa_apr_band` (8) points of
   that month's target. A decision that added +30 gets clipped on the next
   tick.
2. **Pull** — `usa_apr_pull` (0.5) of whatever gap survives is closed. A
   legal deviation is ~94% gone after four months.

So the player has a real 16-point corridor to play in, and permanent
divergence is impossible. Measured behaviour with the shipped curve:

| Date | Target | Approval, no input |
|---|---|---|
| Aug 2025 | 40 | 39.7 |
| Aug 2026 | 34 | 34.6 |
| Aug 2027 | 21 | 22.0 |
| Jul 2028 | 12 | 12.7 |
| Dec 2028 | 7 | 8.2 |

Approval trails roughly a point above target on a falling curve, which is
what a lagging average should do. The 2028 window lands at 12.4 → 8.2.

## Writing to the bars from your own content

Never `set_variable = { aproval_rate = ... }`. Use:

```
set_temp_variable = { apr_delta = -4 }
USA_apr_add = yes

set_temp_variable = { chaos_delta = 12 }
USA_chaos_add = yes
```

Both refresh the display variable, the modifiers and the tier spirit at once.

## Chaos

Not on rails. It creeps up at most 1 point/month, scaled by how far approval
is below 50 and stability is below 50%, and never falls on its own. Your
assassinations, terror attacks and midterm events do the real work through
`USA_chaos_add`.

## Ending it in 2028

From your collapse event:

```
USA = { USA_apr_shutdown = yes }
```

That sets `usa_approval_system_off`, stops the monthly tick, removes the tier
spirit and the dynamic modifier, and freezes both bars at their last value.
To hide the panel too, add this to the `visible` block of
`simp_propoganda_category`:

```
NOT = { has_global_flag = usa_approval_system_off }
```

## Extending past 2028

Add more `add_to_array` lines to the curve, then raise the ceiling in
`clamp_variable = { var = usa_apr_month min = 0 max = 47 }` inside
`USA_apr_monthly_tick` to match. The clamp is what freezes the curve at its
last entry, so a mismatch means the curve stops early.

## Tier spirits

Six spirits, one active at a time, swapping at 45 / 38 / 31 / 24 / 15. They
use vanilla idea art out of the box — `interface/USA_approval_spirits.gfx` has
a commented block for dropping in your own. Step modifiers live on the
spirits; the smooth scaling (stability, war support, PP, consumer goods,
conscription) lives in the dynamic modifier `USA_approval_dm`.

## Note on the driver

`on_monthly_pulse_country` fires on a rolling ~30-day cycle per country, not
on the 1st. Over four years the curve can drift a few days out of alignment
with the calendar. If you need exact month boundaries, replace the driver with
a day counter inside your existing `on_daily_USA` block.
