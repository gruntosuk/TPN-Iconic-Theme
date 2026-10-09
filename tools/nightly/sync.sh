cd ~/mnt/tpn-build; N=~/mnt/Emulation/"TPN Iconic Theme"
for c in n501 pippin studio2 orao ondra; do mkdir -p "$N/sources/$c"; cp -f sources/$c/* "$N/sources/$c/"; done
for c in studio2 orao ondra n501 pippin; do cp -f mockups/$c.jpg "$N/TPN Iconic/mockups/"; done
cp -f TODO.md PROMPTS.md CREDITS-TPN.md NIGHTLY_LOG.md iconic-tpn/TODO.md /dev/null 2>/dev/null
for f in TODO.md PROMPTS.md CREDITS-TPN.md NIGHTLY_LOG.md; do cp -f iconic-tpn/$f "$N/TPN Iconic/$f" ; done
for f in TODO.md PROMPTS.md CREDITS-TPN.md NIGHTLY_LOG.md; do cp -f iconic-tpn/$f "$N/$f"; done
echo docs > work/nightly/sync_state.txt
cp -f iconic-tpn_20261009_b.zip "$N/TPN Iconic/iconic-tpn_20261009_b.zip"
cmp iconic-tpn_20261009_b.zip "$N/TPN Iconic/iconic-tpn_20261009_b.zip" && echo zipok >> work/nightly/sync_state.txt
echo done >> work/nightly/sync_state.txt
