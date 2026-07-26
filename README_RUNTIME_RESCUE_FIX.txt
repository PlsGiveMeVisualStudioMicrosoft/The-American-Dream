BELIZE-GUATEMALA RUNTIME RESCUE FIX

Main repairs:
- Removed UTF-8 BOM bytes from non-localisation script files. These bytes broke the first decision category, scripted effect, dynamic modifier file, ideas file and focus file.
- Restored TAD_BG_clamp_tension and TAD_BG_clamp_metrics scripted effects.
- Restored Belize/Guatemala minigame decision categories and foreign/intelligence decisions.
- Replaced invalid reinforce_rate with land_reinforce_rate.
- Replaced invalid stability/political_power triggers with has_stability/has_political_power.
- Replaced three missing Guatemala focus icons with present generic icons.
- Haiti can request Belizean aid at 25 Haitian escalation, independent of Belize-Guatemala tension.
- Haiti AI requests aid and later repays troop/arms debt through Haiti decisions at very high AI priority.

Start a new game for focus trees, initial state modifiers and country history. Existing saves may recover decisions after one day, but are not guaranteed to rebuild all parsed content.
