# -*- coding: utf-8 -*-
"""MY judgement of each bill, kept deliberately apart from the facts.

Added 3 September 2026, when he asked for "the ones that are much more usefull
either by knowledge importance or the prestige ones on top".

Two numbers per bill, 1 to 5:

  prestige  - how much the NAME carries. Whether saying you did it means
              anything to a medical school, a lab, or a hiring panel. RSNA,
              MICCAI, NeurIPS, ICMR, NASA, IIT Bombay and the Tata Group carry
              weight; a college fest hackathon does not, however good it is.

  learning  - how much HE would actually learn that matters for the path he is
              on: medicine, then research, then AI. Real clinical data scores
              high even with no prize; a big-money hackathon for a generic app
              scores low even though it pays.

They are separate on purpose. The SBI scholarship is prestige 4 and learning 1 -
it is money, not education. DALPHIN is prestige 2 and learning 4 - nobody has
heard of it and it will teach him more than most things here.

THIS FILE IS OPINION AND THE PAGE SAYS SO. It lives in its own file so that no
future session confuses it with `bills_*.py`, where every value has to be
something a source literally printed. He is meant to disagree with these.
"""

# id -> (prestige, learning)
RANK = {
    # ---- medicine and biology
    'dat-parkinsons':            (4, 5),
    'rsna-knee':                 (5, 5),
    'autopet-v':                 (4, 4),
    'icmr-sts':                  (5, 5),
    'amia-public-2026':          (4, 3),
    'pharmaorbit':               (1, 2),
    'dream-cache':               (5, 4),
    'dream-q':                   (4, 3),
    'dream-digital-pen':         (4, 4),
    'virtual-embryo':            (5, 5),
    'snomed-ct':                 (4, 5),
    'brain-to-text':             (4, 5),
    'falcon-neural':             (3, 4),
    'eeg-saad':                  (4, 4),
    'clip2-cadenza':             (3, 4),
    'tianchi-phenotype':         (3, 5),
    'clear-ec':                  (3, 4),
    'rare26':                    (4, 4),
    'topaneu-26':                (4, 4),
    'atm26':                     (4, 4),
    'selma3d-2026':              (3, 3),
    'surgvu-2026':               (4, 4),
    'chimera-agent':             (4, 5),
    'lunovo26':                  (3, 4),
    'dalphin':                   (2, 4),
    'beetle':                    (2, 4),
    'panther':                   (3, 3),
    'toothfairy3':               (3, 2),
    'dengai':                    (2, 4),
    'flu-shot':                  (2, 4),
    'zindi-climate-health':      (3, 5),
    'hack2heal':                 (1, 2),
    'sbi-asha-medical':          (4, 1),
    'virtual-cell':              (5, 5),
    'biohub-cells':              (5, 4),
    'univabio':                  (2, 4),

    # ---- research, AI and machine learning
    'arc-paper':                 (4, 4),
    'aimo-interp':               (4, 4),
    'csir-societal':             (4, 2),
    'hyperspectral-tracking':    (3, 3),
    'arc-whitebox':              (4, 4),
    'arc-agi-3':                 (5, 4),
    'arc-agi-2':                 (5, 4),
    'kaggriculture':             (3, 3),
    'ptcg':                      (4, 3),
    'playground-ev':             (2, 4),
    'kaggle-getting-started':    (1, 4),
    'road-barbados-handwriting': (3, 4),
    'dr-docbench':               (4, 4),
    'perception-test':           (5, 4),
    'lost-in-transcription':     (3, 4),
    'whats-up-docs':             (1, 3),
    'quantiphy':                 (5, 4),
    'learn2design':              (4, 4),
    'fair-universe':             (5, 5),
    'prc-taxi-out':              (4, 4),
    'zindi-bias-bounty':         (3, 4),
    'zindi-drought':             (3, 3),
    'nebius-nvidia':             (4, 4),
    'opencv-2026':               (4, 4),
    'amd-lablab-academy':        (3, 4),
    'assemblyai-voice':          (3, 3),
    'agentic-graphrag':          (3, 4),
    'crunchdao-structural-break':(3, 4),
    'numerai':                   (3, 3),
    'zindi-briisp':              (1, 3),
    'qiskit-fall':               (3, 3),
    'dream-q-placeholder':       (0, 0),  # removed below by the coverage assert

    # ---- build, hackathons, general
    'amazon-bss':                (4, 3),
    'ml-empower-3':              (2, 3),
    'next-byte-v4':              (1, 2),
    'nextgen-blr':               (1, 2),
    'prom-fall':                 (1, 2),
    'global-mesh':               (1, 3),
    'gatewayhacks-2026':         (2, 2),
    'revenuecat-shipaton':       (3, 3),
    'gibc-v2':                   (2, 2),
    'agentic-cinema':            (2, 3),
    'agents-for-humans':         (2, 3),
    'ai-builders-2026':          (2, 3),
    'call-e':                    (2, 3),
    'wearedevelopers':           (2, 2),
    'nextstep-hacks':            (1, 2),
    'hyperbloom-sept':           (1, 2),
    'prom-virgo':                (1, 2),
    'compsphere-12':             (1, 2),
    'galuxium-nexus':            (1, 2),
    'ai-content-engine':         (1, 2),
    'rice-urban':                (3, 3),
    'muba-blockchain':           (1, 1),
    'code-kitchen':              (3, 2),
    'mlh-ghw-data':              (2, 3),
    'hackcbs-9':                 (3, 2),
    'hacknex-s2':                (1, 2),
    'innohacks-4':               (1, 2),
    'csh-social-impact':         (1, 2),
    'seize-da-flaq':             (1, 3),
    'slay-ctf':                  (1, 4),
    'dogfood-72':                (2, 2),
    'quhack':                    (2, 2),
    'hack2ignite':               (1, 2),
    'global-innovation-hack':    (1, 2),
    'black-box-protocol':        (1, 2),
    'powernext-ai':              (2, 2),
    'void-hacks-8':              (1, 2),
    'semicon-sarcathon':         (5, 3),
    'prysm-26':                  (1, 1),
    'paradox-hackathon':         (1, 1),
    'tech-horizon-2':            (2, 2),

    # ---- India, government, prestige names, money
    'innovation-for-her':        (4, 3),
    'digital-shram':             (3, 2),
    'avinya-27':                 (3, 2),
    'sih-2026':                  (5, 3),
    'tata-imagination':          (5, 3),
    'asian-paints-alchemy':      (3, 2),
    'et-ai-agentic':             (4, 3),
    'pareidolia':                (1, 2),
    'iitm-polymer':              (4, 3),
    'yuva-yodha':                (5, 3),
    'nasa-space-apps':           (5, 3),
    'xprize-quantum':            (5, 2),
    'reliance-foundation-ug':    (4, 1),
    # ---- added by the 10 September 2026 sweep
    'gopwnit-ctf':               (1, 4),   # nobody has heard of it; you would learn real security
    'snapdragon-ai-lab':         (4, 3),   # Qualcomm's name is the whole prestige here
    'quantumxpo':                (1, 4),   # a college expo, and the cheapest look at quantum you will get
    'codexnovas-innovathon':     (1, 3),   # private company, no prize stated - practice, not a credential
    'namma-space':               (4, 4),   # IIT Bombay Techfest, and genuinely hard computer vision
    'mhtechin-innovation':       (2, 3),   # real money if it is real; the company is unknown
    'ies-student-innovation':    (1, 2),   # an idea and a pitch; the headline prize needs verifying
    'krunch-analytics':          (4, 3),   # IIT Madras carries it; business case, not science
    'math-o-stellar':            (2, 2),   # a college fest maths contest, and it is fine that it is
    'neural-interfaces-2026':    (3, 5),
    'bharat-innovation-2':       (2, 3),
    'hacksprint-devpost':        (1, 3),
    'techcommons-v2':            (1, 2),
    'amplifai':                  (4, 5),
    'flare-recist-3d':           (4, 5),
    'uusic-continuous':          (3, 4),
    'slm-medical-advice':        (2, 4),
    'bioml-local-rank':          (3, 4),
    'bioml-global-align':        (3, 4),
    'fusion-equilibrium':        (5, 4),
}

RANK.pop('dream-q-placeholder', None)
