# Iconic TPN - to-do list

## Start here - adding new art

1. Pick a system from section B1, C, D or E below.
2. Find the system in section 5 (Gemini prompts) at the bottom of this file. Attach a style reference from the Iconic-style-refs folder on the Mac desktop, paste the STANDARD BLOCK with the system scene line, and generate in Gemini.
3. Download with Gemini's own download button (full size, never screenshots).
4. Find a system image (cabinet / console / computer photo on a PLAIN white or flat grey background) and a logo (transparent PNG or platform badge).
5. Save all three into **Downloads/Iconic Images**, named with the system code:
   - `<code>_bg.jpg` - background, e.g. `alice32_bg.jpg`
   - `<code>_cab.png` - system image, e.g. `alice32_cab.png`
   - `<code>_logo.png` - logo, e.g. `alice32_logo.png`
6. Tell Claude which systems are ready. Claude processes them, installs into the theme, renders mockups, files the originals in `sources/<code>/` on the NAS and ticks them off here.

Rules: new Gemini chat per system; cinematic poster moment, one large hero close to the viewer, centre-right; left third mostly empty; no text/logos/UI/cabinets in backgrounds; no upscaled art. Full standard: see section 1 and section 5.

Links: [PROMPTS.md](PROMPTS.md) - [CREDITS-TPN.md](CREDITS-TPN.md) - mockups: `stuff/Emulation/TPN Iconic Theme/TPN Iconic/mockups` - originals: `stuff/Emulation/TPN Iconic Theme/sources`

Working copy: Mac ~/tpn-build/iconic-tpn - zip on NAS: stuff/Emulation/TPN Iconic Theme/TPN Iconic

## 1. Theme - general

- [x] Sega ALLS and Sega RingEdge custom art installed (background, cabinet, logo)
- [x] PS Vita background redone (2026-10-09): painted LittleBigPlanet image supplied by the user, fitted to 16:9; fox cub versions reserved for PS3/PSP (sources/_reserved_for_ps3/)
- [ ] GameCube background redone with an original ghost-hunter scene (2026-10-09), awaiting user decision (keep, or restore the original Iconic art); gc-jp and gch variants still show the old art
- [ ] Remake all backgrounds in section B1 with custom art (Gemini scene + cabinet/hardware image + sticker logo), same standard as the Sega boards - no upscaled art
- [ ] Work through PROMPTS.md (one Gemini prompt per system, plus what photo/logo to find); save results to Downloads/Iconic Images named <code>_bg / <code>_cab / <code>_logo
- [ ] Standard for all new art: new Gemini chat per system, style reference attached, cinematic poster moment (not a game screenshot), one large hero close to the viewer in the centre-right, left third mostly empty, bottom calm, no text/logos/UI/cabinets; full download size (1376x768 or larger); logos via make_logo.py; cabinets via cutout_flat.py (plain backgrounds only); arcade cabinets: same gentle three-quarter angle as the others (front mostly facing the viewer, turned slightly left, narrow side strip on the right), side art influenced by the chosen game for that system, system logo on the marquee (check all three every time); computers flat top-down overhead view like Iconic C64/Amiga
- [x] Hypermax frame fix applied to all 60 remaining Hypermax systems (background layer only) - mockups in TPN Iconic/mockups/hypermax_bg_only; replace any plain ones with custom art
- [ ] Generate replacement art (Gemini) for systems using borrowed or no art - see sections C and D
- [ ] Regional styling for Japanese / Chinese variants without their own art
- [ ] Description text for all new systems (currently blank)
- [ ] Find hardware images for systems still on the generic placeholder
- [ ] Logos for systems showing text only
- [ ] Check the 28 Hypermax system images are hardware, not logos (controllers_preview.jpg)
- [ ] Consider an Initial D 6/7/8 cabinet for RingEdge (current cut-out is Ver.3 / NAOMI 2)
- [ ] Install on the PC and test in RetroBat (dark and light schemes)
- [x] Update CREDITS-TPN.md for Gemini-generated art (ALLS, RingEdge) - keep adding as new art goes in
- [ ] Create private GitHub repo from ~/tpn-build/iconic-tpn
- [ ] Add an About this fork section to the README before the repo goes up: unofficial fork of Iconic (ES) by Delgan (based on Iconic ES-DE by Siddy212), not affiliated with or endorsed by the Iconic authors; all original Iconic artwork unchanged; added backgrounds for systems Iconic did not cover are AI-generated (Google Gemini); salvaged art credited in CREDITS-TPN.md
- [ ] Keep AI art out of any contributions back to the original Iconic project unless Delgan says he is happy with it
- [ ] Optional courtesy: before sharing publicly, send Delgan a short note on the Iconic GitHub (what it is, unofficial fork, new backgrounds are AI) so he can raise any concerns early
- [ ] Before sharing with TPN: confirm they are happy with AI backgrounds (they already use AI, so likely fine); keep AI labels in CREDITS-TPN.md; any AI background can be swapped for human-made art later (one file per system)
- [ ] Optional: offer to the TPN team (needs their OK for Hypermax art; keep ckau-book CC BY-NC-SA credit)

## 2. Arcade Classics

- [ ] Confirm where the arcade ROMs and RetroBat gamelists live (NAS or PC)
- [ ] Decide rating source for Unplayed Classics: own ratings or scraped ratings
- [ ] Agree folder layout: Manufacturer / Genre / Unplayed Classics (by genre) - check genre list and merges (e.g. shmup variants, light gun list)
- [ ] Generate grouping and review proposed folders and game counts
- [ ] Write es_systems_custom entry for the Arcade Classics system
- [ ] Build link-creation script (run as admin on the PC; Developer Mode; allow symlinks to NAS)
- [ ] Generate gamelist for the new system (metadata and media from existing arcade gamelist)
- [ ] Per-game emulator settings for PixN PC arcade boards, or hybrid collections fallback - test a few per board first
- [ ] Play-count check across both systems; scheduled overnight refresh
- [ ] Theme tile and background for Arcade Classics
- [ ] Test on the PC

## 3. No Mercy mods

- [ ] Install es_systems_nomercy.cfg in RetroBat/emulationstation/.emulationstation
- [ ] Create roms/n64nomercy (or point path at the NAS)
- [ ] Tell Claude which folder the existing mods are in (full NAS search timed out)
- [ ] Patch any .xdelta / .ips / .bps mods onto your own No Mercy ROM
- [ ] Test Mupen64Plus-Next vs Project64; switch to -system n64 if settings do not apply
- [ ] Theme art for No Mercy Mods (background, logo, system image)

## 4. Systems not in the original Iconic theme (180)

Every system in the PixN build that the original Iconic theme has no art for, with where its current art comes from.

### A. Custom art - done (56)

