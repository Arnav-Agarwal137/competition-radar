# -*- coding: utf-8 -*-
"""My two ratings for THE PASS WALL, kept apart from the facts on purpose.

Same contract as judgement.py for the bill wall, and for the same reason: every
value in passes.py has to be something a page literally printed, and none of
these numbers are. Keeping them in a different file means a future session cannot
confuse an opinion for a transcription.

  prestige - does the NAME mean anything to a medical school, a lab or a panel.
  learning - how much HE would actually learn, for medicine, then research, then AI.

They are separate on purpose and the split earns its keep more here than it did
on the bill wall. ML Collective is prestige 2, learning 5 - nobody has heard of
it and its weekly reading group would teach him more than most things on this
page. RSNA membership is the mirror image, 4 and 2 - it is a line on a CV, not an
education. Collapsing them into one score would hide exactly the entries worth
seeing.

Anything rated 1 on prestige is not a criticism. Zooniverse leaves no mark at
all; that is what it IS, and the page says so on its face rather than pretending.
"""

RANK = {
 # ---- fellowships: the heaviest things here, and the ones he would miss
 'srfp-science-academies':      (5, 5),
 'gsoc':                        (5, 5),
 'icts-ltvsp':                  (5, 5),
 'jncasr-srfp':                 (5, 5),   # names MBBS, pays, and it is in his brother's city
 'khorana':                     (5, 5),   # names MBBS too, funded, in the US - and years away
 'outreachy':                   (4, 4),
 'spar':                        (3, 5),
 'mlh-fellowship':              (3, 4),

 # ---- schools
 'icts-winter-biophysics':      (4, 5),
 'icts-living-matter':          (4, 4),
 'icts-water':                  (4, 3),
 # 'icts-tidal' removed 4 Sep 2026 - its own page says "active researchers
 # (PhD, postdoctoral and faculty levels)" in a field unconnected to either of
 # his degrees. Not borderline once opened, so it came off the wall.

 # ---- workshops and short courses
 'blr-microscopy-16':           (4, 5),
 'ncbs-flow-cytometry':         (4, 5),
 'embo-indiabio-oct':           (4, 4),
 'ncbs-ciff-microscopy':        (3, 4),
 'ncbs-collab-projects':        (3, 3),
 'zebrafish-sathyabama':        (2, 4),
 'invitro-cancer-sathyabama':   (2, 4),

 # ---- online courses
 'swayam-nptel':                (4, 4),
 'bluedot-agi-strategy':        (3, 5),   # no CV asked for, and it ends in a certificate
 'bluedot-technical-ai-safety': (3, 5),
 'openwho':                     (3, 3),
 'bluedot-future-of-ai':        (2, 2),   # two hours. Honest about what that buys

 # ---- membership
 'rsna-member-in-training':     (4, 2),   # a line on a CV, not an education

 # ---- communities and open research
 'cohere-labs-community':       (4, 5),
 'ml-collective':               (2, 5),   # the mirror of RSNA, and the point of two axes

 # ---- peer review
 'prereview':                   (3, 5),

 # ---- citizen science: no mark left, and the page says so
 'zooniverse':                  (1, 3),
 'foldit':                      (1, 3),

 # ---- grant
 'emergent-ventures-india':     (5, 3),

 # ---- roles
 'sgb-mediators':               (3, 4),
 'sgb-externship':              (3, 4),
 'sgb-internship':              (3, 3),

 # ---- conferences
 'ncbs-spatialomics':           (4, 4),
 'ncbs-manotsava':              (4, 4),
 'wcmsr':                       (3, 5),   # low name recognition, highest learning-per-rupee here
 'cgtcon-2026':                 (3, 3),

 # ---- talks
 'ncbs-annual-talks-2027':      (4, 4),
 'sgb-quantum':                 (2, 3),
 'iisc-spicmacay':              (2, 1),   # a concert. Rated honestly

 # ---- ambassadorships, terms unread
 'github-campus-experts':       (4, 3),
 'msft-student-ambassador':     (3, 2),

 # ---- certification: a real credential, and almost nobody his age holds one
 'nida-gcp':                    (4, 4),
 'iscb-student-member':         (3, 3),   # a real society, but membership alone teaches little
 'iiser-pune-sspc':             (4, 5),   # a real summer in a real lab - if the eligibility holds

 # ---- publishing: the most durable mark available to him, and the cheapest
 'ijms':                        (3, 5),   # a student journal; the SKILL is what scores
 'cureus':                      (3, 4),   # real, peer-reviewed, and it costs money

 # ---- mentorship: the output is a decision, not a certificate
 'eighty-thousand-hours-advising': (2, 4),

 # ---- talks
 'iisc-open-day':               (3, 3),
}
