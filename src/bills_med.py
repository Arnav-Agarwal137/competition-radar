# -*- coding: utf-8 -*-
"""Medicine and research bills.

Every field here is either what a source literally printed, or the words "Not
stated". Nothing is inferred. The first pass carried lines like "startup
challenges commonly end in an in-person pitch" - a guess wearing the costume of
a fact, and exactly the thing that costs a week.

conf: 'verified' = I opened the competition's own page and read these fields
      'listing'  = transcribed from a listing; fields it did not print say so
difficulty: 1-5, my judgement of how hard it is FOR HIM, not in the abstract
view: my recommendation on actually proceeding. Labelled as mine on the page.
"""

BILLS = [

dict(id='dat-parkinsons', name='DaT Parkinson&rsquo;s Challenge',
  host='French Society of Nuclear Medicine (SFMN)', platform='DrivenData',
  url='https://www.drivendata.org/competitions/311/dat-parkinsons-challenge/',
  domain='med', kind='Medical imaging competition',
  blurb='Classify dopamine transporter (DaT) scans as normal or abnormal. Real nuclear-medicine '
        'imaging, run by an actual medical society.',
  submit='A computer vision model as code, in a ZIP archive, plus documentation on their template.',
  fmt='remote', location='Entirely online',
  travel='None to compete. WINNERS are invited to an in-person ceremony in France, hosted by the SFMN.',
  fee='None. The rules say NO PURCHASE NECESSARY TO ENTER OR WIN.',
  prize='&euro;25,000 total &mdash; &euro;12,500 first, &euro;7,500 second, &euro;5,000 third',
  team='Natural persons only. Legal entities cannot participate.',
  eligible='Natural persons aged 18 or over, resident in eligible territories. You are 18, so you qualify.',
  effort='Heavy, but a well-defined binary classification task.',
  difficulty=4,
  deadline_text='16 September 2026, 23:59 UTC', deadline='2026-09-16', precision='exact',
  extra='DaT scans image the dopamine system; reduced uptake is the imaging signature of Parkinsonian syndromes.',
  why='Nuclear medicine imaging, judged by a medical society, free, and you are exactly old enough. '
      'The closest thing on this wall to the career you are walking into.',
  view='Thirteen days is not enough to win this from a standing start and I will not pretend '
       'otherwise. It is enough to download the data, look at real DaT scans, and submit something. '
       'Do that. You will have handled clinical imaging before your first anatomy viva, and the '
       'dopamine pathway is on your syllabus anyway.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#f1f7f4', ink='#0b5c46', rule='#0b5c46', treatment='t-clinic'),
  tags=['nuclear medicine','imaging','free','18+']),

dict(id='rsna-knee', name='RSNA Knee Abnormality Detection',
  host='Radiological Society of North America', platform='Kaggle',
  url='https://www.kaggle.com/competitions/rsna-knee-abnormality-detection',
  domain='med', kind='Research competition',
  blurb='Detect knee abnormalities from multimodal medical imaging, judged against a held-out set.',
  submit='A code notebook that Kaggle runs against hidden test data.',
  fmt='remote', location='Entirely online', travel='None stated at any stage.',
  fee='Free', prize='$77,000', team='Solo or team',
  eligible='Open. A Kaggle account is required. No student or country restriction stated.',
  effort='Heavy. Medical imaging is its own craft and the field is strong.',
  difficulty=5,
  deadline_text='about 2 months to go', deadline='2026-11-03', precision='derived',
  extra='2,962 teams had entered when the listing was read.',
  why='Radiology plus machine learning is the exact overlap almost nobody at your stage occupies.',
  view='Do not try to win this. Enter it to read other people&rsquo;s public notebooks, which are '
       'the best free radiology-AI course in existence and exist whether or not you submit. Two '
       'months is real runway for reading.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#f6f3fa', ink='#3b2f7a', rule='#3b2f7a', treatment='t-bulletin'),
  tags=['radiology','deep learning','imaging']),

dict(id='autopet-v', name='autoPET V',
  host='MICCAI 2026 challenge community', platform='Grand Challenge',
  url='https://autopet-v.grand-challenge.org/',
  domain='med', kind='Academic medical imaging challenge',
  blurb='Interactive, clinician-in-the-loop lesion segmentation in whole-body PET/CT. Your algorithm '
        'makes a first segmentation, then improves it in response to corrective scribbles marking '
        'false positives and false negatives.',
  submit='An algorithm packaged as a container, per the official repository.',
  fmt='remote', location='Online. Hosted at MICCAI 2026.',
  travel='Not stated on the challenge page.',
  fee='Not stated on the challenge page', prize='<b>&euro;6,000 in total</b>, read off the challenge&rsquo;s own Prizes page: two categories, Simulated Interaction and Clinician-Driven Interaction, each paying <b>&euro;1,500 / &euro;1,000 / &euro;500</b> for first, second and third. Ties share the combined pot for the positions involved. One condition from the Rules page: the organisers&rsquo; own baselines hold their leaderboard positions but are <b>not eligible for prize money</b>, and a resubmitted baseline only qualifies if it comes with a genuine data-centric approach.',
  team='Not stated on the challenge page', eligible='No restriction by age, country or background is printed. The Rules page states exactly one bar, and it is the usual one: <b>&ldquo;Researchers affiliated with the institutes of the organizers are not allowed to participate.&rdquo;</b> Nothing there excludes you.',
  effort='Heavy. Containerised submission and 3D medical volumes.',
  difficulty=5,
  deadline_text='Accepting submissions until 25 September 2026 per the Grand Challenge listing. '
                'The challenge page itself prints no deadline.',
  deadline='2026-09-25', precision='listing',
  extra='Evaluated twice: simulated interaction for reproducibility, and real clinician-driven interaction.',
  why='PET/CT is the imaging you will meet in oncology, and clinician-in-the-loop is the honest '
      'shape of medical AI &mdash; the machine drafts, the doctor corrects.',
  view='Flagged as thin on purpose: its own page states almost nothing beyond the task. Read the '
       'task, keep the idea, and do not plan around it until you have opened the repository '
       'yourself. Worth knowing MICCAI exists more than worth entering this round.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#f3f8fb', ink='#14556e', rule='#14556e', treatment='t-clinic'),
  stretch=True, tags=['PET/CT','segmentation','MICCAI']),

dict(id='icmr-sts', name='ICMR Short Term Studentship',
  host='Indian Council of Medical Research', platform='icmr.gov.in',
  url='https://www.icmr.gov.in/short-term-studentship-sts',
  domain='med', kind='Research studentship, ANNUAL',
  blurb='A faculty-guided research project for 1st and 2nd year MBBS and BDS students, with a '
        'stipend and an ICMR certificate on completion.',
  submit='A research proposal with a faculty guide, through your medical college.',
  fmt='remote', location='At your own medical college', travel='None.',
  fee='Free', prize='&#8377;60,000 stipend', team='Individual',
  eligible='1st and 2nd Professional MBBS and BDS students ONLY. That will be you from next year.',
  effort='A summer project alongside coursework.',
  difficulty=2,
  deadline_text='CLOSED for 2026 &mdash; the deadline was 30 May 2026. The next window is expected '
                'around April to May 2027 by analogy with this year. That is an ESTIMATE, not a stated date.',
  deadline='', precision='recurring',
  extra='Results are announced two to three months after the deadline.',
  why='The entry that proves why this wall exists. It shut in May, it pays &#8377;60,000, and it is '
      'open to exactly the student you are about to become.',
  view='Do nothing now. Put "ICMR STS opens" in your reminders for 1 April 2027, and spend one '
       'evening in first year finding a faculty guide &mdash; the guide is the bottleneck, not the '
       'proposal. Almost everyone who misses this misses it for want of a supervisor.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#fbf5eb', ink='#8a4a12', rule='#8a4a12', treatment='t-gazette'),
  recurring=True, tags=['MBBS','annual','stipend','India']),

dict(id='amia-public-2026', name='AMIA Public Challenge 2026',
  host='American Medical Informatics Association', platform='Kaggle',
  url='https://www.kaggle.com/competitions/amia-public-challenge-2026',
  domain='med', kind='Medical informatics competition &mdash; CLOSED',
  blurb='A medical informatics prediction challenge run alongside the AMIA meeting.',
  submit='Predictions on Kaggle.',
  fmt='remote', location='Entirely online', travel='None stated.',
  fee='Free', prize='Kudos only. It awarded no points or medals.', team='Solo or team',
  eligible='Open.', effort='Medium.', difficulty=3,
  deadline_text='CLOSED. It ran 14 April to 15 June 2026 and is now in late-submission mode only.',
  deadline='2026-06-15', precision='exact',
  extra='830 entrants, 217 teams, 2,492 submissions.',
  why='On the wall as a correction, not an opportunity. The weekly harvester added this on '
      '3 September as though it were live. It had been shut for eleven weeks.',
  view='You cannot win this. It stays up because AMIA runs one most years, so the name is worth '
       'knowing, and because it is the honest record of a mistake this wall made about itself. '
       'Late-submission mode still lets you download the data and try the task with no clock on it.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#f2f0ed', ink='#5c5550', rule='#8c8378', treatment='t-letter'),
  tags=['informatics','closed','a correction']),

dict(id='virtual-cell', name='Arc Institute Virtual Cell Challenge 2026',
  host='Arc Institute', platform='virtualcellchallenge.org',
  url='https://virtualcellchallenge.org',
  domain='research', kind='Grand challenge',
  blurb='Predict how six unseen human cell lines respond to CRISPRi gene knockdowns, with no '
        'training data from any of them. Zero-shot.',
  submit='Predicted expression profiles, scored by Arc&rsquo;s open cell-eval tool.',
  fmt='remote', location='Entirely online', travel='None.',
  fee='Free', prize='$100,000 grand prize, $50,000 second, $25,000 third',
  team='Individuals, labs or companies. No affiliation needed.',
  eligible='Anyone. That clause is the one that matters for you.',
  effort='Heavy. The final test set drops 22 October 2026.',
  difficulty=5,
  deadline_text='5 November 2026, 23:59 UTC (05:29 IST on 6 November)',
  deadline='2026-11-05', precision='exact',
  extra='2025 round: over 5,000 registrants from 114 countries, but only around 300 made a final submission.',
  why='Already on your board as T-008, and the 54-unit guide for it is on your phone.',
  view='Register today even if you never submit &mdash; free, minutes, and an unregistered '
       'competition is one you cannot enter on a whim in October. Then give it two weekends: '
       'environment and data first, the two baselines second. If weekend one is miserable rather '
       'than interesting, you have your answer cheaply.',
  conf='verified', checked='2026-09-02',
  theme=dict(paper='#edf3fb', ink='#1b4f8a', rule='#1b4f8a', treatment='t-bulletin'),
  stretch=True, tags=['biology','zero-shot','on your board']),

dict(id='biohub-cells', name='Biohub &mdash; Cell Tracking During Development',
  host='Chan Zuckerberg Biohub', platform='Kaggle',
  url='https://www.kaggle.com/competitions/biohub-cell-tracking-during-development',
  domain='research', kind='Research competition',
  blurb='Detect and track individual zebrafish cells through 3D space and time as an embryo develops.',
  submit='A code notebook scored on held-out microscopy data.',
  fmt='remote', location='Entirely online', travel='None stated.',
  fee='Free', prize='$60,000', team='Solo or team',
  eligible='Open. A Kaggle account is required.',
  effort='Heavy. Tracking in 3D over time is genuinely hard.',
  difficulty=5,
  deadline_text='about a month to go', deadline='2026-10-03', precision='derived',
  extra='3,028 teams.',
  why='Developmental biology you already half-know, with the computation bolted on.',
  view='The biology is the part you have an edge in; the tracking is the part you do not. More '
       'winnable than the Virtual Cell, because the ground truth is visible &mdash; you can watch '
       'whether your tracks are right instead of trusting a metric.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#eff7f1', ink='#1f6b4a', rule='#1f6b4a', treatment='t-bulletin'),
  tags=['biology','microscopy','3D tracking']),

