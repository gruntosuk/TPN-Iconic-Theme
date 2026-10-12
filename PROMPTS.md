# Iconic TPN - art prompt sheet

Work down the list. For each system you need three things: a background, a system image and a logo.

## How to use

1. In Gemini, attach one style reference from the Iconic-style-refs folder on the Mac desktop (SNES is the best all-rounder).
2. Paste the STANDARD BLOCK below, replacing [SCENE] with ONLY the system's Scene line. Never paste the Note lines - they are for you (which game it is based on, which photo to look for).
3. Download with Gemini's own download button (full size, 1376x768). Never screenshots. Start a NEW Gemini chat for every system.
4. Save into Downloads/Iconic Images, ideally renamed with the system code: e.g. alice32_bg.jpg, alice32_cab.png, alice32_logo.png. Then tell Claude which systems are ready.

## STANDARD BLOCK (paste every time)

> Using the attached image as a style reference, create a background in the same bold, painted illustration style: a dramatic cinematic poster moment, not a game screenshot. One large hero close to the viewer and one clear focus of action, not lots of small things. Scene: [SCENE]. Requirements: 16:9, 1920x1080; the hero large in the centre-right; the left third darker and mostly empty (sky, haze or shadow); the bottom edge calm, dark and uncluttered; no text, no numbers, no score, no titles, no logos, no borders, no arcade cabinet, no screen frame, no joysticks or buttons, no UI of any kind.

If Gemini adds text or signs anyway, reply: remove all text, signs and lettering.

Tips that work: always start a NEW Gemini chat per system (follow-ups edit the previous image, so old mistakes carry over). Ask for a cinematic poster moment, not a game screenshot. One large hero close to the viewer and one clear target beats lots of small things. Say the left third should be mostly empty.

## System images and logos

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

## CABINET FALLBACK (when no good real cabinet photo exists)

Some boards shipped in generic cabinets (Aleck 64, many Japanese boards), so there is no distinctive cabinet to photograph. Build one in Gemini from parts. Start a NEW chat, attach NO style reference, and upload three images:

1. a generic arcade cabinet photo for the shape (a Japanese sit-down candy cabinet such as a Sega Astro City suits most Japanese boards; an upright or racing cabinet where that fits better),
2. the system's logo (for the marquee),
3. a screenshot of the system's signature game (for the screen - ideally the same game the background is based on).

