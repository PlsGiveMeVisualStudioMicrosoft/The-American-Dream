# Haiti content implementation

Start date: **1 January 2025**

## 1.19.2 crash hotfix

- Replaced unsupported `clear_country_flag` effects with `clr_country_flag`.
- Rewrote `>=` and `<=` variable checks using strict comparisons supported by the active parser.
- Replaced two missing focus icons and the unsupported party-popularity effect.
- Recruited all three historical council presidents in country history so later events only promote them.
- Corrected Viv Ansanm's invalid election date.
- Added character name lists for `VIV`, `GRF` and `KRB` to prevent AI commander-generation failures when time starts.
- Added an empty legacy localisation file so installing over the earlier Haiti build does not leave duplicate localisation keys.
- Fixed the National Palace fort construction by assigning it to Port-au-Prince province `8694` instead of the invalid province `0` selected by state scope.

## AI decision and balance rewrite

- Replaced every factor-only `ai_will_do` block in the Haiti decision file with a non-zero `base` weight. Decision MTTH defaults to zero, so multiplying it by a factor had left both the gangs and Haiti unable to select their operations.
- Armed-group daily PP has been reduced to roughly `0.65` (Viv Ansanm), `0.75` (Gran Grif) and `0.85` (Kraze Baryè) while focusing. Stacked generic illicit-economy and leader PP bonuses were removed, and large focus PP rewards were cut.
- Haiti produces roughly `0.25` PP per day while focusing at the start, about `0.4–0.5` after the Emergency Council, and improves again after reopening customs.
- Major gang operations use AI weights between `140` and `180`, higher PP costs and longer individual cooldowns. Internal consolidation actions remain available but no longer print large amounts of PP.
- Every major operation creates an immediate shared 18-day national lock and gives the attacker 45 days of Operational Exhaustion. Only one gang can therefore launch a large attack at a time, and the same gang cannot monopolise the sequence.
- Haiti's checkpoint, convoy, intelligence, regional-support and CSSM decisions also have real base weights, allowing the government AI to respond instead of leaving escalation completely one-sided.

## Decision feedback

- Added success and failure reports for PNH checkpoint raids.
- Added completion reports for humanitarian convoys and joint intelligence operations.
- Haiti now receives reports identifying the armed group responsible for checkpoint attacks, roadblocks and stockpile raids.
- Regional-support decisions now produce a named response from the current candidate country.
- Gang interference in the regional contest produces intelligence reports identifying the responsible organization and the influence lost.
- CSSM reconnaissance, limited supplies, emergency supplies and arms interceptions now each have a separate result event.

## Playable countries

| Tag | Country | Starting leader | Starting territory |
| --- | --- | --- | --- |
| `HAI` | Republic of Haiti | Leslie Voltaire | Government district, Northern Haiti, Southern Haiti, Gonâve Island |
| `VIV` | Viv Ansanm Coalition | Jimmy Chérizier | Metropolitan Belt |
| `GRF` | Gran Grif | Luckson Elan | Artibonite |
| `KRB` | Kraze Baryè | Vitel'Homme Innocent | Eastern Capital Corridor |

The armed groups are represented as de facto territorial authorities. They begin in an unstable standoff instead of an immediate formal war so the Haitian campaign does not resolve through AI combat during the opening weeks. The standoff is governed by a shared escalation system; at 100 escalation, Haiti enters separate wars with all three armed groups. No formal gang faction is created because the obsolete faction effect caused a reproducible game crash in HOI4 1.19.

## State split

The original single Haiti state (74) was divided without modifying `provinces.bmp`:

- `74`: Port-au-Prince Government District
- `82`: Artibonite
- `83`: Northern Haiti
- `84`: Southern Haiti
- `85`: Metropolitan Belt
- `86`: Eastern Capital Corridor
- `87`: Gonâve Island

All 22 original Haitian provinces remain assigned exactly once. Port-au-Prince province `8694` now forms state `74` by itself, while Gonâve province `9623` forms state `87`. Haiti retains cores on every new state; each armed group also has a core on its own starting territory. `provinces.bmp` remains untouched; `map/buildings.txt` contains the corrected state assignments plus Gonâve placements for its civilian factory, airport and dockyard.