dict(id='arc-paper', name='ARC Prize 2026 &mdash; Paper Track',
  host='ARC Prize Foundation', platform='Kaggle',
  url='https://www.kaggle.com/competitions/arc-prize-2026-paper-track',
  domain='research', kind='Paper track',
  blurb='Write up a conceptual approach to the ARC Prize. Judged on the idea and the writing, not '
        'on a leaderboard score.',
  submit='A paper.',
  fmt='remote', location='Entirely online', travel='None stated.',
  fee='Free', prize='$450,000 across the track', team='Solo or team',
  eligible='Open.',
  effort='Medium. A thinking and writing task, not an engineering one.',
  difficulty=3,
  deadline_text='about 2 months to go', deadline='2026-11-03', precision='derived',
  extra='Only 168 teams, against 2,738 on ARC-AGI-3.',
  why='The only entry on this wall where the deliverable is an argument rather than a trained model.',
  view='The one I would actually push you towards. You write well, you have two months, and 168 '
       'teams against 2,738 says most people did not notice the track exists. You do not need to '
       'solve ARC to write something worth reading about why it is hard, and reading enough to '
       'write that is the best introduction to the field there is.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#f7f4ef', ink='#2f2b26', rule='#b4482f', treatment='t-letter'),
  tags=['writing','reasoning','uncrowded']),

dict(id='aimo-interp', name='AIMO Interpretability Challenge',
  host='AI Mathematical Olympiad', platform='Codabench',
  url='https://www.codabench.org/competitions/16180/',
  domain='research', kind='Interpretability challenge',
  blurb='Build a system that decides whether an AI model solved an olympiad problem robustly, or '
        'got the right answer for spurious reasons.',
  submit='A Codabench submission bundle conforming to the interface in their getting-started repository.',
  fmt='remote', location='Online. A competition workshop runs at NeurIPS 2026 on 11&ndash;12 December.',
  travel='None required to compete.',
  fee='Not stated', prize='$12,500 across both tracks', team='Not stated',
  eligible='Open to everyone &mdash; academic researchers, independent researchers and industry '
           'practitioners alike, in their own words.',
  effort='Medium to heavy, but conceptually unusual rather than compute-heavy.',
  difficulty=4,
  deadline_text='1 November 2026', deadline='2026-11-01', precision='exact',
  extra='Two tracks. Submissions go through Codabench, not Kaggle.',
  why='Interpretability asks whether a model is right for real reasons &mdash; the same question '
      'you will be asked about every diagnostic tool for the rest of your career.',
  view='Fifty-nine days and explicitly open to independent researchers. If the ARC Paper Track '
       'interests you, read this straight after: same instinct, that the reasoning matters more '
       'than the score. Smaller prize, far fewer entrants, more tractable.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#f4f1fa', ink='#4a2f7a', rule='#4a2f7a', treatment='t-bulletin'),
  tags=['interpretability','NeurIPS','open to all']),

dict(id='csir-societal', name='CSIR Societal Platform',
  host='Council of Scientific and Industrial Research', platform='MyGov Innovate India',
  url='https://innovateindia.mygov.in/csir-societal-platform-2024/',
  domain='research', kind='Open call for problems',
  blurb='Submit a real problem from society that science and technology could solve. You are not '
        'proposing the solution &mdash; you are naming the problem. Fourteen domains, healthcare among them.',
  submit='A problem statement in one of 14 domains, through the portal. Incomplete applications are '
         'discarded without comment.',
  fmt='remote', location='Online only', travel='None.',
  fee='Not stated', prize='Not stated. This is a standing platform, not a prize competition.',
  team='Not stated', eligible='Indian nationals residing in India only.',
  effort='Very light. One well-framed problem.',
  difficulty=1,
  deadline_text='16 February 2024 to 31 December 2026', deadline='2026-12-31', precision='exact',
  extra='Domains include agriculture, disaster management, energy, environment, healthcare and infrastructure.',
  why='The longest runway on the wall and the lowest effort on it.',
  view='Do this in an idle hour, not as a project. You are about to spend years watching healthcare '
       'problems at close range that nobody has written down. Write one down. There is no prize, '
       'and that is fine &mdash; a named problem in a CSIR portal is a thing you can point at, and '
       'it costs an evening.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#fdf7ea', ink='#6b4a12', rule='#6b4a12', treatment='t-gazette'),
  tags=['government','healthcare','one evening']),

dict(id='hyperspectral-tracking', name='Hyperspectral Object Tracking Challenge 2026',
  host='WHISPERS 2026 workshop community', platform='Kaggle',
  url='https://www.kaggle.com/competitions/hyperspectral-object-tracking-challenge-2026',
  domain='research', kind='Academic benchmark competition',
  blurb='Track objects through hyperspectral video &mdash; imagery with far more colour bands than '
        'a normal camera records.',
  submit='A <code>submission.csv</code> generated from a Kaggle Notebook, scored on a live '
         'leaderboard. The rules add two requirements: participants must upload model code to Kaggle '
         'and run it in a Kaggle Notebook, and <b>the ID sequence in the submission file must match '
         'the published specification</b> at kaggle.com/datasets/yuhan414/id-sequence.',
  fmt='remote', location='Entirely online',
  travel='None &mdash; it runs entirely on Kaggle.',
  fee='No fee is named anywhere in the Official Competition Rules. The only stated requirement to '
      'enter is a registered Kaggle.com account.',
  prize='$3,526. The Official Rules themselves commit to nothing specific &mdash; they say only that '
        '&ldquo;Prizes, if any, will be awarded to Participants with the best scores&rdquo;.',
  team='<b>Solo only.</b> Printed in the rules: &ldquo;The maximum team size is one member&rdquo;, and '
       '&ldquo;Each person may only participate with information from one competing team&rdquo;. '
       'Submissions may be made from one Kaggle account only; using more than one is disqualifying.',
  eligible='Printed in the Official Competition Rules. You must be a registered Kaggle.com account '
           'holder and <b>the older of 18 or the age of majority where you live</b> &mdash; you turn '
           'eligible on both counts in India. Residents of Crimea, the so-called DNR and LNR, Cuba, '
           'Iran and North Korea are excluded, as is anyone under US export controls or sanctions.',
  effort='Heavy. Real computer-vision research with meaningful compute needed.',
  difficulty=5,
  deadline_text='The listing printed a relative countdown rather than a date; read on 3 September 2026 as &ldquo;6 days to go&rdquo;, which puts the deadline at <b>9 September 2026</b>. That date has passed and this is CLOSED. Recorded as derived, not exact, because the source never printed the date itself.', deadline='2026-09-09', precision='derived',
  extra='812 entrants, 232 teams, 3,207 submissions.',
  why='On the wall corrected. The weekly harvester recorded this as "about 3 months to go, prize '
      'not stated, 41 teams". It is six days, $3,526, and 232 teams.',
  view='Too late to start, and I am saying so rather than letting you find out. The reason it stays '
       'up is that it runs annually against the WHISPERS workshop, so the useful move is to note '
       'the name and catch the 2027 edition in spring. That is what this wall is actually for.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#f0f4f8', ink='#2b4a63', rule='#2b4a63', treatment='t-chart'),
  tags=['computer vision','annual','too late this round']),


dict(id='pharmaorbit', name='PharmaOrbit 2026 &mdash; India&rsquo;s Biggest Pharma Quiz',
  host='PharmaOrbit', platform='Unstop',
  url='https://unstop.com/quiz/pharmaorbit-2026-indians-biggest-pharma-quiz-pharmaorbit-1735986',
  domain='med', kind='Online pharmacology quiz',
  blurb='Fifteen multiple-choice questions in ten minutes, with negative marking, on pharmaceutical '
        'knowledge. Individual entry, entirely online.',
  submit='An online quiz attempt. Nothing to build and nothing to write.',
  fmt='remote', location='Online', travel='None.',
  fee='FREE. The Unstop API returns isPaid false.',
  prize='<b>No cash at all.</b> Winner, first and second runner-up get Unstop goodies, a free .xyz '
        'domain, a Certificate of Excellence and a mention on the PharmaOrbit LinkedIn page. The '
        'top 299 get a free .xyz domain. <b>The top 30 are offered a medical writing internship</b>, '
        'and 30+ student ambassador places are offered. Every participant gets a national-level '
        'digital participation certificate.',
  team='Individual only &mdash; 1 to 1.',
  eligible='The listing addresses &ldquo;D.Pharm, B.Pharm, Pharm.D, M.Pharm, or are a pharmacy '
           'graduate <b>or aspirant</b>&rdquo;. <b>It does not name MBBS.</b> The eligibility block '
           'on the API is empty, so nothing is formally excluded, but this is written for pharmacy '
           'students and you are not one.',
  effort='Ten minutes. This is the lowest-effort bill on the entire wall.',
  difficulty=2,
  deadline_text='Registration runs 16 August to <b>30 September 2026</b>, read off the Unstop public '
                'API on 7 September 2026.',
  deadline='2026-09-30', precision='exact',
  extra='817 registered when read. Negative marking is stated on the listing, so guessing is '
        'punished.',
  why='It is the only medicine-adjacent thing open on Unstop, it costs ten minutes, and the reward '
      'that matters is not the podium &mdash; it is the <b>medical writing internship offered to the '
      'top 30</b>, which is a real first line on an empty page.',
  view='<b>Flagged, because it is written for pharmacy students and you are about to start MBBS.</b> '
       'I am not going to pretend that is a perfect fit. But nothing on the listing excludes you, the '
       'pharmacology overlaps a first-year MBBS syllabus heavily, it costs ten minutes, and the '
       'downside is losing a quiz nobody will ever know you entered. Read the eligibility line '
       'yourself before you register and decide &mdash; that is your call, not mine.',
  conf='listing', checked='2026-09-07',
  theme=dict(paper='#f0e6d2', ink='#6b4415', rule='#6b4415', treatment='t-ticket'),
  tags=['ten minutes','pharmacy not medicine','internship for top 30','flagged']),