| Done | System | Name | Background | System image | Logo | To do |
|---|---|---|---|---|---|---|
| - [x] | abc80 | ABC 80 | Atlantis sunken city (Gemini) - installed | custom: ABC 80 keyboard unit photo cut-out | custom |  |
| - [x] | actionmax | Actionmax | Sonic Fury jet dogfight (Gemini) - installed (bg from a 1024px copy - swap for full-size if re-downloaded) | custom: ActionMax console and light gun (supplied cut-out) | custom |  |
| - [x] | aleck64 | Aleck 64 | Starfighter scene (Gemini) - installed | custom: Gemini-built Astro City-style cabinet with Aleck 64 marquee | custom |  |
| - [x] | alice32 | Alice 32 | Space pirate raid (Gemini) - installed | custom: Gemini top-down render of the Alice 32 from a reference photo | custom |  |
| - [x] | apogeebk01 | Apogee BK-01 | Bad Road Soviet car (Gemini) - installed | custom: Gemini top-down render from the Carbon theme Apogee BK-01 photo | custom |  |
| - [x] | aquarius | Aquarius Home Computer System | Treasure of Tarmin-style dungeon (Gemini) - installed | custom: Gemini top-down render from the Carbon theme Aquarius photo | custom |  |
| - [x] | beena | Advanced Pico BEENA | Storybook-style: original girl in a yellow raincoat jumping in a rainbow puddle splash (Gemini, original) - installed | Gemini render from a text description (accuracy unverified), cut out - installed | custom |  |
| - [x] | bk | Elektronika BK | Cosmonaut walking to a red-lit space station on an ice planet (Gemini, generic) - installed | custom: Elektronika BK-0010 keyboard photo (Carbon theme, transparent) cropped | custom |  |
| - [x] | cassettevision | Cassette Vision | Kikori no Yosaku-style woodcutter (Gemini) - installed | custom: Epoch Cassette Vision console photo cut-out (Carbon theme photo) | custom |  |
| - [x] | cbm2 | Commodore CBM-II | Astronaut watching a lunar lander touch down (Gemini, generic) - installed | custom: Commodore 710 (CBM-II) photo (Carbon theme) cut out, front view | custom |  |
| - [x] | cgenie | Colour Genie EG2000 | Astronaut vs one-eyed slime alien (Gemini) - installed | custom: Carbon theme photo (already flat top-down, transparent PNG), cropped - no Gemini render needed | custom |  |
| - [x] | elektronika | Elektronika IM | Farmhand girl catching a golden egg in a basket, Ну, погоди!-style egg catching (Gemini, original character) - installed | custom: Elektronika IM Nu, pogodi! handheld photo (Carbon theme, transparent) cropped and doubled | custom |  |
| - [x] | ep128 | Enterprise One Two Eight | Jetpack explorer vs crystalline space-whale (Gemini) - installed | custom: Gemini top-down render of the Enterprise 128 from the Carbon theme photo | custom |  |
| - [x] | exl100 | EXL 100 | Hover-bike rider vs giant mechanical scorpion (Gemini) - installed | custom: Carbon theme photo cut-out (console, keyboard and joysticks; already flat top-down) | custom |  |
| - [x] | gaelco | Gaelco PowerVR | Radikal Bikers-style: original pizza courier on an orange scooter racing a rainy neon street, pizzas flying (Gemini, original character) - installed; year set to 1996 (unsure) | PixN Carbon Gaelco A.V. TRACK cabinet image used as-is, cut-out (small, 248x283) - installed | custom |  |
| - [x] | galaxy | Galaksija | Diamond Mine miner (Gemini) - installed | custom: Gemini top-down render from the Carbon theme Galaksija photo | custom |  |
| - [x] | gamewave | Game Wave Family Entertainment System | Game-show-style: original robot host with a glowing question mark under spotlights (Gemini, original) - installed | Gemini render of the console on green, cut out - installed | custom |  |
| - [x] | hec2hr | Hector 2HR | Mining robot vs crystal cavern (Gemini) - installed | custom: Gemini top-down render of the Hector 2HR keyboard unit from the Carbon theme photo | custom |  |
| - [x] | hyperscan | HyperScan | Card-battler-style: original silver-haired duellist summoning a golden dragon from a glowing card (Gemini, original; no licensed card game) - installed | Gemini render from a Wikimedia photo reference, cut out - installed | custom |  |
| - [x] | ibmpcjr | IBM PC Jr | Knight arriving at fairy-tale castle, King's Quest-style (Gemini) - installed | custom: Carbon theme photo cut-out (transparent PNG, 3/4 view; Gemini top-down render failed twice) | custom |  |
| - [x] | igspgm | PolyGame Master (PGM) | Oriental Legend / Knights of Valour-style: original Three Kingdoms halberd general facing an armoured war boar in a misty gorge (Gemini, original characters) - installed | Gemini three-cabinet group (PGM-style blue centre cabinet + two muted game cabinets), green-screen cut-out - installed | custom |  |
| - [x] | jupace | Jupiter Ace | Starfighter vs alien hive over Jupiter (Gemini) - installed | custom: Gemini top-down render from a Jupiter Ace photo (Carbon theme) | custom |  |
| - [x] | m5 | Sord M5 | Ninja vs oni demon, moonlit pagoda (Gemini) - installed | custom: Gemini render of the Sord M5 from the ckau photo (slightly angled, matches the real wedge-shaped unit) | custom |  |
| - [x] | mbee | MicroBee | Bunyip Adventure bunyip billabong (Gemini) - installed | custom: Gemini top-down render of the MicroBee keyboard unit from the Carbon theme photo | custom |  |
| - [x] | microvsn | Microvision Milton Bradley | Space ranger vs cosmic wasp, Cosmic Hunter-style (Gemini, generic) - installed | custom: Microvision photo (Carbon theme) straightened and cut out | custom |  |
| - [x] | mpu1000 | MPU-1000 | Rocket patrol vs alien saucer, early TV-game style (Gemini, generic) - installed | custom: Acetronic MPU-1000 console and joystick photo (Carbon theme) cropped, 3/4 view | custom |  |
| - [x] | mtx512 | MTX 512 | Miner-astronaut vs spider walker in crystal cavern (Gemini) - installed | custom: Gemini top-down render of the MTX512 keyboard unit from the Carbon theme photo | custom |  |
| - [x] | myvision | My Vision KH-1000 | Master player at floating shogi/mahjong board (Gemini, generic) - installed | custom: My Vision TV, cartridge and console photo (Carbon theme) cropped | custom |  |
| - [x] | n501 | NUON Enhanced DVD Player / DVD-N501 | Tempest-style tube shooter: golden bat-wing starfighter firing down a neon vortex tunnel at a red crystal enemy (Gemini, original) - installed; name shortened to NUON DVD-N501, hardware type set to console | custom: PixN Carbon NUON console image (Samsung DVD player + controller) used as-is, cut-out | custom |  |
| - [x] | namco11 | System 11 | Tekken-style martial arts clash (Gemini) - installed | custom: Gemini three-image cabinet (System 32 angle ref + Namco System 11 marquee logo + Tekken-style side art from the background) | custom |  |
| - [x] | neogeo64 | Hyper Neo Geo 64 | Samurai-duel-style: original white-haired female ronin slashing at a blue oni on a stormy sea-cliff (Gemini, original) - installed | Gemini three-cabinet group (Hyper Neo Geo 64 red centre + Samurai Shodown 64 and Fatal Fury Wild Ambition side cabinets, real games), green-screen cut-out - installed | custom |  |
| - [x] | ondra | Ondra | Tenebra-style crypt puzzle: wanderer at a cracking rune door (Gemini, original character) - installed | custom: Gemini flat top-down render of the Ondra from a Wikimedia Commons photo (OndraComputer.jpg) | custom |  |
| - [x] | orao | Orao | Nevidljivi-style invisible presence in a foggy fortress courtyard (Gemini, original character) - installed | custom: Gemini flat top-down render of the Orao from a Wikimedia Commons photo (Orao-IMG 7278.jpg, CC licence) | custom |  |
| - [x] | p2000t | Philips P2000 | Retro rocket-plane vs mechanical kraken (Gemini) - installed | custom: Gemini flat plan-view render of the P2000T from the Carbon theme photo (3 follow-ups needed for top-down) | custom |  |
| - [x] | pecom64 | Pecom 64 | Cosmonaut vs rusted robot guardian (Gemini) - installed | custom: Gemini top-down render from the Carbon theme Pecom 64 photo (keys redone black on 2nd pass) | custom |  |
| - [x] | pegasus | Aamber Pegasus | Mountain warden vs stone golem (Gemini, generic) - installed | custom: Aamber Pegasus photo (Carbon theme, already flat top-down) cropped | custom |  |
| - [x] | pippin | Pippin @mark | Storybook steam tank engine tribute: original teal-green and copper engine on a stone viaduct at golden hour, no face or lettering (Gemini, original) - installed; year corrected 1986 to 1996 | custom: Gemini green-screen render of the Apple Bandai Pippin Atmark console and controller from a Wikimedia Commons photo (Pippin-Atmark-Console-Set.png), cut out | custom |  |
| - [x] | pocketstation | Sony PocketStation | Rain-coat adventurer riding a glowing manta ray over floating islands (Gemini, generic) - installed | custom: Sony PocketStation photo (Carbon theme, transparent) cropped | custom |  |
| - [x] | pv2000 | PV-2000 | Astronaut kid vs chrome robot crab on the moon (Gemini, generic) - installed | custom: Gemini top-down render of the Casio PV-2000 from the Carbon theme photo | custom |  |
| - [x] | rawthrills | RAW Thrills | The Fast and the Furious-style: original unbadged yellow-and-black-striped sports coupe jumping a ramp through a fireball (Gemini, original) - installed; year set to 2004 | Gemini three-cabinet group (RAW Thrills red standard centre cabinet + FAST LANE and ALIEN SIEGE side cabinets, original games), cut out; logo on a black plate - installed | custom |  |
| - [x] | segaalls | Sega ALLS | House of the Dead (Gemini) - installed | SWDC cabinet cut-out - installed | custom |  |
| - [x] | segaer | Sega Europa-R | Sega Rally-style scene (Gemini) - installed | - | custom |  |
| - [x] | seganu | Sega Nu | Hatsune Miku-style concert (Gemini) - installed | custom: Luigi's Mansion Arcade cabinet (supplied cut-out) | custom |  |
| - [x] | segare | Sega RingEdge | Initial D (Gemini) - installed | Initial D Ver.3 cabinet cut-out - installed (Ver.3 is NAOMI 2 era) | custom |  |
| - [x] | segarw | Sega RingWide | Daytona-style oval (Gemini) - installed | - | custom |  |
| - [x] | segasystem32 | System 32 | Golden Axe-style barbarian (Gemini) - installed | custom: Gemini-generated early-90s Sega upright cabinet (green screen) | custom |  |
| - [x] | sorcerer | Sorcerer | Sorcerer vs dragon cavern (Gemini) - installed | custom: Gemini top-down render from the Carbon theme Sorcerer photo | custom |  |
| - [x] | studio2 | Studio II | Bowling-style strike, giant marble ball vs ten pins (Gemini; built-in Studio II game) - installed | custom: RCA Studio II console photo (Carbon theme, transparent) cropped, 3/4 view | custom |  |
| - [x] | sv8000 | Super Vision 8000 | Retro pilot vs saucer mothership over a night city (Gemini, generic) - installed | custom: Bandai Super Vision 8000 photo (Carbon theme) cut out | custom |  |
| - [x] | tvc64 | TVC 64 | Hungarian warrior on winged horse vs three-headed dragon (Gemini) - installed | custom: Gemini top-down render of the Videoton TVC from a public-domain Wikimedia photo | custom |  |
| - [x] | tvgames | TV Games | Sports-style: original astronaut swinging a neon bat at a flaming comet on a neon grid (Gemini, original) - installed | Generic Gemini joystick (original photo showed licensed characters), cut out - installed | custom |  |
| - [x] | unis | UNIS Arcade Machines | Sky Kart-style: original teal-ponytail girl in a yellow helmet driving a pink go-kart off a rainbow trail among balloons and confetti (Gemini, original character) - installed | Gemini three-cabinet group (UNIS blue centre cabinet + Sky Kart and Ticket Rush game cabinets, original games), green-screen cut-out - installed | custom |  |
| - [x] | vemulator | Sega Visual Memory Unit | Round robot companion leaping over a neon ocean (Gemini, generic) - installed | custom: Dreamcast VMU photo (Carbon theme, transparent) cropped and doubled | custom |  |
| - [x] | vg5k | VG-5000 | Deep-sea diver vs luminous jellyfish, sunken palace (Gemini) - installed | custom: Gemini top-down render of the Philips VG-5000 from the Carbon theme photo | custom |  |
| - [x] | vidbrain | Videobrain Family Computer | American football quarterback under floodlights, VideoBrain Football-style (Gemini, generic) - installed | custom: VideoBrain console photo (Carbon theme) cut out, 2x upscaled, edge halo removed | custom |  |
| - [x] | zinc | Zinc | Rival Schools-style: original schoolboy in a red scarf flying-kicking against a setting sun with cherry petals (Gemini, original character) - installed; metadata renamed Sony ZN (ZiNc), 1995 | Gemini three-cabinet group (Sony ZN-style centre cabinet + two muted game cabinets), green-screen cut-out - installed | custom |  |