## Included systems

- Updated 2025 politics, stability, war support and starting technologies
- Separate starting division templates and units for all four tags
- Historical council rotation from Leslie Voltaire to Fritz Alphonse Jean on 7 March 2025 and Laurent Saint-Cyr on 7 August 2025
- All three council presidents and three armed-group leaders as characters
- A 51-focus Haitian tree with security, counter-operation, democratic, military, negotiated, CSSM and recovery paths
- A 39-focus armed-group tree with a short shared opening and three fully distinct operational branches
- Haiti-specific national spirits, party names, country names and event text
- The real Haitian flag in every ideology slot and 156×210 DDS leader portraits
- Haiti added to the interesting-country list in the 2025 bookmark

## Haitian crisis and regional mission

- Escalation begins at 35 and can be changed by Haiti, armed-group decisions and major focuses. Reaching 100 starts the Haitian War.
- Gang endgame focuses no longer set escalation directly to 100. They require at least 80 escalation, warn Haiti, and then begin a 35-day final preparation. Haiti can interrupt the operation by pushing escalation below 80; a completed offensive adds 12 escalation.
- The old four generic raid buttons are hidden in new games. Viv Ansanm now specialises in metropolitan barricades, airport pressure and port seizures; Gran Grif in road extortion, truck ambushes and coastal shipments; Kraze Baryè in ransom, vehicle theft and eastern-corridor disruption.
- Major attack results are resolved on Haiti's event option. Manpower, weapons, vehicles and convoys use real scripted effects visible in the native option tooltip; flavour descriptions no longer pretend that an unapplied loss occurred.
- Standard major operations add 3–8 escalation while internal actions usually add 0–2. Their frequency is unchanged, but each major result now adds one more escalation than the previous balance pass.
- Haiti's three recurring crisis responses use variable prices. Checkpoint raids begin at 30 PP, convoy protection at 25 PP and joint intelligence at 45 PP; the relevant price permanently rises by 5 PP every time that response is used.
- **Delay the Catastrophe** opens a three-focus intelligence detour and limited counter-operation tokens. Haiti can temporarily fracture Viv Ansanm's coalition, expose Gran Grif's routes or freeze Kraze Baryè's ransom channels. Success blocks major decisions and crushes PP generation for 90 days without changing division attack, defence or organization.
- The **Seek a Regional Leader** focus opens an influence contest at zero. The Dominican Republic is approached first, followed by a player-selected Jamaica or Bahamas if a candidate refuses.
- Haiti wins the current candidate at +60 influence. The armed groups win at -60; each gains stability and military access to the refusing country. Their influence actions are deliberately much more expensive.
- A human candidate chooses whether to accept or refuse. AI candidates follow the influence outcome.
- Securing a candidate unlocks the **Caribbean Security Support Mission** branch. Aid becomes stronger at high escalation or during open war.
- The **Caribbean Joint Security Brigade** is a locked, seasoned 8-width formation with four infantry battalions, engineers and support artillery. It is controlled by Haiti and can only deploy at 60 escalation or during war.
- If Haiti loses Port-au-Prince after deployment, it has 21 days to recover the capital. Otherwise, the brigade is withdrawn.
- The final mission choices are mutually exclusive: **Support, Not Occupation** leads to a Haitian-led force, while **Foreign Protection of the Ports** leads to stabilization at any cost.

## Gonâve Island development and security