dict(id='dream-cache', name='DREAM x CACHE Target 2035 Drug Discovery Challenge',
  host='DREAM Challenges with CACHE and Target 2035', platform='Synapse',
  url='https://www.synapse.org/Synapse:syn75349604/wiki/641044',
  domain='med', kind='Drug discovery machine learning challenge',
  blurb='Build DEL-ML models to discover hits &mdash; bioactive, drug-like molecules &mdash; for the '
        'kinase PGK2, using DNA-Encoded Library data. The second run of the Target 2035 DEL-ML '
        'challenge; the first one, on the protein WDR91, is written up on ChemRxiv.',
  submit='Printed in full on the Tasks and Submit tabs. Validation split: a .txt of <b>50 rows</b>, one '
         'Catalog ID per line, named Team_NAME_UNIQUEID.txt. Test split: a 3-column CSV &mdash; CatalogID, '
         'Sel_50 (a 0/1 flag marking exactly 50 diverse picks) and Score (a confidence for every compound '
         'in the split). Files are uploaded to your own Synapse project, which <b>must be made public or '
         'the submission is invalid</b>, and you must hold the Synapse &ldquo;Certified User&rdquo; badge '
         'to upload at all. <b>A separate written method report is required for each submission.</b> '
         'Sample baseline code, a conda environment and a worked deduplication notebook are all supplied.',
  fmt='remote', location='Online, on Synapse',
  travel='Not stated on the challenge pages.',
  fee='Free. The only gate is a Synapse account plus &ldquo;Synapse Certification&rdquo;, which the '
      'rules page describes as &ldquo;a brief quiz based on the Sage Bionetworks Terms of Service&rdquo;.',
  prize='NOT CASH &mdash; CO-AUTHORSHIP. Printed on the Incentives page: &ldquo;All participants '
        'whose workflow performs better than random selection in the Blind test phase and Active '
        'learning phase will be invited as co-authors on an article to be published in a scientific '
        'Journal.&rdquo; <b>But that is not the whole rule.</b> The Writeup tutorial adds a second, '
        'harder condition: &ldquo;To be considered for the Prospective phase and as co-authors in the '
        'overview paper you have to: Submit a separate writeup for each of your submissions.&rdquo; '
        '<b>A good score with no write-up earns nothing.</b> The top 5 groups of each step are '
        'additionally invited into a real prospective screening campaign; that phase is <b>not free</b> '
        '&mdash; entrants buy their own predicted compounds, at a price the pages do not state &mdash; '
        'though the CA$20,000 assay cost is waived, and compound costs are covered by the SGC for '
        'MAINFRAME members placing top 2. The prospective phase can be declined without losing the '
        'co-authorship, which is earned in the free September and October rounds.',
  team='Solo or team. The Submit tab says one Synapse project per team, shared with all members, and a '
       'team must be registered for the challenge separately from an individual. No size limit is printed.',
  eligible='No eligibility restriction is printed anywhere. Registration is open on Synapse and '
           '<b>229 people had registered</b> when the page was read on 7 September. Two account gates '
           'apply to everyone: the Synapse Certification quiz, and &mdash; Synapse&rsquo;s own words '
           '&mdash; &ldquo;If you are between 13 and 18, you must submit a Child Minor Addendum for '
           'access.&rdquo; Data access is separate again, through AIRCHECK, and is <b>auto-approved only '
           'for a university or academic email address</b>; anything else goes to manual review.',
  effort='Heavy in skill, <b>light in hardware</b>. It is cheminformatics on top of machine learning and '
         'the data format is its own discipline &mdash; but the file you actually train on is '
         '<b>7.5 million rows, not the 898 million of the full library</b>, because DEL sequencing only '
         'ever sees what stuck. An ordinary laptop is enough, and the organisers supply the environment '
         'file, the cleaning script and a worked notebook. The download quota is the real constraint: '
         '<b>ten dataset downloads per rolling 30 days</b>, across all challenge files combined.',
  difficulty=5,
  deadline_text='Registration opened 16 June 2026. Read off the challenge&rsquo;s own Timeline wiki, '
                'last modified 27 August 2026: the Blind test step was <b>&ldquo;extended for two '
                'extra weeks from Sept 15th to Sept 30th&rdquo;</b>; the Active learning step runs '
                '1&ndash;31 October; the Prospective phase runs 1 November to <b>15 December 2026</b>, '
                'submission limit 1. Write-ups are accepted 16 June to 31 October. All deadlines are '
                '23:59 UTC.',
  deadline='2026-12-15', precision='exact',
  extra='A Q&amp;A webinar was held 7 July 2026 and the recording is linked from the wiki. '
        'CORRECTED 7 September 2026: this wall previously showed 15 September as the deadline, taken '
        'from a summary page, and marked the prize &ldquo;not stated&rdquo;. Both were wrong &mdash; '
        'the Timeline and Incentives tabs had never been opened. '
        'CORRECTED AGAIN, later the same day, after the Tasks, Submit, Evaluation, Data, Hit Selection, '
        'Deduplicate and Writeup tabs were read as well: this card had claimed a baseline model would '
        'clear the co-authorship bar, which is <b>not printed anywhere</b> &mdash; it was an inference '
        'stated as fact. It had also said the submission format was &ldquo;not stated&rdquo; when the '
        'Tasks tab specifies it exactly, and it omitted the mandatory write-up entirely. '
        '<b>The deadline was re-confirmed as 30 September</b> against the Timeline tab: one page, last '
        'edited 15 June, still shows 15 September, but two independently updated pages both carry the '
        'extension. Scoring detail worth knowing: entries are ranked on the number of distinct chemical '
        '<i>series</i> first and raw hit count only as a tiebreak, so fifty near-identical molecules '
        'score worse than ten spread across three families.',
  why='DREAM is the challenge series closest to biomedical research proper, and the reward here is '
      'the one thing you actually lack: <b>a name on a published paper</b>. Not for winning &mdash; '
      'for beating random selection.',
  view='<b>This is now the most valuable bill on the wall for you, and it nearly got written off.</b> '
       'You have until 30 September for the blind test step and until 15 December for the whole thing, '
       'not the eight days this wall was telling you. You will not top the leaderboard against '
       'cheminformatics groups. You do not have to: the co-authorship bar is <i>better than random '
       'selection</i>, plus a write-up. <b>How reachable that bar is, honestly:</b> the organisers '
       'publish their own baseline &mdash; a LightGBM model on ECFP4 fingerprints &mdash; and it found '
       '5 hits across 3 chemical series in the top 50 of the validation split, but only <b>1 hit in the '
       'top 50 of the deciding test split</b>. With roughly 431 true hits in 400,000 compounds, 50 '
       'random picks would be expected to contain 0.05 hits and would contain even one about 5% of the '
       'time, so that single hit does clear random &mdash; but not by a landslide, and <b>the organisers '
       'have not published how &ldquo;better than random&rdquo; is actually adjudicated</b>. Treat the '
       'byline as a real prospect, not a formality. Your own cost is about <b>45 minutes of sign-ups</b> '
       'and two dates; that asymmetry is the whole argument. A byline in a journal at eighteen is worth '
       'more than every cash prize on this wall put together.',
  conf='verified', checked='2026-09-07',
  theme=dict(paper='#fbf2f2', ink='#4c2222', rule='#4c2222', treatment='t-clinic'),
  tags=['drug discovery','DREAM','cheminformatics','free']),

dict(id='dream-q', name='DREAM-Q: Target 2035 Quantum Challenge',
  host='DREAM Challenges', platform='Synapse',
  url='https://www.synapse.org/Synapse:syn75465972/wiki/641827',
  domain='quantum', kind='Quantum computing for drug discovery',
  blurb='Develop quantum or hybrid quantum-classical methods to predict hits for the target protein '
        'PGK2 from mass-spectrometry-derived molecular data. A submission must have a quantum '
        'component that is essential to the approach, not decorative.',
  submit='Printed in full on the Submit tab. Each phase has a leaderboard stage and a final stage: '
         '<b>two leaderboard submissions of 30 molecules, then one final submission</b> per phase. '
         'The Phase 1 final needs three things &mdash; a prediction file giving your top 30 hits and a '
         'ranking of all ~300 held-out ASMS compounds; a <b>method write-up</b> stating the modelling '
         'workflow, the role of the quantum component and <b>why that component is necessary</b>; and '
         'reproducibility details (frameworks, simulator settings, preprocessing). Phase 2 is the same '
         'over 250 compounds but run on real hardware, and additionally wants the device name, job IDs, '
         'qubit count and layout, circuit depth, shot count, transpiler and error-mitigation settings. '
         '<b>Every template and submission link on that tab is still a placeholder reading &ldquo;TO BE '
         'SHARED&rdquo;</b>, so the exact file formats are not published yet.',
  fmt='remote', location='Online, on Synapse',
  travel='None &mdash; the challenge runs entirely on Synapse.',
  fee='Free, beyond a Synapse account. For Phase 2 hardware the page names the <b>IBM Open Plan</b>, '
      'which is free, and says select participants may be invited to apply for additional time on IBM '
      'Quantum computers.',
  prize='Not stated on the pages read.',
  team='Solo or team. The Submit tab says one Synapse project per team, shared with every member, and '
       'a team must be <b>registered for the challenge separately</b> from an individual. No size limit '
       'is printed. There were <b>18 registered participants</b> when the page was read on 7 September '
       '2026 &mdash; the smallest field of anything on this wall.',
  eligible='No restriction by age, country or affiliation is printed. The Terms and Conditions tab sets '
           'out what is actually required: you must be a <b>registered Synapse user</b>, and to upload '
           'anything you must also be <b>Synapse Certified</b>, which it describes as passing &ldquo;a '
           'brief quiz based on the Sage Bionetworks Terms of Service&rdquo;. Two conditions bind you '
           'afterwards: challenge data may be used <b>only</b> for this challenge &mdash; not for '
           'unrelated research or anything commercial &mdash; and an <b>embargo</b> forbids reporting '
           'overall challenge results until organisers and participants have jointly published the '
           'overview paper. Phase 1 is explicitly open to teams with NO access to quantum hardware '
           '&mdash; simulators are allowed &mdash; and the top Phase 1 teams are given quantum '
           'resources for Phase 2.',
  effort='Heavy, and in a field you have not touched.',
  difficulty=5,
  deadline_text='Read off the challenge&rsquo;s own Timeline wiki: announced 12 July 2026; training '
                'data released and <b>Phase 1 opens 25 September 2026</b>; <b>Phase 1 submissions '
                'close 27 November 2026</b>; quantum resource decisions 7 December; Phase 2 runs 15 '
                'December 2026 to <b>28 February 2027</b>. All deadlines 23:59 UTC. The site prints '
                'its own caveat: &ldquo;This challenge site is currently being updated. Dates &hellip; '
                'may continue to change.&rdquo;',
  deadline='2027-02-28', precision='exact',
  extra='A webinar is scheduled for <b>17 September 2026, 12pm EST</b>; the page says the link goes '
        'to registered participants only. Phase 1 may be done entirely on simulators using the '
        'DREAM-CACHE DEL-ML training data as a proxy before the real ASMS data lands on 25 September. '
        'CORRECTED 7 September 2026: this wall previously said &ldquo;no closing date is printed on '
        'either page&rdquo;. There is a Timeline tab, and it prints five of them. '
        'CORRECTED AGAIN the same day, by a sweep of every card for this exact fault: <b>this wiki has '
        'eleven tabs</b> and only two had ever been opened, so what you submit, who may enter and the '
        'team rules were all recorded here as &ldquo;not stated&rdquo; while the Submit and Terms and '
        'Conditions tabs stated them plainly. <b>Only the prize is genuinely unstated</b> &mdash; this '
        'challenge has no incentives page at all, which is not the same thing as one I failed to read.',
  why='Phase 1 needing no quantum hardware is the unusual part &mdash; it is a rare door into '
      'quantum that does not start with owning a quantum computer. Eighteen entrants is the other.',
  view='This is a stretch entry and I am labelling it as one. But the numbers changed when the '
       'timeline was actually read: <b>eighteen registered participants</b>, Phase 1 not even open '
       'until 25 September, and simulators allowed. If you are ever going to look at quantum, this is '
       'the cheapest look you will get. Read the wiki once. If the maths is opaque, leave it &mdash; '
       'there is no shame in a bill you looked at and put down.',
  conf='verified', checked='2026-09-07',
  theme=dict(paper='#effbf3', ink='#1b4c29', rule='#1b4c29', treatment='t-stencil'),
  tags=['quantum','drug discovery','stretch','no hardware needed']),

dict(id='dream-digital-pen', name='The Digital Pen Feature Extraction Challenge',
  host='DREAM Challenges', platform='Synapse',
  url='https://www.synapse.org/Synapse:syn68634259/wiki/633407',
  domain='med', kind='Cognitive assessment challenge',
  blurb='Develop open-source methods to better contextualise pen-and-paper cognitive assessments, '
        'centred on the Digital Clock Drawing Test, and evaluate how well algorithms predict '
        'cognitive domains and risk factors from it.',
  submit='Not stated. The challenge has not launched yet.',
  fmt='remote', location='Online, on Synapse',
  travel='Not stated.', fee='Not stated', prize='Not stated', team='Not stated',
  eligible='Not stated. A Pre-Register button is live on the Synapse page.',
  effort='Not knowable yet &mdash; the data has not been described.',
  difficulty=3,
  deadline_text='<b>&ldquo;Coming in 2026.&rdquo;</b> No date, and the wording on the Synapse page '
                'has softened since 3 September, when the summary page said &ldquo;Launching Fall '
                '2026&rdquo;. Pre-registration is open now and is still the only thing to do. '
                'Re-read 7 September 2026: still not launched.',
  deadline='', precision='none',
  extra='The clock-drawing test is a bedside screen for cognitive impairment &mdash; you will be '
        'asked to administer one in your own clinical years.',
  why='THIS IS THE ONE TO PRE-REGISTER FOR. It has not started. Registering now means you hear the '
      'launch on day one instead of six days before it closes, which is the exact wound this wall '
      'exists to stop reopening.',
  view='Do this today. It costs one form. A challenge you enter on day one is a completely different '
       'proposition from one you find in its last week, and this is a clinical test you will '
       'personally be trained to administer.',
  conf='verified', checked='2026-09-07',
  theme=dict(paper='#f5ecfb', ink='#35134c', rule='#35134c', treatment='t-letter'),
  tags=['cognition','pre-register','not launched yet','free']),