### B. Hypermax background (frame removed) - looks OK (3)

| Done | System | Name | Background | System image | Logo | To do |
|---|---|---|---|---|---|---|
| - [ ] | captpower | Captain Power and the Soldiers of the Future | Hypermax background (frame removed) | - | ckau-book | description text |
| - [ ] | karaoke | Karaoke | Hypermax background (frame removed) | - | ckau-book | description text |
| - [ ] | namco3xx | Namco 357/369 | Hypermax background (frame removed) | - | text only | needs logo; description text |

### B1. REMAKE - custom art needed (17)

| Done | System | Name | Background | System image | Logo | To do |
|---|---|---|---|---|---|---|
| - [ ] | appleios | iOS | Hypermax background (frame removed) | - | ckau-book | REMAKE: generic placeholder shared with other systems - new custom art; description text |
| - [ ] | avgn | The Angry Video Game Nerd | Hypermax background (frame removed) | - | ckau-book | REMAKE: Hypermax picture only fills half the screen (do not upscale) - new custom art; description text |
| - [ ] | exboard | eX-Board | Hypermax background (frame removed) | - | text only | REMAKE: generic placeholder shared with other systems - new custom art; needs logo; description text |
| - [ ] | fightcade | Fightcade 2 | Hypermax background (frame removed) | - | text only | REMAKE: Hypermax picture only fills half the screen (do not upscale) - new custom art; needs logo; description text |
| - [ ] | hikaru | Hikaru | Hypermax background (frame removed) | - | ckau-book | REMAKE: Hypermax picture only fills half the screen (do not upscale) - new custom art; description text |
| - [ ] | igtslots | IGT slots (fruit machines) | Hypermax background (frame removed) | - | text only | REMAKE: Hypermax picture only fills half the screen (do not upscale) - new custom art; needs logo; description text |
| - [ ] | konamipc | Konami PC Based | Hypermax background (frame removed) | - | text only | REMAKE: generic placeholder shared with other systems - new custom art; needs logo; description text |
| - [ ] | mononcol | Monon Color | Hypermax background (frame removed) | - | ckau-book | REMAKE: generic placeholder shared with other systems - new custom art; description text |
| - [ ] | namcoes3 | Namco System ES3 | Hypermax background (frame removed) | - | text only | REMAKE: Hypermax picture only fills half the screen (do not upscale) - new custom art; needs logo; description text |
| - [ ] | nesicax | NESiCAxLive | Hypermax background (frame removed) | - | text only | REMAKE: Hypermax picture only fills half the screen (do not upscale) - new custom art; REMAKE: generic placeholder shared with other systems - new custom art; needs logo; description text |
| - [ ] | nesicax2 | NESiCAxLive 2 | Hypermax background (frame removed) | - | text only | REMAKE: Hypermax picture only fills half the screen (do not upscale) - new custom art; REMAKE: generic placeholder shared with other systems - new custom art; needs logo; description text |
| - [ ] | radio | Radio | Hypermax background (frame removed) | - | ckau-book | REMAKE: Hypermax picture only fills half the screen (do not upscale) - new custom art; description text |
| - [ ] | rx78 | Gundam RX-78 | Hypermax background (frame removed) | - | ckau-book | REMAKE: Hypermax picture only fills half the screen (do not upscale) - new custom art; REMAKE: generic placeholder shared with other systems - new custom art; description text |
| - [ ] | screenshots | Screenshots | Hypermax background (frame removed) | - | ckau-book | REMAKE: Hypermax picture only fills half the screen (do not upscale) - new custom art; description text |
| - [ ] | snotec | Super Note Club | Hypermax background (frame removed) | - | ckau-book | REMAKE: generic placeholder shared with other systems - new custom art; description text |
| - [ ] | sys80 | System-80 | Hypermax background (frame removed) | - | ckau-book | REMAKE: generic placeholder shared with other systems - new custom art; description text |
| - [ ] | videodriver | Video Driver | Hypermax background (frame removed) | - | ckau-book | REMAKE: Hypermax picture only fills half the screen (do not upscale) - new custom art; description text |

### C. Borrowed art - needs its own background (36)

| Done | System | Name | Background | System image | Logo | To do |
|---|---|---|---|---|---|---|
| - [ ] | 2ship | 2 Ship 2 Harkinian | borrowed: Iconic ports | - | text only | needs its own art; needs logo; description text |
| - [ ] | amazon | Amazon Prime Gaming | borrowed: Iconic windows | - | text only | needs its own art; needs logo; description text |
| - [ ] | bk001001 | BK 0010-01 | borrowed: Elektronika BK art | - | ckau-book | needs its own art; description text |
| - [ ] | bsyndrome | Bermuda Syndrome | borrowed: Iconic ports | - | text only | needs its own art; needs logo; description text |
| - [ ] | c16 | Commodore 16 | borrowed: Iconic cplus4 | - | text only | needs its own art; needs logo; description text |
| - [ ] | clonehero | Clone Hero | borrowed: Iconic ports | - | text only | needs its own art; needs logo; description text |
| - [ ] | dinothawr | Dinothawr | borrowed: Iconic ports | - | text only | needs its own art; needs logo; description text |
| - [ ] | dusklight | DuskLight | borrowed: Iconic ports | - | text only | needs its own art; needs logo; description text |
| - [ ] | eagames | EA Games | borrowed: Iconic windows | - | text only | needs its own art; needs logo; description text |
| - [ ] | gemrb | GemRB - Infinity Engine Open-Source Implementation | borrowed: Iconic ports | - | text only | needs its own art; needs logo; description text |
| - [ ] | halflife | Half-Life | borrowed: Iconic xash3d-fwgs | - | text only | needs its own art; needs logo; description text |
| - [ ] | konamilcd | Konami | borrowed: Iconic lcdgames | - | text only | needs its own art; needs logo; description text |
| - [ ] | laseractive | Pioneer Laserdisc | borrowed: Iconic laserdisc | - | text only | needs its own art; needs logo; description text |
| - [ ] | locomalito | Locomalito | borrowed: Iconic ports | - | text only | needs its own art; needs logo; description text |
| - [ ] | love | LÖVE | borrowed: Iconic ports | - | text only | needs its own art; needs logo; description text |
| - [ ] | max | Commodore Max Machine | borrowed: Iconic c64 | - | text only | needs its own art; needs logo; description text |
| - [ ] | msxlaserdisk | MSX Palcom LaserDisc | borrowed: Iconic laserdisc | - | text only | needs its own art; needs logo; description text |
| - [ ] | opengoal | OpenGOAL | borrowed: Iconic ports | - | text only | needs its own art; needs logo; description text |
| - [ ] | openlara | OpenLara | borrowed: Iconic ports | - | text only | needs its own art; needs logo; description text |
| - [ ] | pcvr | PC VR | borrowed: Iconic windows | - | text only | needs its own art; needs logo; description text |
| - [ ] | pdark | Perfect Dark | borrowed: Iconic ports | - | text only | needs its own art; needs logo; description text |
| - [ ] | pinballfx | Pinball FX | borrowed: Iconic fpinball | - | text only | needs its own art; needs logo; description text |
| - [ ] | pinballfx2 | Pinball FX2 | borrowed: Iconic fpinball | - | text only | needs its own art; needs logo; description text |
| - [ ] | pinballfx3 | Pinball FX3 | borrowed: Iconic fpinball | - | text only | needs its own art; needs logo; description text |
| - [ ] | pinballm | Pinball M | borrowed: Iconic fpinball | - | text only | needs its own art; needs logo; description text |
| - [ ] | pocketchallengev2 | Pocket Challenge V2 | borrowed: Iconic wonderswan | - | text only | needs its own art; needs logo; description text |
| - [ ] | powerbomberman | Power Bomberman | borrowed: Iconic ports | - | text only | needs its own art; needs logo; description text |
| - [ ] | redriver2 | ReDriver2 | borrowed: Iconic ports | - | text only | needs its own art; needs logo; description text |
| - [ ] | soh | Ship of Harkinian | borrowed: Iconic ports | - | text only | needs its own art; needs logo; description text |
| - [ ] | starship | Starship | borrowed: Iconic ports | - | text only | needs its own art; needs logo; description text |
| - [ ] | tiger | Tiger | borrowed: Iconic lcdgames | - | text only | needs its own art; needs logo; description text |
| - [ ] | winbigfish | Big Fish Games | borrowed: Iconic windows | - | text only | needs its own art; needs logo; description text |
| - [ ] | wingamehouse | GameHouse | borrowed: Iconic windows | - | text only | needs its own art; needs logo; description text |
| - [ ] | wingog | Good Old Games | borrowed: Iconic windows | - | text only | needs its own art; needs logo; description text |
| - [ ] | winpopcap | PopCap Games | borrowed: Iconic windows | - | text only | needs its own art; needs logo; description text |
| - [ ] | zaccariapinball | Zaccaria Pinball | borrowed: Iconic vpinball | - | text only | needs its own art; needs logo; description text |

