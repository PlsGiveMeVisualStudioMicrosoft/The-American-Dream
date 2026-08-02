THE AMERICAN DREAM - CONGRESS WINDOW (drag-and-drop patch)
=========================================================

WHAT THIS ADDS
  * A floating window with a fully drawn House (435 seats) and Senate
    (100 seats) hemicycle, coloured by party (GOP red / Dem blue), plus
    the Washington Scoreboard readouts (tribes / legitimacy / approval
    / chaos).
  * Opened by the round Capitol emblem button sitting on the
    president portrait (static button + clicked_sound, on
    simp_propoganda.gui). Closed by the window's own X.
  * A faint Capitol backdrop. To use your own image, overwrite
    gfx/interface/usa_congress_bg.dds (1040x500, .dds) - nothing
    else to change.
  * The diagram is a pure VISUALISER: it reads usa_house_gop/dem and
    usa_senate_gop/dem and paints them. It does NOT own the numbers.

HOW IT DRIVES ITSELF
  common/on_actions/USA_congress_on_actions.txt paints the diagram at
  on_startup and every day, the moment has_country_flag =
  usa_ad_initialized is set - by YOUR Congress/tribes init, or by the
  fallback seeder in USA_congress.txt on a bare install. It is no longer
  gated behind THIS file setting that flag (that was why the boxes were
  empty). Nothing here touches your inauguration on_action anymore.

HOW TO INSTALL
  Drop the contents of this zip into your mod's root folder and let it
  MERGE / OVERWRITE.

    EDITED  interface/simp_propoganda.gui                        (+ Congress button)
    EDITED  common/scripted_guis/simp_propoganda_scripted_gui.txt (+ button effect)

    NEW     interface/USA_congress.gui / .gfx
    NEW     gfx/interface/usa_congress_parties.dds
    NEW     common/scripted_effects/USA_congress.txt
    NEW     common/scripted_guis/USA_congress_scripted_gui.txt
    NEW     common/scripted_localisation/USA_congress_scripted_loc.txt
    NEW     common/on_actions/USA_congress_on_actions.txt
    NEW     common/decisions/USA_ad_scoreboard.txt
    NEW     common/decisions/categories/USA_ad_categories.txt
    NEW     localisation/english/USA_ad_scoreboard_l_english.yml

TUNING
  Fallback starting numbers live at the top of
  common/scripted_effects/USA_congress.txt (USA_congress_seed_defaults);
  they only apply on a bare install with no other Congress system.

MOVING SEATS FROM YOUR OWN CONTENT
  Change the named variables; the daily tick repaints automatically, or
  force it now:
    add_to_variable        = { usa_house_gop = 3 }
    subtract_from_variable = { usa_house_dem = 3 }
    USA_congress_refresh = yes