- **Build Hotels on Gonâve Island** requires more than 15% stability, adds one civilian factory and creates a +10% consumer-goods burden that automatically expires after three years.
- **Open Gonâve to Tourism** requires more than 20% stability, grants 5% stability and adds -15% consumer goods. Together, the two development spirits provide the requested net -5% consumer-goods effect.
- Completing **Map the Armed Networks** reveals the island threat and unlocks a 0–3 security system. Guard reinforcement costs 180 rifles, ferry escorts 120, the permanent local watch 450 and later local-watch reinforcement 120. The local watch becomes available after two raids are repelled.
- At security levels 0/1/2/3, an armed-group landing has an 80%/55%/30%/10% chance to succeed. A successful landing creates a temporary breach and transfers rifles from Haiti to the attacker.
- A gang holding a breach chooses a second-stage operation: loot unfinished hotel sites, rob tourists, or burn the resorts. The three armed groups use different AI preferences for these targets.
- Losing state `87` suspends all Gonâve economic benefits and resets security to zero. Retaking it restores completed development benefits, but Haiti must rebuild the guard.
- **Establish the Gonâve Development Authority** extends the focus branch into resource and transport planning. It unlocks mutually exclusive-in-progress timed projects for offshore resources, an airport, a deepwater harbor and shipyards.
- Gonâve petroleum development now has five sequential projects lasting 70/90/110/130/150 days and costing 60/75/90/110/130 PP. Every active stage imposes a 65% consumer-goods-factor penalty and adds 3 oil on completion, up to 15 oil total. The first field also grants 5,000 fuel and unlocks national fuel programs.
- Fuel programs have both an immediate stockpile cost and a fixed daily drain. Their daily cost ranges from 300 fuel for the fishing fleet to 2,550 for Caribbean exports; programs shut down automatically when the reserve reaches zero.
- Haiti can use fuel for hospitals and water pumps, ferries, local support, tanker escorts, channel patrols, gang tracking, generators, the capital grid, motorized police, CSSM transport, coastal interdiction, emergency airlift and regional exports.
- Viv Ansanm targets offshore platforms, Gran Grif targets tanker routes and Kraze Baryè targets petroleum engineers. Their AI gives these operations very high priority, but the shared major-operation lock prevents simultaneous attacks. Haiti receives twelve days of warning and can reinforce the relevant security layer or run a decoy convoy.
- Successful petroleum attacks steal fuel in proportion to the current oil stage. A permanent dispersed-reserve project halves offshore and tanker losses; sabotage can remove 3 oil temporarily, while emergency repair crews can restore it early.
- The 80-day airport, 90-day shipyard and 100-day harbor projects carry temporary civilian burdens, then add their actual state buildings and permanent tourism or dockyard bonuses.
- **Restore the Port-au-Prince Harbor** adds a naval base to state `74`. Gonâve's new harbor adds a naval base to state `87`.
- Successful weapon-seizure events now move materially significant stockpiles: coastal cargo rises from 100 to 300 rifles, the national-port seizure from 120 to 360, and the Artibonite arms truck from 80 to 240. Gonâve landing losses were scaled in the same direction.
- Because state ownership and province assignment changed, this version requires a new game and is not intended for older saves.

## Distinct armed-group gameplay

- Every armed group begins with **Non-State Armed Group**. Political advisors, mobilization and conscription changes, economic laws and trade laws cost 1000% more Political Power. Military commanders remain usable. The restriction disappears only after the organization owns and claims all seven Haitian states.
- **Viv Ansanm** plays around coalition cohesion and metropolitan pressure. Its focuses unlock coalition councils, capital barricades, airport disruption and an enhanced national-port raid.
- **Gran Grif** plays around the Savien stronghold and control of Artibonite's roads. Its focuses unlock road extortion, arms-truck hijacking and the Saint-Marc corridor.
- **Kraze Baryè** plays around the ransom economy, vehicle theft and the Torcelle-Tabarre network. Its high-value kidnapping triggers an interactive Haitian response: pay, refuse or attempt a risky rescue.
- All major gang operations now send explicit feedback events to Haiti, while equipment-transfer operations also report the exact result to the attacking group. Native event-option effects are the mechanical source of truth.

## Art note

Leader portraits are stylized game illustrations, not documentary photographs. The Luckson Elan portrait is explicitly an artistic representation because reliable reference photography is limited. The three armed-group flags are fictional gameplay identifiers; these organizations do not have well-established standardized national flags.

## Research anchors