dict(id='virtual-embryo', name='Virtual Embryo Challenge &mdash; Mouse Embryo Development',
  host='Laude Institute, at NeurIPS 2026', platform='virtualembryo.ai',
  url='https://virtualembryo.ai/challenge',
  domain='med', kind='Computational biology competition',
  blurb='Predict how life takes shape, across three tasks: forecast gene-expression distributions at '
        'future developmental stages; predict future gene expression AND 3D spatial location '
        'together across molecular, cellular and tissue scales; and predict how genetic knockouts '
        'change embryonic development.',
  submit='Models submitted through the portal and scored against hidden test sets. Unlimited format '
         'checks, no biological feedback before you designate up to two official test submissions '
         'per task.',
  fmt='remote', location='Online. Winners announced at NeurIPS 2026.',
  travel='Not stated for competing. $30,000 of the pot is TRAVEL AWARDS &mdash; 15 to 20 '
         'early-career grants.',
  fee='Not stated on the challenge page',
  prize='$54,000 in winner prizes &mdash; $27,000 per track, split $8,000 first, $5,000 &times; 2 '
        'second, $3,000 &times; 3 third. Plus $30,000 in travel awards and a $20,000 community '
        'contribution award paying up to 100 contributors $200 each.',
  team='Two tracks scored on the same metrics and the same hidden test sets: a <b>Human Team</b> track and an <b>Agent Team</b> track. No size limit is printed for either.',
  eligible='No eligibility restriction is printed. The part worth knowing is a route in that does not require winning anything: a <b>$20,000 Community Contribution Award</b>, paid as <b>$200 each to as many as 100 contributors</b> for tutorials, tools and documentation. A hundred separate ways to have taken part in a NeurIPS competition track without topping a leaderboard.',
  effort='Heavy. Single-cell genomics on top of machine learning.',
  difficulty=5,
  deadline_text='Portal opened 10 August 2026, starter kit 15 August. Test phase begins 20 October, '
                'test leaderboard 2 December, final submissions due 11 December 2026.',
  deadline='2026-12-11', precision='exact',
  extra='This is the same problem family as the Arc Virtual Cell Challenge already on this wall, run '
        'by different people on mouse embryos rather than cell perturbation.',
  why='Three months of runway, a $20,000 pot that pays ordinary contributors $200 each, and a '
      'subject that is literally developmental biology. Almost nothing else here pays you for '
      'turning up.',
  view='The community contribution award is the realistic target and it is a genuinely good one: '
       '$200 for a useful contribution, up to 100 people. Aim at that, read the starter kit, and '
       'treat the leaderboard as optional. You have until December, which is real time.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#fbf9e9', ink='#4c440b', rule='#4c440b', treatment='t-riso'),
  tags=['developmental biology','NeurIPS','pays contributors','long runway']),

dict(id='snomed-ct', name='SNOMED CT Entity Linking Benchmark',
  host='DrivenData with SNOMED International', platform='DrivenData',
  url='https://www.drivendata.org/benchmarks/310/benchmark-snomed-ct/',
  domain='med', kind='Clinical NLP benchmark',
  blurb='Find the spans of text in real de-identified doctors&rsquo; notes that name a clinical '
        'concept, and link each one to the right concept in the SNOMED Clinical Taxonomy. The data '
        'is described as the largest publicly available set of labelled clinical notes.',
  submit='Code as a zip archive with model files and prediction logic, run in a container. The model '
         'description is written separately on the platform.',
  fmt='remote', location='Entirely online',
  travel='None stated at any stage.',
  fee='Not stated', prize='No prize. It is a benchmark, not a prize competition.',
  team='One unique DrivenData account per person. Using more than one account gets you removed.',
  eligible='Open to all participants subject to applicable laws. You must comply with your '
           'employer&rsquo;s policies and hold no conflicting legal obligations.',
  effort='Moderate to heavy. The NLP is standard; the medical vocabulary is the hard part, and it is '
         'the part you actually have.',
  difficulty=3,
  deadline_text='Open, with no end date stated. Permanently available.',
  deadline='', precision='none',
  extra='SNOMED CT is the clinical terminology the NHS and many Indian hospital systems code to. '
        'Learning it is directly useful in a hospital, not only in a competition.',
  why='The single most clinical thing on any platform swept today. Real doctors&rsquo; notes, real '
      'terminology, no deadline, no prize to lose. Your medical vocabulary is the edge here, not a '
      'handicap.',
  view='Start here if you start anywhere. No deadline means no pressure, the task rewards knowing '
       'what a clinical phrase MEANS, and by the time you are on the wards you will read SNOMED '
       'codes the way you read a drug chart. This is the best fit-to-effort ratio on the wall.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#e5f8fb', ink='#22454c', rule='#22454c', treatment='t-clinic'),
  tags=['clinical NLP','SNOMED','no deadline','best fit']),

dict(id='brain-to-text', name='Brain-to-Text Benchmark &rsquo;24',
  host='Brain-to-Text 2024 organisers', platform='EvalAI',
  url='https://eval.ai/web/challenges/challenge-page/2099/overview',
  domain='med', kind='Neural decoding benchmark',
  blurb='Decode attempted speech from neural activity recorded in a person with paralysis. You are '
        'given held-out sentences of neural data and must produce the transcription; performance is '
        'word error rate over 1,200 sentences.',
  submit='A 1,200-line .txt file, one decoded sentence per line, in the order given by the '
         'competition hold-out files.',
  fmt='remote', location='Entirely online',
  travel='None stated at any stage.',
  fee='Not stated', prize='Not stated. The 2024 round has been won and the benchmark now runs open.',
  team='Not stated on the challenge page',
  eligible='Not stated on the challenge page. The data is released under CC0 1.0 public domain.',
  effort='Heavy. Sequence modelling on neural time series.',
  difficulty=5,
  deadline_text='The 2024 round officially ended 1 June 2024 and was won. EvalAI lists the benchmark '
                'as open until 13 January 2027 and the page says it is &ldquo;kept open indefinitely '
                'to support further research&rdquo;.',
  deadline='2027-01-13', precision='exact',
  extra='The winning entry cut word error rate from 9.76% to 5.81% on the PyTorch baseline.',
  why='Brain-computer interfaces are neurology and engineering at once, and this is the public '
      'benchmark the field actually measures itself against.',
  view='You will not beat 5.81%. That is not the reason to open it. The data is CC0 and the baseline '
       'is PyTorch, so this is a free, permanent, real neural dataset to learn on with a scoreboard '
       'attached. Sixteen months of runway means it can sit until you want it.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#fbe2f0', ink='#632346', rule='#632346', treatment='t-bulletin'),
  tags=['neuroscience','BCI','open data','long runway']),

dict(id='falcon-neural', name='FALCON &mdash; Few-shot Algorithms for Consistent Neural Decoding',
  host='FALCON benchmark team', platform='EvalAI',
  url='https://eval.ai/web/challenges/challenge-page/2319/overview',
  domain='med', kind='Neural decoding benchmark',
  blurb='Neural decoders predict behaviour from brain activity, and they degrade as the recording '
        'drifts from day to day. FALCON measures methods that generalise or adapt to held-out days '
        'across several timescales &mdash; the failure mode that stops real implants working.',
  submit='Container-based submission. Instructions and examples are in the challenge GitHub repo.',
  fmt='remote', location='Entirely online',
  travel='None stated at any stage.',
  fee='Not stated', prize='Not stated', team='Not stated',
  eligible='Not stated. Datasets and challenge are licensed CC BY 4.0.',
  effort='Heavy, and it is Docker-based, which is a skill in itself.',
  difficulty=5,
  deadline_text='No closing date. EvalAI carries an end date of 2099, which is how that platform '
                'marks a permanently open benchmark.',
  deadline='', precision='none',
  why='The problem it names &mdash; a decoder that works on Monday and fails on Thursday &mdash; is '
      'the actual reason brain implants are hard, and almost nobody outside the field knows it.',
  view='Lower priority than Brain-to-Text: same field, more infrastructure to fight. Read its GitHub '
       'README for the idea, and come back to it after you have submitted to something simpler.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#f2f9f0', ink='#2b6319', rule='#2b6319', treatment='t-chart'),
  tags=['neuroscience','evergreen','Docker','stretch']),

dict(id='eeg-saad', name='ICASSP 2027 EEG-sAAD Challenge',
  host='ICASSP 2027 Grand Challenge', platform='Codabench',
  url='https://www.codabench.org/competitions/17856/',
  domain='med', kind='EEG signal processing grand challenge',
  blurb='Selective Auditory Attention Decoding from EEG: given brain recordings from someone '
        'listening to competing sounds, work out which speaker they are attending to. This is the '
        'core problem behind an attention-steered hearing aid.',
  submit='Not stated on the listing. Registration requires a team name, the full name of every team '
         'member including supervisors, their institutes, and at least one working email address.',
  fmt='remote', location='Online. ICASSP 2027 is held in Toronto in May 2027.',
  travel='Not stated for competing.',
  fee='Not stated', prize='Not stated. Codabench prints no reward field for it.',
  team='Not stated, but registration asks for a team name and a list of members.',
  eligible='Not stated on the listing. The Terms page was not opened.',
  effort='Heavy. EEG is noisy and the preprocessing is most of the work.',
  difficulty=4,
  deadline_text='Starts 8 September 2026. No closing date is printed on the Codabench listing; '
                'ICASSP 2027 itself is in May 2027.',
  deadline='', precision='none',
  extra='56 participants were registered when the listing was read.',
  why='It has not started yet, which on this wall is the best possible state for a competition to be '
      'in. EEG plus hearing is physiology you will be taught anyway.',
  view='Worth watching rather than committing to: no prize is printed and the deadline is not '
       'stated, so the terms need reading before you spend a weekend on it. But it starts in five '
       'days, so you are early for once.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#ededf9', ink='#130f63', rule='#130f63', treatment='t-clinic'),
  tags=['EEG','hearing','starts soon','ICASSP']),

dict(id='clip2-cadenza', name='CLIP2 &mdash; Cadenza Lyrics Intelligibility Prediction',
  host='Cadenza Project Team', platform='EvalAI',
  url='https://eval.ai/web/challenges/challenge-page/2703/overview',
  domain='med', kind='Audio and hearing-loss machine learning challenge',
  blurb='People with hearing loss struggle to make out lyrics in music. Build a metric that predicts, '
        'automatically, how intelligible the lyrics in a piece of music will be &mdash; the way '
        'speech-intelligibility metrics drove speech enhancement forward. CLIP2 adds AI-generated '
        'music across more genres, with reverberation and background noise.',
  submit='A CSV with exactly two columns in order: signal_ID (matching the FLAC filename) and '
         'intelligibility_score.',
  fmt='remote', location='Entirely online',
  travel='None stated at any stage.',
  fee='Not stated',
  prize='Not stated on the EvalAI page &mdash; it defers to the Cadenza challenge website for rules.',
  team='Not stated on the EvalAI page',
  eligible='Not stated on the EvalAI page',
  effort='Moderate. The submission format is a two-column CSV, which is about as gentle as an audio '
         'challenge gets.',
  difficulty=3,
  deadline_text='Open since 8 June 2026, closing 8 January 2027 at 23:59.',
  deadline='2027-01-08', precision='exact',
  extra='It follows CLIP1, which ran at ICASSP 2026.',
  why='Audiology is medicine, and this is the rare hearing-loss challenge where the output is one '
      'number per audio file rather than a trained container.',
  view='Four months of runway and a CSV submission. If you want one audio-domain entry to learn on, '
       'take this one rather than a speech challenge &mdash; the medical framing means the papers '
       'you read while doing it are papers about patients.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#f9efe9', ink='#633f2d', rule='#633f2d', treatment='t-ticket'),
  tags=['hearing loss','audio','long runway','gentle submission']),

dict(id='tianchi-phenotype', name='Phenotype Concept Recognition (Tianchi AI Large Model Competition)',
  host='Tianchi, Alibaba Cloud', platform='Tianchi',
  url='https://tianchi.aliyun.com/competition/entrance/532512',
  domain='med', kind='Biomedical NLP competition',
  blurb='Automatically find human phenotype descriptions in biomedical literature and normalise them '
        'to the Human Phenotype Ontology. The page names the real difficulties: long full-text '
        'articles, abbreviations, elliptical and negated phrasing, compound entities, and an '
        'ontology too large and too hierarchical for string matching to work.',
  submit='Not stated in the section read.',
  fmt='remote', location='Online',
  travel='Not stated.',
  fee='Not stated',
  prize='Not stated. The card shows &ldquo;Highlight&rdquo; where other Tianchi competitions show a '
        'bonus figure, so no cash amount is printed.',
  team='Not stated. 166 teams had entered when the page was read.',
  eligible='Not stated. THE PAGE IS IN CHINESE and a Tianchi/Alibaba account is required to register '
           '&mdash; only you can create that, I will not create accounts.',
  effort='Moderate for the NLP, high for the ontology work.',
  difficulty=4,
  deadline_text='Race time 20 August to 27 September 2026. The page showed &ldquo;Sign up remaining: '
                '24 days 13 hours&rdquo; when read on 3 September.',
  deadline='2026-09-27', precision='exact',
  extra='HPO is the standard vocabulary for describing clinical features in rare-disease diagnosis '
        'and gene discovery. Tagged Medical Health, NLP and LLM on Tianchi.',
  why='Rare-disease phenotyping is one of the few places where a doctor who can code is worth more '
      'than an engineer who cannot. This is that task, exactly.',
  view='The barrier is language and an account, not difficulty. If you are willing to work through '
       'a Chinese-language page with translation, this is a better subject match than most of the '
       'English-language AI bills here. Three weeks is thin but the task is well defined.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#e6f9f2', ink='#23634b', rule='#23634b', treatment='t-gazette'),
  tags=['rare disease','HPO','Chinese language','account needed']),

