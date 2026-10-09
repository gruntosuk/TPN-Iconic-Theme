# Nightly log

## 2026-10-02

Systems completed (3): aquarius, jupace, mbee. All three are computers (section B1), so each has a Gemini background, a Gemini top-down machine render on green, and a sticker logo. Mockups: mockups/aquarius.jpg, jupace.jpg, mbee.jpg.

| System | Game used for the background | Notes |
|---|---|---|
| aquarius (Mattel Aquarius, 1983) | Treasure of Tarmin-style dungeon crawl: armoured hero with torch vs minotaur | Machine image needed one redo (first render was cropped at the edges and had a duplicate ESC key); logo from Carbon "Mattel Aquarius.png" |
| jupace (Jupiter Ace, 1982) | Generic ACE-branded space shooter (red-and-white starfighter vs crystalline hive beside a gas giant) | Background redone once (ringed moon and planet crowded the left third). Metadata year corrected 1981 -> 1982. Logo from Carbon "jupiter ace.png" |
| mbee (MicroBee, 1982) | Bunyip Adventure (Grotnik Software, 1984, Australian) | Machine image is the keyboard unit only (no monitor). Logo from Carbon "appliedtechnologymicrobeealt.png" (black-text version, since the white one vanishes on the sticker border) |

For the user to review:
- Jupiter Ace has few original games and I could not confirm one specific original title, so the scene is a generic ACE-style shooter rather than a named game. Swap the scene if you prefer a named game.
- The MicroBee machine render is the Premium PLUS badged variant (taken from the Carbon photo) and its lid looks long/blank compared with a real unit; worth a glance.
- The bunyip came out walrus-like (tusks); on-brief but check you like it.
- Gemini quirk: a new image only appears after reloading the chat page. The Drive picker sometimes pops up when uploading; it was closed without inserting anything.
- Gemini downloads were copied from ~/Downloads (Downloads is not deletable from the VM, so the Gemini_Generated_Image_*.jpeg files are still there).
- The ~/tpn-build/venv is a Mac venv and does not run in the Linux VM; the system python3 (with cv2/PIL) was used instead.

## 2026-10-02 (second run)

Systems completed (3): cgenie, sorcerer, pecom64. All computers (section B1). Mockups: mockups/cgenie.jpg, sorcerer.jpg, pecom64.jpg.