- UN Security Council, Luckson Elan: https://main.un.org/securitycouncil/en/content/luckson-elan
- UN Security Council, Vitel'Homme Innocent: https://main.un.org/securitycouncil/en/content/vitelhomme-innocent
- UN sanctions list, Viv Ansanm and Gran Grif: https://scsanctions.un.org/consolidated
- UN Human Rights Office, spreading gang violence in Haiti: https://www.ohchr.org/en/press-releases/2025/07/spreading-gang-violence-poses-major-risk-haiti-and-caribbean-sub-region

## Recommended in-game smoke test

1. Start the 2025 bookmark as Haiti.
2. Confirm Leslie Voltaire, the real Haitian flag, the Republic of Haiti name, 12% stability, 42% war support and the six starting national spirits.
3. Open the focus tree and complete **A Nation on the Brink**.
4. Verify the introductory event fires.
5. Confirm `VIV`, `GRF` and `KRB` are selectable and use their own leaders, flags, units and shared focus tree.
6. Confirm all seven Haitian states have names and no province appears as an unassigned map error.
7. Run to 7 March and 7 August 2025 and confirm the historical council-president rotations.
8. Raise escalation to 100 and confirm Haiti enters open war with all three armed groups.
9. Complete **Seek a Regional Leader**, test the +60/-60 influence outcomes and confirm failed candidates grant military access to all three armed groups.
10. Secure a partner, deploy the Caribbean Joint Security Brigade, and confirm it has four infantry battalions, engineers, support artillery and seasoned experience.
11. After brigade deployment, lose state 74 and confirm the 21-day withdrawal countdown; retaking it before the deadline should preserve the unit.
12. Start as each armed group and confirm its two unique starting spirits, distinct focus branch and tag-specific decisions.
13. Confirm the civilian government laws and political advisors cost 1000% more PP while military command remains available.
14. As a gang, reach 80 escalation and complete the warning focus. Confirm Haiti receives 35 days of warning and lowering escalation below 80 interrupts the final offensive.
15. Test a Gran Grif arms-truck or coastal-shipment raid. Hover the Haitian event option and confirm that manpower, convoys and equipment are shown as native effects and are actually removed when clicked.
16. Complete **Map the Armed Networks**, verify the Gonâve Security category appears, and test both an initially armed and unguarded island.
17. Complete the two Gonâve development focuses at the required stability thresholds. Confirm state `87` gains a civilian factory, tourism produces a net -5% consumer-goods effect and grants 5% stability.
18. As a gang, open a breach at different security levels and select a follow-up operation. Confirm both sides receive the appropriate result events and Haiti can clear the disruption.
19. Lose and retake state `87`; confirm economic spirits are suspended during occupation, restored after liberation and island security restarts at zero.
20. Observe all three armed groups for several months and confirm only one major operation can be active within an 18-day window.
21. Complete **Delay the Catastrophe**, spend a counter-operation token and confirm success suppresses the target's decisions for 90 days without modifying its division combat stats.
22. Use each recurring Haitian crisis decision twice and confirm only that decision's PP price increases by 5 after every use.
23. Complete all five Gonâve oil stages. Confirm they last 70/90/110/130/150 days, each shows the 65% consumer-goods burden, each adds exactly 3 oil on expiry and the final total is 15 oil.
24. Complete the airport, shipyard and harbor projects one at a time. Confirm state `87` receives the corresponding buildings and permanent benefits, while state `74` receives its naval base from the Port-au-Prince focus.
25. Confirm the continuous-focus palette appears to the right of the Haitian focus branches instead of covering the lower security path.
26. Start several fuel programs together and confirm the displayed daily commitment matches the actual daily stockpile loss. Empty the reserve and confirm all active programs shut down.
27. Observe Viv Ansanm, Gran Grif and Kraze Baryè after the first oil field opens. Confirm only one petroleum operation begins at a time, Haiti receives a twelve-day warning and the matching attacker receives a success/failure report.
28. Test offshore sabotage, tanker hijacking and engineer abduction at multiple oil stages. Confirm stolen fuel scales upward, the decoy affects the result and distributed reserves halve offshore/tanker losses.
