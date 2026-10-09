# target theme name -> (source theme name, kind)
# variant = same system family: copy logo, background, overlay, controller, metadata (renamed)
# art     = borrow background/overlay only; logo falls back to theme text; minimal metadata
M = {
# regional (existing JP art)
'megadrive-jp':('megadrivejp','variant'),'saturn-jp':('saturnjp','variant'),
# regional (no JP art yet - parent for now)
'dreamcast-jp':('dreamcast','variant'),'gc-jp':('gc','variant'),'n64-jp':('n64','variant'),
'ps2-jp':('ps2','variant'),'psx-jp':('psx','variant'),'mark3':('mastersystem','variant'),
# hacks / add-ons / sub-libraries
'gch':('gc','variant'),'ggh':('gamegear','variant'),'n64h':('n64','variant'),'ps2h':('ps2','variant'),
'ps3h':('ps3','variant'),'psxh':('psx','variant'),'wiih':('wii','variant'),'wiiware':('wii','variant'),
'wiiueshop':('wiiu','variant'),'wiiu-sky':('wiiu','variant'),'xbla':('xbox360','variant'),
'pspminis':('psp','variant'),'neogeomvs':('neogeo','variant'),'nomad':('genesis','variant'),
'segachannel':('megadrive','variant'),'megadrive-msu':('msu-md','variant'),'nes-msu':('nes','variant'),
'nes_hd':('nes','variant'),'nes_aladdin':('nes','variant'),'3dsen':('nes','variant'),'datach':('famicom','variant'),
'dendy':('famicom','variant'),'snescd':('snes','variant'),'gba2players':('gba','variant'),
'n64recomp':('n64','variant'),'supercharger':('atari2600','variant'),'c64gs':('c64','variant'),
'amiga3000':('amiga','variant'),'amiga4000':('amiga','variant'),'cpc464p':('amstradcpc','variant'),
'megacd32x':('sega32x','variant'),'segacd32x':('sega32x','variant'),'tduo':('tg-cd','variant'),
'sc-3000':('sg-1000','variant'),'hbmame':('mame','variant'),'mame-aknf':('mame','variant'),
'win311':('windows3x','variant'),'win95':('windows9x','variant'),'win98':('windows9x','variant'),
'exodos':('dos','variant'),'exowin3x':('windows3x','variant'),'exowin9x':('windows9x','variant'),
'loopy':('casloopy','variant'),'segastv':('stv','variant'),'typex':('type-x','variant'),'typex2':('type-x','variant'),
'cave':('cave3rd','variant'),'rtcw':('iortcw','variant'),'xash3d_fwgs':('xash3d-fwgs','variant'),
'pocketchallengev2':('wonderswan','art'),'pocketstation':('psx','art'),'vemulator':('dreamcast','art'),
# PC arcade boards -> TeknoParrot art
'segaalls':('teknoparrot','art'),'segaer':('teknoparrot','art'),'seganu':('teknoparrot','art'),
'segare':('teknoparrot','art'),'segarw':('teknoparrot','art'),'nesicax':('teknoparrot','art'),
'nesicax2':('teknoparrot','art'),'namco3xx':('teknoparrot','art'),'namcoes3':('teknoparrot','art'),
'konamipc':('teknoparrot','art'),'rawthrills':('teknoparrot','art'),'unis':('teknoparrot','art'),
'wahlap':('teknoparrot','art'),'exboard':('teknoparrot','art'),
# classic arcade boards
'hikaru':('naomi','art'),'aleck64':('n64','art'),'neogeo64':('neogeo','art'),'gaelco':('arcade','art'),
'igspgm':('arcade','art'),'namco11':('arcade','art'),'namco12':('arcade','art'),'segasystem32':('arcade','art'),
'zinc':('arcade','art'),'fightcade':('arcade','art'),'igtslots':('arcade','art'),
# pinball / laserdisc / LCD
'pinballfx':('fpinball','art'),'pinballfx2':('fpinball','art'),'pinballfx3':('fpinball','art'),
'pinballm':('fpinball','art'),'zaccariapinball':('vpinball','art'),
'laseractive':('laserdisc','art'),'msxlaserdisk':('laserdisc','art'),'konamilcd':('lcdgames','art'),'tiger':('lcdgames','art'),
# PC storefronts
'wingog':('windows','art'),'winbigfish':('windows','art'),'wingamehouse':('windows','art'),
'winpopcap':('windows','art'),'eagames':('windows','art'),'amazon':('windows','art'),'pcvr':('windows','art'),
# ports
'2ship':('ports','art'),'soh':('ports','art'),'pdark':('ports','art'),'opengoal':('ports','art'),
'redriver2':('ports','art'),'openlara':('ports','art'),'bsyndrome':('ports','art'),'dinothawr':('ports','art'),
'gemrb':('ports','art'),'halflife':('xash3d-fwgs','art'),'powerbomberman':('ports','art'),'starship':('ports','art'),
'dusklight':('ports','art'),'locomalito':('ports','art'),'clonehero':('ports','art'),
# computers in known families
'c16':('cplus4','art'),'max':('c64','art'),'cbm2':('pet','art'),'bk':('_default','skip'),
}
M.update({'iqueplayer':('n64','variant'),'gog':('windows','art'),'love':('ports','art'),'ghostship':('ports','art')})