| System | Game / scene used for the background | Notes |
|---|---|---|
| cgenie (Colour Genie EG2000, 1982) | Generic retro sci-fi shooter: orange-suited astronaut firing at a one-eyed green slime alien in a purple crater | System image is the Carbon theme photo itself (already a flat top-down view with transparent background), cropped, not upscaled (1012x560). Logo from Carbon "eaca eg2000 colour genie.png" |
| sorcerer (Exidy Sorcerer, 1978) | Fantasy dungeon: violet-robed sorcerer conjuring a blue fireball at a red dragon (after the machine's name) | Gemini top-down render from the Carbon photo, one follow-up to flatten the view. Logo from Carbon "exidy classics.png" (Exidy company logo). Metadata year corrected 1979 -> 1978 |
| pecom64 (Pecom 64, 1985) | Generic cosmonaut with energy wrench vs rusted robot guardian on a red planet | Gemini first answered with text, needed an explicit "generate an image" follow-up, then a redo because the keys came out white (real keys are black). Logo from Carbon "pecom 64.png". Metadata year corrected 1987 -> 1985 |

For the user to review:
- Web searches found no specific original title for any of the three machines, so all three scenes are generic and flagged as such in PROMPTS.md. Swap in a named game if you prefer.
- Sorcerer machine render is slightly wedge/tilted-looking because the real machine is wedge-shaped; I left it matching the real unit rather than forcing a perfect orthographic view.
- Pecom 64 render: key layout is Gemini's invention (plausible but not an exact copy); the badge is printed on the dark panel rather than a sticker shape.
- Colour Genie machine photo keeps the original photo's slight sheen/yellowing; it is a real photo, not a render.
- Environment notes: the user's Chrome could not open file:// URLs; the style reference was screenshotted from GitHub and uploaded to Gemini, and reference photos were uploaded via device_stage_files + file_upload. /tmp in the VM was not writable for make_logo.py (a root-owned file), so a copy with a different temp path was used (the tool itself is unchanged). make_todo.py was run from a copy with the NAS path changed to the VM mount.
- Gemini quirks again: a new image only shows after reloading the chat page; the attach-menu click needs repeating until the file input appears.
- Gemini_Generated_Image_*.jpeg files remain in Downloads (cannot be deleted from the VM).


## 2026-10-03

Systems completed (3): ibmpcjr, exl100, hec2hr. All computers (section B1). Mockups: mockups/ibmpcjr.jpg, exl100.jpg, hec2hr.jpg.

| System | Game / scene used for the background | Notes |
|---|---|---|
| ibmpcjr (IBM PCjr, 1983/84) | Fairy-tale adventure in the spirit of PCjr's King's Quest: armoured knight with plumed helmet and blue cape raising a glowing sword at a castle, small dragon on a tower | System image is the Carbon theme photo cut-out (3/4 view, NOT top-down): Gemini's top-down render came out rotated, cropped and with invented keys twice, so I dropped it. Logo from Carbon "ibm pc jr.png" |
| exl100 (Exelvision EXL 100, 1984) | Generic: orange-suited rider on a motorbike-style hover-bike vs giant black mechanical scorpion in an orange canyon | System image is the Carbon photo (console, keyboard and two joysticks, already flat top-down, transparent), trimmed. Logo from Carbon "exelvision exl 100.png" (small butterfly + wordmark) |
| hec2hr (Hector 2HR, 1983) | Generic: rusty drill-armed mining robot in a crystal cavern over lava, small scout drone | Gemini top-down render of the keyboard unit on green, worked first time, cut out with cutout_green.py. Logo from Carbon "hector hrx.png" (HRX-badged) |

For the user to review:
- PCjr machine image is a 3/4 photo, not a top-down view like the other computers. Swap in a top-down render if you find a good reference.
- No specific original game could be confirmed for EXL 100 or Hector 2HR (searches returned only list pages), so both scenes are generic and flagged as such in PROMPTS.md. The PCjr knight deliberately avoids the King's Quest hero.
- The EXL 100 hero is on a motorbike (Gemini ignored "hover-bike"); fine for the scene.
- Hector logo shows the HRX badge, not 2HR. PCjr release year left at 1983 (announced Nov 1983, shipped Mar 1984).
- ZIP: could not overwrite iconic-tpn.zip (deleting/replacing files is not permitted in the connected folders). The new full build is iconic-tpn_20261003.zip, in TPN Iconic on the NAS and as iconic-tpn_20261003_full.zip in ~/tpn-build (a 0-byte iconic-tpn_20261003.zip stub there is safe to delete). The old iconic-tpn.zip is stale; delete it and rename the new one if you like.
- NAS was mounted; sources, mockups, TODO, PROMPTS, CREDITS and this log were copied.
- Gemini quirks again: the Drive picker popped up on upload (closed without selecting anything); the send button moves down once an image is attached; images only show after a page reload. A chat named "MTX512 Top-Down Product Photo..." appeared in Gemini's history that this run did not create (probably another session) - ignore.
- Gemini_Generated_Image_*.jpeg files remain in Downloads (cannot be deleted from the VM).


## 2026-10-03 (second run)

Systems completed (3): mtx512, p2000t, m5. All computers (section B1). Mockups: mockups/mtx512.jpg, p2000t.jpg, m5.jpg.

| System | Game / scene used for the background | Notes |
|---|---|---|
| mtx512 (Memotech MTX512, 1983) | Generic British 8-bit sci-fi shooter scene: bubble-helmeted miner-astronaut with jetpack firing a cutting beam at a brass robotic spider walker in a crystal cavern (Kilopede avoided as a Centipede clone) | First background was redone: the hero came out looking like a famous bounty-hunter character, so I asked for a different hero (stocky white-and-blue miner suit). Machine image is a Gemini top-down render of the keyboard unit on green (worked first time; the F-key block is duplicated slightly oddly: two function-key columns). Logo is a house-style wordmark (Memotech + MTX512 on a red block), because the Carbon "memotech mtx.png" is white and vanished on the sticker border |
| p2000t (Philips P2000T, 1980) | Generic: red-and-cream rivet-plated rocket-plane vs rusty mechanical kraken over a stormy North Sea (Dutch machine) | Machine image needed three follow-ups: Gemini kept the angled view until I described the plan-view layout explicitly. Result is a true top-down but the key legends/small badge text are invented (the small spec-list text beside the Philips badge is gibberish at this size). Edges were ragged so I trimmed 14px and rounded the corners. Logo is a house-style wordmark (Philips blue + P2000T on a dark block) |
| m5 (Sord M5, 1982) | Generic: indigo ninja leaping a moonlit rooftop vs a giant horned oni behind a pagoda | Machine image is Gemini's render from the ckau photo; it stays slightly angled (the real M5 is wedge-shaped and Gemini would not flatten it further), so it reads as a high 3/4 view rather than a pure top-down. A bright green line along the bottom edge and a trimmed 10px were cleaned. Metadata year corrected 1983 -> 1982 (Japan release). Logo is a house-style wordmark (Sord + M5 on an orange block) |

For the user to review:
- None of the three machines has a confirmed original title (searches only returned list pages), so all three scenes are generic and flagged as such in PROMPTS.md. Swap in a named game if you prefer.
- M5 system image is not a perfect top-down (see above); P2000T render has gibberish micro-text near the Philips badge.
- Backgrounds: left third is dark but the MTX512 spider walker sits partly in the left third; check you are happy with that.
- All three logos are wordmarks (not original logos). Replace them if you find clean transparent PNGs; make_logo.py takes any transparent PNG.
- Another Gemini/Chrome session shared Downloads and the Gemini account during this run (Gemini history showed chats I did not create, and an unrelated desert-scorpion image landed in Downloads at the moment of my first machine-image download). I caught it because I viewed every download before using it, and re-downloaded the right file; but if anything from tonight looks wrong, that is the likely cause.
- ZIP: new full build is iconic-tpn_20261003_b.zip (TPN Iconic on the NAS and ~/tpn-build); older zips cannot be overwritten from the connected folders.
- Gemini_Generated_Image_*.jpeg files remain in Downloads (cannot be deleted from the VM).
- p2000t controller re-rendered: duplicate W/X removed, duplicate E/S legends blanked (those two keys are now blank extra keys). Old art: replaced/p2000t_controllers_dupkeys.webp
- 2026-10-03 p2000t controller re-rendered: duplicate W/X removed; duplicate E/S legends blanked (two keys are blank extras). Old art: replaced/p2000t_controllers_dupkeys.webp. Zip not rebuilt.
- p2000t keyboard: blank keys removed by compressing rows 1-2 horizontally (no duplicates, no blanks).
- p2000t keypad: gibberish legends replaced with drawn real labels (÷ × − 7-9 4-6 1-3 0 00 .; ZOEK/START/STOP/CLR secondary). Layout partly reconstructed, not verified against a photo.
- m5 machine image replaced with a true top-down Gemini render made from the user's reference photo (ref: Downloads/Iconic Images/m5_cab.webp). Old art: replaced/m5_controllers_angled.webp. Zip not rebuilt.
- mtx512 logo replaced with the real MTX512 lettering from the user's photo of the machine's badge (white on black plate with red lines), sticker border applied. Old: replaced/mtx512_logos_wordmark.webp. Zip not rebuilt.
- m5 logo replaced with the real Sord M5 logo (user-supplied, Downloads/Iconic Images/m5_logo.jpg), cut out and sticker-bordered. Old: replaced/m5_logos_wordmark.webp. Zip not rebuilt.
- p2000t logo replaced: redrawn striped-line P2000T lettering after the badge on the machine (user photo; Philips shield not used), light on dark plate, sticker border. Old: replaced/p2000t_logos_wordmark.webp. Zip not rebuilt.
- p2000t logo: the 2 given rounder, more curved corners to match the original badge.
- p2000t logo: reverted the rounded 2 at the user's request; back to the square-cornered version.
- mtx512 controller: repeated F1/F3 keys and gibberish keypad legends redrawn (keypad 7-9/4-6/1-3/0 . ENT with cursor arrows; F1-F8 in 2x4). Old: replaced/mtx512_controllers_dupF.webp. Zip/NAS controller copy not updated.


## 2026-10-04

Systems completed (3): vg5k, tvc64, ep128. All computers (sections B1 and D). Mockups: mockups/vg5k.jpg, tvc64.jpg, ep128.jpg.

| System | Game / scene used for the background | Notes |
|---|---|---|
| vg5k (Philips VG-5000, 1984) | Generic French 8-bit undersea adventure: brass-suited deep-sea diver with a harpoon lamp vs a giant luminous jellyfish creature among the columns of a sunken palace | Machine image is a Gemini top-down render from the Carbon photo (worked first time, keyboard layout and badge kept). Logo: Carbon orange "VG 5000" lettering (the Carbon file named "philips vg 5000.png"; "vg5000.png" is a white PHILIPS + VG 5000 version that vanishes on the white sticker) |
| tvc64 (Videoton TVC 64, 1985) | Generic Hungarian folk-tale fantasy (taltos winged-horse legend): embroidered-tunic warrior on a rearing white winged horse vs a three-headed storm dragon on a castle tower | No machine photo existed locally, so the reference is the public-domain Wikimedia Commons photo Videoton_TVC_01.JPG (cropped); Gemini top-down render worked first time. Logo: Carbon "videoton tv 64.png" |
| ep128 (Enterprise 128, 1985) | Generic space-shooter: red-and-white jetpack explorer vs a crystalline space-whale over a purple alien desert with a ringed planet | Machine image is a Gemini top-down render from the Carbon photo (worked first time). Logo: house-style wordmark (Enterprise + rainbow bar + One Two Eight) in the layout of the Carbon "Enterprise Sixty Four" logo, dark text because the Carbon one is white and vanishes on the sticker. Metadata year corrected 1986 -> 1985 |

For the user to review:
- No original game could be confirmed for any of the three machines, so all three scenes are generic and flagged as such in PROMPTS.md. The TVC rider scene is close to a classic "St George" image; swap if you prefer.
- Hero placement: VG-5000 diver sits slightly left of centre-right with columns in the left third; EP128 jetpack hero is near centre.
- Enterprise 128 render has small invented key legends (function-key labels); the TVC render has plausible but not exact legends. The TVC cut-out has a tiny speck at its bottom-right corner.
- Mockup title for ep128 ("Enterprise One Two Eight") is clipped in the mockup panel by the renderer's width limit; consider a shorter systemName.
- TVC release year left at 1985 (Wikipedia says "around 1986").
- Metadata/zip: iconic-tpn.zip and older zips cannot be overwritten or deleted from the connected folders, so the new full build is iconic-tpn_20261004.zip (in ~/tpn-build and in TPN Iconic on the NAS).
- NAS was mounted; sources, mockups, TODO, PROMPTS, CREDITS and this log were copied. Originals were COPIED to sources/ (deleting is not permitted), so copies remain in ~/tpn-build/incoming.
- Gemini quirks: the attach-menu "+" click needs repeating until the file input appears; typing before the attachment thumbnail finished loading lost the text; Enter sends the prompt; downloads land in Downloads as Gemini_Generated_Image_*.jpeg.
- Gemini_Generated_Image_*.jpeg and tvc_ref.jpg remain in Downloads (cannot be deleted from the VM).

### Files
- Installed in the theme (iconic-tpn/_inc/): backgrounds/vg5k.webp, backgrounds/tvc64.webp, backgrounds/ep128.webp; controllers/vg5k.webp, controllers/tvc64.webp, controllers/ep128.webp; logos/vg5k.webp, logos/tvc64.webp, logos/ep128.webp; metadata/ep128.xml (year 1986 -> 1985)
- Mockups (mockups/, also on the NAS): vg5k.jpg, tvc64.jpg, ep128.jpg
- Originals (sources/<code>/, also on the NAS): vg5k/: vg5k_bg.jpg, vg5k_cab_raw.jpg; tvc64/: tvc64_bg.jpg, tvc64_cab_raw.jpg, tvc64_ref_wikimedia.jpg; ep128/: ep128_bg.jpg, ep128_cab_raw.jpg, ep128_logo_wordmark_src.png
- Backups of old art (replaced/): vg5k_backgrounds.webp, vg5k_controllers.webp, vg5k_logos.webp, tvc64_backgrounds.webp, tvc64_controllers.webp, ep128_logos.webp
- Records: NIGHTLY_LOG.md, TODO.md, PROMPTS.md, CREDITS-TPN.md, salvage_log.tsv, controllers_log.tsv, make_todo.py
- Zip: iconic-tpn_20261004.zip (~/tpn-build and NAS TPN Iconic folder)
- Leftovers: Gemini_Generated_Image_*.jpeg (and tvc_ref.jpg) in Downloads; copies of the originals in ~/tpn-build/incoming


## 2026-10-05

Systems completed (3): cassettevision, pv2000, microvsn. Mockups: mockups/cassettevision.jpg, pv2000.jpg, microvsn.jpg.
Beena (originally picked) was dropped: no hardware photo exists locally or on Wikimedia Commons, and a text-only Gemini render risked a wrong machine. Microvision was taken instead.

| System | Game / scene used for the background | Notes |
|---|---|---|
| cassettevision (Epoch Cassette Vision, 1981) | Kikori no Yosaku-style woodcutter chopping a giant cedar in a misty Japanese forest (original Cassette Vision title; scene was already the PROMPTS.md scene) | First Gemini result accepted. Console: Carbon photo (975x550, transparent) cut out with cutout_flat. Logo: Carbon yellow "Cassette Vision" lettering on a dark rounded plate (yellow vanishes on the white sticker otherwise), then make_logo. |
| pv2000 (Casio PV-2000, 1983) | Generic: orange-suited astronaut kid leaping at a giant chrome robot crab, Earth behind (no original title confirmed) | Machine image: Gemini top-down render from the Carbon photo (4x enlarged reference), cut out with cutout_green. Logo: house-style wordmark (CASIO small grey, PV-2000 navy, yellow bar); the Carbon SVG is a Japanese pixel-kanji logo that renders cropped. Bg needed one follow-up; Earth stayed top-left, so the left third is not dark. |
| microvsn (Microvision, 1979) | Cosmic Hunter-style: space ranger vs giant cosmic wasp in a violet nebula | First result REJECTED and redone: Gemini copied the style reference's famous armoured hero. Re-requested an original character (white/teal flight suit, goggles, ray pistol). Console: Carbon photo straightened (rotated 20 deg, 2x upscaled before rotation) and cut out. Logo: Carbon SVG render (qlmanage) recoloured to transparent, sticker-styled. systemName shortened from "Microvision Milton Bradley" to "Microvision" because it was clipped in the mockup. |

For the user to review:
- None of the three has a confirmed original title except Cassette Vision (scene is a real title, generic art); PV-2000 and Microvision scenes are generic.
- PV-2000 background: Earth and bright areas sit in the left third (not dark/quiet), and the astronaut suit has tiny flag/patch details. Consider a redo.
- PV-2000 machine render has some invented/duplicated key legends ("Entrge", duplicate W, S, X). Logo is a wordmark, not the real badge.
- Microvision: hero is far right and partly cropped by the frame edge; the Block Buster cartridge label is visible on the handheld photo.
- Microvision logo/console come from the Carbon theme; check licence if the theme is shared.
- Process note: file_upload from the Mac is not permitted in these runs, so the style reference reaches Gemini by screenshot of the GitHub image; the Gemini "+" menu needs several clicks before the file input appears.
- NAS SYNC PENDING: /Volumes/stuff was not mounted/accessible. Everything was done locally. To copy to the NAS (TPN Iconic Theme): sources/cassettevision, sources/pv2000, sources/microvsn (from ~/tpn-build/sources/); mockups/cassettevision.jpg, pv2000.jpg, microvsn.jpg (to TPN Iconic/mockups/); iconic-tpn_20261005.zip (to TPN Iconic/); TODO.md, PROMPTS.md, CREDITS-TPN.md, NIGHTLY_LOG.md.
- make_todo.py was updated (custom dict) but could not be run because it reads the original Iconic folder on the NAS; TODO.md was edited by hand (3 rows moved to section A, counts 31/33). Re-run make_todo.py when the NAS is back to confirm.
- Stray copies of TODO.md, PROMPTS.md and CREDITS-TPN.md were also written to ~/tpn-build/ (harmless).
- Local http servers on 127.0.0.1:8766 (and a pre-existing one on 8765) were left running in the Mac session.
- Gemini_Generated_Image_*.jpeg files remain in Downloads (cannot be deleted from the VM).

### Files
- Installed in the theme (iconic-tpn/_inc/): backgrounds/cassettevision.webp, backgrounds/pv2000.webp, backgrounds/microvsn.webp; controllers/cassettevision.webp, controllers/pv2000.webp, controllers/microvsn.webp; logos/cassettevision.webp, logos/pv2000.webp, logos/microvsn.webp; metadata/microvsn.xml (systemName shortened)
- Mockups (mockups/): cassettevision.jpg, pv2000.jpg, microvsn.jpg
- Originals (sources/<code>/): cassettevision/: cassettevision_bg.jpg, cassettevision_cab_src.png, cassettevision_logo_src.png; pv2000/: pv2000_bg.jpg, pv2000_cab_raw.jpg, pv2000_ref_carbon_x4.png, pv2000_logo_src.png; microvsn/: microvsn_bg.jpg, microvsn_cab_src_carbon.png, microvsn_logo_src.png
- Backups of old art (replaced/): cassettevision_backgrounds.webp, cassettevision_controllers.webp, cassettevision_logos.webp (if existed), pv2000_backgrounds.webp, pv2000_controllers.webp, pv2000_logos.webp (if existed), microvsn_backgrounds.webp, microvsn_controllers.webp, microvsn_logos.webp (if existed)
- Records: NIGHTLY_LOG.md, TODO.md, PROMPTS.md, CREDITS-TPN.md, salvage_log.tsv, controllers_log.tsv, make_todo.py
- Zip: iconic-tpn_20261005.zip (~/tpn-build only; NAS copy pending)
- Leftovers: Gemini_Generated_Image_*.jpeg in Downloads; copies in ~/tpn-build/incoming; stray TODO/PROMPTS/CREDITS copies in ~/tpn-build; http.server on port 8766

### 2026-10-05 follow-up (user instruction)
- User said Samus-style fan art is fine on non-Nintendo systems. microvsn background swapped to the first Gemini result (Metroid-style armoured hero vs cosmic wasp). Previous ranger version backed up as replaced/microvsn_backgrounds_ranger.webp and sources/microvsn/microvsn_bg_v2_ranger.jpg; first version saved as sources/microvsn/microvsn_bg_v1_metroid_style.jpg (also incoming/microvsn_bg_v1.jpg). Mockup re-rendered (mockups/microvsn.jpg). The 'avoid clones' line in NIGHTLY_RUN.md was NOT changed.
- Zip rebuilt as iconic-tpn_20261005_b.zip (~/tpn-build; NAS copy still pending). Another Gemini_Generated_Image_lfgqholfgqholfgq.jpeg added to Downloads.

- 2026-10-05: NIGHTLY_RUN.md rule changed at user's request: fan-art style is fine; do not use one system's mascots/characters on other systems.

- 2026-10-05 (final): user clarified - fan art style is fine but never a famous character on a system other than its own. microvsn background REVERTED to the original-character ranger version; mockup re-rendered; NIGHTLY_RUN.md rule reworded. Zip: iconic-tpn_20261005_c.zip.

- 2026-10-05 (beam fix, user request): microvsn background replaced with a Gemini follow-up (same chat) where the bolt clearly comes from the ranger's pistol and hits the wasp's thorax. New original: sources/microvsn/microvsn_bg_v3_beamfix.jpg (also incoming/). Previous ranger version backed up as replaced/microvsn_backgrounds_ranger_v2.webp. Mockup re-rendered. Zip NOT rebuilt yet; NAS copy still pending.

- 2026-10-05 (interactive): Microvision background v4 (staged: ranger right facing left, single bolt into wasp, nothing behind him) installed over v3 (user said beams unconnected / shooting behind him). Source: sources/microvsn/microvsn_bg_v4_staged.jpg; v3 backup in replaced/microvsn_backgrounds_v3.webp. Mockup re-rendered. Zip NOT rebuilt yet (iconic-tpn_20261005_c.zip is stale); NAS still pending.

- 2026-10-05 (interactive): Microvision background v5 (rear over-the-shoulder view of original ranger, wasp small and fully visible in the distance, bolt connects) installed over v4 (wasp hidden by burst). Source: sources/microvsn/microvsn_bg_v5_rear.jpg; v4 backup replaced/microvsn_backgrounds_v4.webp. Mockup re-rendered. Zip NOT rebuilt; NAS pending.

- 2026-10-05 (interactive): Microvision background v6 (rear view ranger lower left, large wasp as centrepiece beside vortex, bolt connects) installed over v5 (wasp too small). Source: sources/microvsn/microvsn_bg_v6_centrepiece.jpg; v5 backup replaced/microvsn_backgrounds_v5.webp. Mockup re-rendered. Zip NOT rebuilt; NAS pending.

- 2026-10-05 (interactive): Microvision background v7 (action moved into right 55% clear of the system column; wasp centrepiece by vortex, rear-view ranger, bolt connects) installed over v6. Source sources/microvsn/microvsn_bg_v7_rightside.jpg; v6 backup replaced/microvsn_backgrounds_v6.webp. Composition rules added to NIGHTLY_RUN.md. Zip NOT rebuilt; NAS pending.

- 2026-10-05 (interactive): Microvision background v8 (ONE small rear-view ranger lower right, small wasp upper right by vortex, single bolt, left 45% empty) installed over v7 (v7 showed two figures, one overlapping the system column; an intermediate 3-figure attempt was rejected and not kept). Source sources/microvsn/microvsn_bg_v8_single.jpg; v7 backup replaced/microvsn_backgrounds_v7.webp. HARD RULE added to NIGHTLY_RUN.md: nothing in the system column. Zip NOT rebuilt; NAS pending.

- 2026-10-05 (interactive): Microvision background v9 (user: v8 too small; wanted characters filling the right 55% but not massive). One rear-view ranger, large wasp, bolt connects. Source sources/microvsn/microvsn_bg_v9_big.jpg; v8 backup replaced/microvsn_backgrounds_v8.webp. KNOWN: ranger back/shoulder just touches the column edge (~x700-730 of 1920) and wasp right wing clips the right frame edge. Zip NOT rebuilt; NAS pending.

- 2026-10-05 (interactive): Microvision background v11 installed (fresh Gemini composition with explicit positions: ranger centre ~58%, wasp ~80%, left 38% empty). Fixes v9 faults (shoulder in column, wing clipped). Gemini ignored two follow-up edits (v10 attempts unchanged; a local rescale of v9 was tried and rejected: reflected-wing artefact). Style is slightly brighter/glossier than v9. Source sources/microvsn/microvsn_bg_v11_fresh.jpg; v9 source kept (microvsn_bg_v9_big.jpg). Zip NOT rebuilt; NAS pending.

- 2026-10-05 (interactive): Zip rebuilt as iconic-tpn_20261005_d.zip with Microvision v11 background (supersedes _c). NAS still pending.


## 2026-10-06

Systems completed (3): vidbrain, cbm2, sv8000. Mockups: mockups/vidbrain.jpg, cbm2.jpg, sv8000.jpg. The NAS was mounted this run, so everything was synced (including last night's pending items).
Swapped from the first plan: Commodore 16 was dropped because the "c16.png" in the Carbon/ckau PixN folders is really a Commodore 128 (mislabelled); no verified C16 photo exists locally.

| System | Game / scene used for the background | Notes |
|---|---|---|
| vidbrain (VideoBrain Family Computer, 1977) | Generic 1970s football: original quarterback (plain blue jersey, white helmet, no logos) mid-throw under floodlights, one defender silhouette behind | First Gemini result accepted. No specific original title confirmed (VideoBrain did ship sports cartridges). Console: Carbon photo (3/4 view, joystick handset) cut out, 2x upscaled, light edge halo removed. Logo: Carbon SVG rendered with cairosvg, sticker-styled. systemName shortened to "VideoBrain" (was clipped). |
| cbm2 (Commodore CBM-II, 1982) | Generic: lone astronaut watching a gold-foiled lunar lander touch down (CBM-II was a business line; no original game confirmed) | First result accepted; left half empty. Machine: Carbon photo of the 710 (front view, transparent), 2x upscaled. Logo: Carbon "commodore CBM-II" SVG, very wide, sticker-styled. |
| sv8000 (Bandai Super Vision 8000, 1979) | Generic: original orange-suited 1970s pilot firing a ray pistol at a saucer mothership over a night city | First result accepted. Console: Carbon photo (flat, near top-down) cut out. Logo: Carbon SVG, sticker-styled. |

For the user to review:
- All three scenes are generic (no confirmed original titles).
- sv8000 background: the beam starts at the very top edge at about 49% across (just right of the column) and passes through the saucer rather than stopping at it; a faint vertical seam sits at about 42% where the dark left panel meets the scene.
- vidbrain background: the quarterback's right hand is close to the right frame edge; defender silhouette sits at 56-66% across (outside the column).
- Machine photos are Carbon theme photos (check licence before sharing the theme); cbm2 is a front view rather than top-down (same as the ibmpcjr precedent).
- Gemini style reference reached Gemini as a screenshot of the GitHub image (file_upload from the Mac is not permitted). The first cbm2 attempt used a low-res reference by mistake; the accepted result was still on style.
- Process note: the VM shell cannot use the Mac venv (~/tpn-build/venv/bin/python is a macOS binary); system python3 (PIL, numpy, cv2) was used and cairosvg was pip-installed for SVG logos.

### Files
- Installed in the theme (iconic-tpn/_inc/): backgrounds/vidbrain.webp, backgrounds/cbm2.webp, backgrounds/sv8000.webp; controllers/vidbrain.webp, controllers/cbm2.webp, controllers/sv8000.webp; logos/vidbrain.webp, logos/cbm2.webp, logos/sv8000.webp; metadata/vidbrain.xml (systemName shortened)
- Mockups (mockups/, also on the NAS): vidbrain.jpg, cbm2.jpg, sv8000.jpg
- Originals (sources/<code>/, also on the NAS): vidbrain/: vidbrain_bg.jpg, vidbrain_cab_src_carbon.png, vidbrain_logo_src.png; cbm2/: cbm2_bg.jpg, cbm2_cab_src_carbon.png, cbm2_logo_src.png; sv8000/: sv8000_bg.jpg, sv8000_cab_src_carbon.png, sv8000_logo_src.png
- Backups of old art (replaced/): vidbrain_backgrounds.webp, vidbrain_controllers.webp, vidbrain_logos.webp, cbm2_backgrounds.webp, cbm2_controllers.webp, sv8000_backgrounds.webp, sv8000_controllers.webp, sv8000_logos.webp
- Records: NIGHTLY_LOG.md, TODO.md, PROMPTS.md, CREDITS-TPN.md, salvage_log.tsv, controllers_log.tsv, make_todo.py
- Zip: iconic-tpn_20261006.zip (~/tpn-build and TPN Iconic on the NAS)
- Leftovers: Gemini_Generated_Image_81wuhc81wuhc81wu.jpeg, Gemini_Generated_Image_5b3x0a5b3x0a5b3x.jpeg, Gemini_Generated_Image_mgh866mgh866mgh8.jpeg in Downloads (cannot be deleted); copies in ~/tpn-build/incoming (vidbrain_bg.jpg, cbm2_bg.jpg, sv8000_bg.jpg); stale zips iconic-tpn_20261006.zip rm blocked (overwritten instead)
- Leftover (2026-10-06): TPN Iconic/iconic-tpn_20261006.zip.part on the NAS is a stray partial copy and can be deleted (rm blocked); the real zip iconic-tpn_20261006.zip there is complete and verified identical.


## 2026-10-07 (run fired 05:17 UTC) - BLOCKED, no systems completed

Blocker: Claude in Chrome extension not reachable ("Browser extension is not connected"), so the Gemini workflow (attach SNES style reference via upload_image) could not run. The built-in browser pane reaches gemini.google.com but has no image/file upload tool, so the style reference cannot be attached. The remote-devices link also dropped briefly mid-run (reconnected). No theme files were changed.

Plan for next run (usable hardware photos already verified in ~/tpn-build/pixn_assets):
- pegasus (Aamber Pegasus): carbon/consoles/pegasus.png, 800x800 RGBA, already flat top-down; logo carbon/logos/pegasus.svg
- mpu1000 (Acetronic/Soltronic MPU-1000 console, 3/4 view with joystick): carbon/consoles/mpu1000.png; logo carbon/logos/mpu1000.svg
- myvision (My Vision KH-1000 TV + cartridge + console): carbon/consoles/myvision.png; logo carbon/logos/myvision.svg
- Games research was thin (searches returned little); pegasus/myvision likely need generic original-character scenes.
Needs: Chrome open on the Mac with the Claude extension signed in.

### Files
- Installed in the theme: none
- Mockups / Originals / Backups: none
- Records: NIGHTLY_LOG.md only
- Zip: none
- Leftovers: none


## 2026-10-07 (retry after Mac update; supersedes the BLOCKED entry above)

Systems completed (3): pegasus, mpu1000, myvision. Mockups: mockups/pegasus.jpg, mpu1000.jpg, myvision.jpg. NAS mounted, everything synced.

| System | Game / scene used for the background | Notes |
|---|---|---|
| pegasus (Aamber Pegasus, 1981) | Generic: original hooded mountain warden with a lantern (rear view) facing a giant stone golem in a storm canyon | No original Pegasus title confirmed. First attempt had the warden at ~30% across (inside the system column), so it was re-prompted as a fresh composition; that came back with column guide lines drawn in, removed by one same-chat follow-up. System image: Carbon photo (already flat top-down) cropped. Logo: Carbon SVG via cairosvg. |
| mpu1000 (Acetronic MPU-1000, 1979) | Rocket Patrol-style: original silver-and-red rocket firing one laser line at one saucer | First try had the rocket tail at ~41% across, so regenerated smaller/further right (tail now ~46%). System image: Carbon photo (console + joystick, 3/4 view) cropped. Logo: Carbon SVG. |
| myvision (My Vision KH-1000, 1983) | Generic: original master player in a red-and-gold kimono placing a jade tile on a floating shogi/mahjong board | First result accepted. System image: Carbon photo (TV, cartridge, console) cropped. Logo: Carbon SVG. |

For the user to review:
- All three scenes are generic or original-character fan art; no specific original titles confirmed (web searches were thin).
- Backgrounds are 1376x768 Gemini downloads scaled to 1920x1080 (same as earlier systems; Gemini's full-size download is 1376x768).
- pegasus: the golem's right shoulder and the rock at the right edge sit close to the frame edge but are not cropped. mpu1000: the rocket tail just clears the column (~46%). myvision: board and a lantern sit close to the right edge (~96-99%).
- myvision display name is still "My Vision KH-1000" (fits the column in the mockup).
- Machine photos are Carbon theme photos (check licence before sharing the theme).
- Chrome extension was unavailable at the 05:17 UTC firing; this run used it after the Mac update finished. The upload menu in Gemini needs the + clicked twice after a fresh page load before the file input appears.

### Files
- Installed in the theme (iconic-tpn/_inc/): backgrounds/pegasus.webp, backgrounds/mpu1000.webp, backgrounds/myvision.webp; controllers/pegasus.webp, controllers/mpu1000.webp, controllers/myvision.webp; logos/pegasus.webp, logos/mpu1000.webp, logos/myvision.webp (no metadata changed)
- Mockups (mockups/, also on the NAS): pegasus.jpg, mpu1000.jpg, myvision.jpg
- Originals (sources/<code>/, also on the NAS): pegasus/: pegasus_bg.jpg, pegasus_cab_src_carbon.png, pegasus_logo_src.png; mpu1000/: mpu1000_bg.jpg, mpu1000_cab_src_carbon.png, mpu1000_logo_src.png; myvision/: myvision_bg.jpg, myvision_cab_src_carbon.png, myvision_logo_src.png
- Backups of old art (replaced/): pegasus_backgrounds.webp, pegasus_controllers.webp, pegasus_logos.webp, mpu1000_backgrounds.webp, mpu1000_controllers.webp, mpu1000_logos.webp, myvision_backgrounds.webp, myvision_controllers.webp, myvision_logos.webp (existing copies from earlier, not overwritten)
- Records: NIGHTLY_LOG.md, TODO.md, PROMPTS.md, CREDITS-TPN.md, salvage_log.tsv, controllers_log.tsv, make_todo.py
- Zip: iconic-tpn_20261007.zip (~/tpn-build and TPN Iconic on the NAS)
- Leftovers: Gemini_Generated_Image_p3v29zp3v29zp3v2.jpeg, Gemini_Generated_Image_9jcgbd9jcgbd9jcg.jpeg, Gemini_Generated_Image_ox3pd8ox3pd8ox3p.jpeg in Downloads (cannot be deleted); copies in ~/tpn-build/incoming (pegasus_bg.jpg, mpu1000_bg.jpg, myvision_bg.jpg)


## 2026-10-08 - 4 systems completed (pocketstation, vemulator, bk, elektronika)

NAS (/Volumes/stuff) was NOT mounted this run (even via the device file tools), so the NAS steps were skipped: **NAS SYNC PENDING**. Everything was done locally (theme, mockups/, sources/, replaced/, zip in ~/tpn-build). Chrome and Gemini worked fine (the Gemini + button needs an odd number of clicks before the file input appears).

Stopped at four, not five: no other unticked B1/C/D/E system had a usable hardware photo (c16 photo is really a C128, tiger/tvgames are licensed-character collages, videodriver is a race car, section D/E systems have no photo at all), so a fifth would have needed a web photo hunt and Gemini render.

| System | Scene | Notes |
|---|---|---|
| pocketstation | Generic: original adventurer in a yellow rain hood riding a giant glowing manta ray over floating islands at sunset | First result accepted. |
| vemulator (Visual Memory Unit) | Generic: original round robot companion with long ears leaping over a neon ocean, ringed planet behind (no Sega characters) | First result accepted. Display name shortened from "Sega Visual Memory Unit" (it was clipped in the system column) in metadata/vemulator.xml. |
| bk (Elektronika BK) | Generic: orange-suited cosmonaut (rear view) walking to a red-lit space station on an ice planet under a giant moon | First result accepted. The Carbon bk logo says "БК 0010-01" (same as bk001001), so I made a wordmark: электроника over БК. |
| elektronika (Elektronika IM) | Nu, pogodi!-style egg catching: original farmhand girl in a red cap catching a golden egg in a basket under a hen-house chute, snowy village at dusk | First result accepted (no wolf or hare used). A small village house sits just right of the system column. |

For the user to review:
- pocketstation: a child in a yellow rain hood could remind people of Six from Little Nightmares; pose and setting are different (riding a manta ray) but swap it if you think it is too close.
- All scenes are original-character fan art; no specific original game titles confirmed for pocketstation, vemulator or bk.
- Machine photos are Carbon theme photos (check licence before sharing the theme); the bk photo is a 3/4 view rather than top-down, vemulator and elektronika photos were small and doubled in size.
- pocketstation and vemulator had overlay files; they were moved (deletion is blocked) to replaced/<code>/overlays-removed-<code>.webp, so they no longer draw over the new backgrounds.
- Backgrounds are 1376x768 Gemini downloads scaled to 1920x1080, as before.
- TODO.md was patched directly (make_todo.py cannot run without the NAS originals); the make_todo.py custom dict was updated so a future regeneration matches.
- Zip created with a redirect (zip -r - > file) because zip's temp-file rename is blocked in the connected folder.

NAS SYNC PENDING - copy to /Volumes/stuff/Emulation/TPN Iconic Theme/ when the NAS is mounted:
- TPN Iconic/iconic-tpn_20261008.zip (from ~/tpn-build)
- TPN Iconic/mockups/: pocketstation.jpg, vemulator.jpg, bk.jpg, elektronika.jpg (from ~/tpn-build/mockups)
- sources/pocketstation, sources/vemulator, sources/bk, sources/elektronika (from ~/tpn-build/sources)
- TODO.md, PROMPTS.md, CREDITS-TPN.md, NIGHTLY_LOG.md (from iconic-tpn/)

### Files
- Installed in the theme (iconic-tpn/_inc/): backgrounds/pocketstation.webp, backgrounds/vemulator.webp, backgrounds/bk.webp, backgrounds/elektronika.webp; controllers/pocketstation.webp, controllers/vemulator.webp, controllers/bk.webp, controllers/elektronika.webp; logos/pocketstation.webp, logos/vemulator.webp, logos/bk.webp, logos/elektronika.webp; metadata/vemulator.xml (systemName shortened); overlays/pocketstation.webp and overlays/vemulator.webp removed (moved to replaced/)
- Mockups (mockups/, NAS pending): pocketstation.jpg, vemulator.jpg, bk.jpg, elektronika.jpg
- Originals (sources/<code>/, NAS pending): pocketstation/: pocketstation_bg.jpg, pocketstation_cab_src_carbon.png, pocketstation_logo_src.png; vemulator/: vemulator_bg.jpg, vemulator_cab_src_carbon.png, vemulator_logo_src.png; bk/: bk_bg.jpg, bk_cab_src_carbon.png, bk_logo_src.png; elektronika/: elektronika_bg.jpg, elektronika_cab_src_carbon.png, elektronika_logo_src.png
- Backups of old art (replaced/): pocketstation/ and vemulator/: backgrounds-<code>.webp, controllers-<code>.webp (where they existed), overlays-<code>.webp, overlays-removed-<code>.webp; bk/ and elektronika/: backgrounds/controllers/logos backups as available (existing copies not overwritten)
- Records: NIGHTLY_LOG.md, TODO.md, PROMPTS.md, CREDITS-TPN.md, salvage_log.tsv, controllers_log.tsv, make_todo.py
- Zip: iconic-tpn_20261008.zip (~/tpn-build only; NAS copy pending)
- Leftovers: Gemini_Generated_Image_4ah4gq4ah4gq4ah4.jpeg, Gemini_Generated_Image_ukaup3ukaup3ukau.jpeg, Gemini_Generated_Image_u2qdtzu2qdtzu2qd.jpeg, Gemini_Generated_Image_w95x5hw95x5hw95x.jpeg in Downloads (cannot be deleted; copies in ~/tpn-build/incoming as <code>_bg.jpg); NAS items above

Update (same day): the NAS was mounted afterwards and the pending sync was completed: zip (verified identical), 4 mockups, 4 sources folders, TODO/PROMPTS/CREDITS/NIGHTLY_LOG copied. NAS SYNC PENDING is cleared.

### Fixes after review (2026-10-08, user feedback)
- aquarius: the old background had a floating hand holding the torch (and the hand sat near the system column). Regenerated (Gemini, knight holds his own torch, left 45% empty) and installed; display name shortened to "Aquarius" (it was clipped in the column). Old art kept: sources/aquarius/aquarius_bg_v1_floating_hand.jpg, replaced/aquarius/backgrounds-aquarius-v1-floating-hand.webp. Mockup: mockups/aquarius.jpg. Knight is slightly cropped by the right frame edge.
- bk: system image was angled; replaced with a Gemini flat top-down render of the BK-0010 photo (green screen, cut out with cutout_green.py), same as other computers. Old: replaced/bk/controllers-bk-v1-angled.webp; raw render: sources/bk/bk_cab_topdown_gemini_raw.jpg. Mockup: mockups/bk.jpg.
- Note for the other Carbon photos used tonight/last night that are not top-down (cbm2, mpu1000, myvision, pocketstation, vemulator, elektronika handheld): same fix available if wanted.
- Idea from user: the original Iconic arcade images use a three-cabinet group (centre front-on, two flanking turned left and right). Our single cabinets could be remade that way.
- segasystem32: first three-cabinet remake (trial, awaiting user OK before the other arcade boards). Gemini with 4 references (OG cps2 group layout, our old cabinet, logo, background); needed one follow-up ("tighter, overlapping like image 1") to get the OG-style cluster. Cut out with cutout_green.py and installed as controllers/segasystem32.webp; old single cabinet in replaced/segasystem32_controllers_single.webp; raw in sources/segasystem32/segasystem32_cab_3cab_gemini_raw.jpg. Files can be uploaded to Gemini via file_upload using the staged path (/mnt/user-data/uploads/...), several at once.

## 2026-10-08 follow-up: System 32 three-cabinet group (OG style)
- segasystem32 controllers image replaced with an OG-style group: blue System 32 branded centre cabinet plus Golden Axe: Revenge of Death Adder (left) and Alien Storm (right) game cabinets with faded vinyl. Previous identical-cabinet group backed up to replaced/segasystem32_controllers_tri_v1_identical.webp; old single cabinet in replaced/segasystem32_controllers_single.webp.
- Rule agreed with user: three-cabinet groups only for upright cabinets (centre = system-branded cabinet in full colour, sides = real game cabinets with muted colours and own vinyl/marquee/screen). Sit-down cabinets (Ringwide, Nu, segaalls, segare, segaer) keep their single images.
- Files: iconic-tpn/_inc/controllers/segasystem32.webp, mockups/segasystem32.jpg, sources/segasystem32/segasystem32_cab_og_style_gemini_raw.jpg

## 2026-10-08 follow-up: remaining upright arcade groups
- aleck64: three-cabinet group INSTALLED (centre Aleck 64 cabinet + Star Soldier: Vanishing Earth + Eleven Beat World Tournament). User says the side cabinets are too faded/grey compared to System 32: needs a redo with BLACK side-cabinet bodies and richer vinyl colour. Previous single cabinet in replaced/aleck64_controllers_single.webp.
- namco11: NOT installed. Gemini attempt (Tekken 2 + Soul Edge sides) had black bodies and vivid art, but the characters spilled outside the cabinet outlines, leaving green holes in the cut-out. Redo needed with art contained inside the cabinets and original characters (the first attempt copied Street Fighter characters from the CPS2 reference; never allow characters from the reference image).
- Gemini image quota ran out on 2026-10-08 (limit resets about 13:42 local time); redo both after the reset.
- Rule: sit-down cabinets stay single; upright systems get the three-cabinet group (see NIGHTLY_RUN.md / PROMPTS.md).

## 2026-10-08 later: Aleck 64 redo, Namco trial
- aleck64: REDONE and INSTALLED. Black side-cabinet bodies, vivid Star Soldier and Eleven Beat vinyl. Faded v1 backed up to replaced/aleck64_controllers_tri_v1_faded.webp, original single in replaced/aleck64_controllers_single.webp. Raw: sources/aleck64/aleck64_cab_3cab_v2_gemini_raw.jpg. Mockup: mockups/aleck64.jpg. Note: the centre marquee still reads "ASTRO CITY" in small text.
- namco11: v2 trial only, NOT installed (still the old single cabinet). Black sides with original Tekken 2 / Soul Edge style art, but a thin green fringe beside the centre cabinet and a busy lower panel on the centre. Trial mockup: work/trial/namco11_3cab_v2.jpg. Waiting on the user's decision to install or retry.

## 2026-10-08 later still: Aleck 64 centre fixed, Namco installed
- aleck64: v3 INSTALLED. The v2 centre had been redrawn by Gemini (logo on screen, extra sticker on the doors). v3 centre is a faithful copy of the original (Astro City gameplay screen, no extra logos). v2 backed up to replaced/aleck64_controllers_tri_v2_centre_redrawn.webp. Raw: sources/aleck64/aleck64_cab_3cab_v3_gemini_raw.jpg.
- namco11: v4 INSTALLED. Previous trials had very long side vinyls (cabinets looked extremely long behind the centre). Fixed by asking for short, compact side vinyls and a front-on centre with a plain lower body. Old single: replaced/namco11/controllers-namco11-single.webp. Raw: sources/namco11/namco11_cab_3cab_v4_gemini_raw.jpg.
- Tip: Gemini copies angled/side art from the reference cabinet photo, so say "centre seen straight front-on, no side panel" and "side vinyl covers only a short panel".

## 2026-10-09 nightly run (safety-net entry after system 3; systems 4-5 attempted next)
Systems finished: studio2, orao, ondra.
- studio2 (Studio II, RCA 1977): game = built-in Bowling. Giant marble bowling ball smashing ten pins on a dark lane, all in the right 55%. Redone once: the first image had neon signs with text ("LUCKY STRIKE", "BOWL-O-RAMA") and was centred, so I re-prompted as a fresh composition (rule from NIGHTLY_RUN.md). System image: Carbon-PixN console photo (already transparent, 3/4 view), cropped. Logo: PixN Carbon svg (RCA Studio II), sticker via make_logo.py.
- orao (Orao, PEL Varazdin 1984): game = Nevidljivi (the only game on the Orao No 0 tape, Suzy Soft 1987). I could not find a description of the game, so the scene is a guess from the title (original hooded investigator + invisible presence shown as a shimmer). System image: Gemini top-down render from a Wikimedia Commons photo (Orao-IMG 7278.jpg), green screen, cut out with cutout_green.py. Logo: PixN Carbon svg (PEL ORAO), sticker.
- ondra (Ondra, Tesla Liberec): game = Tenebra (atmospheric puzzle game; ported to the Ondra in 2024). Not a period title, as I could not confirm any 1980s Ondra game; please review. Original wanderer in a red poncho at a cracking stone door. System image: Gemini top-down render from the Wikimedia Commons photo OndraComputer.jpg; cutout_green.py left a ragged 1-2 px edge on the black case, so I trimmed the outer edge (top vents removed by cropping). Logo: PixN Carbon svg with its dark rectangle removed. Metadata: Ondra release year corrected 1985 -> 1987 (production start; 1985 was the prototype).
- Nothing regenerated apart from studio2 (1). No hero in the system column; no famous characters used.
- Reference photos were taken from Wikimedia Commons pages (screenshots uploaded to Gemini); check the licences if the theme is published (CREDITS lists them as Wikimedia Commons).
- NAS: mounted and writable. A stray empty file ".wtest" was left in "TPN Iconic Theme" on the NAS (my write test; rm blocked) - safe to delete.

## 2026-10-09 nightly run, systems 4-5 (final update)
Five systems finished in total: studio2, orao, ondra, n501, pippin.
- n501 (NUON DVD-N501, VM Labs 2000 / Samsung 2001): game = Tempest 3000 style tube shooter. Original golden bat-wing starfighter firing down a neon vortex at a red crystal enemy, right 55%. System image: Carbon-PixN NUON image as-is (it shows a Samsung-type DVD player, not the exact N501). Logo: Carbon NUON logo with the "FROM NOW ON" tagline cropped off. Metadata: name shortened so it is not clipped, hardware set to console.
- pippin (Pippin @mark, Apple/Bandai 1996): game = a rally racer (Racing Days style; I could not confirm a specific title, please review). Original cobalt striped rally coupe drifting a mountain hairpin at dusk, right 55%; the car resembles a classic Escort rally car with a very small grille badge. System image: Gemini green-screen render of the Wikimedia Commons Pippin set photo (console plus controller), cut with a copy of cutout_green.py that keeps the controller (work/nightly/cutout_multi.py). Logo: Carbon Pippin logo, grey background removed. Metadata: release year 1986 corrected to 1996.
- No regenerations for these two. Left 45% empty in both; no famous characters.
- Hardware photos for orao, ondra and pippin came from Wikimedia Commons; check licences if publishing.

### Files
- Installed in the theme (iconic-tpn/_inc/): backgrounds/{studio2,orao,ondra,n501,pippin}.webp; controllers/{studio2,orao,ondra,n501,pippin}.webp; logos/{studio2,orao,ondra,n501,pippin}.webp; metadata/ondra.xml (year 1985 to 1987), metadata/n501.xml (name shortened to "NUON DVD-N501", hardware console), metadata/pippin.xml (year 1986 to 1996)
- Mockups (mockups/, also on the NAS in TPN Iconic/mockups): studio2.jpg, orao.jpg, ondra.jpg, n501.jpg, pippin.jpg
- Originals (sources/<code>/, also on the NAS): studio2/: studio2_bg.jpg, studio2_cab_src_carbon.png, studio2_logo_src.png; orao/: orao_bg.jpg, orao_cab_gemini_raw.jpg, orao_logo_src.png; ondra/: ondra_bg.jpg, ondra_cab_gemini_raw.jpg, ondra_logo_src.png; n501/: n501_bg.jpg, n501_cab_src_carbon.png, n501_logo_src.png; pippin/: pippin_bg.jpg, pippin_cab_gemini_raw.jpg, pippin_logo_src.png
- Backups of old art (replaced/): backgrounds-{studio2,orao,ondra,n501,pippin}-old.webp; logos-{studio2,orao,ondra,n501,pippin}-old.webp (no controller backups: none existed)
- Records changed: NIGHTLY_LOG.md, TODO.md, PROMPTS.md, CREDITS-TPN.md, salvage_log.tsv, controllers_log.tsv, make_todo.py
- Zip: iconic-tpn_20261009_b.zip (~/tpn-build and NAS TPN Iconic/); the earlier iconic-tpn_20261009.zip only covers the first three systems
- Leftovers: .wtest empty file on the NAS (undeletable); Gemini_Generated_Image_*.jpeg downloads in Downloads (undeletable; copies are in incoming/); 3 extra Chrome tabs closed

- Systems completed: tonight 5, total done 46 (section A)
- Systems left: 73 (B1 27, C 36, D 0, E 10)
- Nights to complete: 15 at 5 per night (25 at 3 per night)

## 2026-10-09 redo (user request): GameCube and PS Vita backgrounds
- gc: new background (original girl ghost-hunter, brass vacuum-lantern, haunted mansion). Old Iconic art (Billy Hatcher) kept in replaced/backgrounds-gc-iconic-original.webp. Variants gc-jp and gch still show the old art.
- psvita: new background for LittleBigPlanet Vita (original stitched felt fox cub in a cardboard and fabric craft world; Sackboy deliberately not used because he is a famous Sony character). First attempt had a platform and lights in the left 45 percent, redone once. Old Iconic art (Gravity Rush) kept in replaced/backgrounds-psvita-iconic-original.webp.
- Files: _inc/backgrounds/gc.webp, psvita.webp; mockups/gc.jpg, psvita.jpg; sources/gc/gc_bg.jpg, sources/psvita/psvita_bg.jpg, psvita_bg_v1_rejected_left_platform.jpg; replaced/backgrounds-{gc,psvita}-iconic-original.webp; records: CREDITS-TPN.md, PROMPTS.md, NIGHTLY_LOG.md

- 2026-10-09 psvita: replaced the fox version with a user-supplied LittleBigPlanet image (Sackboy), fitted to 16:9 with a blurred scenery extension on the left (layout only, no generation). It is a glossy 3D-render look, not the painted style of the other backgrounds. Fox version kept in replaced/backgrounds-psvita-fox-version.webp. Source: sources/psvita/psvita_bg_lbp_user_supplied.jpg

- 2026-10-09 psvita: user supplied a painted LittleBigPlanet image (1376x768, Sackboy; made by the user in Gemini), fitted to 1920x1080 (layout only, no generation) and installed. Replaces the earlier LBP versions. Source: sources/psvita/psvita_bg_lbp_painted_v2_user.jpg; earlier versions: replaced/backgrounds-psvita-fox-version.webp, -lbp-render-version.webp, -lbp-painted-v1.webp

- 2026-10-09 psvita: applied a local (non-generative) grade to the user-supplied painted LBP image: contrast and brightness lift, slight softening of the knit texture on the character. A rim-light attempt was dropped (messy). Ungraded version kept in replaced/backgrounds-psvita-lbp-painted-v2-ungraded.webp.

- 2026-10-09 psvita: installed the newest user-supplied painted LBP image (psvita_bg_lbp_painted_v3_user.jpg, 1376x768, layout only). Earlier versions kept in replaced/.
- RESERVED FOR PS3 (user request): the fox cub craft-world backgrounds are kept in sources/_reserved_for_ps3/ (also on the NAS) to use when we reach PS3 (ps3 / LittleBigPlanet-style craft world). Use the clean-left version (v2).
- Update: the fox backgrounds are also earmarked for PSP (user: "maybe PSP as well as PS3"). Use for whichever fits.
- psvita mockup: description limited to 4 lines (bottom two removed at user request; render with MAXLINES=4 python work/nightly/mk.py psvita). Mockup only, metadata unchanged.

- 2026-10-09 ps2: background replaced with an original Vice City-style tribute (Gemini, one generation, no characters). Old Iconic art (Ratchet and Clank) kept in replaced/backgrounds-ps2-iconic-original.webp. Files: _inc/backgrounds/ps2.webp, mockups/ps2.jpg, sources/ps2/ps2_bg_vicecity_tribute.jpg. ps2-jp and ps2h variants still show the old art.

- 2026-10-09 ps2: installed the user's edited version of the Vice City tribute (a character added by the user, 1377x768, layout/fit only, no generation). The no-character Gemini version is kept in replaced/backgrounds-ps2-vicecity-no-character.webp and sources/ps2/ps2_bg_vicecity_tribute.jpg.

- 2026-10-09 ps2: installed a composite: user Gemini-blended character version (1024x572, painted into the scene) for the right side, with the clean left side and signage from the earlier no-clutter version (Gemini had added a left palm, cassettes, sunglasses, a newspaper and readable neon signs, which were removed by compositing). Source: sources/ps2/ps2_bg_vicecity_gemini_blend_user.png; result: ps2_bg_vicecity_character_composite_1920.jpg. Earlier versions in replaced/.
- 2026-10-09 PS2 interim: user's clean Vice City v2 (1024x572, little city on left removed locally) installed for mockup until 1080p version from Gemini; previous composite backed up as replaced/backgrounds-ps2-vicecity-composite-final.webp
- 2026-10-09 PS2: user's 1376x768 Vice City v3 installed, little city on left removed locally; 1024 interim backed up in replaced/
- 2026-10-09 PS Vita: user-supplied grapple-swing Sackboy v4 (Gemini would not enlarge him); layout-only zoom 1.3x anchored right, installed
- 2026-10-09 PS Vita: v5 = v3 scene on the right (stalls kept) + v4 clean haze on the left, 1.3x zoom, installed
- 2026-10-09 PS Vita: v6 = Gemini faithful re-render (sharpen only) of the v5 zoomed crop (1375x768), installed; v5 soft backed up
- 2026-10-09: removed stale original Iconic overlays for psvita, ps2, gc (old-art arm/claw leftovers); backed up in replaced/overlays-*-iconic-original.webp
- 2026-10-09 PS3: reserved fox craft-world v2 installed as ps3 background; Iconic original backed up in replaced/
- 2026-10-09 GameCube: Resident Evil 4 style village tribute (environment only, no characters) installed; ghost-hunter version backed up in replaced/
- 2026-10-09 PS3: Uncharted-style jungle temple tribute (environment only, seam softened locally) installed over the fox art; fox version kept in replaced/ and sources/_reserved_for_ps3 (for PSP)
- 2026-10-09: added CHARACTER_OUTLINE.md (generic Gemini brief for adding a character that fits the theme)
- 2026-10-09 PS3: user's Gemini character version (1024x768) fitted 16:9 (crop rows 130-706), gentler seam fade, installed
- 2026-10-09 PS3: Gemini edit of the clean background (user's mockup upload had UI baked in): character smaller, hands to the rope rails; installed
- 2026-10-09 PS3: character re-added small via Gemini from the clean no-character background plus the user's character reference; installed
2026-10-09: PS3 background re-done as Gemini zoom-out of the Uncharted scene (character smaller); previous backed up replaced/backgrounds-ps3-uncharted-small-character-v1.webp
2026-10-09: GameCube background replaced with Grant's RE4 village + character version (via Gemini); no-character version backed up replaced/backgrounds-gc-re4-village-no-character.webp
2026-10-09: GameCube RE4 background re-done as Gemini zoom-out (character smaller); previous backed up replaced/backgrounds-gc-re4-leon-large.webp
2026-10-09: GameCube RE4: Leon moved forward by compositing (cutout) onto Gemini clean zoomed-out village; previous backed up replaced/backgrounds-gc-re4-leon-zoomout-v1.webp
2026-10-09: GameCube: removed green smudge behind legs in Leon composite (leg mask by trouser colour)
2026-10-09: GameCube to be redone as Super Smash Bros-style stage (RE4 too dark). RE4 village art kept in sources/spare/ to repurpose (candidates: Wii, PC).
2026-10-09: GameCube main background is now a Smash Bros-style floating arena (Gemini, seam fixed, no characters; Grant to add characters). RE4 version kept as gc_1 (sources/gc/gc_1_re4_leon_forward.webp and sources/spare/).