dict(id='clear-ec', name='CLEAR-EC &mdash; Corneal Endothelium Graft Quality',
  host='Grand Challenge community', platform='Grand Challenge',
  url='https://clear-ec.grand-challenge.org/',
  domain='med', kind='Ophthalmology imaging challenge',
  blurb='Given a specular microscopy image of the corneal endothelium, output the three metrics eye '
        'banks use to judge a graft: cell density, coefficient of variation and hexagonality.',
  submit='A containerised algorithm that reads specular microscopy images and outputs the three '
         'predicted metrics, run against a hidden test set on Grand Challenge.',
  fmt='remote', location='Online, on Grand Challenge',
  travel='Not stated. The winning model is to be piloted in eye banks; whether that involves you is '
         'not stated.',
  fee='Not stated on the challenge page', prize='Not stated on the challenge page',
  team='Not stated on the challenge page', eligible='Not stated on the challenge page',
  effort='Heavy. Containerised submission plus a regression task on microscopy images.',
  difficulty=4,
  deadline_text='Registration opened 15 July. Phase I (screening) submissions due 14 September 2026; '
                'Phase I evaluation complete 30 September. Up to three submissions in Phase I, two '
                'in Phase II.',
  deadline='2026-09-14', precision='exact',
  extra='Corneal endothelial cell density is the number that decides whether a donated cornea can be '
        'transplanted at all.',
  why='Ophthalmology, transplant medicine and image analysis in one task, and the metric being '
      'predicted is a real clinical go/no-go decision.',
  view='Eleven days and a container to build. Too tight to win from cold. Open it to see what a '
       'graft-quality decision actually looks like as data, then watch for the next edition.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#f7e3f9', ink='#731f7a', rule='#731f7a', treatment='t-clinic'),
  tags=['ophthalmology','transplant','container','tight']),

dict(id='rare26', name='RARE26 &mdash; Rare Early Cancer Detection in Endoscopy',
  host='MICCAI 2026 challenge community', platform='Grand Challenge',
  url='https://rare26.grand-challenge.org/',
  domain='med', kind='Academic medical imaging challenge',
  blurb='Detect rare, early-stage cancer in a low-prevalence clinical setting: early neoplastic '
        'change during surveillance of Barrett&rsquo;s oesophagus. The whole difficulty is that '
        'almost every image is normal.',
  submit='Algorithm submissions across a sanity-check phase, an open development phase and a closed '
         'testing phase.',
  fmt='remote', location='Online. Results presented at MICCAI 2026, 4&ndash;8 October, Abu Dhabi.',
  travel='Not stated for competing.',
  fee='Not stated on the challenge page',
  prize='&euro;1,000 first, &euro;500 second, &euro;250 third, &euro;150 fourth, &euro;100 fifth. '
        'All participants are invited as authors on the forthcoming journal publication.',
  team='Not stated on the challenge page', eligible='Not stated on the challenge page',
  effort='Heavy, and the class imbalance is the whole problem.',
  difficulty=5,
  deadline_text='Open Development Phase ran 1 May to 31 August 2026 and is OVER. Closed Testing '
                'Phase 1&ndash;7 September 2026. Report submissions due 14 September 2026, end of day, UTC.',
  deadline='2026-09-07', precision='exact',
  extra='Barrett&rsquo;s oesophagus is the pre-malignant change that follows chronic reflux; '
        'surveillance endoscopy exists to catch exactly what this challenge is detecting.',
  why='Authorship on the journal paper for ALL participants is unusual and is worth more to a first-'
      'year medical student than the &euro;1,000 top prize.',
  view='I am putting this up knowing you have missed it: the development phase closed on 31 August, '
       'four days before you read this. It is here so you know the series exists and register for '
       'RARE27 in the spring. This is precisely the miss this wall was built to stop, and I would '
       'rather show you the shape of it than quietly leave it off.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#f3f9e0', ink='#657a12', rule='#657a12', treatment='t-bulletin'),
  tags=['endoscopy','oncology','authorship for all','you have missed the window']),

dict(id='topaneu-26', name='TopAneu 2026 &mdash; Aneurysm Detection and Segmentation',
  host='MICCAI 2026 challenge community', platform='Grand Challenge',
  url='https://topaneu-26.grand-challenge.org/',
  domain='med', kind='Academic medical imaging challenge',
  blurb='Two tasks on cerebral vasculature: predict whether an aneurysm is present at each of 50-plus '
        'named vessel locations, and segment aneurysms at voxel level with vessel-specific labels.',
  submit='Docker containers uploaded to the Grand Challenge platform.',
  fmt='remote', location='Online. Challenge event at MICCAI on 27 September 2026.',
  travel='Not stated for competing. The top 5 teams are invited to present their methods at the '
         'event.',
  fee='Not stated on the challenge page', prize='<b>No cash. Co-authorship and a platform</b>, printed on the Participation page: the top five teams per task are &ldquo;invited to contribute to the challenge publication and to present their methods at the MICCAI challenge event&rdquo;. The authorship is capped &mdash; <b>a maximum of three co-authorships per submission</b> on the challenge paper, with further names added only on request and justification under the ICMJE authorship guidelines.',
  team='<b>One account per person, and at most one team.</b> Printed on the Participation page: &ldquo;A single account per participant. You can not submit from multiple grand-challenge accounts&rdquo;, and &ldquo;Each participant can join at most one team.&rdquo; Only one team member submits algorithms, and a team may not exceed one submission per final phase unless pre-approved for genuinely distinct algorithms. Members of the organisers&rsquo; own research groups may take part and appear on the leaderboard, but are <b>not eligible for awards</b>.',
  eligible='A VERIFIED Grand Challenge account is mandatory &mdash; your profile must be complete '
           'and verified before you can join. Abstract submission is mandatory for all participants.',
  effort='Heavy. 3D vascular imaging and a containerised pipeline.',
  difficulty=5,
  deadline_text='Training data 15 June and 31 July 2026, sanity check from 1 August. Submission '
                'window 10&ndash;21 September 2026. Deadline 21 September 2026.',
  deadline='2026-09-21', precision='exact',
  extra='A ruptured cerebral aneurysm is a subarachnoid haemorrhage &mdash; one of the emergencies '
        'you will be examined on.',
  why='Neuroradiology, and the mandatory abstract means every participant writes something citable.',
  view='Eighteen days, a Docker pipeline and 3D volumes: not winnable from a standing start. The '
       'verified-account requirement is worth doing NOW regardless, because it is a prerequisite for '
       'every Grand Challenge on this wall and it takes a day to clear.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#edf2f6', ink='#37597a', rule='#37597a', treatment='t-chart'),
  tags=['neuroradiology','Docker','verified account needed','MICCAI']),

dict(id='atm26', name='Airway Tree Modeling 26 (ATM26)',
  host='MICCAI 2026 challenge community', platform='Grand Challenge',
  url='https://atm26.grand-challenge.org/',
  domain='med', kind='Academic medical imaging challenge',
  blurb='Three tracks on the airway: binary airway segmentation from chest CT; branch-wise '
        'anatomical labelling of airway branches; and landmark recognition from bronchoscopy video '
        'for endobronchial intervention.',
  submit='Segmentation masks, anatomically labelled airway trees, or bronchoscope localisation '
         'estimates depending on track. The final test phase is submitted via a Google Form.',
  fmt='remote', location='Online. Associated with MICCAI 2026, 27 September to 1 October.',
  travel='Not stated.',
  fee='Not stated on the challenge page', prize='<b>No cash &mdash; authorship.</b> Printed on the challenge page: &ldquo;at most the three authors of the top five performing methods are qualified as authors in the final challenge paper.&rdquo; So a top-five finish converts into a byline for up to three people, and nothing below that does.',
  team='Not stated on the challenge page', eligible='No restriction by age, country or background is printed. The Registration page states the whole entry route in two steps: click <b>Join</b> on Grand Challenge to register your team, and <b>sign the Data Usage Agreement</b>. Nothing else is asked.',
  effort='Heavy. 3D CT segmentation.',
  difficulty=5,
  deadline_text='Registration opened 15 June 2026, sanity-check 15 July, validation 31 July, final '
                'test phase opened 20 August 2026. NO CLOSING DATE IS PRINTED &mdash; the page gives '
                'only the MICCAI dates of 27 September to 1 October 2026.',
  deadline='', precision='none',
  extra='Track 3 is bronchoscopy video, which is the procedure itself rather than an image of it.',
  why='Anatomical labelling of the bronchial tree is anatomy you are about to memorise anyway, done '
      'by machine.',
  view='The missing closing date is the problem here, not the difficulty. Do not plan around it '
       'until you have emailed the organisers or seen a date; a challenge whose deadline is not '
       'printed is one you can lose by assuming.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#f6eaed', ink='#7a2b3b', rule='#7a2b3b', treatment='t-clinic'),
  tags=['respiratory','CT','deadline not printed','MICCAI']),

dict(id='selma3d-2026', name='SELMA3D 2026 &mdash; Light-Sheet Microscopy Segmentation',
  host='MICCAI SiG-CompPath', platform='Grand Challenge',
  url='https://selma3d2026.grand-challenge.org/',
  domain='med', kind='Microscopy segmentation challenge',
  blurb='Self-supervised learning for segmenting 3D light-sheet microscopy images, in two tasks: one '
        'with training data fixed, one with open data allowed. Evaluated across four structure '
        'types &mdash; isolated sparse, isolated dense, contiguous sparse, contiguous dense.',
  submit='Segmentation models evaluated on 3D light-sheet microscopy volumes.',
  fmt='remote', location='Online, on Grand Challenge',
  travel='Not stated.',
  fee='Not stated on the challenge page',
  prize='Per task: $125 first, $75 second, $50 third, sponsored by MICCAI SiG-CompPath.',
  team='Not stated on the challenge page', eligible='Open, with one exclusion of the usual kind: the Participate Rules page says participants from the organisers&rsquo; own groups &ldquo;are welcome to join&rdquo; but &ldquo;are not eligible for awards&rdquo;. The same page adds a publication route the prize line does not mention &mdash; <b>participants who submit valuable work are welcome to contribute to the publication, with up to three authors from each team</b> &mdash; and, unusually, encourages independent publication with <b>no embargo</b>.',
  effort='Heavy. Self-supervised learning on 3D volumes.',
  difficulty=5,
  deadline_text='Training set 23 April 2026, preliminary test set 30 May, preliminary test phase '
                'opened 10 August 2026. FINAL TEST PHASE DATES ARE NOT STATED.',
  deadline='', precision='none',
  extra='Light-sheet microscopy images whole cleared organs in 3D &mdash; it is how a whole mouse '
        'brain gets photographed cell by cell.',
  why='Self-supervised learning is the technique the field is moving to, and here it is attached to '
      'a real microscopy problem rather than a benchmark of cat photos.',
  view='The prize is $125, so enter this for the technique and not the money. Same warning as ATM26: '
       'the final phase has no printed date, so do not build a plan on it.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#e7f6e8', ink='#1f7a26', rule='#1f7a26', treatment='t-riso'),
  tags=['microscopy','self-supervised','small prize','deadline not printed']),

