import os, sys
NL=chr(10); T=chr(9)
sys.path.insert(0,'iconic-tpn/_tools'); from tpn_map import M
def tsv(p): return [l.split(T) for l in open(p).read().split(NL) if l.strip()]
names={r[1]:r[2] for r in tsv('all_systems.tsv')}
orig=set(os.path.splitext(f)[0] for f in os.listdir(('/Volumes/stuff/Emulation/TPN Iconic Theme/iconic-es-main/_inc/backgrounds')))
ctrl_orig=set(os.path.splitext(f)[0] for f in os.listdir(('/Volumes/stuff/Emulation/TPN Iconic Theme/iconic-es-main/_inc/controllers')))
logo_orig=set(os.path.splitext(f)[0] for f in os.listdir(('/Volumes/stuff/Emulation/TPN Iconic Theme/iconic-es-main/_inc/logos')))
I='iconic-tpn/_inc/'
salv={r[0]:r for r in tsv('salvage_log.tsv')}
arc={r[0]:r[1] for r in tsv('arcade_bg_log.tsv')}
ctl={r[0]:r[1] for r in tsv('controllers_log.tsv')}
themes=sorted(set(names)-orig)
custom={"igspgm":"Oriental Legend / Knights of Valour-style: original Three Kingdoms halberd general facing an armoured war boar in a misty gorge (Gemini, original characters) - installed","zinc":"Rival Schools-style: original schoolboy in a red scarf flying-kicking against a setting sun with cherry petals (Gemini, original character) - installed; metadata renamed Sony ZN (ZiNc), 1995","gaelco":"Radikal Bikers-style: original pizza courier on an orange scooter racing a rainy neon street, pizzas flying (Gemini, original character) - installed; year set to 1996 (unsure)","unis":"Sky Kart-style: original teal-ponytail girl in a yellow helmet driving a pink go-kart off a rainbow trail among balloons and confetti (Gemini, original character) - installed","rawthrills":"The Fast and the Furious-style: original unbadged yellow-and-black-striped sports coupe jumping a ramp through a fireball (Gemini, original) - installed; year set to 2004","pippin":"Racing Days-style rally game: original cobalt rally coupe drifting a mountain hairpin at dusk (Gemini, original) - installed; year corrected 1986 to 1996","n501":"Tempest-style tube shooter: golden bat-wing starfighter firing down a neon vortex tunnel at a red crystal enemy (Gemini, original) - installed; name shortened to NUON DVD-N501, hardware type set to console","ondra":"Tenebra-style crypt puzzle: wanderer at a cracking rune door (Gemini, original character) - installed","orao":"Nevidljivi-style invisible presence in a foggy fortress courtyard (Gemini, original character) - installed","studio2":"Bowling-style strike, giant marble ball vs ten pins (Gemini; built-in Studio II game) - installed","segaalls":"House of the Dead (Gemini) - installed","segare":"Initial D (Gemini) - installed","segarw":"Daytona-style oval (Gemini) - installed","segaer":"Sega Rally-style scene (Gemini) - installed","seganu":"Hatsune Miku-style concert (Gemini) - installed","aleck64":"Starfighter scene (Gemini) - installed","abc80":"Atlantis sunken city (Gemini) - installed","actionmax":"Sonic Fury jet dogfight (Gemini) - installed (bg from a 1024px copy - swap for full-size if re-downloaded)","alice32":"Space pirate raid (Gemini) - installed","segasystem32":"Golden Axe-style barbarian (Gemini) - installed","apogeebk01":"Bad Road Soviet car (Gemini) - installed","namco11":"Tekken-style martial arts clash (Gemini) - installed","galaxy":"Diamond Mine miner (Gemini) - installed","aquarius":"Treasure of Tarmin-style dungeon (Gemini) - installed","jupace":"Starfighter vs alien hive over Jupiter (Gemini) - installed","mbee":"Bunyip Adventure bunyip billabong (Gemini) - installed","cgenie":"Astronaut vs one-eyed slime alien (Gemini) - installed","sorcerer":"Sorcerer vs dragon cavern (Gemini) - installed","pecom64":"Cosmonaut vs rusted robot guardian (Gemini) - installed","ibmpcjr":"Knight arriving at fairy-tale castle, King's Quest-style (Gemini) - installed","exl100":"Hover-bike rider vs giant mechanical scorpion (Gemini) - installed","hec2hr":"Mining robot vs crystal cavern (Gemini) - installed","mtx512":"Miner-astronaut vs spider walker in crystal cavern (Gemini) - installed","p2000t":"Retro rocket-plane vs mechanical kraken (Gemini) - installed","m5":"Ninja vs oni demon, moonlit pagoda (Gemini) - installed","vg5k":"Deep-sea diver vs luminous jellyfish, sunken palace (Gemini) - installed","tvc64":"Hungarian warrior on winged horse vs three-headed dragon (Gemini) - installed","ep128":"Jetpack explorer vs crystalline space-whale (Gemini) - installed","cassettevision":"Kikori no Yosaku-style woodcutter (Gemini) - installed","pv2000":"Astronaut kid vs chrome robot crab on the moon (Gemini, generic) - installed","microvsn":"Space ranger vs cosmic wasp, Cosmic Hunter-style (Gemini, generic) - installed","vidbrain":"American football quarterback under floodlights, VideoBrain Football-style (Gemini, generic) - installed","cbm2":"Astronaut watching a lunar lander touch down (Gemini, generic) - installed","sv8000":"Retro pilot vs saucer mothership over a night city (Gemini, generic) - installed","pegasus":"Mountain warden vs stone golem (Gemini, generic) - installed","mpu1000":"Rocket patrol vs alien saucer, early TV-game style (Gemini, generic) - installed","myvision":"Master player at floating shogi/mahjong board (Gemini, generic) - installed","elektronika":"Farmhand girl catching a golden egg in a basket, Ну, погоди!-style egg catching (Gemini, original character) - installed","bk":"Cosmonaut walking to a red-lit space station on an ice planet (Gemini, generic) - installed","vemulator":"Round robot companion leaping over a neon ocean (Gemini, generic) - installed","pocketstation":"Rain-coat adventurer riding a glowing manta ray over floating islands (Gemini, generic) - installed"}
custom_ctl={'igspgm':'Gemini three-cabinet group (PGM-style blue centre cabinet + two muted game cabinets), green-screen cut-out - installed','zinc':'Gemini three-cabinet group (Sony ZN-style centre cabinet + two muted game cabinets), green-screen cut-out - installed','gaelco':'PixN Carbon Gaelco A.V. TRACK cabinet image used as-is, cut-out (small, 248x283) - installed','unis':'Gemini three-cabinet group (UNIS blue centre cabinet + Sky Kart and Ticket Rush game cabinets, original games), green-screen cut-out - installed','rawthrills':'Cabinet image from the PixN Carbon set, cut-out; logo placed on a black plate (white-on-white) - installed','segaalls':'SWDC cabinet cut-out - installed','segare':'Initial D Ver.3 cabinet cut-out - installed (Ver.3 is NAOMI 2 era)'}
JP_NOART={'dreamcast-jp','gc-jp','n64-jp','ps2-jp','psx-jp','mark3','iqueplayer'}
import json
BR=json.load(open('iconic-tpn/_tools/bg_review.json'))
FRAME=set(BR['frame']); PLACE=set(n for g in BR['dups'] for n in g)
rows=[]; groups={}
for t in themes:
    todo=[]
    if t in custom: bg=custom[t]
    elif t in arc: bg='Hypermax background (frame removed)' if arc[t]=='hypermax-bg' else arc[t]
    elif t in M:
        src,kind=M[t]; bg=('Iconic '+src+' art (same family)') if kind=='variant' else ('borrowed: Iconic '+src)
    elif t in salv:
        bg={'hypermax-bg':'Hypermax background (frame removed)','ckau':'ckau-book background','ckau-art':'ckau-book art on Iconic default'}.get(salv[t][2],salv[t][2])
    else: bg='none'
    if t=='bk001001': bg='borrowed: Elektronika BK art'
    if not os.path.exists(I+'backgrounds/%s.webp'%t): bg='NONE (theme default)'
    if t in custom: bg=custom[t]
    if 'Hypermax' in bg and t not in custom:
        g='B. Hypermax background (frame removed) - looks OK'
        if t in FRAME: todo.append('REMAKE: Hypermax picture only fills half the screen (do not upscale) - new custom art'); g='B1. REMAKE - custom art needed'
        if t in PLACE: todo.append('REMAKE: generic placeholder shared with other systems - new custom art'); g='B1. REMAKE - custom art needed'
    elif bg.startswith('borrowed'): todo.append('needs its own art'); g='C. Borrowed art - needs its own background'
    elif 'NONE' in bg or bg=='none': todo.append('needs art'); g='D. No art yet'
    elif 'installed' in bg: todo=[]; g='A. Custom art - done'
    elif 'ckau' in bg: todo.append('review / consider custom art'); g='E. ckau-book art - review'
    else: g='F. Covered by Iconic art (same system family)'
    if t in JP_NOART: todo.append('regional (JP/CN) styling')
    c=custom_ctl.get(t) or ('Iconic' if t in ctrl_orig else ctl.get(t,''))
    if not os.path.exists(I+'controllers/%s.webp'%t) and t not in custom_ctl: c='generic placeholder'; todo.append('needs system image')
    elif c.startswith('hypermax'): todo.append('check system image is hardware, not a logo')
    lg='Iconic' if t in logo_orig else ('ckau-book' if os.path.exists(I+'logos/%s.webp'%t) else 'text only')
    if t in custom: lg='custom'
    if lg=='text only': todo.append('needs logo')
    box='- [x]' if t in custom else '- [ ]'
    if t not in custom: todo.append('description text')
    groups.setdefault(g,[]).append('| %s | %s | %s | %s | %s | %s | %s |'%(box,t,names.get(t,''),bg,c or '-',lg,'; '.join(todo)))