### E. ckau-book art - review (10)

| Done | System | Name | Background | System image | Logo | To do |
|---|---|---|---|---|---|---|
| - [ ] | bml3 | MB-6890 Basic Master level 3 | ckau-book art on Iconic default | generic placeholder | ckau-book | review / consider custom art; needs system image; description text |
| - [ ] | digiblst | digiBLAST | ckau-book art on Iconic default | generic placeholder | ckau-book | review / consider custom art; needs system image; description text |
| - [ ] | gameking3 | GameKing 3 | ckau-book art on Iconic default | generic placeholder | ckau-book | review / consider custom art; needs system image; description text |
| - [ ] | m21 | M21 | ckau-book art on Iconic default | generic placeholder | ckau-book | review / consider custom art; needs system image; description text |
| - [ ] | namco12 | System 12 | ckau-art on arcade | generic placeholder | text only | review / consider custom art; needs system image; needs logo; description text |
| - [ ] | segaai | Sega AI Computer | ckau-book art on Iconic default | generic placeholder | ckau-book | review / consider custom art; needs system image; description text |
| - [ ] | smc777 | SMC-777 | ckau-book background | generic placeholder | ckau-book | review / consider custom art; needs system image; description text |
| - [ ] | vgm | Video Game Movies | ckau-book art on Iconic default | generic placeholder | ckau-book | review / consider custom art; needs system image; description text |
| - [ ] | vii | Vii | ckau-book art on Iconic default | generic placeholder | ckau-book | review / consider custom art; needs system image; description text |
| - [ ] | wahlap | Wahlap Arcade Machines | ckau-art on arcade | - | text only | review / consider custom art; needs logo; description text |

### F. Covered by Iconic art (same system family) (58)

| Done | System | Name | Background | System image | Logo | To do |
|---|---|---|---|---|---|---|
| - [ ] | 3dsen | 3DSen | Iconic nes art (same family) | - | ckau-book | description text |
| - [ ] | amiga3000 | Amiga 3000 | Iconic amiga art (same family) | - | ckau-book | description text |
| - [ ] | amiga4000 | Amiga 4000 | Iconic amiga art (same family) | - | ckau-book | description text |
| - [ ] | c64gs | Commodore 64 Game System | Iconic c64 art (same family) | - | ckau-book | description text |
| - [ ] | cave | CAVE | Iconic cave3rd art (same family) | - | ckau-book | description text |
| - [ ] | cpc464p | Amstrad CPC 464+ | Iconic amstradcpc art (same family) | - | ckau-book | description text |
| - [ ] | datach | Datach Joint ROM System | Iconic famicom art (same family) | - | ckau-book | description text |
| - [ ] | dendy | Dendy Classic | Iconic famicom art (same family) | - | ckau-book | description text |
| - [ ] | dreamcast-jp | Dreamcast (Japan) | Iconic dreamcast art (same family) | - | ckau-book | regional (JP/CN) styling; description text |
| - [ ] | exodos | eXoDOS | Iconic dos art (same family) | - | ckau-book | description text |
| - [ ] | exowin3x | eXoWin3x | Iconic windows3x art (same family) | - | ckau-book | description text |
| - [ ] | exowin9x | eXoWin9x | Iconic windows9x art (same family) | - | ckau-book | description text |
| - [ ] | gba2players | Game Boy Advance 2 Players | Iconic gba art (same family) | - | ckau-book | description text |
| - [ ] | gc-jp | GameCube (Japan) | Iconic gc art (same family) | - | ckau-book | regional (JP/CN) styling; description text |
| - [ ] | gch | GameCube Hacks | Iconic gc art (same family) | - | ckau-book | description text |
| - [ ] | ggh | Game Gear Hacks | Iconic gamegear art (same family) | - | ckau-book | description text |
| - [ ] | hbmame | MAME Homebrew | Iconic mame art (same family) | - | ckau-book | description text |
| - [ ] | iqueplayer | iQue Player | Iconic n64 art (same family) | - | ckau-book | regional (JP/CN) styling; description text |
| - [ ] | loopy | Casio Loopy | Iconic casloopy art (same family) | - | ckau-book | description text |
| - [ ] | mame-aknf | MAME All Killer No Filler | Iconic mame art (same family) | - | ckau-book | description text |
| - [ ] | mark3 | Mark III - Master System | Iconic mastersystem art (same family) | - | ckau-book | regional (JP/CN) styling; description text |
| - [ ] | megacd32x | Mega-CD 32x | Iconic sega32x art (same family) | - | ckau-book | description text |
| - [ ] | megadrive-jp | Megadrive (Japan) | Iconic megadrivejp art (same family) | - | ckau-book | description text |
| - [ ] | megadrive-msu | MD-MSU | Iconic msu-md art (same family) | - | ckau-book | description text |
| - [ ] | n64-jp | Nintendo 64 (Japan) | Iconic n64 art (same family) | - | ckau-book | regional (JP/CN) styling; description text |
| - [ ] | n64h | Nintendo 64 Hacks | Iconic n64 art (same family) | - | ckau-book | description text |
| - [ ] | n64recomp | Nintendo 64 Recompilation | Iconic n64 art (same family) | - | ckau-book | description text |
| - [ ] | neogeomvs | Neo Geo MVS | Iconic neogeo art (same family) | - | ckau-book | description text |
| - [ ] | nes-msu | Nintendo Entertainment System (MSU1) | Iconic nes art (same family) | - | ckau-book | description text |
| - [ ] | nes_aladdin | NES Aladdin Deck Enhancer | Iconic nes art (same family) | - | ckau-book | description text |
| - [ ] | nes_hd | Nintendo Entertainment System - Famicom HD | Iconic nes art (same family) | - | ckau-book | description text |
| - [ ] | nomad | SEGA Nomad | Iconic genesis art (same family) | - | ckau-book | description text |
| - [ ] | ps2-jp | Playstation 2 (Japan) | Iconic ps2 art (same family) | - | ckau-book | regional (JP/CN) styling; description text |
| - [ ] | ps2h | Playstation 2 Hacks | Iconic ps2 art (same family) | - | ckau-book | description text |
| - [ ] | ps3h | Playstation 3 Hacks | Iconic ps3 art (same family) | - | ckau-book | description text |
| - [ ] | pspminis | PlayStation Portable Minis | Iconic psp art (same family) | - | ckau-book | description text |
| - [ ] | psx-jp | PlayStation (Japan) | Iconic psx art (same family) | - | ckau-book | regional (JP/CN) styling; description text |
| - [ ] | psxh | PlayStation Hacks | Iconic psx art (same family) | - | ckau-book | description text |
| - [ ] | rtcw | RealRTCW | Iconic iortcw art (same family) | - | ckau-book | description text |
| - [ ] | saturn-jp | Saturn (Japan) | Iconic saturnjp art (same family) | - | ckau-book | description text |
| - [ ] | sc-3000 | Sega SC-3000 | Iconic sg-1000 art (same family) | - | ckau-book | description text |
| - [ ] | segacd32x | 32x CD | Iconic sega32x art (same family) | - | ckau-book | description text |
| - [ ] | segachannel | Megadrive - Sega Channel | Iconic megadrive art (same family) | - | ckau-book | description text |
| - [ ] | segastv | ST-V | Iconic stv art (same family) | - | ckau-book | description text |
| - [ ] | snescd | Nintendo Super Nintendo CD | Iconic snes art (same family) | - | ckau-book | description text |
| - [ ] | supercharger | Starpath Supercharger | Iconic atari2600 art (same family) | - | ckau-book | description text |
| - [ ] | tduo | TurboDuo | Iconic tg-cd art (same family) | - | ckau-book | description text |
| - [ ] | typex | Taito Type X | Iconic type-x art (same family) | - | ckau-book | description text |
| - [ ] | typex2 | Taito Type X2 | Iconic type-x art (same family) | - | ckau-book | description text |
| - [ ] | wiih | Wii Hacks | Iconic wii art (same family) | - | ckau-book | description text |
| - [ ] | wiiu-sky | Wii U - Skylanders | Iconic wiiu art (same family) | - | ckau-book | description text |
| - [ ] | wiiueshop | Nintendo Wii U eShop | Iconic wiiu art (same family) | - | ckau-book | description text |
| - [ ] | wiiware | Nintendo WiiWare | Iconic wii art (same family) | - | ckau-book | description text |
| - [ ] | win311 | Windows 3.11 | Iconic windows3x art (same family) | - | ckau-book | description text |
| - [ ] | win95 | Windows 95 | Iconic windows9x art (same family) | - | ckau-book | description text |
| - [ ] | win98 | Windows 98 | Iconic windows9x art (same family) | - | ckau-book | description text |
| - [ ] | xash3d_fwgs | Xash3D-FWGS | Iconic xash3d-fwgs art (same family) | - | ckau-book | description text |
| - [ ] | xbla | Xbox Live Arcade | Iconic xbox360 art (same family) | - | ckau-book | description text |


## 5. Gemini prompts (from PROMPTS.md)


Work down the list. For each system you need three things: a background, a system image and a logo.

### How to use