dict(id='surgvu-2026', name='Surgical Visual Understanding 2026 (SurgVU)',
  host='EndoVis at MICCAI 2026', platform='Grand Challenge',
  url='https://surgvu26.grand-challenge.org/',
  domain='med', kind='Surgical video challenge',
  blurb='Pick one of two categories: train a model to localise surgical tools and their key-points '
        'in video using only tool-presence labels as weak supervision, or answer questions about '
        'short surgical video clips.',
  submit='Model predictions &mdash; tool localisation with key-points, or video question-answering '
         'responses.',
  fmt='remote', location='Online. Part of EndoVis at MICCAI 2026 in Strasbourg, France.',
  travel='Not stated for competing.',
  fee='Not stated on the challenge page',
  prize='&ldquo;Cash prizes that can total up to $8,500.&rdquo;',
  team='<b>Team-based, but a team of one is explicitly fine</b> &mdash; printed as &ldquo;The challenge is team-based, even if you are a team of one. Each member of your team is only a member of this team, and no other.&rdquo; To be considered you must file a complete final report, a GitHub codebase and a pre-recorded presentation video by the deadline.', eligible='No age or nationality bar is printed; internal Intuitive teams may take part but are <b>not eligible for prizes</b>. The Challenge Guidelines carry the part that matters most here: if you are a top finalist your report may feed a joint publication led by the organisers, and <b>&ldquo;each participating team will have at least one contributing co-author in the author list&rdquo;</b> &mdash; qualified only by the number of final teams. Note the data embargo: SurgVU data may be used for publication only after the challenge results are submitted.',
  effort='Heavy. Weakly supervised video, which is harder than it sounds.',
  difficulty=5,
  deadline_text='Launched 8 May 2026. NO SUBMISSION DEADLINE IS PRINTED on the page. The final event '
                'is MICCAI 2026.',
  deadline='', precision='none',
  extra='EndoVis is the long-running surgical-vision challenge series; a place in it is a real line '
        'on a CV in this field.',
  why='Surgical video is the closest computer vision gets to an operating theatre, and the '
      'video-question-answering track needs someone who knows what is happening in the picture.',
  view='The VQA track is the one for you &mdash; understanding the surgery is half the task and that '
       'half is free to you. But no deadline is printed anywhere, so write to the organisers before '
       'you commit a week.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#ebe4f6', ink='#240b4c', rule='#240b4c', treatment='t-ticket'),
  tags=['surgery','video','deadline not printed','EndoVis']),

dict(id='chimera-agent', name='CHIMERA-agent &mdash; Prostate Decision Agents',
  host='MICCAI 2026 challenge community', platform='Grand Challenge',
  url='https://chimera-agent.grand-challenge.org/',
  domain='med', kind='Clinical decision agent challenge',
  blurb='Three clinical decisions on prostate cancer: an MRI-only decision before biopsy, risk '
        'stratification combining MRI and biopsy, and pathology prediction after radical '
        'prostatectomy. You are not asked to train models &mdash; you are asked to design decision '
        'policies that orchestrate existing pretrained, modality-specific foundation models.',
  submit='Two JSON files per case, about 5 KB each: one with the prediction, one with the reasoning. '
         'The reasoning trace must explain what evidence was used, how missing or conflicting '
         'information was handled, and why the decision follows.',
  fmt='remote', location='Online. Associated with a half-day workshop at MICCAI 2026.',
  travel='Not stated.',
  fee='Not stated on the challenge page', prize='<b>&euro;3,000 across two rounds, plus a $500 special award</b>, read off the challenge&rsquo;s own Awards page. Each of the two submission rounds &mdash; Round 1 at MICCAI 2026, Round 2 in November 2026 &mdash; carries <b>&euro;1,500</b>, split &euro;750 / &euro;500 / &euro;250. Separately there is a <b>$500 SiG-CompPath award for the Most Innovative Agentic AI Solution</b>, which is judged on the idea rather than the leaderboard.',
  team='<b>Everyone forms a team, even a team of one</b>, and each individual may belong to only one team. Entering the Closed Testing Phase additionally requires a <b>six-page manuscript</b> in the MICCAI Springer template, excluding references, plus a GitHub URL with the source under a permissive licence.', eligible='<b>&ldquo;Open to participants worldwide&rdquo;</b>, excluding residents of North Korea, Crimea and anywhere else under EU financial or goods sanctions. Members of sponsoring or organising centres may enter but are not eligible for prizes or final rankings in the Closed Testing Phase. An <b>embargo</b> applies: results on the public training data may not be published until the challenge journal paper and the baseline paper are out, and any publication must cite the challenge.',
  effort='Moderate by the standards of this platform &mdash; no model training, but the clinical '
         'reasoning has to be right.',
  difficulty=3,
  deadline_text='NO DATES ARE PRINTED and the challenge has NO TIMELINE PAGE &mdash; '
                '/timeline/ returns 404.',
  deadline='', precision='none',
  extra='It asks for a written reasoning trace alongside every prediction, which is closer to how a '
        'clinician is actually assessed than any other entry on this wall.',
  why='THE BEST STRUCTURAL FIT ON THIS ENTIRE WALL. It explicitly does not want a model trained from '
      'scratch; it wants good clinical decision policy plus written justification, using models '
      'someone else built. That is a medical student with AI tooling, described exactly.',
  view='Chase this one. Register, read the task pages, and ask the organisers for the timeline since '
       'the page has none. Of everything swept today, this is the competition where your medicine is '
       'the qualification and the machine learning is the part you can buy off the shelf.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#f6efe1', ink='#4c3f22', rule='#4c3f22', treatment='t-gazette'),
  tags=['prostate','clinical reasoning','no training needed','best structural fit']),

dict(id='lunovo26', name='LUNOVO26 &mdash; Lung Nodule Volumetry',
  host='Grand Challenge community', platform='Grand Challenge',
  url='https://lunovo26.grand-challenge.org/',
  domain='med', kind='Medical imaging challenge',
  blurb='Measure the VOLUME of pulmonary nodules in lung cancer screening, rather than the diameter, '
        'and be judged on how accurately. The stated aim is transparent comparison of academic and '
        'commercial volumetry algorithms on the same data.',
  submit='An algorithm container. The route printed on How To Participate: contact the organisers to sign a research agreement, register a grand-challenge.org account, join the challenge (which reveals the Data, Evaluation and submission-instruction pages), build your algorithm container, submit it to each phase, and receive scores published on the leaderboards.',
  fmt='remote', location='Online, on Grand Challenge',
  travel='Not stated.',
  fee='Not stated on the challenge page', prize='Not stated on the challenge page',
  team='Not stated on the challenge page', eligible='<b>YOU CANNOT ENTER THIS ONE.</b> Printed at the top of the challenge&rsquo;s own How To Participate page: &ldquo;NOTE: The LUNOVO26 challenge is currently only open for vendors with a CE-certified product for lung nodule volumetry.&rdquo; Entering also requires signing a research agreement with Radboud University Medical Center. This is a <b>commercial device validation study wearing a challenge&rsquo;s clothes</b> &mdash; a CE mark is a regulatory certification for a medical product on the European market, so the bar is a company with an approved device, not a person with a model.',
  effort='Heavy. 3D CT again.',
  difficulty=4,
  deadline_text='Debug phase live 7 April 2026, Phase 1 on phantom data live 10 July 2026. '
                'NO CLOSING DATE IS PRINTED on the page or its timeline.',
  deadline='', precision='none',
  extra='Phase 1 runs on PHANTOM data &mdash; manufactured objects of known volume &mdash; so the '
        'ground truth is exact rather than a radiologist&rsquo;s opinion.',
  why='Nodule follow-up is decided by volume doubling time, so this is the measurement a real '
      'screening programme depends on.',
  view='<b>You are not eligible, and this card used to tell you to enter it.</b> It said phantom '
       'data made this an unusually clean first imaging challenge and to look at Phase 1. That '
       'advice was worthless: the challenge is open only to vendors holding a CE-certified '
       'lung-nodule product, and it wants a signed research agreement with a Dutch university '
       'hospital before you may even see the data pages. It stays on the wall as a marker of what '
       'a vendor-validation study looks like from the outside, so the next one is recognised '
       'before the work rather than after it.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#ddf6f5', ink='#1b4c4b', rule='#1b4c4b', treatment='t-chart'),
  tags=['lung cancer','screening','phantom data','deadline not printed']),

dict(id='dalphin', name='DALPHIN &mdash; Pathology Vision-Language Benchmark',
  host='Grand Challenge community', platform='Grand Challenge',
  url='https://dalphin.grand-challenge.org/',
  domain='med', kind='Long-term benchmark, not a prize competition',
  blurb='Evaluates vision-language models on six pathology tasks: tissue and organ recognition, '
        'neoplastic status, neoplastic behaviour, diagnosis, and both multiple-choice and '
        'free-response questions about a case.',
  submit='Model responses per task, following the instructions on each submission page.',
  fmt='remote', location='Entirely online',
  travel='None stated at any stage.',
  fee='Not stated',
  prize='NONE. The page states plainly: &ldquo;There are no submission deadlines, prizes, or formal '
        'publication opportunities.&rdquo;',
  team='Not stated', eligible='Not stated',
  effort='Moderate. You are evaluating existing vision-language models, not training one.',
  difficulty=3,
  deadline_text='No deadline. It describes itself as a long-term benchmark rather than a challenge.',
  deadline='', precision='none',
  why='Multiple-choice and free-response questions about pathology cases &mdash; that is a viva, '
      'automated. You can measure how well a model does on questions you will yourself be asked.',
  view='Not a competition and it says so. Use it as a sandbox: run an off-the-shelf vision-language '
       'model against real pathology questions and see where it fails. That single afternoon will '
       'teach you more about medical AI than reading about it for a month.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#f4ebf1', ink='#4c133e', rule='#4c133e', treatment='t-hoard'),
  tags=['pathology','benchmark','no prize','sandbox']),

dict(id='beetle', name='BEETLE &mdash; Breast Histopathology Segmentation',
  host='Grand Challenge community', platform='Grand Challenge',
  url='https://beetle.grand-challenge.org/',
  domain='med', kind='Long-term benchmark, not a prize competition',
  blurb='Semantic segmentation of H&amp;E-stained breast cancer whole-slide images into four classes: '
        'invasive epithelium, non-invasive epithelium, necrosis, and other.',
  submit='Predictions on 170 regions of interest from the evaluation set. You download the images '
         'from Zenodo, run your algorithm and submit the predictions; ranking is by Dice coefficient.',
  fmt='remote', location='Entirely online',
  travel='None stated at any stage.',
  fee='Not stated',
  prize='NONE. Stated as a long-term benchmark with &ldquo;no submission deadlines, prizes, or '
        'formal publication opportunities&rdquo;.',
  team='Not stated', eligible='Not stated',
  effort='Moderate to heavy, but the images come as a plain download rather than a container.',
  difficulty=3,
  deadline_text='No deadline. Long-term benchmark.',
  deadline='', precision='none',
  extra='H&amp;E is haematoxylin and eosin, the routine stain behind nearly every slide you will '
        'ever look at down a microscope.',
  why='Histopathology is a subject you are about to sit exams in, and here it is as a segmentation '
      'problem with public data and no clock.',
  view='Good second sandbox after DALPHIN. Download from Zenodo, look at the slides, and try to beat '
       'the baseline. Learning to tell invasive from non-invasive epithelium by eye is worth doing '
       'whether or not the model works.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#edf4e8', ink='#294c0b', rule='#294c0b', treatment='t-hoard'),
  tags=['histopathology','benchmark','no prize','public data']),

dict(id='panther', name='PANTHER &mdash; Pancreatic Tumour Segmentation',
  host='Grand Challenge community', platform='Grand Challenge',
  url='https://panther.grand-challenge.org/',
  domain='med', kind='Post-challenge leaderboard &mdash; the competition itself is over',
  blurb='Two tasks: pancreatic tumour segmentation in diagnostic T1-weighted contrast-enhanced MRI '
        '(92 annotated and 367 unannotated images), and in T2-weighted MR-Linac images used for '
        'adaptive radiotherapy (50 annotated).',
  submit='<b>Fully automated methods in Docker containers only</b> &mdash; semi-automated or interactive methods are explicitly not permitted. The container must carry all its own resources and <b>run offline with no internet access</b>. Reaching the Testing Phase also requires completing the organisers&rsquo; technical report form.',
  fmt='remote', location='Entirely online',
  travel='Not stated.',
  fee='Not stated',
  prize='The &euro;500 / &euro;300 / &euro;200 per task WERE THE 2025 PRIZES and have been awarded. '
        'Nothing is on offer in the post-challenge phase.',
  team='Up to three members of each of the top three teams per task were invited as co-authors, in '
       'the 2025 round.',
  eligible='<b>&ldquo;Anyone can participate in this phase of the challenge&rdquo;</b> during the Open Development Phase, printed on the Phases &amp; Rules page. Members of the sponsoring hospitals &mdash; Radboud UMC and Odense University Hospital &mdash; may enter but cannot compete for prizes. Two hard rules: <b>anonymous entry is forbidden</b>, real names and affiliations must show on a verified Grand Challenge profile, and anyone using duplicate profiles is disqualified.',
  effort='Heavy. Pancreatic tumour boundaries are hard even for radiologists.',
  difficulty=5,
  deadline_text='THE CHALLENGE IS OVER. Closed testing ended 31 August 2025, results announced 9 '
                'September 2025, presented at MICCAI 2025. Only the post-challenge submission phase '
                'is still open, with no end date.',
  deadline='', precision='none',
  extra='Grand Challenge still lists it as &ldquo;Accepting submissions&rdquo;, which is how a dead '
        'competition looks alive. Its timeline page is the only thing that tells you otherwise.',
  why='Kept on the wall deliberately, as an open dataset and as a warning: this is what an expired '
      'challenge looks like when a listing says it is open.',
  view='Do not enter this expecting a competition. Enter it if you want annotated pancreatic MRI to '
       'practise on, which is genuinely valuable and free. And remember the shape of it &mdash; '
       '&ldquo;accepting submissions&rdquo; is not the same as &ldquo;open&rdquo;.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#e5e7f4', ink='#2d3663', rule='#2d3663', treatment='t-letter'),
  tags=['pancreas','MRI','competition is over','dataset only']),