out=['# Iconic TPN - to-do list','',
'## Start here - adding new art','',
'1. Pick a system from section B1, C, D or E below.',
'2. Find the system in section 5 (Gemini prompts) at the bottom of this file. Attach a style reference from the Iconic-style-refs folder on the Mac desktop, paste the STANDARD BLOCK with the system scene line, and generate in Gemini.',
'3. Download with Gemini\'s own download button (full size, never screenshots).',
'4. Find a system image (cabinet / console / computer photo on a PLAIN white or flat grey background) and a logo (transparent PNG or platform badge).',
'5. Save all three into **Downloads/Iconic Images**, named with the system code:',
'   - `<code>_bg.jpg` - background, e.g. `alice32_bg.jpg`',
'   - `<code>_cab.png` - system image, e.g. `alice32_cab.png`',
'   - `<code>_logo.png` - logo, e.g. `alice32_logo.png`',
'6. Tell Claude which systems are ready. Claude processes them, installs into the theme, renders mockups, files the originals in `sources/<code>/` on the NAS and ticks them off here.','',
'Rules: new Gemini chat per system; cinematic poster moment, one large hero close to the viewer, centre-right; left third mostly empty; no text/logos/UI/cabinets in backgrounds; no upscaled art. Full standard: see section 1 and section 5.','',
'Links: [PROMPTS.md](PROMPTS.md) - [CREDITS-TPN.md](CREDITS-TPN.md) - mockups: `stuff/Emulation/TPN Iconic Theme/TPN Iconic/mockups` - originals: `stuff/Emulation/TPN Iconic Theme/sources`','',
'Working copy: Mac ~/tpn-build/iconic-tpn - zip on NAS: stuff/Emulation/TPN Iconic Theme/TPN Iconic','',
'## 1. Theme - general','',
'- [x] Sega ALLS and Sega RingEdge custom art installed (background, cabinet, logo)',
'- [x] PS Vita background redone (2026-10-09): painted LittleBigPlanet image supplied by the user, fitted to 16:9; fox cub versions reserved for PS3/PSP (sources/_reserved_for_ps3/)',
'- [ ] GameCube background redone with an original ghost-hunter scene (2026-10-09), awaiting user decision (keep, or restore the original Iconic art); gc-jp and gch variants still show the old art',
'- [ ] Remake all backgrounds in section B1 with custom art (Gemini scene + cabinet/hardware image + sticker logo), same standard as the Sega boards - no upscaled art',
'- [ ] Work through PROMPTS.md (one Gemini prompt per system, plus what photo/logo to find); save results to Downloads/Iconic Images named <code>_bg / <code>_cab / <code>_logo',
'- [ ] Standard for all new art: new Gemini chat per system, style reference attached, cinematic poster moment (not a game screenshot), one large hero close to the viewer in the centre-right, left third mostly empty, bottom calm, no text/logos/UI/cabinets; full download size (1376x768 or larger); logos via make_logo.py; cabinets via cutout_flat.py (plain backgrounds only); arcade cabinets: same gentle three-quarter angle as the others (front mostly facing the viewer, turned slightly left, narrow side strip on the right), side art influenced by the chosen game for that system, system logo on the marquee (check all three every time); computers flat top-down overhead view like Iconic C64/Amiga',
'- [x] Hypermax frame fix applied to all 60 remaining Hypermax systems (background layer only) - mockups in TPN Iconic/mockups/hypermax_bg_only; replace any plain ones with custom art',
'- [ ] Generate replacement art (Gemini) for systems using borrowed or no art - see sections C and D',
'- [ ] Regional styling for Japanese / Chinese variants without their own art',
'- [ ] Description text for all new systems (currently blank)',
'- [ ] Find hardware images for systems still on the generic placeholder',
'- [ ] Logos for systems showing text only',
'- [ ] Check the 28 Hypermax system images are hardware, not logos (controllers_preview.jpg)',
'- [ ] Consider an Initial D 6/7/8 cabinet for RingEdge (current cut-out is Ver.3 / NAOMI 2)',
'- [ ] Install on the PC and test in RetroBat (dark and light schemes)',
'- [x] Update CREDITS-TPN.md for Gemini-generated art (ALLS, RingEdge) - keep adding as new art goes in',
'- [ ] Create private GitHub repo from ~/tpn-build/iconic-tpn',
'- [ ] Add an About this fork section to the README before the repo goes up: unofficial fork of Iconic (ES) by Delgan (based on Iconic ES-DE by Siddy212), not affiliated with or endorsed by the Iconic authors; all original Iconic artwork unchanged; added backgrounds for systems Iconic did not cover are AI-generated (Google Gemini); salvaged art credited in CREDITS-TPN.md',
'- [ ] Keep AI art out of any contributions back to the original Iconic project unless Delgan says he is happy with it',
'- [ ] Optional courtesy: before sharing publicly, send Delgan a short note on the Iconic GitHub (what it is, unofficial fork, new backgrounds are AI) so he can raise any concerns early',
'- [ ] Before sharing with TPN: confirm they are happy with AI backgrounds (they already use AI, so likely fine); keep AI labels in CREDITS-TPN.md; any AI background can be swapped for human-made art later (one file per system)',
'- [ ] Optional: offer to the TPN team (needs their OK for Hypermax art; keep ckau-book CC BY-NC-SA credit)','',
'## 2. Arcade Classics','',
'- [ ] Confirm where the arcade ROMs and RetroBat gamelists live (NAS or PC)',
'- [ ] Decide rating source for Unplayed Classics: own ratings or scraped ratings',
'- [ ] Agree folder layout: Manufacturer / Genre / Unplayed Classics (by genre) - check genre list and merges (e.g. shmup variants, light gun list)',
'- [ ] Generate grouping and review proposed folders and game counts',
'- [ ] Write es_systems_custom entry for the Arcade Classics system',
'- [ ] Build link-creation script (run as admin on the PC; Developer Mode; allow symlinks to NAS)',
'- [ ] Generate gamelist for the new system (metadata and media from existing arcade gamelist)',
'- [ ] Per-game emulator settings for PixN PC arcade boards, or hybrid collections fallback - test a few per board first',
'- [ ] Play-count check across both systems; scheduled overnight refresh',
'- [ ] Theme tile and background for Arcade Classics',
'- [ ] Test on the PC','',
'## 3. No Mercy mods','',
'- [ ] Install es_systems_nomercy.cfg in RetroBat/emulationstation/.emulationstation',
'- [ ] Create roms/n64nomercy (or point path at the NAS)',
'- [ ] Tell Claude which folder the existing mods are in (full NAS search timed out)',
'- [ ] Patch any .xdelta / .ips / .bps mods onto your own No Mercy ROM',
'- [ ] Test Mupen64Plus-Next vs Project64; switch to -system n64 if settings do not apply',
'- [ ] Theme art for No Mercy Mods (background, logo, system image)','',
'## 4. Systems not in the original Iconic theme (%d)'%len(themes),'',
'Every system in the PixN build that the original Iconic theme has no art for, with where its current art comes from.','']
for g in sorted(groups):
    out+=['### %s (%d)'%(g,len(groups[g])),'','| Done | System | Name | Background | System image | Logo | To do |','|---|---|---|---|---|---|---|']+sorted(groups[g])+['']
# PROMPTS_APPEND: include the full Gemini prompt sheet at the end so everything is in one file
pr=open('iconic-tpn/PROMPTS.md').read().split(NL)
pr=[l for l in pr if not l.startswith('# Iconic TPN - art prompt sheet')]
pr=[('#'+l if l.startswith('## ') else l) for l in pr]
out+=['','## 5. Gemini prompts (from PROMPTS.md)','']+pr
open('iconic-tpn/TODO.md','w').write(NL.join(out))
print(len(themes)); print({g:len(v) for g,v in sorted(groups.items())})