1. In Gemini, attach one style reference from the Iconic-style-refs folder on the Mac desktop (SNES is the best all-rounder).
2. Paste the STANDARD BLOCK below, replacing [SCENE] with ONLY the system's Scene line. Never paste the Note lines - they are for you (which game it is based on, which photo to look for).
3. Download with Gemini's own download button (full size, 1376x768). Never screenshots. Start a NEW Gemini chat for every system.
4. Save into Downloads/Iconic Images, ideally renamed with the system code: e.g. alice32_bg.jpg, alice32_cab.png, alice32_logo.png. Then tell Claude which systems are ready.

### STANDARD BLOCK (paste every time)

> Using the attached image as a style reference, create a background in the same bold, painted illustration style: a dramatic cinematic poster moment, not a game screenshot. One large hero close to the viewer and one clear focus of action, not lots of small things. Scene: [SCENE]. Requirements: 16:9, 1920x1080; the hero large in the centre-right; the left third darker and mostly empty (sky, haze or shadow); the bottom edge calm, dark and uncluttered; no text, no numbers, no score, no titles, no logos, no borders, no arcade cabinet, no screen frame, no joysticks or buttons, no UI of any kind.

If Gemini adds text or signs anyway, reply: remove all text, signs and lettering.

Tips that work: always start a NEW Gemini chat per system (follow-ups edit the previous image, so old mistakes carry over). Ask for a cinematic poster moment, not a game screenshot. One large hero close to the viewer and one clear target beats lots of small things. Say the left third should be mostly empty.

### System images and logos