dict(id='toothfairy3', name='ToothFairy3 &mdash; CBCT Multi-Class Segmentation',
  host='ODIN workshop, MICCAI', platform='Grand Challenge',
  url='https://toothfairy3.grand-challenge.org/',
  domain='med', kind='Post-challenge leaderboard &mdash; the competition itself is over',
  blurb='Multi-class segmentation in cone-beam CT volumes of the jaw. Task 1 is judged partly on '
        'runtime; Task 2 is interactive segmentation of the inferior alveolar canal guided by clicks.',
  submit='Not stated on the overview page.',
  fmt='remote', location='Entirely online',
  travel='Not stated.',
  fee='Not stated', prize='<b>&euro;3,600 across the two tasks</b>, printed on the challenge&rsquo;s own Ranking &amp; Prizes page: <b>&euro;1,000 first, &euro;500 second, &euro;300 third</b> in each of Task 1 and Task 2, paid to the top three teams or individuals. Tied ranks split the prize evenly. Worth knowing before you optimise anything: the ranking is not accuracy alone &mdash; it averages independent rankings of Dice score, 95th-percentile Hausdorff distance and <b>inference time</b>, with peak memory used as the tie-break. A slow, accurate model loses.', team='Not stated', eligible='No restriction by age, country or background is printed anywhere. What the F.A.Q. does state is the thing worth entering for: <b>&ldquo;All challenge participants will be invited to co-author a journal publication&rdquo;</b>, under the policy in the structured submission document. Not the winners. Every participant.',
  effort='Heavy.',
  difficulty=5,
  deadline_text='THE CHALLENGE IS OVER. Debug phase opened 1 July 2025, test phase 8 August 2025, '
                'submission deadline postponed to 24 August 2025, results presented at the ODIN '
                'workshop at MICCAI 2025 on 25 September 2025.',
  deadline='', precision='none',
  extra='The inferior alveolar canal carries the nerve that a dental surgeon must not cut &mdash; '
        'which is why an interactive, click-corrected segmentation task exists for it.',
  why='Kept for the same reason as PANTHER: the listing calls it open, the timeline says it closed a '
      'year ago, and the difference is worth being able to see.',
  view='Nothing to win. The data and the task are still interesting if you want a jaw-anatomy '
       'segmentation problem. Otherwise, treat this card as a lesson about listings.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#f4e4e2', ink='#632b23', rule='#632b23', treatment='t-letter'),
  tags=['dental','CBCT','competition is over','listing lied']),

dict(id='dengai', name='DengAI: Predicting Disease Spread',
  host='DrivenData', platform='DrivenData',
  url='https://www.drivendata.org/competitions/44/dengai-predicting-disease-spread/',
  domain='med', kind='Practice competition',
  blurb='Predict the number of dengue fever cases reported each week in San Juan, Puerto Rico and '
        'Iquitos, Peru, from environmental and climate data.',
  submit='Predictions in the specified format, uploaded to the site. You may be asked for the '
         'algorithm afterwards.',
  fmt='remote', location='Entirely online',
  travel='None stated at any stage.',
  fee='Free &mdash; the official rules state there is no purchase or donation necessary to enter.',
  prize='None. Labelled an &ldquo;intermediate practice&rdquo; competition.',
  team='Not stated',
  eligible='Individuals over 18, and valid legal entities not in bankruptcy. Excludes officers, '
           'directors and employees of the sponsor and DrivenData. Residents of countries designated '
           'by the US Treasury&rsquo;s Office of Foreign Assets Control are ineligible &mdash; India '
           'is not one of them.',
  effort='Light to moderate. Tabular time series.',
  difficulty=2,
  deadline_text='Listed as about 1 year left, and the site says the deadline may be extended because '
                'it is for learning.',
  deadline='', precision='none',
  extra='Dengue is endemic across most of India and you will see it clinically within a year.',
  why='An epidemiology forecasting problem, no prize to lose, no clock, and the disease is one you '
      'will be treating.',
  view='This is the on-ramp. Tabular data, a well-worn problem with hundreds of public solutions to '
       'read afterwards, and a subject you already understand better than most people entering it. '
       'Do this before you touch anything containerised.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#def4e7', ink='#196338', rule='#196338', treatment='t-riso'),
  tags=['epidemiology','practice','on-ramp','no clock']),

dict(id='flu-shot', name='Flu Shot Learning: H1N1 and Seasonal Flu Vaccines',
  host='DrivenData', platform='DrivenData',
  url='https://www.drivendata.org/competitions/66/flu-shot-learning/',
  domain='med', kind='Practice competition',
  blurb='Predict whether a person received the H1N1 vaccine and the seasonal flu vaccine, from their '
        'background, opinions and health behaviours.',
  submit='Predictions in the format given on the competition site, uploaded through the entry form.',
  fmt='remote', location='Entirely online',
  travel='None stated at any stage.',
  fee='Free &mdash; the official rules state there is no purchase or donation necessary to enter.',
  prize='None. Explicitly &ldquo;a practice competition designed to be accessible to participants at '
        'all levels&rdquo;.',
  team='Not stated',
  eligible='Natural persons over 18. Excludes officers, directors, employees and advisory board '
           'members of the sponsor and DrivenData and their immediate families. Residents of '
           'OFAC-designated countries are ineligible; India is not one.',
  effort='Light. Classification on a clean tabular dataset.',
  difficulty=2,
  deadline_text='Listed as about 11 months left, with the note that the deadline may be extended.',
  deadline='', precision='none',
  extra='Vaccine hesitancy modelled from attitudes and behaviour &mdash; public health, not just '
        'prediction.',
  why='The gentlest genuinely medical dataset anywhere on this wall, and the subject is one you will '
      'argue about with patients for the rest of your career.',
  view='Take this one the same week as DengAI. Two evenings each. Their real value is that they '
       'teach you the whole submission loop &mdash; download, model, submit, score &mdash; on a task '
       'where nothing is at stake, so that when a real deadline lands you are not learning the '
       'plumbing under pressure.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#ecdbf4', ink='#4b0f63', rule='#4b0f63', treatment='t-riso'),
  tags=['public health','practice','on-ramp','two evenings']),

dict(id='zindi-climate-health', name='Climate Risk and Health Prediction Challenge',
  host='Zindi', platform='Zindi',
  url='https://zindi.world/competitions/climate-risk-health-prediction-challenge',
  domain='med', kind='Health data science competition',
  blurb='Build a supervised model that predicts whether a recorded death falls into a '
        'climate-sensitive category, using health, demographic, geographic and climate data. Real '
        'mortality records, in low-resource settings where rainfall and temperature shift who dies.',
  submit='A CSV with three columns: ID, TargetF1 (binary prediction) and TargetRAUC (probability). '
         'Setting your own probability threshold is forbidden &mdash; the default 0.5 must be used.',
  fmt='remote', location='Entirely online',
  travel='None stated at any stage.',
  fee='Free. Only open-source languages and tools are permitted; no paid services and no free trials '
      'that need a credit card.',
  prize='$500 first, $300 second, $200 third, plus 1,000 Zindi points.',
  team='Maximum team size 4. No new members in the final 5 days.',
  eligible='&ldquo;Open to all.&rdquo; 10 submissions per day, 300 overall.',
  effort='Moderate. Imbalanced binary classification, scored 60% F1 and 40% ROC-AUC.',
  difficulty=3,
  deadline_text='Opened 18 August 2026, closes 19 October 2026, private leaderboard revealed the '
                'same day.',
  deadline='2026-10-19', precision='exact',
  extra='Zindi&rsquo;s fields are far smaller than Kaggle&rsquo;s, which is why its prizes are '
        'genuinely winnable. 658 had joined, 302 were active, when the page was read.',
  why='Mortality data, climate exposure and vulnerability &mdash; this is public health as a '
      'prediction problem, and it is beginner-flagged by Zindi itself.',
  view='The best realistic shot at actually WINNING money on this wall. Six weeks of runway, '
       'beginner-friendly, three hundred active competitors rather than three thousand, a plain CSV '
       'submission, and a subject where knowing what a climate-sensitive death is gives you an edge '
       'in feature engineering. If you enter one thing seriously this month, enter this.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#f1f1e9', ink='#63632d', rule='#63632d', treatment='t-bulletin'),
  tags=['public health','mortality','winnable','beginner friendly']),

dict(id='hack2heal', name='Hack2Heal 2.0 &mdash; Global Healthcare Innovation Hackathon',
  host='Hack2Heal', platform='Devpost',
  url='https://hack2heal.devpost.com/',
  domain='med', kind='Healthcare hackathon',
  blurb='A global healthcare innovation hackathon, run online through Devpost.',
  submit='A Devpost project submission. Specific requirements are on the hackathon&rsquo;s own page.',
  fmt='remote', location='Online',
  travel='None stated at any stage.',
  fee='Not stated', prize='$100 in cash prizes',
  team='Not stated on the Who can participate block',
  eligible='Above the legal age of majority in your country of residence; STUDENTS ONLY; companies '
           'and professional organisations excluded; all countries and territories except the '
           'standard exceptions.',
  effort='Light. A week-long online hackathon.',
  difficulty=2,
  deadline_text='Submission period 25 August to 10 September 2026. Deadline 10 September 2026 at '
                '23:45 IST &mdash; the only bill on this wall whose deadline is printed in your own '
                'time zone.',
  deadline='2026-09-10', precision='exact',
  why='It is healthcare, it is online, it is students only, and it is small. The prize is nominal but '
      'the barrier is nominal too.',
  view='One week left and $100 on the table, so this is about the submission, not the money. If you '
       'want a healthcare project on a public profile with your name on it before you start MBBS, '
       'this is the cheapest way to get one.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#e5eef1', ink='#2b637a', rule='#2b637a', treatment='t-stencil'),
  tags=['healthcare','students only','small','IST deadline']),

dict(id='sbi-asha-medical', name='SBI Platinum Jubilee Asha Scholarship for Medical Students 2026',
  host='SBI Foundation', platform='Buddy4Study',
  url='https://www.buddy4study.com/page/sbi-asha-scholarship-program',
  domain='med', kind='Scholarship',
  blurb='A scholarship for Indian MBBS students, paid by direct benefit transfer. Part of a wider '
        'Asha programme covering classes 9 to 12, undergraduates, postgraduates, IIT and IIM '
        'students and some overseas universities, with awards from &#8377;15,000 to &#8377;15,00,000 '
        'a year depending on category.',
  submit='An online application through the programme portal. The application process is entirely '
         'online.',
  fmt='remote', location='Application is online',
  travel='None stated.',
  fee='Free &mdash; NO APPLICATION FEE. The page states this explicitly.',
  prize='Financial assistance of up to &#8377;2,00,000 per academic year for the medical category.',
  team='Individual application.',
  eligible='Indian nationals pursuing an MBBS programme at an eligible medical institution in India. '
           'You must be studying at an All India Institute of Medical Sciences, OR a medical college '
           'ranked in the Top 50 under the applicable NIRF rankings. At least 75% marks or 7.0 CGPA '
           'in the previous academic year or qualifying examination, with a 10% relaxation for SC '
           'and ST applicants. Total annual family income from all sources must not exceed '
           '&#8377;6,00,000. A valid NEET scorecard or rank document from the current or previous '
           'academic year is required where applicable.',
  effort='An afternoon of paperwork.',
  difficulty=1,
  deadline_text='Deadline 19 September 2026.',
  deadline='2026-09-19', precision='exact',
  extra='Found on Buddy4Study, a source this wall had named and never opened. There are 13 live '
        'medical scholarships listed there; this is the one that fits you.',
  why='&#8377;2,00,000 a year, for being an MBBS student, with a NEET scorecard you already hold. '
      'This is the highest value-per-hour item on the entire wall and it is not a competition at all.',
  view='CHECK THE TWO CONDITIONS TODAY: whether your allotted college is AIIMS or NIRF top 50, and '
       'whether family income is under &#8377;6,00,000. If both hold, apply before 19 September '
       '&mdash; sixteen days. If your college is not in the top 50 you are out, and it is better to '
       'know that in ten minutes than to find out in October. This is exactly the kind of thing '
       'nobody tells you about and everybody assumes you already knew.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#f1e2e8', ink='#7a1f45', rule='#7a1f45', treatment='t-gazette'),
  tags=['scholarship','MBBS','money','check today']),

]