> Using the three attached images, create a product photograph of an arcade cabinet: use the shape of the cabinet in image 1, repaint it in [COLOUR SCHEME], put the logo from image 2 on the lit marquee at the top, and show the game from image 3 on the screen. Three-quarter view facing left (the front of the cabinet turned towards the left of the picture), standing on a plain, solid bright green background (#00FF00) with even studio lighting. Clean, realistic, sharp detail. No other text or brand names, no people. No shadow of any kind (no floor shadow, no drop shadow), no reflection and no glow around it - the background must be perfectly flat, even green right up to hard, clean edges.

If Gemini adds a shadow anyway, reply: remove the shadow completely; flat, even green background with no shadow, reflection or glow, and hard clean edges; change nothing else. The solid green background is what lets it cut out cleanly - white would blend into any white trim on the cabinet. Ask for it facing left from the start, so it never needs mirroring. The logo on the marquee is the one place a logo belongs. Save it as <code>_cab.png (or .jpg).

## OBSCURE COMPUTERS AND CONSOLES

Iconic always uses GAME art, never the machine itself - even for obscure computers (Dragon 32, CoCo, SAM Coupe, PET all show game scenes). The machine appears only in the system image slot. So every system's background must be based on an actual game released for it. Where no game is listed yet, ask Claude to research the system's best-known game first and write the Scene line from it. Avoid clones of famous games (e.g. a Pac-Man clone) - pick a game original to that machine or its home scene, so it cannot be mistaken for another company's game. Also avoid scenes that read as a famous franchise even if the game is original (e.g. an explorer with a hat grabbing a golden idol reads as Indiana Jones) - change the hero or setting, or choose another game.

---

## Arcade boards

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

## Pinball

- **pinballfx / pinballfx2 / pinballfx3** - three different digital pinball scenes
  - Scene (paste this): a steel ball racing up a glowing ramp, flippers, bumpers and lights
  - Note, based on: vary colour and theme for each (do not paste)
- **pinballm** - Pinball M
  - Scene (paste this): a horror-themed pinball table in the dark, skulls and ghouls lit in red and green
- **zaccariapinball** - Zaccaria Pinball
  - Scene (paste this): a classic 1980s Italian pinball table with painted backglass, warm arcade lighting

## Consoles and handhelds

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

## Laserdisc

- **laseractive** - Pioneer LaserActive
  - Scene (paste this): a glowing laserdisc spinning, beaming out a full-motion-video sci-fi adventure
- **msxlaserdisk** - MSX Palcom LaserDisc
  - Scene (paste this): an animated full-motion-video space battle projected from a laserdisc

## Media folders

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

## PC ports

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

## PC stores and VR

- **amazon / eagames / wingog / winbigfish / wingamehouse / winpopcap** - each a different PC-gaming scene with no logos
  - Scene (paste this): GOG = classic PC game boxes and floppy disks; Big Fish / GameHouse / PopCap = bright casual games (hidden-object, match-3, garden defence); EA = blockbuster sports and action; Amazon = a glowing library of game worlds
- **pcvr** - PC VR
  - Scene (paste this): a player in a VR headset surrounded by a neon virtual world

## Home computers (template unless noted)

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

## Other

- gamewave, snotec and similar family/edu systems: keep them bright and cheerful so they read as a set.

## Used on nightly runs (games / scenes chosen)

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

## Arcade three-cabinet groups (2026-10-08)
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

### 2026-10-12 night run (gamewave, tvgames, hyperscan, beena, neogeo64)
- gamewave - game-show style: original orange-and-steel robot host in a bow tie holding a glowing marquee question mark under spotlights, confetti, silhouetted crowd. Console: Gemini render on green from the Carbon picture.
- tvgames - sports style: original astronaut swinging a neon bat at a flaming comet over a neon grid, ringed planet. Console: generic Gemini joystick on light grey (the green version lost the black body), cut out with a flat cutout.
- hyperscan - card-battler style: original silver-haired duellist in a red cloak summoning a golden dragon from a glowing card, purple storm sky (Marvel card game deliberately not used). Console: Gemini render on light grey from a Wikimedia photo.
- beena - storybook: original girl in a yellow raincoat and red boots jumping into a rainbow puddle splash, dusk meadow. Attempts: v1 had flowers in the left 45 percent, v2 lost the style reference and had a mushroom on the left, v3 accepted (strict "right 45%" composition, style ref attached). Console: Gemini render on green from a text description (no usable photo found), despilled.
- neogeo64 - Samurai-duel style: original white-haired female ronin slashing at a blue oni with a spiked club on a stormy sea-cliff. Three-cabinet group prompt = the segasystem32 version, recoloured vivid red with the Hyper Neo Geo 64 logo, sides IRON FANG and STORM RIDERS (original), "GLOSSY BLACK, rich, NOT faded" wording; refs = cps2 group, Sega cabinet group, logo, background. Worked first time. The centre control panel still carries a tiny SEGA mark inherited from the shape reference (not visible at theme size).
- Gemini UI notes: the "+" button needs repeated clicks; after upload the thumbnails can open an image editor (press the back arrow, nothing is saved); click the send arrow if Return does not send.
- 2026-10-12 neogeo64 redo (user: ALWAYS use real games on the side cabinets): same three-cabinet prompt but "real Hyper Neo Geo 64 game cabinets", LEFT SAMURAI SHODOWN 64 by SNK, RIGHT FATAL FURY WILD AMBITION by SNK, with marquee text and side art described. Gemini produced recognisable marquees and side art first time.