- System image: a photo on a PLAIN background (white or flat grey), matching Iconic's own conventions:
  - Arcade boards: the cabinet in three-quarter view, facing LEFT (front turned towards the left of the picture).
  - Computers: seen from DIRECTLY OVERHEAD - a flat, top-down view of the keyboard, squared up, no perspective (like Iconic's C64, Amiga, ZX Spectrum).
  - For a computer with no good top-down photo, have Gemini make one from a reference photo: a clean product photograph of this [computer], seen from directly overhead: a flat, top-down view looking straight down at the keyboard, squared up, no perspective, on a plain solid bright green background (#00FF00), computer only. No shadow of any kind, no reflection and no glow around it - perfectly flat, even green right up to hard, clean edges. Sega Retro, Wikipedia and manufacturer product shots are ideal. Busy or dark backgrounds will not cut out cleanly.
- Logo: a transparent PNG if possible. Platform badge packs (like the RingEdge/RingWide ones) are fine; Claude extracts the logo from the badge.


CABINET RULES (all arcade boards - check every one before accepting it):
- Rotation: the same gentle three-quarter angle as the existing cabinets (Sega System 32, Sega ALLS, Aleck 64): the FRONT of the cabinet mostly faces the viewer, turned slightly to the left, with only a narrow strip of the side panel showing on the right. Not side-on, not rotated further than the others. Attach an existing cabinet cut-out as the angle reference.
- Side art: the side panel must show artwork influenced by the game chosen for that system's background (e.g. Tekken-style fighters for Namco System 11) - an original illustration in that game's spirit, not a copy of the box art.
- Marquee: the system's logo on the lit marquee at the top (attach the logo image).
- Green background, no shadow, whole cabinet in frame, as below.

### CABINET FALLBACK (when no good real cabinet photo exists)

Some boards shipped in generic cabinets (Aleck 64, many Japanese boards), so there is no distinctive cabinet to photograph. Build one in Gemini from parts. Start a NEW chat, attach NO style reference, and upload three images:

1. a generic arcade cabinet photo for the shape (a Japanese sit-down candy cabinet such as a Sega Astro City suits most Japanese boards; an upright or racing cabinet where that fits better),
2. the system's logo (for the marquee),
3. a screenshot of the system's signature game (for the screen - ideally the same game the background is based on).

> Using the three attached images, create a product photograph of an arcade cabinet: use the shape of the cabinet in image 1, repaint it in [COLOUR SCHEME], put the logo from image 2 on the lit marquee at the top, and show the game from image 3 on the screen. Three-quarter view facing left (the front of the cabinet turned towards the left of the picture), standing on a plain, solid bright green background (#00FF00) with even studio lighting. Clean, realistic, sharp detail. No other text or brand names, no people. No shadow of any kind (no floor shadow, no drop shadow), no reflection and no glow around it - the background must be perfectly flat, even green right up to hard, clean edges.

If Gemini adds a shadow anyway, reply: remove the shadow completely; flat, even green background with no shadow, reflection or glow, and hard clean edges; change nothing else. The solid green background is what lets it cut out cleanly - white would blend into any white trim on the cabinet. Ask for it facing left from the start, so it never needs mirroring. The logo on the marquee is the one place a logo belongs. Save it as <code>_cab.png (or .jpg).

### OBSCURE COMPUTERS AND CONSOLES

Iconic always uses GAME art, never the machine itself - even for obscure computers (Dragon 32, CoCo, SAM Coupe, PET all show game scenes). The machine appears only in the system image slot. So every system's background must be based on an actual game released for it. Where no game is listed yet, ask Claude to research the system's best-known game first and write the Scene line from it. Avoid clones of famous games (e.g. a Pac-Man clone) - pick a game original to that machine or its home scene, so it cannot be mistaken for another company's game. Also avoid scenes that read as a famous franchise even if the game is original (e.g. an explorer with a hat grabbing a golden idol reads as Indiana Jones) - change the hero or setting, or choose another game.

---

### Arcade boards

- **aleck64** - Aleck 64
  - Scene (paste this): a single sleek white-and-blue starfighter, large and close to the viewer, banking hard as it fires a bright laser at a giant insect-like alien warship looming above a ruined, burning planet; a few smaller alien ships in the distance; glowing explosions and a huge cracked moon in the sky.
  - Note, based on: Star Soldier: Vanishing Earth (do not paste)
  - Note, photo to find: no distinctive cabinet exists - use the CABINET FALLBACK: Japanese sit-down candy cabinet, bright blue with white trim (the Aleck 64 cartridge colours), Aleck 64 logo on the marquee, Star Soldier: Vanishing Earth screenshot on the screen. Current theme image is the PCB. (do not paste)
- **exboard** - eX-Board
  - Scene (paste this): two anime fighting-game heroines clashing in mid-air with magical energy
  - Note, based on: Arcana Heart (do not paste)
  - Note, photo to find: eX-Board / Examu cabinet (do not paste)
- **fightcade** - Fightcade 2
  - Scene (paste this): two classic arcade street fighters squaring up under neon lights, crowd of retro arcade cabinets behind
  - Note, photo to find: a classic fighting-game candy cabinet (do not paste)
- **gaelco** - Gaelco PowerVR
  - Scene (paste this): a pizza-delivery scooter racer weaving through city traffic, pizzas flying
  - Note, based on: Radikal Bikers (do not paste)
  - Note, photo to find: Radikal Bikers cabinet (do not paste)
- **hikaru** - Sega Hikaru
  - Scene (paste this): a jet-pack hero flying over an alien world firing at giant creatures
  - Note, based on: Planet Harriers (do not paste)
  - Note, photo to find: Planet Harriers or Brave Fire Fighters cabinet (do not paste)
- **igspgm** - PolyGame Master
  - Scene (paste this): Three Kingdoms warriors with halberds and swords battling an army
  - Note, based on: Knights of Valour (do not paste)
  - Note, photo to find: PGM cabinet (do not paste)
- **igtslots** - IGT slots
  - Scene (paste this): glowing fruit machines, spinning reels of cherries, bells and lucky sevens, coins cascading
  - Note, photo to find: an IGT slot machine (do not paste)
- **konamipc** - Konami PC Based
  - Scene (paste this): a vampire hunter with a whip facing Dracula's castle under a blood moon
  - Note, based on: e.g. Castlevania: The Arcade (do not paste)
  - Note, photo to find: Castlevania: The Arcade cabinet (do not paste)
- **namco11** - Namco System 11
  - Scene (paste this): two martial artists mid-kick in a dramatic 3D fighting-game arena
  - Note, based on: Tekken / Tekken 2 (do not paste)
  - Note, photo to find: Tekken 2 cabinet (do not paste)
- **namco12** - Namco System 12
  - Scene (paste this): two weapon fighters clashing blades, sparks flying, in an ancient temple
  - Note, based on: Soulcalibur (do not paste)
  - Note, photo to find: Soulcalibur cabinet (do not paste)
- **namcoes3** - Namco System ES3
  - Scene (paste this): a pilot in an enclosed cockpit pod racing through a space battle trench (e.g. Star Wars: Battle Pod) or a Tekken 7-style fight
  - Note, photo to find: Battle Pod or Tekken 7 cabinet (do not paste)
- **neogeo64** - Hyper Neo Geo 64
  - Scene (paste this): two samurai duelling in falling cherry blossoms at dusk
  - Note, based on: Samurai Shodown 64 (do not paste)
  - Note, photo to find: Hyper Neo Geo 64 cabinet (do not paste)
- **nesicax** - NESiCAxLive
  - Scene (paste this): two anime fighting-game characters clashing with huge energy attacks
  - Note, based on: e.g. BlazBlue / King of Fighters (do not paste)
  - Note, photo to find: Taito Vewlix cabinet (do not paste)
- **nesicax2** - NESiCAxLive 2
  - Scene (paste this): a street fighter charging a fireball in a neon city at night
  - Note, based on: e.g. Street Fighter V Type Arcade (do not paste)
  - Note, photo to find: Taito Vewlix cabinet. (Make it different from nesicax.) (do not paste)
- **rawthrills** - RAW Thrills
  - Scene (paste this): a flying car launching off a ramp through an explosion, arcade-racing chaos
  - Note, based on: e.g. Cruis'n Blast (do not paste)
  - Note, photo to find: Cruis'n Blast or Big Buck Hunter cabinet (do not paste)
- **segasystem32** - Sega System 32
  - Scene (paste this): a barbarian warrior with a huge axe fighting skeleton soldiers
  - Note, based on: Golden Axe: The Revenge of Death Adder (do not paste)
  - Note, photo to find: System 32 cabinet (do not paste)
- **unis** - UNIS arcade
  - Scene (paste this): bright amusement-arcade family games, light-up buttons and prize tickets
  - Note, photo to find: a UNIS cabinet (do not paste)
- **wahlap** - Wahlap arcade
  - Scene (paste this): a busy modern Chinese arcade with racing and dance machines glowing
  - Note, photo to find: a Wahlap cabinet (do not paste)
- **zinc** - Sony ZN (Zinc)
  - Scene (paste this): high-school brawlers fighting in a schoolyard at sunset
  - Note, based on: Rival Schools (do not paste)
  - Note, photo to find: Rival Schools cabinet (do not paste)
- **actionmax** - ActionMax
  - Scene (paste this): a VHS light-gun game, 1980s jet fighter dogfight seen through a crosshair
  - Note, based on: Sonic Fury (do not paste)
  - Note, photo to find: ActionMax console with light gun (do not paste)

### Pinball

- **pinballfx / pinballfx2 / pinballfx3** - three different digital pinball scenes
  - Scene (paste this): a steel ball racing up a glowing ramp, flippers, bumpers and lights
  - Note, based on: vary colour and theme for each (do not paste)
- **pinballm** - Pinball M
  - Scene (paste this): a horror-themed pinball table in the dark, skulls and ghouls lit in red and green
- **zaccariapinball** - Zaccaria Pinball
  - Scene (paste this): a classic 1980s Italian pinball table with painted backglass, warm arcade lighting

### Consoles and handhelds

- **beena** - Advanced Pico BEENA
  - Scene (paste this): a colourful storybook world bursting out of the pages, cheerful kids' learning adventure
- **cassettevision** - Cassette Vision
  - Scene (paste this): a woodcutter chopping trees in a bright Japanese forest (Kikori no Yosaku), retro toy style
- **gamewave** - Game Wave
  - Scene (paste this): a family game-show night, trivia and party games on a big screen, excited family on the sofa
- **hyperscan** - HyperScan
  - Scene (paste this): comic-book superheroes battling, trading cards glowing as they are scanned
- **microvsn** - Microvision
  - Scene (paste this): a block-breaker ball smashing a wall of bricks, early handheld LCD style
  - Note, based on: Block Buster (do not paste)
- **mononcol** - Monon Color
  - Scene (paste this): a small modern Chinese handheld with a colourful fantasy RPG adventure
- **mpu1000** - MPU-1000
  - Scene (paste this): a late-1970s TV game console, simple space-shooter action on a glowing TV
- **myvision** - My Vision
  - Scene (paste this): Japanese board games come to life, mahjong tiles and shogi pieces on a glowing board
- **pocketchallengev2** - Pocket Challenge V2
  - Scene (paste this): a cheerful kids' learning handheld adventure with friendly characters
- **pocketstation** - PocketStation
  - Scene (paste this): a cute virtual pet playing mini-games on a tiny monochrome screen
- **snotec** - Super Note Club
  - Scene (paste this): a kids' learning laptop with bright educational games popping out
- **sv8000** - Super Vision 8000
  - Scene (paste this): a 1979 Japanese TV game console with colourful early shooting games
  - Note, based on: template-style (do not paste)
- **vemulator** - Sega VMU
  - Scene (paste this): a tiny cute creature raised on a glowing monochrome memory-card screen
- **vii** - Vii
  - Scene (paste this): a family playing motion-control sports games in the living room
- **gameking3** - GameKing 3
  - Scene (paste this): a small Chinese handheld with a colourful platform adventure
- **digiblst** - digiBLAST
  - Scene (paste this): a kids' handheld with cartoon adventure games bursting out of the screen
- **n501** - NUON
  - Scene (paste this): a psychedelic neon vector tunnel shooter, ship spinning around the rim
  - Note, based on: Tempest 3000 (do not paste)
- **studio2** - RCA Studio II
  - Scene (paste this): a 1977 TV game console with simple blocky games on a vintage TV, 70s living room
- **pippin** - Pippin
  - Scene (paste this): a mid-90s multimedia CD console, a colourful interactive CD-ROM adventure world (no brand logos)
- **elektronika** - Elektronika IM
  - Scene (paste this): a cartoon wolf catching falling eggs in a basket, Soviet LCD handheld style
- **konamilcd** - Konami LCD
  - Scene (paste this): 1980s Konami LCD handhelds, black-and-white LCD sprites of classic action games
- **tiger** - Tiger
  - Scene (paste this): 1990s Tiger Electronics LCD handheld games, cartoon action on a monochrome screen

### Laserdisc

- **laseractive** - Pioneer LaserActive
  - Scene (paste this): a glowing laserdisc spinning, beaming out a full-motion-video sci-fi adventure
- **msxlaserdisk** - MSX Palcom LaserDisc
  - Scene (paste this): an animated full-motion-video space battle projected from a laserdisc

### Media folders

- **avgn** - The Angry Video Game Nerd
  - Scene (paste this): a cluttered retro gamer's room, stacks of old cartridges, a glowing CRT, beer and a controller thrown down in frustration (no real person)
- **radio** - Radio
  - Scene (paste this): a vintage radio studio, glowing ON AIR light, microphone and soundwaves
- **screenshots** - Screenshots
  - Scene (paste this): a burst of floating game screenshots like photographs caught in a camera flash
- **tvgames** - TV Games
  - Scene (paste this): a plug-and-play joystick connected to a retro TV bursting with classic games
- **vgm** - Video Game Movies
  - Scene (paste this): a cinema screen showing epic game-inspired movie scenes, popcorn and projector beam

### PC ports

- **2ship** - 2 Ship 2 Harkinian (Majora's Mask)
  - Scene (paste this): a menacing moon with a face falling towards a clock town at dusk
- **soh** - Ship of Harkinian (Ocarina of Time)
  - Scene (paste this): a young green-clad hero with a sword and shield on a vast field at sunrise
- **starship** - Starship (Star Fox 64)
  - Scene (paste this): a squadron of sleek space fighters racing over an alien planet, laser fire
- **pdark** - Perfect Dark
  - Scene (paste this): a female secret agent with a sci-fi pistol on a neon skyscraper rooftop at night
- **opengoal** - OpenGOAL (Jak and Daxter)
  - Scene (paste this): a young hero and his orange furry sidekick on a lush tropical island
- **openlara** - OpenLara (Tomb Raider)
  - Scene (paste this): a female adventurer with twin pistols in a vast ancient tomb
- **halflife** - Half-Life
  - Scene (paste this): a scientist in a hazard suit with a crowbar in an underground research facility, alien portals
- **redriver2** - ReDriver2 (Driver 2)
  - Scene (paste this): a 1970s muscle-car chase through city streets at night, police lights behind
- **bsyndrome** - Bermuda Syndrome
  - Scene (paste this): a WWII pilot fighting dinosaurs in a lost jungle world
- **dinothawr** - Dinothawr
  - Scene (paste this): a cute dinosaur pushing ice blocks on a frozen puzzle stage
- **gemrb** - GemRB (Infinity Engine)
  - Scene (paste this): a fantasy adventuring party at a torchlit dungeon entrance
- **locomalito** - Locomalito
  - Scene (paste this): a medieval knight fighting monsters in a dark castle, retro-inspired
  - Note, based on: Maldita Castilla (do not paste)
- **powerbomberman** - Power Bomberman
  - Scene (paste this): a little bomb-dropping hero in a maze, bombs exploding in fiery crosses
- **clonehero** - Clone Hero
  - Scene (paste this): a rock guitarist on stage, glowing note highway flying towards them
- **dusklight** - DuskLight
  - Scene (paste this): a moody twilight indie adventure scene
- **love** - LOVE engine
  - Scene (paste this): a colourful collage of charming indie games made with code

### PC stores and VR

- **amazon / eagames / wingog / winbigfish / wingamehouse / winpopcap** - each a different PC-gaming scene with no logos
  - Scene (paste this): GOG = classic PC game boxes and floppy disks; Big Fish / GameHouse / PopCap = bright casual games (hidden-object, match-3, garden defence); EA = blockbuster sports and action; Amazon = a glowing library of game worlds
- **pcvr** - PC VR
  - Scene (paste this): a player in a VR headset surrounded by a neon virtual world

### Home computers (template unless noted)

- **abc80** - Luxor ABC 80 (Sweden, 1978)
  - Scene (paste this): a deep-sea diver in a vintage brass diving helmet, large and close to the viewer, swimming down towards the ruins of a vast sunken city of marble columns and domed temples glowing with mysterious blue-green light on the ocean floor; shafts of light from far above, shoals of fish and drifting bubbles, a huge dark shape of a sea creature moving in the distance
  - Note, based on: Atlantis, a Swedish adventure game released through ABC-klubben in 1983 (do not paste). Rejected: Glipp (reads as Pac-Man), Inka-statyettens forbannelse (reads as Indiana Jones).
  - Note, photo to find: the ABC 80 computer (beige keyboard unit) on a plain background (do not paste)
- **alice32** - Matra Alice 32 (France, 1984)
  - Scene (paste this): a swashbuckling space pirate in a long red coat and a bubble-visor helmet, large and close to the viewer, leaping across the hull of a huge cargo spaceship with a glowing treasure crate under one arm, a ray pistol in the other hand; her small, battered, rusty spaceship (not a sailing ship) docked against the hull with its airlock hatch open, sparks and green gas venting out, a purple nebula and a ringed planet behind
  - Note, based on: Pillage Cosmique (1984), an original French space action game for the Alice 32/90; Galaxion and Galixian avoided (Galaxian clones) (do not paste)
  - Note, photo to find: the Alice 32 (distinctive red case) on a plain background (do not paste)
- **apogeebk01** - Apogee BK-01 (USSR, 1988)
  - Scene (paste this): a small, battered, boxy 1980s Soviet-style car, large and close to the viewer, launching over a huge pothole on a terrible broken country road through a snowy birch forest at dusk, mud and slush spraying from its wheels, a bumper hanging off, headlights glowing; the road ahead cracked, flooded and full of craters, crows scattering from the trees
  - Note, based on: Bad Road, an original BK-01 driving game (Boa Constrictor and the Tetris game avoided as clones) (do not paste)
  - Note, photo: top-down Gemini render from the Carbon theme apogeebk-01.png (do not paste)
- **appleios** - iOS
  - Scene (paste this): colourful mobile-game worlds bursting out of a smartphone screen (no brand logos)
- **aquarius** - Mattel Aquarius (USA, 1983)
  - Scene (paste this): a lone armoured adventurer holding a flaming torch and a short sword, large and close to the viewer, squaring up to a huge horned bull-headed minotaur emerging from the shadows of a vaulted stone dungeon corridor; torchlight, scattered gold coins and a glowing treasure chest in the background
  - Note, based on: Treasure of Tarmin style dungeon crawl (the Aquarius cartridge game); generic hero and minotaur used, no franchise branding (do not paste)
- bk / bk001001 - Elektronika BK (USSR) (template; make the two different)
- bml3 - Hitachi Basic Master Level 3 (Japan, 1980) - game to be researched (ask Claude)
- c16 - Commodore 16 - game to be researched (ask Claude)
- **cbm2** - Commodore CBM-II
  - Scene (paste this): an early-80s office with the machine running a game after hours
  - Note, based on: template variant (do not paste)
- **cgenie** - Colour Genie EG2000 (Hong Kong, 1982)
  - Scene (paste this): a lone astronaut in a chunky orange retro space suit leaps through the air firing a glowing blaster at a giant one-eyed green blob alien rising out of a purple crater on a desert moon, a ringed planet faint in the dark sky
  - Note, based on: generic Colour Genie-era sci-fi shooters - not a specific clone; no single original title confirmed (do not paste)
- **ep128** - Enterprise 128 (UK, 1985)
  - Scene (paste this): a lone space explorer in a chunky red-and-white retro-futuristic suit with a jetpack, large and close to the viewer, swooping low over a purple alien desert and firing a bright energy beam at a colossal crystalline space-whale creature rising from behind jagged green mountains, a huge ringed planet and two small moons in the teal sky
  - Note, based on: generic 1980s British/Hungarian space-shooter scene; no specific original Enterprise title confirmed (do not paste)
- **exl100** - Exelvision EXL 100 (France, 1984)
  - Scene (paste this): a young explorer in an orange flight suit and goggles riding a glowing hover-bike, large and close to the viewer, banking hard through a deep orange desert canyon as a giant mechanical scorpion with black armour rears up behind; dust and sparks flying; a few floating rock islands high above
  - Note, based on: no specific original title confirmed - generic scene in the EXL 100's orange-and-black colours (do not paste)
- **galaxy** - Galaksija (Yugoslavia, 1983)
  - Scene (paste this): a determined miner with a lamp on his helmet and a pickaxe, large and close to the viewer, deep inside a vast underground diamond mine, swinging into a rock wall that bursts open to reveal a cavern of giant glowing blue-white diamonds; mine-cart tracks and wooden supports, falling rocks and glittering dust, a rickety cart full of gems tipping over beside him
  - Note, based on: Diamond Mine, a Galaksija game broadcast over the radio show Ventilator 202; Light Cycle Race avoided (reads as Tron) (do not paste)
- **hec2hr** - Hector 2HR (France, 1983)
  - Scene (paste this): a hulking rusty mining robot with glowing yellow eyes and drill arms, large and close to the viewer, smashing through a wall of giant glowing crystals inside a cavern, a river of lava below and a small hovering scout drone beside it; sparks and crystal shards flying
  - Note, based on: no specific original title confirmed - generic scene (do not paste)
- **ibmpcjr** - IBM PCjr
  - Scene (paste this): a knight arriving at a fairy-tale castle, adventure-game style
  - Note, based on: King's Quest, made for the PCjr (do not paste). Installed scene (armoured knight with plumed helmet and blue cape raising a glowing sword at a fairy-tale castle, small dragon on a tower) deliberately avoids the King's Quest hero and is not a copy of the game.
- **jupace** - Jupiter Ace (UK, 1982)
  - Scene (paste this): a single sleek red-and-white delta-wing starfighter, large and close to the viewer, banking hard past a huge banded gas giant with a swirling storm as it fires a bright laser at a giant spiky crystalline alien asteroid-hive drifting among tumbling rocks; glowing explosion sparks. (Gemini needed a follow-up to keep the left third dark and drop the ringed moon.)
  - Note, based on: generic ACE-branded space shooters (Ace Star / Aceteroids type) - not a specific clone; Space Invaders and Asteroids avoided as clones of famous games (do not paste)
- m21 - M21 - game to be researched (ask Claude)
- **m5** - Sord M5 (Japan, 1982)
  - Scene (paste this): a masked ninja in a dark-indigo costume with a red scarf, large and close to the viewer, mid-leap across a moonlit rooftop with a flashing sword as a towering horned stone-skinned oni demon with glowing eyes rises from the shadows of a pagoda behind; a huge pale full moon, drifting cherry blossom petals and mist
  - Note, based on: generic Japanese ninja action games of the M5 era; no single original M5 title confirmed (do not paste)
- max - Commodore MAX Machine (Japan, 1982) - game to be researched (ask Claude)
- **mbee** - MicroBee (Australia, 1982)
  - Scene (paste this): a huge shaggy dark mythical bunyip creature, with a seal-like head, long tusks and glowing eyes, rearing up out of a moonlit Australian outback billabong, large and close to the viewer, water streaming off it; ghost gums and red rocks silhouetted under a giant full moon and southern stars, a small wooden canoe tipping in the foreground ripples
  - Note, based on: Bunyip Adventure (Grotnik Software, 1984), an Australian MicroBee text adventure (do not paste)
- **mtx512** - Memotech MTX512 (UK, 1983)
  - Scene (paste this): a lone stocky miner-astronaut in a chunky white-and-blue pressure suit with a round glass bubble helmet and twin-tank jetpack, large and close to the viewer, blasting a bright energy beam from a handheld cutting tool at a huge brass-and-steel robotic spider walker rising out of a glowing crystal cavern on an alien moon; purple and teal crystals, drifting dust and sparks. (First attempt looked like a famous bounty-hunter character, so the hero was redone.)
  - Note, based on: generic British 8-bit sci-fi shooters; no single original MTX title confirmed (Kilopede avoided as a Centipede clone) (do not paste)
- ondra - Ondra (Czechoslovakia) - game to be researched (ask Claude)
- orao - Orao (Yugoslavia) - game to be researched (ask Claude)
- **p2000t** - Philips P2000T (Netherlands, 1980)
  - Scene (paste this): a daring pilot in a red-and-cream retro rocket-plane with chunky rivets, large and close to the viewer, banking low over a stormy grey-green sea as a gigantic rusty mechanical kraken bursts out of the waves behind it with tentacles whipping through spray; lightning in the clouds, golden sunset glow on the horizon
  - Note, based on: generic P2000T-era action games (North Sea storm theme for the Dutch machine); no single original title confirmed (do not paste)
- **pecom64** - Pecom 64 (Yugoslavia, 1985)
  - Scene (paste this): a lone cosmonaut in a red and white retro spacesuit with a glowing jet pack swings a bright energy wrench at a towering rusted robot guardian on a rust-red alien planet under a huge pale sun
  - Note, based on: generic Pecom-era arcade-style games; no single original title confirmed (do not paste)
- pegasus - Aamber Pegasus (New Zealand, 1981) - game to be researched (ask Claude)
- pv2000 - Casio PV-2000 (Japan, 1983) - DONE 2026-10-05: no original title confirmed; generic scene used - a bright orange-suited astronaut kid leaping across a cratered moon toward a giant chrome robot crab, blue Earth behind (retro 1980s Japanese computer-game poster mood)
- **rx78** - Bandai RX-78 (Japan, 1983)
  - Scene (paste this): a giant white robot mech standing over a city (named after the famous mech)
- **segaai** - Sega AI Computer (Japan, 1986)
  - Scene (paste this): a friendly educational computer with storybook learning games
  - Note, based on: template variant (do not paste)
- smc777 - Sony SMC-777 (Japan, 1983) - game to be researched (ask Claude)
- **sorcerer** - Exidy Sorcerer (USA, 1978)
  - Scene (paste this): a bearded sorcerer in flowing violet robes thrusts a glowing staff forward, conjuring a blazing blue fireball against a huge red dragon rearing up inside a torch-lit stone cavern
  - Note, based on: generic fantasy dungeon games for the Sorcerer (machine name theme) - no single title confirmed (do not paste)
- sys80 - System-80 - game to be researched (ask Claude)
- **tvc64** - Videoton TV Computer (Hungary, 1985)
  - Scene (paste this): a young Hungarian folk-legend warrior in a red-and-white embroidered tunic and a feathered cap, large and close to the viewer, riding a rearing white winged horse and swinging a glowing sword at a huge three-headed storm dragon coiling around a ruined castle tower on a Carpathian mountain peak at dusk, lightning in the purple sky
  - Note, based on: generic Hungarian folk-tale fantasy (taltos horse legend) for the TVC's home market; no specific original TVC title confirmed (do not paste)
- **vg5k** - Philips VG-5000 (France, 1984)
  - Scene (paste this): a lone deep-sea diver in a brass-and-copper atmospheric diving suit, large and close to the viewer, holding up a glowing harpoon lamp as a giant luminous jellyfish-like sea creature drifts down out of the dark among the toppled columns of a sunken French seaside palace, shafts of green light from the surface above
  - Note, based on: generic French 8-bit undersea adventure; no specific original VG 5000 title confirmed (do not paste)
- vidbrain - VideoBrain Family Computer (USA, 1978) - game to be researched (ask Claude)
- **videodriver** - Video Driver
  - Scene (paste this): a retro driving toy, a road racing towards you on a TV screen

### Other

- gamewave, snotec and similar family/edu systems: keep them bright and cheerful so they read as a set.

### Used on nightly runs (games / scenes chosen)

- 2026-10-05 cassettevision - woodcutter chopping a giant cedar in a misty Japanese forest (Kikori no Yosaku-style, a real Cassette Vision title).
- 2026-10-05 pv2000 - generic: astronaut kid vs chrome robot crab on the moon (no original title confirmed).
- 2026-10-05 microvsn - Cosmic Hunter-style: original space ranger (white/teal flight suit, ray pistol) vs a giant cosmic wasp in a violet nebula. First Gemini result was a Samus-style hero (another system's character), so it was rejected and the original-character ranger version is installed (sources/microvsn/microvsn_bg_v2_ranger.jpg; rejected one kept as microvsn_bg_v1_metroid_style.jpg).
- 2026-10-06 vidbrain - generic: 1970s American football quarterback (plain blue jersey) mid-throw under stadium floodlights, defender silhouette behind (VideoBrain shipped sports cartridges such as Football; no specific original title confirmed).
- 2026-10-06 cbm2 - generic: lone astronaut watching a gold-foiled lunar lander touch down on the moon (CBM-II/B-series was mainly a business line; no specific original game confirmed).
- 2026-10-06 sv8000 - generic: young 1970s pilot in an orange flight suit firing a ray pistol at a saucer mothership over a night city (original character; no specific original Super Vision 8000 title confirmed).
- 2026-10-07 pegasus - generic: original hooded mountain warden with a lantern (rear view) facing a giant stone golem in a storm canyon (no specific original Pegasus title confirmed).
- 2026-10-07 mpu1000 - Rocket Patrol-style (early TV-game space shooter, MP1000 family): silver-and-red rocket firing a laser at one alien saucer (original ship design).
- 2026-10-07 myvision - generic: original master player in a red-and-gold kimono placing a jade tile on a floating shogi/mahjong board with giant carved pieces and lanterns (My Vision shipped Japanese board-game cartridges; no specific title confirmed).
- 2026-10-08 pocketstation - generic: original adventurer in a yellow rain hood (seen from behind) riding one giant glowing blue manta ray above floating rock islands at golden sunset (PocketStation had pet/mini-game software; no specific original title confirmed).
- 2026-10-08 vemulator - generic: original round-bodied robot companion with long ears and a glowing teal belly leaping over a neon ocean with a ringed planet (VMU hosted pet/mini-games; no specific original title used, avoided Sega characters).
- 2026-10-08 bk - generic: original cosmonaut in a retro orange spacesuit (rear view) striding across a frozen planet towards a red-lit space station under a giant moon (Soviet BK-0010 software scene; no specific original title confirmed).
- 2026-10-08 elektronika - Nu, pogodi!-style egg catching (the Elektronika IM LCD hit): original farmhand girl in a red knitted cap (not the game wolf or hare) catching a glowing golden egg in a wicker basket under a wooden hen-house chute in a snowy village at dusk.

- 2026-10-09 studio2 - built-in Bowling (RCA Studio II shipped with Addition, Bowling, Doodle, Freeway, Patterns): a huge glossy amber-and-teal marble bowling ball smashing into ten white pins on a dark wooden lane, pins and splinters exploding outward, no people/characters, no signage (first try had neon signs with text; regenerated as a fresh composition with explicit right-side placement).
- 2026-10-09 orao - Nevidljivi (The Invisible One, the one game on the Orao No 0 tape, Suzy Soft 1987; Orao also had Yugoslav ports/clones): original hooded investigator in a green coat (rear view) raising an oil lantern in a foggy Balkan fortress courtyard, an invisible presence shown only as a glassy shimmer, sparks and wet footprints. Scene guessed from the title; the game itself was not seen.
- 2026-10-09 ondra - Tenebra (modern atmospheric puzzle game with roguelike looks, ported to the Tesla Ondra in 2024 by 72ka; not a period title - original Ondra games were hard to confirm): original wanderer in a patched red poncho and striped scarf (rear view) holding a glowing blue crystal staff before a colossal cracked stone door with abstract glowing patterns (no letters), deep crypt.
- 2026-10-09 n501 - Tempest 2000 / Tempest 3000 style tube shooter (NUON launch showpiece, Jeff Minter): original golden bat-wing starfighter in the foreground firing a cyan beam down a neon wireframe vortex tunnel at a red crystalline enemy, no text.
- 2026-10-09 pippin - Racing Days / rally-style racer on the Pippin (original blue striped rally coupe drifting through a mountain hairpin at dusk with a dust and gravel spray; no text and no real-game characters). Pippin game library is small; title chosen as a plausible driving game.
- 2026-10-09 gc - Luigi's Mansion-style ghost hunt: original girl in a yellow raincoat with a brass headlamp and vacuum-lantern drawing in green spectral mist, moonlit haunted mansion hall (Gemini).
- 2026-10-09 psvita - LittleBigPlanet Vita-style craft world (user worked on the game): original stitched felt fox cub leaping for a glitter paper star among cardboard and quilted-cloth platforms (Gemini). Sackboy NOT used; first version had a platform in the left 45 percent so it was redone as a fresh composition.
- 2026-10-09 ps2 - Vice City-style tribute (user request; GTA3 first asked, user chose Vice City): original unbadged hot-pink and white 1980s wedge sports convertible on an ocean boulevard at sunset, palms, big pink sun, neon art-deco hotels, no people or text, all in the right 55 percent (Gemini).

### Arcade three-cabinet groups (2026-10-08)
Attach 4 images: 1 OG cps2 group on light grey (layout), 2 existing cabinet on light grey, 3 system logo, 4 background.
Prompt (segasystem32 version, accepted): "Using the four attached images, create a product photograph of ONE tight compact group of THREE upright arcade cabinets, arranged exactly like image 1 (the Capcom CPS2 group), and copying how image 1 works. CENTRE cabinet: in front, facing straight at the viewer, the system's own branded cabinet in full bright colour: it is the cabinet from image 2 but recoloured in vivid <system colour> with the <system> logo from image 3 on the marquee and on the lower front panel, and a boot screen showing the <system> logo, just as the centre CPS2 cabinet shows the Capcom Play System logo and a Capcom Presents screen. LEFT and RIGHT cabinets: game cabinets standing slightly behind the centre one, each turned about 30 degrees outward, overlapping behind the centre cabinet's edges, with their side panels touching it. They have black bodies with slightly faded, muted colours (like the outer cabinets in image 1), each with full-height vinyl artwork on its visible side panel, its own game marquee on top, and gameplay on its screen. LEFT game: <game 1 + art description + marquee text>. RIGHT game: <game 2 ...>. NO green gaps between the cabinets. Plain solid bright green background (#00FF00), no shadow of any kind, flat even green right up to hard clean edges."
Sit-down systems keep a single sit-down cabinet (user decision).

### 2026-10-10 night run (igspgm, zinc, gaelco, unis, rawthrills)
- igspgm - Oriental Legend / Knights of Valour-style: rear view of an original armoured Three Kingdoms general swinging a gilded halberd at a charging armoured boar in a misty gorge; hero centre-right, left 45% empty rock and mist. Cabinets: three-cabinet group (PGM-style centre + two muted game cabinets).
- zinc - Rival Schools-style: original schoolboy in a long red scarf flying-kick at a huge setting sun, cherry petals, school building far right; left third empty dusk haze. Cabinets: three-cabinet group.
- gaelco - Radikal Bikers-style: original pizza courier on an orange scooter splashing through a rainy neon city street, pizza boxes flying; a taxi in the left area was removed with a Gemini edit. Controller: PixN Carbon Gaelco A.V. TRACK cabinet.
- unis - Sky Kart-style (original): teal-ponytail girl in a yellow helmet and orange suit driving a pink go-kart with a rainbow trail, balloons and confetti on the right; first two versions rejected (Mario-like look; balloons on the left). Cabinets: UNIS blue centre cabinet, left SKY KART, right TICKET RUSH (invented games).
- rawthrills - The Fast and the Furious-style: unbadged yellow sports coupe with black stripes jumping a ramp through a fireball at dusk; fire trail dimmed out of the left area.
- zinc redo 2026-10-10: three-cabinet prompt with "both side cabinets must have solid GLOSSY BLACK bodies and be as rich, bright and fully saturated as the centre cabinet. NOT faded, NOT grey, NOT washed out"; refs = cps2_grey, zinc logo, zinc background; sides SCHOOL CLASH / STAR KNIGHT (original).