BILLS.append(dict(
 id='neural-interfaces-2026',
 domain='med',
 kind='Neural decoding benchmark',
 name='Neural Interfaces 2026',
 host='Neural Interfaces 2026 organisers',
 platform='Codabench',
 url='https://www.codabench.org/competitions/17974/',
 blurb='Four separate EEG and EMG decoding tracks, each scored on a held-out split by the platform itself: reconstruct which image someone was looking at, decode an imagined movement, predict how long it takes them to fall asleep, and recover hand-joint angles from wrist muscle signals.',
 submit='<b>A trained model &mdash; code and weights.</b> The platform runs inference itself on the held-out split, so you never see the test data. Track 1 is ranked by top-5 retrieval accuracy, Track 2 by balanced accuracy, Track 3 by binned mean absolute error, Track 4 by mean angular error in degrees. All four are built on benchopt and neuralbench.',
 fmt='remote',
 location='Online, on Codabench',
 travel='None.',
 fee='Free. Codabench is an open platform and no entry fee is printed.',
 prize='Not stated. No prize is published on any of the four track pages.',
 team='Not stated on the competition records.',
 eligible='Not stated. No eligibility restriction of any kind is printed on the track pages &mdash; Codabench requires only an account. <b>That is an absence, not a permission</b>, so read the rules tab before counting on it.',
 effort='Heavy. Each track wants a trained model, not a CSV of answers.',
 difficulty=5,
 deadline_text='Warm-up phases opened 31 August and 1 September 2026 and run to <b>15 October 2026</b>; the Sealed Final phase then runs 15 October to <b>15 November 2026</b> on tracks 1, 3 and 4. Track 2 (BCI Decoding) currently lists a warm-up phase only.',
 deadline='2026-11-15',
 precision='exact',
 why='This is the closest thing on either wall to the intersection you are actually building a life on: it is neurophysiology and it is machine learning, and there is no way to do one half without the other. The wall already carries the Brain-to-Text benchmark for the same reason; this one has <b>four tracks, a live warm-up phase you can enter today, and real EEG and EMG data</b> rather than a closed 2024 archive.',
 view='<b>Use the warm-up phase and expect to lose.</b> That is not defeatism &mdash; a sealed-final benchmark against people with EEG labs is not winnable from a laptop in your first MBBS term, and the value here is not the leaderboard. It is that four curated neural datasets, a scoring harness and a baseline are handed to you for nothing, and working through even one track teaches you what an EEG epoch actually is. Start with <b>Track 3, sleep onset</b> &mdash; it predicts a single number rather than an image or a trajectory, so the modelling is the simplest of the four while the physiology is the most clinical. One clash to note: the sealed final closes 15 November, which is your IIT Madras quiz day.',
 conf='verified',
 checked='2026-09-10',
 theme={'paper': '#ded7ea', 'ink': '#3d2c5e', 'rule': '#3d2c5e', 'treatment': 't-chart'},
 tags=['EEG', 'EMG', 'neuroscience', 'free', 'four tracks', 'no prize stated'],
))


BILLS.append(dict(
 id='amplifai',
 domain='med',
 kind='Medical imaging challenge',
 name='AMPLIFAI &mdash; Annotated Multi-Phase Liver Imaging for AI',
 host='University of Maryland School of Medicine',
 platform='Codabench',
 url='https://www.codabench.org/competitions/14290/',
 blurb='Automated characterisation of hepatocellular carcinoma lesions in multi-phase abdominal CT, scored against standardised clinical <b>LI-RADS</b> categories &mdash; the same radiological grading a reporting radiologist assigns by eye.',
 submit='A self-contained container run inside the organisers&rsquo; own secure environment. The Test Phase gives <b>174 cases, a 3-hour execution limit and one NVIDIA RTX 4090</b>; the earlier Validation Phase used 59 cases and 60 minutes. A submission guide is published at github.com/UM-IHC-CA2i/amplifai-codabench.',
 fmt='remote',
 location='Online, inside the organisers&rsquo; secure compute environment',
 travel='None.',
 fee='Free. No entry fee is printed anywhere in the record.',
 prize='<b>1st: $1,000 &nbsp;&middot;&nbsp; 2nd: $500 &nbsp;&middot;&nbsp; 3rd: $250.</b> The top three teams are additionally asked to nominate a co-author on the joint challenge paper.',
 team='Not stated. The terms speak of &ldquo;teams&rdquo; throughout but print no size limit.',
 eligible='<b>Registration must be APPROVED by the organising team, and they say so plainly: they &ldquo;reserve the right to approve or deny participation at their discretion.&rdquo;</b> You must give your name, <b>organisation</b>, nationality and contact details. No age, country or student restriction is printed &mdash; but the data is US clinical imaging, is never distributed to you, and every model runs inside their environment.',
 effort='Heavy. A containerised model on multi-phase CT, and you never see the test data.',
 difficulty=5,
 deadline_text='Two phases, both printed on the record: Validation 17&ndash;31 July 2026, and the <b>Test Phase 1 August to 16 September 2026</b>. The terms block is stamped &ldquo;Last Updated: 6/2/2026&rdquo;.',
 deadline='2026-09-16',
 precision='exact',
 why='This is the shape of medical AI you will actually meet as a doctor: not a tidy benchmark, but liver CT graded into the same LI-RADS categories a radiologist writes in a report, run on data you are never allowed to hold. <b>And it pays cash</b>, which almost nothing clinical on this wall does.',
 view='<b>Six days, an approval gate, and a container to build &mdash; so realistically you are not entering this one.</b> It is on the wall anyway for two reasons. It is the first cash-paying clinical imaging challenge found on this platform, which tells you the seam exists; and AMPLIFAI is the kind of thing that runs again, so the useful move now is to read the LI-RADS task and the submission guide while it is live, and be ready when it returns. Do not register while you have no institution to name &mdash; the approval is discretionary and an empty organisation field is the field they will look at.',
 conf='verified',
 checked='2026-09-10',
 theme={'paper': '#fceeea', 'ink': '#7a2e22', 'rule': '#7a2e22', 'treatment': 't-clinic'},
 tags=['liver CT', 'LI-RADS', 'cash prize', 'approval needed', 'closing'],
))

BILLS.append(dict(
 id='flare-recist-3d',
 domain='med',
 kind='Medical image segmentation challenge',
 name='Pan-cancer Segmentation in CT: RECIST-to-3D',
 host='Jun Ma / FLARE organisers',
 platform='Codabench',
 url='https://www.codabench.org/competitions/17652/',
 blurb='Turn a <b>RECIST measurement</b> &mdash; the single long-axis line an oncologist draws across a tumour to track whether it is growing &mdash; into a full three-dimensional segmentation of that lesion, across cancers, on CT.',
 submit='<b>A Docker container AND a methodology paper of at least eight pages in LNCS format.</b> The rules are explicit that a complete solution is both, and that registered participants who submit neither &ldquo;will be listed in the dishonest list&rdquo;.',
 fmt='remote',
 location='Online, on Codabench',
 travel='None.',
 fee='Free. No entry fee is printed.',
 prize='Not stated. The record carries no reward string and the rules mention none.',
 team='<b>At most six people per team.</b> Printed in rule 1.',
 eligible='<b>An affiliation e-mail is required, and this is the gate that matters for you.</b> Rule 1: register &ldquo;with their real names, affiliations (including department, full name of university/institute/company, country), and affiliation E-mails. Incomplete and redundant registrations will be removed without notice.&rdquo; Multiple teams from one research group are barred. Methods must be <b>fully automatic</b> &mdash; no manual annotation.',
 effort='Heavy, and half of it is writing. The paper is a hard requirement, not a courtesy.',
 difficulty=5,
 deadline_text='One phase on the record: Development Phase <b>1 July to 31 December 2026</b>. <b>Read rule 6 before trusting the rest:</b> it tells participants to post pre-trained models on the forum &ldquo;before April 15, 2026&rdquo;, a date already five months past, so this rules block appears carried over from an earlier FLARE edition and the other dates in it should be confirmed on the forum.',
 deadline='2026-12-31',
 precision='exact',
 why='RECIST is not a computer-vision abstraction &mdash; it is the measurement oncology actually uses to decide whether a treatment is working, and you will see it written in reports for the rest of your career. A challenge that converts that one line into a volume is medicine and imaging in the same task. Jun Ma&rsquo;s FLARE challenges are also among the better-run in the field.',
 view='<b>The eight-page LNCS paper is the real entry requirement, and that is the argument for it.</b> Almost everything else on this wall asks for a model; this asks for a model and a written method, which is the thing that turns a competition entry into something you can cite. Three and a half months is enough time to do both badly and learn a great deal. <b>The affiliation e-mail is the blocker while you have no college</b> &mdash; so park this until MCC allots your seat, then come back to it, and check the forum for the real current dates before you start.',
 conf='verified',
 checked='2026-09-10',
 theme={'paper': '#e8f0e6', 'ink': '#28502c', 'rule': '#28502c', 'treatment': 't-gazette'},
 tags=['oncology', 'RECIST', 'segmentation', 'paper required', 'needs an institution'],
))

BILLS.append(dict(
 id='uusic-continuous',
 domain='med',
 kind='Continuous medical imaging benchmark',
 name='UUSIC Continuous Private Benchmark',
 host='UUSIC organisers',
 platform='Codabench',
 url='https://www.codabench.org/competitions/17694/',
 blurb='A permanently open, blinded benchmark for unified multi-organ ultrasound AI &mdash; one sequestered test set, evaluated continuously, for as long as the benchmark runs.',
 submit='Code, executed automatically on a private, network-isolated evaluation server. You never see the test data and the server never reaches the internet.',
 fmt='remote',
 location='Online, on Codabench',
 travel='None.',
 fee='Free. No entry fee is printed.',
 prize='Not stated. This is a standing benchmark rather than a prize competition.',
 team='Not stated on the record.',
 eligible='Not stated. No eligibility restriction of any kind appears in the terms, which govern only conduct on the evaluation server. <b>That is an absence, not a permission.</b>',
 effort='Heavy in the modelling, light in the logistics &mdash; there is no deadline to organise around.',
 difficulty=4,
 deadline_text='One phase, and it is the longest runway on this wall by a wide margin: <b>1 July 2026 to 1 August 2036</b>. The terms add that scores may be recomputed when evaluator defects are corrected, and that evaluator and dataset versions are recorded with every release.',
 deadline='2036-08-01',
 precision='exact',
 why='Ultrasound is the imaging you will personally hold a probe for &mdash; it is bedside, cheap, and the modality an Indian hospital has most of. A benchmark on it that never closes means this can sit on the wall until a term you actually have time in, which is true of almost nothing else here.',
 view='<b>Treat this as a shelf, not a deadline.</b> Three participants have submitted eight times, so the field is empty and will stay that way; the value is a curated multi-organ ultrasound test set with a scoring harness attached, available whenever you want it. The honest caution is that a benchmark with no closing date is also a benchmark with no pressure, and this wall exists because things without pressure never get done. Give it a week in a holiday, or leave it.',
 conf='verified',
 checked='2026-09-10',
 theme={'paper': '#e6eff2', 'ink': '#1f4a58', 'rule': '#1f4a58', 'treatment': 't-chart'},
 tags=['ultrasound', 'evergreen', 'no deadline', 'empty field'],
))
