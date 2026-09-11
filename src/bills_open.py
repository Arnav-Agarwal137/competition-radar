# -*- coding: utf-8 -*-
"""Government, corporate and open-to-anyone bills. Same rules as bills_med.py."""

BILLS = [

dict(id='innovation-for-her', name='Innovation for Her &mdash; Ideas for Women&rsquo;s Safety',
  host='Ministry of Women and Child Development', platform='MyGov Innovate India',
  url='https://innovateindia.mygov.in/innovation-for-her/',
  domain='open', kind='Government ideas challenge',
  blurb='Propose an original idea for improving the safety and security of women and girls. A '
        'written proposal, not a build.',
  submit='One PDF, maximum 2 MB, four pages or 2,000 words, images optional. One entry per person.',
  fmt='remote', location='Online only, through the MyGov portal', travel='None at any stage.',
  fee='No fee is mentioned anywhere in the rules',
  prize='1st &#8377;20,000 &middot; 2nd &#8377;15,000 &middot; 3rd to 5th &#8377;10,000 each &middot; '
        'certificates for all participants',
  team='One entry per participant',
  eligible='Open to all Indian citizens. Students, start-ups, institutions and organisations '
           'explicitly encouraged. No age bar stated.',
  effort='Light. A weekend of thinking and one careful document.',
  difficulty=1,
  deadline_text='21 August to 16 September 2026', deadline='2026-09-16', precision='exact',
  extra='Runs on MyGov Innovate India, the same class of portal the Gujarat challenge lived on.',
  why='No code, no team, no travel, no fee, a real ministry behind it, and the deliverable is 2,000 '
      'words of clear thinking.',
  view='If you do exactly one thing off this wall in the next fortnight, do this. It costs a weekend, '
       'it needs nothing you do not already have, and the skill it tests &mdash; framing a problem '
       'and arguing for a solution in four pages &mdash; is the one you are already good at and will '
       'use in every grant application for the rest of your life. The prize is small. The rep is not.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#fdf4f0', ink='#9c2b4a', rule='#9c2b4a', treatment='t-gazette'),
  tags=['government','no code','do this one']),

dict(id='digital-shram', name='Digital Shram Sankalp',
  host='Ministry of Labour and Employment', platform='MyGov Innovate India',
  url='https://innovateindia.mygov.in/digital-shram-sankalp/',
  domain='open', kind='Government challenge',
  blurb='A Ministry of Labour and Employment challenge on the rights and welfare of workers.',
  submit='Not stated on the listing',
  fmt='remote', location='Online, through the MyGov portal',
  travel='Not stated', fee='Not stated on the listing', prize='Not stated on the listing',
  team='Not stated on the listing', eligible='Not stated on the listing',
  effort='Not stated. Unknown until its own page is opened.',
  difficulty=0,
  deadline_text='5 August to 18 September 2026', deadline='2026-09-18', precision='exact',
  extra='Found on the MyGov Innovate India hub on 3 September 2026.',
  why='On the wall because the hub it came from is the one that would have caught Gujarat.',
  view='I am being blunt: I know the name and the dates and nothing else, and I have not opened its '
       'own page. Do not commit time to this on the strength of this card. If the Innovation for Her '
       'brief appeals, spend ten minutes opening this one too, since it is the same portal and the '
       'same shape of submission.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#f7f5ef', ink='#4a5a2b', rule='#4a5a2b', treatment='t-gazette'),
  tags=['government','India','barely known']),

dict(id='avinya-27', name='Avinya 27 &mdash; Energy Startup Challenge',
  host='Ministry of Petroleum and Natural Gas', platform='MyGov Innovate India',
  url='https://innovateindia.mygov.in/avinya27-energy-startup-challenge/',
  domain='build', kind='Government startup challenge',
  blurb='A challenge promoting Indian start-ups in the energy sector.',
  submit='Not stated on the listing',
  fmt='remote', location='Online, through the MyGov portal',
  travel='Not stated', fee='Not stated on the listing', prize='Not stated on the listing',
  team='Not stated on the listing',
  eligible='Not stated on the listing. The title says START-UP, which normally means a registered '
           'company &mdash; but the page does not say so, and I am not going to pretend it does.',
  effort='Not stated.', difficulty=0,
  deadline_text='21 August to 15 September 2026', deadline='2026-09-15', precision='exact',
  extra='Found on the MyGov Innovate India hub on 3 September 2026.',
  why='Kept so the wall shows what the energy ministry is actually running.',
  view='Probably not for you, and I say probably rather than definitely because the eligibility is '
       'genuinely not printed. Twelve days and an unstated brief is a bad combination. Skip unless '
       'energy is something you care about independently.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#fdf9e8', ink='#7a5a12', rule='#7a5a12', treatment='t-gazette'),
  tags=['government','startup','probably not you']),

dict(id='sih-2026', name='Smart India Hackathon 2026',
  host='Ministry of Education Innovation Cell and AICTE', platform='sih.gov.in',
  url='https://sih.gov.in',
  domain='build', kind='National hackathon',
  blurb='India&rsquo;s largest national product-development competition. Ministries publish real '
        'problem statements; student teams build prototypes.',
  submit='A prototype, nominated through your college.',
  fmt='hybrid', location='An internal college round first, then a national grand finale in person',
  travel='PHASE TWO IS PHYSICAL. The grand finale is held in person at a nominated centre.',
  fee='Free', prize='National prizes; the finale itself is the real prize',
  team='A team, through a college',
  eligible='Requires a college SPOC to nominate your team. You are between school and MBBS &mdash; '
           'whether your incoming college participates is the whole question.',
  effort='Heavy.', difficulty=4,
  deadline_text='SPOCs submit nominated ideas by 30 September 2026', deadline='2026-09-30', precision='exact',
  extra='Launched 21 August 2026.',
  why='The closest national analogue to the Gujarat challenge you missed, and it is still open.',
  view='The blocker here is administrative, not technical, and it is answerable with one email. '
       'Once you know your MBBS college, write to whoever runs the innovation cell and ask if they '
       'have an SIH SPOC. Even if 2026 is too soon, that email puts you on the list for 2027, which '
       'is worth far more than this year&rsquo;s round.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#f4f7fb', ink='#1a3a6b', rule='#c9962e', treatment='t-gazette'),
  tags=['India','government','needs a college']),

dict(id='tata-imagination', name='Tata Imagination Challenge 2026',
  host='Tata Group', platform='Unstop',
  url='https://unstop.com/competitions/crp-tata-imagination-challenge-2026-tata-group-1740413',
  domain='open', kind='Ideas competition',
  blurb='Tata Group&rsquo;s flagship national ideas challenge. Individual participation, open brief.',
  submit='An idea submission. No code required.',
  fmt='remote', location='Online',
  travel='Not stated on the listing.',
  fee='Free', prize='Not stated on the listing', team='Individual participation only',
  eligible='Engineering, undergraduate, postgraduate and management students, per the listing.',
  effort='Light to medium. Rewards thinking, not building.',
  difficulty=2,
  deadline_text='10 days left, read 3 September 2026', deadline='2026-09-13', precision='derived',
  extra='Posted 24 August 2026. Featured on Unstop.',
  why='No code, individual, a national brand, and it rewards framing a problem.',
  view='Ten days is enough for an ideas submission if you start this week. A Tata Group line on a '
       'record reads well to Indian institutions in a way a Kaggle rank does not, and you are '
       'building both kinds of record. The catch: the prize is unstated and later rounds may be '
       'physical, neither of which the listing says.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#f6f2ec', ink='#4a3a7a', rule='#4a3a7a', treatment='t-letter'),
  tags=['ideas','no code','India','tight']),

dict(id='asian-paints-alchemy', name='Asian Paints Alchemy 2026',
  host='Asian Paints', platform='Unstop',
  url='https://unstop.com/competitions/crp-asian-paints-alchemy-2026-asian-paints-1704498',
  domain='open', kind='Corporate case competition',
  blurb='A national corporate case and innovation competition, open across disciplines.',
  submit='A case submission.',
  fmt='remote', location='Online', travel='Not stated on the listing.',
  fee='Free', prize='Not stated on the listing', team='1 to 2 members',
  eligible='Arts, commerce, sciences and engineering students, undergraduate and postgraduate, '
           'per the listing. Medicine is not excluded.',
  effort='Medium.', difficulty=2,
  deadline_text='28 days left, read 3 September 2026', deadline='2026-10-01', precision='derived',
  extra='22,420 already registered &mdash; the most crowded thing on this wall.',
  why='Four weeks of runway and open to every discipline, which for once includes medicine.',
  view='Twenty-two thousand entrants is a warning, not a disqualification &mdash; most of them will '
       'submit nothing. But be honest with yourself about why you would enter: this is a corporate '
       'case competition, and if business cases do not interest you, it is four weeks better spent '
       'on the Barbados OCR one.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#fbf1f4', ink='#8a2b4a', rule='#8a2b4a', treatment='t-riso'),
  tags=['case study','India','very crowded']),

dict(id='et-ai-agentic', name='ET AI Hackathon: Agentic Edition',
  host='Economic Times, presented by Accenture', platform='Unstop',
  url='https://unstop.com/hackathons/crp-et-ai-hackathon-agentic-edition-presented-by-accenture-economic-times-1744885',
  domain='ai', kind='Hackathon',
  blurb='An agentic AI hackathon run by the Economic Times with Accenture.',
  submit='An agentic system.',
  fmt='remote', location='Online', travel='Not stated on the listing.',
  fee='Free. Unstop marks it not paid.',
  prize='&#8377;1,00,000 first, &#8377;60,000 second, &#8377;40,000 third.', team='1 to 4 members',
  eligible='The listing says EXPERIENCED PROFESSIONALS.',
  effort='Medium.', difficulty=3,
  deadline_text='End date 2 November 2026, from Unstop&rsquo;s own API. CORRECTED &mdash; the first '
                'pass read &ldquo;17 days left&rdquo; off the listing and derived 20 September, '
                'which was six weeks early.',
  deadline='2026-11-02', precision='exact',
  extra='351 registered when the API was read on 3 September 2026, up from 280 on the first pass.',
  why='Agentic AI is the thing you already do daily, the prize is &#8377;2 lakh, and it now turns '
      'out to run until November. The eligibility line is the problem, not the skill.',
  view='Two things changed on the re-sweep and both are in your favour: the deadline is 2 November '
       'rather than 20 September, and the prize that was missing is &#8377;1,00,000 for first. That '
       'gives you two months instead of two weeks. The eligibility clause still says experienced '
       'professionals &mdash; my reading is that it shuts you out, but that is my guess and not '
       'something the listing states about you, so spend five minutes on their clause before '
       'anything else. If it is soft, this is one of the best-value entries on the wall.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#fdf5ea', ink='#a04a12', rule='#a04a12', treatment='t-ticket'),
  tags=['agents','India','eligibility risk','deadline corrected']),

dict(id='pareidolia', name='The Pareidolia Paradox',
  host='SIES GST Nerul', platform='Unstop',
  url='https://unstop.com/hackathons',
  domain='ai', kind='Machine learning and computer vision challenge',
  blurb='A machine learning and computer vision challenge run by a Mumbai engineering college.',
  submit='A model.',
  fmt='remote', location='Online', travel='Not stated on the listing.',
  fee='&#8377;100 per team', prize='Not stated on the listing', team='1 to 3 members',
  eligible='Undergraduate and postgraduate, per the listing.',
  effort='Medium.', difficulty=2,
  deadline_text='18 days left, read 3 September 2026', deadline='2026-09-21', precision='derived',
  find='No direct link captured &mdash; this opens Unstop&rsquo;s hackathon list. Search there for '
       'the exact title.',
  extra='Posted 3 September 2026, so it was brand new when read.',
  why='Cheap, small, computer vision, eighteen days.',
  view='&#8377;100 and a small college field is a low-risk way to run a whole computer-vision '
       'pipeline end to end with a deadline on it. Not a prize to chase &mdash; a rehearsal. If the '
       'Barbados OCR competition appeals but feels large, do this one first as practice.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#f2f0f8', ink='#4a3a8a', rule='#4a3a8a', treatment='t-riso'),
  tags=['computer vision','cheap','rehearsal']),

dict(id='iitm-polymer', name='ML Hackathon: Polymer Property Prediction',
  host='IIT Madras', platform='Unstop',
  url='https://unstop.com/hackathons',
  domain='ai', kind='Machine learning hackathon',
  blurb='Predict polymer properties from data. A straight machine-learning task set by IIT Madras.',
  submit='A model and predictions.',
  fmt='remote', location='Online', travel='Not stated on the listing.',
  fee='&#8377;500 per team', prize='Not stated on the listing', team='1 to 4 members',
  eligible='Everyone can apply, per the listing.',
  effort='Medium.', difficulty=3,
  deadline_text='The listing printed a relative countdown rather than a date; read on 3 September 2026 as &ldquo;6 days left&rdquo;, which puts the deadline at <b>9 September 2026</b>. That date has passed and this is CLOSED. Recorded as derived, not exact, because the source never printed the date itself.', deadline='2026-09-09', precision='derived',
  find='No direct link captured &mdash; this opens Unstop&rsquo;s hackathon list. Search there for '
       'the exact title.',
  extra='Posted 2 September 2026.',
  why='Your own institution &mdash; you are enrolled in the IIT Madras BS programme.',
  view='Six days and &#8377;500 to enter, with the prize unstated. I would skip this one and watch '
       'for the next IIT Madras hackathon instead, now that you know they run them. Being enrolled '
       'there is a real advantage; spending it on six days of runway is not the way to use it.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#f0f6f4', ink='#1a5a5a', rule='#1a5a5a', treatment='t-chart'),
  tags=['IIT Madras','paid entry','too tight']),

dict(id='tech-horizon-2', name='Tech Horizon 2.0 &mdash; National Level Hackathon',
  host='IEEE SMC Society, GNITC chapter', platform='Unstop',
  url='https://unstop.com/hackathons/tech-horizon-20-national-level-hackathon-guru-nanak-institutions-technical-campus-gnitc-hyderabad-1677311',
  domain='build', kind='National hackathon',
  blurb='A national hackathon with 14 tracks, including Health &amp; Biotech and Generative AI.',
  submit='An idea or prototype submission for one of the 14 tracks.',
  fmt='remote', location='Not stated on the listing',
  travel='Not stated on the listing.',
  fee='Not stated on the listing', prize='Not stated on the listing',
  team='Not stated on the listing', eligible='Not stated on the listing',
  effort='Not stated.', difficulty=0,
  deadline_text='Not stated on the listing as an exact date', deadline='', precision='none',
  extra='Hosted at Guru Nanak Institutions Technical Campus, Hyderabad. IEEE Systems, Man and '
        'Cybernetics Society chapter.',
  why='It has a Health and Biotech track, which is rarer in student hackathons than it should be.',
  view='The harvester added this with a guess in the format field &mdash; that a 48-hour sprint '
       '"suggests" an in-person finale. It suggests nothing; the listing does not say. I have '
       'stripped the guess and left the blanks. An IEEE chapter and a health track make it worth '
       'ten minutes of your own reading, but nothing here should move you before you do that.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#eef2f6', ink='#2b3a5a', rule='#2b3a5a', treatment='t-chart'),
  tags=['India','health track','mostly unknown']),


dict(id='yuva-yodha', name='Yuva Yodha Energy Tech Hackathon',
  host='Schneider Electric India', platform='HackerEarth',
  url='https://www.yuvayodhatech.com/',
  domain='open', kind='Corporate innovation challenge',
  blurb='Submit an idea against one of four energy-sector challenges &mdash; sustainable '
        'agriculture, smart buildings, grid reliability, or smart manufacturing &mdash; then build a '
        'prototype if you get through.',
  submit='An idea submission first. Selected teams go on to a prototype and judging phase.',
  fmt='hybrid', location='Online for the idea and prototype phases.',
  travel='THE BEST 10 IDEAS present at the Schneider Electric India corporate office at a final '
         'event, and the finale is in January 2027. Travel terms are not stated.',
  fee='Not stated',
  prize='&#8377;45,00,000 total. Grand prize &#8377;20,00,000, runner-up &#8377;15,00,000, third '
        '&#8377;10,00,000. The top 10 teams also get mentorship and pre-placement interview '
        'opportunities.',
  team='1 to 4 members.',
  eligible='Indian citizen or resident, at least 18 years old, and CURRENTLY ENROLLED AS A FULL-TIME '
           'STUDENT IN INDIA in an undergraduate, postgraduate or STEM programme.',
  effort='Moderate for the idea stage, heavy if you reach the prototype phase.',
  difficulty=3,
  deadline_text='Idea submission 15 August to 4 October 2026. Prototype and judging 11 October to '
                '22 November. Top teams announced 6 December 2026. Finale January 2027.',
  deadline='2026-10-04', precision='exact',
  extra='This is the largest rupee prize on the wall by a wide margin, and it was found on '
        'HackerEarth &mdash; a source the wall had named and never opened.',
  why='&#8377;45 lakh, open to any full-time Indian student aged 18 or over, and the first stage is '
      'an IDEA rather than a build. That first stage is one document.',
  view='Enter the idea stage. It closes on 4 October, which is a month, and it costs you a written '
       'submission rather than a working system. Smart buildings and grid reliability both have '
       'obvious hospital angles &mdash; theatre and cold-chain power reliability is a real problem '
       'you will see from the inside. Even if the prototype phase later clashes with first-year '
       'MBBS, the idea stage is cheap and the pre-placement route is a genuine door.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#eadff1', ink='#5d2b7a', rule='#5d2b7a', treatment='t-gazette'),
  tags=['Rs 45 lakh','Indian students','idea stage first','biggest rupee prize']),

dict(id='dogfood-72', name='Dogfood &mdash; 72-Hour Hackathon',
  host='Hackathon Raptors', platform='Unstop',
  url='https://unstop.com/hackathons/dogfood-72-hour-hackathon-hackathon-raptors-1748391',
  domain='build', kind='Hackathon',
  blurb='A 72-hour build, listed on Unstop with no eligibility filter at all &mdash; the listing '
        'says &ldquo;All&rdquo;.',
  submit='Not stated on the listing.',
  fmt='remote', location='Listed as city-based work location on Unstop; the listing does not name a city.',
  travel='Not stated on the listing.',
  fee='FREE. Unstop marks it not paid.',
  prize='&#8377;80,000 first, &#8377;50,000 second, &#8377;35,000 third, then &#8377;20,000 and '
        '&#8377;15,000.',
  team='1 to 4 members.',
  eligible='Unstop&rsquo;s eligibility filter reads &ldquo;All&rdquo; &mdash; no course, year or '
           'institution restriction.',
  effort='Light. Three days.',
  difficulty=2,
  deadline_text='Registration 2 September to 25 September 2026, closing 23:30 IST.',
  deadline='2026-09-25', precision='exact',
  extra='135 registered when the listing was read &mdash; a small field for that money.',
  why='The best prize-to-field ratio on Unstop right now: &#8377;2 lakh spread across five places '
      'with barely a hundred entrants, and no eligibility bar.',
  view='Three weeks to register, three days to build. The &ldquo;All&rdquo; eligibility and the tiny '
       'field are what make this worth your time over the bigger-name Indian hackathons where you '
       'are one of two thousand.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#f1efdc', ink='#7a731f', rule='#7a731f', treatment='t-ticket'),
  tags=['no eligibility bar','small field','free','three days']),

dict(id='quhack', name='QuHack Hackathon',
  host='RGUKT Nuzvid', platform='Unstop',
  url='https://unstop.com/hackathons/quhack-hackathon-rajiv-gandhi-university-of-knowledge-technologies-rgukt-nuzvid-1746545',
  domain='build', kind='Hackathon',
  blurb='A university-run hackathon on Unstop.',
  submit='Not stated on the listing.',
  fmt='remote', location='Listed as city work location on Unstop; the city is not printed on the listing.',
  travel='Not stated on the listing.',
  fee='FREE. Unstop marks it not paid.',
  prize='&#8377;1,00,000 first, &#8377;50,000 second, &#8377;25,000 third.',
  team='1 to 3 members.',
  eligible='Undergraduate, postgraduate, engineering students, management, arts and commerce '
           '&mdash; the widest Unstop filter set, which includes you.',
  effort='Light to moderate.',
  difficulty=2,
  deadline_text='Registration closes 20 September 2026. Listing end date 7 October 2026.',
  deadline='2026-10-07', precision='exact',
  extra='509 registered when the listing was read.',
  why='&#8377;1.75 lakh, free, and the eligibility filter explicitly includes non-engineering courses.',
  view='Register by 20 September even if you are unsure &mdash; registration and submission are '
       'separate dates here, and the second gives you until October. That gap is the useful part.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#d9ecf1', ink='#12647a', rule='#12647a', treatment='t-bulletin'),
  tags=['free','non-engineering welcome','register early','Rs 1.75 lakh']),

dict(id='hack2ignite', name='Hack 2 Ignite',
  host='G H Raisoni International Skill Tech University', platform='Unstop',
  url='https://unstop.com/hackathons/hack-2-ignite-gh-raisoini-international-skill-tech-university-1745045',
  domain='build', kind='Hackathon',
  blurb='A university hackathon listed on Unstop.',
  submit='Not stated on the listing.',
  fmt='remote', location='Listed as city work location on Unstop; the city is not printed.',
  travel='Not stated on the listing.',
  fee='FREE. Unstop marks it not paid.',
  prize='&#8377;70,000 first, &#8377;50,000 second, &#8377;30,000 third.',
  team='Not printed in the fields read.',
  eligible='Not printed in the fields read beyond the standard Unstop student filters.',
  effort='Light to moderate.',
  difficulty=2,
  deadline_text='Listing end date 3 October 2026.',
  deadline='2026-10-03', precision='exact',
  extra='134 registered when the listing was read.',
  why='&#8377;1.5 lakh free to enter with a small field and a month of runway.',
  view='Solid middle option. A month is enough to build something properly rather than in a panic, '
       'and the field is small enough that a finished project stands out.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#fbf2f7', ink='#4c2237', rule='#4c2237', treatment='t-riso'),
  tags=['free','small field','a month','Rs 1.5 lakh']),

dict(id='global-innovation-hack', name='Global Innovation Hackathon 2026 &mdash; Build for a Better Future',
  host='Bharat Academix', platform='Unstop',
  url='https://unstop.com/hackathons/global-innovation-hackathon-2026-build-for-a-better-future-bharat-academix-1748404',
  domain='build', kind='Hackathon',
  blurb='An open-brief innovation hackathon listed on Unstop.',
  submit='Not stated on the listing.',
  fmt='remote', location='Listed as city work location on Unstop; the city is not printed.',
  travel='Not stated on the listing.',
  fee='FREE. Unstop marks it not paid.',
  prize='&#8377;51,000 first, &#8377;21,000 second, &#8377;11,000 third.',
  team='1 to 6 members.',
  eligible='Undergraduate, postgraduate, engineering students, management, arts and commerce.',
  effort='Light to moderate.',
  difficulty=2,
  deadline_text='Registration closes 16 September 2026. Listing end date 27 September 2026.',
  deadline='2026-09-27', precision='exact',
  extra='586 registered when the listing was read &mdash; a larger field than the others taken here.',
  why='An open brief means a medical project qualifies, and teams of up to six give room for '
      'classmates.',
  view='Register by 16 September. The open brief is the point: build the health thing you actually '
       'want to build and enter it here as well as somewhere else.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#f2fbef', ink='#254c1b', rule='#254c1b', treatment='t-stencil'),
  tags=['open brief','free','teams up to six','register by 16 Sep']),

dict(id='black-box-protocol', name='The Black-Box Protocol: Stage 03 &mdash; System Convergence',
  host='TechHelp4U', platform='Unstop',
  url='https://unstop.com/hackathons/the-black-box-protocol-stage-03-system-convergence-techhelp4u-1745778',
  domain='build', kind='Hackathon series, third stage',
  blurb='The third stage of a running series, listed on Unstop with eligibility &ldquo;All&rdquo;.',
  submit='Not stated on the listing.',
  fmt='remote', location='Listed as city work location on Unstop; the city is not printed.',
  travel='Not stated on the listing.',
  fee='FREE. Unstop marks it not paid.',
  prize='&#8377;25,000 first, &#8377;15,000 second, &#8377;10,000 third, out of a stated '
        '&#8377;1,50,000 pool.',
  team='2 to 4 members. YOU CANNOT ENTER ALONE.',
  eligible='Unstop&rsquo;s eligibility filter reads &ldquo;All&rdquo;.',
  effort='Light to moderate.',
  difficulty=2,
  deadline_text='Registration closes 25 September 2026. Listing end date 7 October 2026.',
  deadline='2026-10-07', precision='exact',
  extra='Being Stage 03, the earlier stages have already run &mdash; check whether entering cold is '
        'allowed before you build anything.',
  why='No eligibility bar and a &#8377;1.5 lakh pool.',
  view='Two flags rather than one: you need a team of at least two, and it is the third stage of '
       'something. Ask the organisers whether Stage 03 accepts new entrants before you spend a '
       'weekend on it.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#edecfb', ink='#18134c', rule='#18134c', treatment='t-chart'),
  tags=['team required','third stage - check','free','no eligibility bar']),

dict(id='powernext-ai', name='Powernext-AI',
  host='Manipal Institute of Technology, Bengaluru', platform='Unstop',
  url='https://unstop.com/hackathons/powernext-ai-manipal-institute-of-technology-bengaluru-1745296',
  domain='ai', kind='Hackathon',
  blurb='An AI hackathon run by MIT Bengaluru, listed on Unstop.',
  submit='Not stated on the listing.',
  fmt='remote', location='Listed as city work location on Unstop. The host is in Bengaluru, where you are now.',
  travel='Not stated on the listing.',
  fee='FREE. Unstop marks it not paid.',
  prize='&#8377;50,000 / &#8377;30,000 / &#8377;20,000, with further &#8377;50,000 and &#8377;30,000 '
        'prizes listed.',
  team='3 to 5 members. YOU CANNOT ENTER ALONE.',
  eligible='Undergraduate and engineering students.',
  effort='Light to moderate.',
  difficulty=2,
  deadline_text='Registration closes 10 September 2026. Listing end date 11 September 2026.',
  deadline='2026-09-11', precision='exact',
  extra='701 registered when the listing was read.',
  why='Bengaluru-hosted, which for the next few weeks is where you are.',
  view='A week, and a minimum team of three. Realistically closed to you unless you already have two '
       'people. On the wall because it is local and because you asked to see the borderline ones.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#fbf0e9', ink='#4c240b', rule='#4c240b', treatment='t-ticket'),
  tags=['Bengaluru','team of 3 minimum','one week','probably closed to you']),

dict(id='agentic-graphrag', name='Agentic GraphRAG Hackathon',
  host='TigerGraph', platform='Unstop',
  url='https://unstop.com/hackathons/agentic-graphrag-hackathon-tigergraph-1747871',
  domain='ai', kind='Corporate hackathon',
  blurb='Build agentic retrieval-augmented generation over graph data, run by TigerGraph.',
  submit='Not stated on the listing.',
  fmt='remote', location='Listed as city work location on Unstop; the city is not printed.',
  travel='Not stated on the listing.',
  fee='FREE. Unstop marks it not paid.',
  prize='&#8377;35,000 first, &#8377;20,000 second, &#8377;15,000 third.',
  team='1 to 5 members.',
  eligible='Undergraduate, postgraduate, engineering students, management, arts and commerce.',
  effort='Moderate. GraphRAG is a specific technique you would have to learn first.',
  difficulty=3,
  deadline_text='Registration closes 14 September 2026. Listing end date 5 October 2026.',
  deadline='2026-10-05', precision='exact',
  extra='Only 68 registered when the listing was read &mdash; the smallest field of any Unstop bill here.',
  why='Sixty-eight entrants for &#8377;70,000, and GraphRAG over a medical knowledge graph is a '
      'genuinely good project idea rather than a contrived one.',
  view='The technique is worth learning on its own account: retrieval over a structured graph is how '
       'you would build anything that answers questions from a drug formulary or a guideline set. '
       'Tiny field, entry alone allowed, three weeks. Good odds.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#e5fbf4', ink='#224c3f', rule='#224c3f', treatment='t-gazette'),
  tags=['GraphRAG','tiniest field','solo allowed','good odds']),

dict(id='void-hacks-8', name='Void Hacks() 8.0',
  host='Shri Vaishnav Vidyapeeth Vishwavidyalaya, Indore', platform='Unstop',
  url='https://unstop.com/hackathons/void-hacks-80-shri-vaishnav-vidyapeeth-vishwavidyalaya-svvv-indore-1745016',
  domain='build', kind='Hackathon',
  blurb='The eighth edition of a university hackathon, listed on Unstop.',
  submit='Not stated on the listing.',
  fmt='remote', location='Listed as city work location on Unstop. Host is in Indore.',
  travel='Not stated on the listing.',
  fee='FREE. Unstop marks it not paid.',
  prize='&#8377;50,000 first, &#8377;30,000 second, &#8377;20,000 third.',
  team='Not printed in the fields read.',
  eligible='Not printed in the fields read beyond the standard Unstop student filters.',
  effort='Light.',
  difficulty=2,
  deadline_text='Listing end date 16 September 2026.',
  deadline='2026-09-16', precision='exact',
  extra='171 registered when the listing was read. An eighth edition means it comes round annually.',
  why='Free, &#8377;1 lakh, and it recurs &mdash; so even a miss tells you when to look next year.',
  view='Thirteen days. Enter if you have something ready. Otherwise note the name for next year: an '
       'eighth edition is a fixture, and fixtures are what a radar should be tracking.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#fae2fb', ink='#612363', rule='#612363', treatment='t-riso'),
  tags=['annual fixture','free','short','note for next year']),

dict(id='semicon-sarcathon', name='SemiCon Hackathon &mdash; Sarcathon 2026',
  host='IIT Bombay', platform='Unstop',
  url='https://unstop.com/hackathons/semicon-hackathon-explore-innovate-build-with-semiconductors-sarcathon-2026-iit-bombay-1744747',
  domain='build', kind='Hackathon',
  blurb='Explore, innovate and build with semiconductors, run by IIT Bombay as part of Sarcathon 2026.',
  submit='Not stated on the listing.',
  fmt='remote', location='Listed as city work location on Unstop. Host is IIT Bombay.',
  travel='Not stated on the listing.',
  fee='FREE. Unstop marks it not paid.',
  prize='&#8377;5,00,000 stated as a single figure on the listing; no split is printed.',
  team='Not printed in the fields read.',
  eligible='Not printed in the fields read beyond the standard Unstop student filters.',
  effort='Heavy if it genuinely means semiconductor work.',
  difficulty=4,
  deadline_text='Listing end date 31 October 2026.',
  deadline='2026-10-31', precision='exact',
  extra='174 registered when the listing was read. &#8377;5 lakh is the second largest rupee prize '
        'on this wall.',
  why='IIT Bombay, &#8377;5 lakh, free, and nearly two months of runway.',
  view='The subject is the question, not the money: semiconductors is the furthest from anything you '
       'have done. Open the page and read what &ldquo;build with semiconductors&rdquo; actually '
       'requires before committing &mdash; if it means fabrication or hardware you do not have, walk '
       'away early rather than late.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#f6f9f0', ink='#506319', rule='#506319', treatment='t-bulletin'),
  tags=['IIT Bombay','Rs 5 lakh','subject may not fit','read it first']),

dict(id='prysm-26', name='Prysm&rsquo;26',
  host='Eshan Group of Institutions, Uttar Pradesh', platform='Unstop',
  url='https://unstop.com/hackathons/prysm26-eshan-group-of-institutions-uttar-pradesh-1747181',
  domain='build', kind='Hackathon',
  blurb='A college hackathon listed on Unstop.',
  submit='Not stated on the listing.',
  fmt='remote', location='Listed as city work location on Unstop; the city is not printed.',
  travel='Not stated on the listing.',
  fee='FREE. Unstop marks it not paid.',
  prize='&#8377;25,000 first, &#8377;15,000 second, &#8377;10,000 third.',
  team='2 to 4 members. YOU CANNOT ENTER ALONE.',
  eligible='Undergraduate, postgraduate, engineering students, management, arts and commerce.',
  effort='Light.',
  difficulty=1,
  deadline_text='Registration closes 1 October 2026.',
  deadline='2026-10-01', precision='exact',
  extra='Only 38 registered when the listing was read.',
  why='Thirty-eight entrants for &#8377;50,000. The arithmetic is favourable even if the prestige is not.',
  view='Needs a partner. If you find one for the Rice hackathon, use the same person here &mdash; '
       'the effort is low and the field is tiny.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#edf2f9', ink='#0f3563', rule='#0f3563', treatment='t-stencil'),
  tags=['tiny field','team of 2 minimum','low effort','free']),

dict(id='slay-ctf', name='Slay CTF',
  host='Jalpaiguri Government Engineering College', platform='Unstop',
  url='https://unstop.com/hackathons/slay-ctf-jalpaiguri-government-engineering-college-jgec-west-bengal-1743206',
  domain='build', kind='Capture-the-flag security contest',
  blurb='A jeopardy-style capture-the-flag: exploit vulnerabilities, crack ciphers and trace digital '
        'footprints against a global leaderboard. Printed on the listing as being built for both '
        'ends of the range &mdash; &ldquo;a beginner looking to break into the world of '
        'cybersecurity&rdquo; and &ldquo;a seasoned hacker hunting for complex challenges&rdquo;.',
  submit='Flags, submitted through the CTF platform. The format is not further described on the listing.',
  fmt='remote', location='Online', travel='None &mdash; the Unstop region field says online.',
  fee='FREE. The Unstop API returns isPaid false and no registration fee.',
  prize='Not stated. The prize array on the listing is empty, and no cash figure is printed anywhere '
        'on it.',
  team='1 to 3 members.',
  eligible='Printed on the listing: &ldquo;Open to all students (UG/PG/Diploma), early-career '
           'professionals, and self-taught security&rdquo; enthusiasts.',
  effort='Moderate. CTF is a distinct skill you have not practised, and the whole point of a long '
         'runway is that you can practise it.',
  difficulty=3,
  deadline_text='Registration runs 23 August to <b>30 November 2026</b>, read off the Unstop public '
                'API on 7 September 2026.',
  deadline='2026-11-30', precision='exact',
  extra='410 registered and 148,305 views when read &mdash; a far bigger field than Seize da Flaq, '
        'which is the other CTF on this wall. Take this one for the learning and that one for the '
        'odds; they do not clash, since this closes eight days after it.',
  why='<b>Twelve weeks of runway on a beginner-friendly CTF is the single best learn-something '
      'setup on this wall.</b> Security rewards puzzle-solving over credentials more than any other '
      'technical field, and it asks for no prior work, no CV and no institution.',
  view='Enter this one to learn, not to place. The listing says in its own words that beginners are '
       'the intended audience, and twelve weeks is enough to work through a beginner CTF course '
       'before you touch a single challenge. The prize is unstated, so assume there is none and let '
       'that be fine &mdash; what you keep is the skill and a leaderboard position you can point at.',
  conf='listing', checked='2026-09-07',
  theme=dict(paper='#dce8f5', ink='#173a5e', rule='#173a5e', treatment='t-stencil'),
  tags=['CTF','beginners welcome','twelve weeks','free']),

dict(id='seize-da-flaq', name='Seize da Flaq',
  host='Cyberonites Club', platform='Unstop',
  url='https://unstop.com/hackathons/seize-da-flaq-cyberonites-club-1724723',
  domain='build', kind='Capture-the-flag security contest',
  blurb='A capture-the-flag security competition listed on Unstop.',
  submit='Not stated on the listing.',
  fmt='remote', location='Listed as city work location on Unstop; the city is not printed.',
  travel='Not stated on the listing.',
  fee='FREE. Unstop marks it not paid.',
  prize='&#8377;15,000 first, &#8377;10,000 second, &#8377;5,000 third.',
  team='1 to 3 members.',
  eligible='Undergraduate, postgraduate, engineering students, management, arts and commerce.',
  effort='Moderate. CTF is a distinct skill you have not practised.',
  difficulty=3,
  deadline_text='Registration closes 16 October 2026. Listing end date 22 November 2026.',
  deadline='2026-11-22', precision='exact',
  extra='Only 11 registered when the listing was read, and the runway is the longest of any Unstop '
        'bill here.',
  why='Nearly three months of runway and eleven entrants. Security is also the one technical field '
      'where puzzle-solving beats prior experience more often than not.',
  view='Longest runway on Unstop by a distance, so this is the one you can actually prepare for. If '
       'you have never done a CTF, that is an argument for entering rather than against &mdash; '
       'there is time to learn, and eleven people are competing.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#f9e9ec', ink='#632d35', rule='#632d35', treatment='t-hoard'),
  tags=['CTF','three months','eleven entrants','time to learn']),

dict(id='paradox-hackathon', name='Paradox Hackathon',
  host='Institute of Engineering and Management, Kolkata', platform='Unstop',
  url='https://unstop.com/hackathons/paradox-hackathon-institute-of-engineering-management-kolkata-1747830',
  domain='build', kind='Hackathon',
  blurb='A college hackathon listed on Unstop.',
  submit='Not stated on the listing.',
  fmt='remote', location='Listed as city work location on Unstop. Host is in Kolkata.',
  travel='Not stated on the listing.',
  fee='FREE. Unstop marks it not paid.',
  prize='&#8377;15,000 first, &#8377;10,000 second, &#8377;5,000 third.',
  team='3 to 4 members. YOU CANNOT ENTER ALONE.',
  eligible='UNDERGRADUATE AND ENGINEERING STUDENTS ONLY &mdash; a narrower filter than most Unstop '
           'listings here.',
  effort='Light.',
  difficulty=1,
  deadline_text='Registration closes 25 September 2026. Listing end date 3 October 2026.',
  deadline='2026-10-03', precision='exact',
  extra='Only 3 registered when the listing was read.',
  why='Three entrants. That is the entire argument.',
  view='Needs three people minimum, and the eligibility filter is undergraduate and engineering, '
       'which you will satisfy as an MBBS undergraduate but might be asked to prove. Low value, '
       'trivially low competition. Take it only if a team already exists.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#e6f9e9', ink='#23632b', rule='#23632b', treatment='t-ticket'),
  tags=['three entrants','team of 3 minimum','low value','narrow eligibility']),

dict(id='nasa-space-apps', name='NASA Space Apps Challenge 2026',
  host='NASA', platform='spaceappschallenge.org',
  url='https://www.spaceappschallenge.org/2026/',
  domain='open', kind='Global hackathon',
  blurb='The largest annual global hackathon, run by NASA on open space and Earth-science data, '
        'across hundreds of local events worldwide plus a universal online event.',
  submit='A project submitted through your local or universal event.',
  fmt='hybrid', location='450+ local events worldwide plus a Universal Event. Registration is open.',
  travel='Depends which event you join. A local event means travelling to that city; the Universal '
         'Event does not. Costs are not stated.',
  fee='Not stated', prize='Not stated on the page read',
  team='<b>No more than six participants per team</b>, printed on the 2026 page.',
  eligible='&ldquo;All ages, skill levels, and professional backgrounds are welcome.&rdquo;',
  effort='Light. It is a weekend.',
  difficulty=2,
  deadline_text='The event runs 14&ndash;15 November 2026. Registration is open now; a closing date '
                'for registration is not stated.',
  deadline='2026-11-15', precision='exact',
  extra='Ten weeks away, and India hosts a large number of local events every year.',
  why='TEN WEEKS OF NOTICE for the biggest open hackathon in the world, with no eligibility bar of '
      'any kind. This is what the wall is for &mdash; you are hearing about it in September for '
      'something in November.',
  view='Register now and pick the event later. It is one weekend, it costs nothing, the data is '
       'genuinely interesting, and by November you will be settled wherever you are studying. '
       'Check the local-events list for a city near your new college before defaulting to the '
       'universal event &mdash; being in a room matters more here than at most hackathons.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#ece3f9', ink='#461f7a', rule='#461f7a', treatment='t-gazette'),
  tags=['NASA','all ages welcome','ten weeks notice','one weekend']),

dict(id='mlh-ghw-data', name='Global Hack Week: Data',
  host='Major League Hacking', platform='MLH',
  url='https://events.mlh.io/events/14416-global-hack-week-data',
  domain='open', kind='Week-long online hack week',
  blurb='One of MLH&rsquo;s Global Hack Weeks: a week of daily online challenges and workshops, this '
        'edition themed on data.',
  submit='Daily challenges submitted through the MLH event platform.',
  fmt='remote', location='&ldquo;Digital Only.&rdquo;',
  travel='None.',
  fee='Not stated', prize='Not stated on the listing',
  team='Not stated on the listing',
  eligible='<b>Explicitly open to university students</b> &mdash; the page lists its audience outright: &ldquo;Minors (Between 13-18), Working Professionals, Students &mdash; University Students, Secondary/High School Students, Other&rdquo;. Participants must be &ldquo;either over 18 years of age or have a parent&rsquo;s permission&rdquo;; at eighteen you clear that alone. This card previously said MLH events are &ldquo;generally student-oriented&rdquo;, which was an inference. The page states it.',
  effort='Light. Daily bite-sized challenges rather than one build.',
  difficulty=1,
  deadline_text='11&ndash;17 September 2026.',
  deadline='2026-09-17', precision='exact',
  extra='MLH&rsquo;s 2026 season is over; this is the 2027 season, which nobody would think to look '
        'for in September 2026. That naming trap is why the first sweep of MLH found only expired '
        'events.',
  why='Digital only, a week long, daily challenges rather than a single deadline, and themed on '
      'data. About as low-commitment as a real hack week gets.',
  view='Good week to dip into while everything else here is still in its build phase. It starts in '
       'eight days and asks for an hour a day rather than a weekend.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#f9f2e0', ink='#7a5d12', rule='#7a5d12', treatment='t-riso'),
  tags=['online only','one hour a day','data themed','MLH']),

dict(id='hackcbs-9', name='hackCBS 9.O',
  host='Shaheed Sukhdev College of Business Studies', platform='MLH',
  url='https://hackcbs.tech/',
  domain='build', kind='In-person student hackathon',
  blurb='One of India&rsquo;s largest student hackathons, held in New Delhi and part of the MLH 2027 '
        'season.',
  submit='Not stated on the MLH listing.',
  fmt='in-person', location='NEW DELHI, INDIA.',
  travel='YOU MUST TRAVEL TO NEW DELHI. Travel and accommodation terms are not stated on the listing.',
  fee='Not stated', prize='Not stated on the MLH listing',
  team='Not stated on the MLH listing', eligible='Not stated on the MLH listing',
  effort='A weekend, plus travel.',
  difficulty=2,
  deadline_text='31 October to 1 November 2026. The application deadline is not stated on the MLH '
                'listing.',
  deadline='2026-10-31', precision='exact',
  why='The best-known student hackathon in India, two months out, and you will know by then where '
      'you are living.',
  view='Only worth it if your college turns out to be in or near Delhi, or if you want the trip. '
       'Listed because it is two months away and the decision is genuinely yours to make later '
       '&mdash; which is only possible because you know about it now.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#edf6f6', ink='#377a7a', rule='#377a7a', treatment='t-chart'),
  tags=['New Delhi','in person','two months out','depends where you land']),

dict(id='hacknex-s2', name='HackNex Season 2',
  host='Innovocon', platform='MLH',
  url='https://innovocon.online/events/hacknex',
  domain='build', kind='In-person student hackathon',
  blurb='A student hackathon in Kalyani, West Bengal, part of the MLH 2027 season.',
  submit='Not stated on the MLH listing.',
  fmt='in-person', location='KALYANI, INDIA.',
  travel='YOU MUST TRAVEL TO KALYANI, WEST BENGAL. Terms not stated.',
  fee='Not stated', prize='Not stated on the MLH listing',
  team='Not stated on the MLH listing', eligible='Not stated on the MLH listing',
  effort='A weekend, plus travel.',
  difficulty=2,
  deadline_text='25&ndash;26 September 2026. Application deadline not stated.',
  deadline='2026-09-26', precision='exact',
  why='Listed for completeness: it is one of only three Indian in-person events in the MLH season '
      'over the next two months.',
  view='Almost certainly not for you unless you are in West Bengal. On the wall because you asked '
       'for the borderline ones rather than my filtering, and because the travel is stated plainly '
       'enough that you can rule it out in five seconds.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#f6eaf3', ink='#7a2b62', rule='#7a2b62', treatment='t-letter'),
  tags=['Kalyani','in person','probably not for you','listed for completeness']),

dict(id='innohacks-4', name='Innohacks 4.0',
  host='Innohacks', platform='MLH',
  url='https://innohacks.live/',
  domain='build', kind='In-person student hackathon',
  blurb='A student hackathon in Ghaziabad, part of the MLH 2027 season.',
  submit='Not stated on the MLH listing.',
  fmt='in-person', location='GHAZIABAD, INDIA.',
  travel='YOU MUST TRAVEL TO GHAZIABAD, UTTAR PRADESH. Terms not stated.',
  fee='Not stated', prize='Not stated on the MLH listing',
  team='Not stated on the MLH listing', eligible='Not stated on the MLH listing',
  effort='A weekend, plus travel.',
  difficulty=2,
  deadline_text='10&ndash;11 October 2026. Application deadline not stated.',
  deadline='2026-10-11', precision='exact',
  why='Same reason as HackNex: one of the few Indian in-person MLH events in range.',
  view='Ghaziabad is next to Delhi, so if you go to hackCBS at the end of October this is the same '
       'part of the country three weeks earlier. Otherwise skip it.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#edf6e7', ink='#447a1f', rule='#447a1f', treatment='t-letter'),
  tags=['Ghaziabad','in person','near Delhi','skip unless travelling']),

dict(id='muba-blockchain', name='MUBA Blockchain Hackathon',
  host='MUBA', platform='Devfolio',
  url='https://muba-hackathon.devfolio.co/',
  domain='build', kind='Online hackathon',
  blurb='A blockchain hackathon, and the only ONLINE hackathon with applications open on Devfolio '
        'when it was checked &mdash; the other nine were all offline college events.',
  submit='Not stated on the Devfolio listing.',
  fmt='remote', location='Listed as ONLINE on Devfolio.',
  travel='None stated.',
  fee='Not stated', prize='Not stated on the Devfolio listing',
  team='Not stated on the Devfolio listing',
  eligible='Devfolio lists the theme restriction as &ldquo;No restrictions&rdquo;. Nothing else is '
           'printed on the listing.',
  effort='Moderate, and in a subject you have not touched.',
  difficulty=3,
  deadline_text='Listed as LIVE with applications open. NO DATES ARE PRINTED on the Devfolio listing.',
  deadline='', precision='none',
  extra='Devfolio was one of the three sources his brother named and it had never been opened. Ten '
        'hackathons had applications open; nine were offline Indian college events with no city '
        'printed on the listing.',
  why='Included because it is the one online option on a source that was named as a seed and never '
      'checked, not because blockchain is a fit.',
  view='I would not spend a weekend on this. Blockchain is not in anything you have said you want, '
       'and no prize, dates or eligibility are printed. It is on the wall so that Devfolio is '
       'honestly represented rather than silently skipped &mdash; and so you can see that Devfolio '
       'is mostly offline college events, which is the useful finding about that source.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#e4e6f6', ink='#0b134c', rule='#0b134c', treatment='t-hoard'),
  tags=['blockchain','no dates printed','poor fit','source now checked']),

dict(id='code-kitchen', name='Code Kitchen S01',
  host='AIM (Analytics India Magazine)', platform='HackerEarth',
  url='https://codekitchen.aim.media/',
  domain='build', kind='Televised build competition',
  blurb='A reality-show format: submit a concept note, audition through virtual tasks and '
        'interviews, then build using pre-funded Google Cloud credits and submit code with a video '
        'screentest. Winners are paired into ten teams of two for a studio phase.',
  submit='A concept note first, then code plus a video screentest.',
  fmt='hybrid', location='Auditions are virtual and nationwide. THE STUDIO PHASE IS FILMED IN A '
                         'STUDIO &mdash; the location is not stated.',
  travel='Implied by the studio phase but the terms are not stated.',
  fee='Not stated',
  prize='&#8377;10,00,000 total prize pool, a Season Best trophy, and free pre-funded Google Cloud '
        'sandbox access.',
  team='Individual registration for auditions. Winners are paired into teams of two for the studio '
       'phase.',
  eligible='Stated as &ldquo;India&rsquo;s working developers&rdquo;. YOU ARE A STUDENT, NOT A '
           'WORKING DEVELOPER, so you may well not qualify. No experience requirement is printed.',
  effort='Heavy, and it takes over your calendar if you get through.',
  difficulty=3,
  deadline_text='NO DATES ARE PRINTED on the page. It is listed as Live on HackerEarth.',
  deadline='', precision='none',
  why='&#8377;10 lakh and Google Cloud credits, listed for completeness because HackerEarth had '
      'never been opened.',
  view='Probably not for you and I would rather say it on the card than let you fill in a concept '
       'note first. It says working developers, it has no printed dates, and the studio phase is a '
       'television commitment. Read it, but expect to be out on eligibility.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#f6e4e1', ink='#4c2a22', rule='#4c2a22', treatment='t-night'),
  tags=['Rs 10 lakh','working developers only','no dates','probably ineligible']),

dict(id='numerai', name='Numerai Tournament',
  host='Numerai', platform='numer.ai',
  url='https://numer.ai/',
  domain='ai', kind='Continuous data science tournament',
  blurb='Build machine learning models on obfuscated financial data and submit predictions of stock '
        'performance every round. The tournament runs continuously rather than in editions.',
  submit='A CSV of predicted stock performance, from features and historical targets they provide.',
  fmt='remote', location='Entirely online',
  travel='None stated at any stage.',
  fee='Not stated. YOU MAY OPTIONALLY STAKE CRYPTOCURRENCY on your model to earn &mdash; '
      'or BURN &mdash; it. Staking is not required to participate.',
  prize='Models are described as &ldquo;paid to data scientists&rdquo;. No payout amounts or '
        'structure are printed on the page.',
  team='Not stated',
  eligible='No tournament eligibility restriction is printed. A disclaimer about the FUND (not the '
           'tournament) says it is designed for institutional investors with some accredited '
           'individuals.',
  effort='Moderate, and continuous rather than one-off.',
  difficulty=3,
  deadline_text='No deadline. It runs in continuous rounds, permanently.',
  deadline='', precision='none',
  extra='THE STAKING PART IS HOW YOU CAN LOSE MONEY HERE. Everything else on this wall can only cost '
        'you time.',
  why='A permanently open tournament with obfuscated data, so it is pure modelling with no domain '
      'knowledge to acquire.',
  view='Submit without staking, if at all. The unstaked tournament is a free, permanent leaderboard '
       'to practise on. DO NOT STAKE CRYPTOCURRENCY &mdash; you are eighteen, it is your money, and '
       'nothing about learning machine learning requires putting funds at risk. I am flagging that '
       'rather than leaving it in the small print.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#ddf6e9', ink='#1b4c32', rule='#1b4c32', treatment='t-chart'),
  tags=['permanent','no domain knowledge needed','DO NOT STAKE','free to enter']),

dict(id='xprize-quantum', name='XPRIZE Quantum Applications',
  host='XPRIZE Foundation', platform='xprize.org',
  url='https://www.xprize.org/prizes/qc-apps',
  domain='quantum', kind='Multi-year global prize',
  blurb='A $5 million prize for demonstrating a real-world application of quantum computing. One of '
        'three XPRIZE competitions currently marked Active, alongside Water Scarcity ($119M) and '
        'Healthspan ($101M).',
  submit='Referenced in the Competition Guidelines document; not detailed on the page itself.',
  fmt='remote', location='Not stated',
  travel='None stated. The prize page describes no in-person requirement.', fee='No fee is named anywhere on the prize page. Two conditions are: the competition is &ldquo;void in those countries where prohibited or restricted by U.S. law&rdquo;, and XPRIZE &ldquo;reserves the right to limit, or restrict upon notice, participation &hellip; to any person or entity at any time for any reason&rdquo;.',
  prize='$5,000,000 total purse. The split across phases is not stated on the page.',
  team='No size limit is printed. The composition, in their words, is deliberately broad: XPRIZE competitions are &ldquo;driven by teams of innovative groups and individuals, comprising subject matter experts, enthusiasts, start-ups, <b>student teams</b>, amateurs, and all problem-solvers in between&rdquo;. The detailed rules sit in a separate guidelines PDF that this page only links to.',
  eligible='&ldquo;XPRIZE competitions are driven by teams of innovative groups and individuals, '
           'comprising subject matter experts, enthusiasts, start-ups, student teams, amateurs, and '
           'all problem-solvers in between.&rdquo; No age requirement is printed.',
  effort='Multi-year. This is not a hackathon.',
  difficulty=5,
  deadline_text='NO CURRENT DEADLINE IS PRINTED. The only dates on the page are Phase II Wild Card '
                'Registration, which opened 14 January 2026 and CLOSED 4 March 2026.',
  deadline='', precision='none',
  extra='XPRIZE Healthspan, at $101 million, is the medical one &mdash; but it is a team-and-'
        'institution effort measured over years, not something a student enters.',
  why='On the wall so that XPRIZE is represented honestly: three prizes are active, the money is '
      'enormous, and the entry windows are effectively closed to a newcomer right now.',
  view='Not enterable today, and I am not going to dress it up. The value of this card is knowing '
       'the series exists and that the windows open and shut on a multi-year cycle. Look again in a '
       'year, when you have a lab and colleagues.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#f1ebf4', ink='#3f134c', rule='#3f134c', treatment='t-night'),
  tags=['$5 million','no open window','multi-year','look again in a year']),

dict(id='reliance-foundation-ug', name='Reliance Foundation Undergraduate Scholarships 2026-27',
  host='Reliance Foundation', platform='Buddy4Study',
  url='https://www.buddy4study.com/scholarship/reliance-foundation-undergraduate-scholarships-2026-27',
  domain='open', kind='Scholarship',
  blurb='An undergraduate scholarship worth up to &#8377;2,00,000, listed among the live medical '
        'scholarships on Buddy4Study.',
  submit='An online application. Details are not printed on the listing page.',
  fmt='remote', location='Application is online',
  travel='None stated.',
  fee='Not stated', prize='Up to &#8377;2,00,000',
  team='Individual application.',
  eligible='&ldquo;For UG students.&rdquo; NOTHING FURTHER IS PRINTED &mdash; course, year, income '
           'limit and exam requirement are all absent from the pages read.',
  effort='An afternoon of paperwork.',
  difficulty=1,
  deadline_text='The category listing shows a deadline of 5 October 2026; the scholarship&rsquo;s '
                'own page says &ldquo;Always Open&rdquo;. THE TWO PAGES DISAGREE and I have not '
                'resolved which is right.',
  deadline='2026-10-05', precision='derived',
  extra='The two dates conflict, so the earlier one is used here. Treat 5 October as the date and '
        'verify on the official Reliance Foundation site before relying on it.',
  why='&#8377;2,00,000 for being an undergraduate, on the same source that turned up the SBI medical '
      'scholarship.',
  view='Worth twenty minutes to check the real eligibility on Reliance Foundation&rsquo;s own site, '
       'because Buddy4Study prints almost nothing. Do the SBI Asha one first &mdash; that one has '
       'full criteria printed and a harder deadline.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#f3f4e8', ink='#494c0b', rule='#494c0b', treatment='t-gazette'),
  tags=['scholarship','conflicting dates','eligibility not printed','verify at source']),

dict(id='csh-social-impact', name='CSH Social Impact Ideathon',
  host='CyberSyntax Hub', platform='Devpost',
  url='https://csh-social-impact-ideathon.devpost.com/',
  domain='open', kind='Online ideathon',
  blurb='An ideathon rather than a hackathon &mdash; low/no-code, open-ended, social good. You '
        'submit an idea, not a working system.',
  submit='A Devpost project submission.',
  fmt='remote', location='Online',
  travel='None stated at any stage.',
  fee='Not stated',
  prize='NO CASH. Seven non-cash prizes are listed.',
  team='Not stated in the eligibility block',
  eligible='Not read individually &mdash; the Devpost API does not return the eligibility block.',
  effort='Very light. It is an idea, and low/no-code is explicitly in scope.',
  difficulty=1,
  deadline_text='Submission period 31 August to 11 September 2026. Deadline 11 September 2026.',
  deadline='2026-09-11', precision='exact',
  extra='45 registered when the listing was read.',
  why='An ideathon asks for the thing you are actually good at &mdash; seeing a problem clearly '
      '&mdash; without needing a working build.',
  view='Eight days and no money, so this is purely about getting a submission behind you. If you '
       'have never entered anything, enter this one first: writing up a health idea properly takes '
       'an evening and removes the psychological barrier to the bigger bills here.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#e5eef4', ink='#2d5163', rule='#2d5163', treatment='t-stencil'),
  tags=['ideathon','no code needed','no cash','start here if nervous']),

dict(id='zindi-briisp', name='Briisp Academy University Hackathon &mdash; AI4D Tourism Classification',
  host='Briisp Academy', platform='Zindi',
  url='https://zindi.world/competitions/ai4d-lab-tanzania-tourism-classification-challenge-briisp-academy',
  domain='ai', kind='Short university hackathon',
  blurb='A four-day classification hackathon on Zindi, run by Briisp Academy under the AI4D Lab '
        'Tanzania programme.',
  submit='Submissions through Zindi.',
  fmt='remote', location='Entirely online',
  travel='None stated at any stage.',
  fee='Free. Zindi requires open-source tools only.',
  prize='500 Zindi points. NO CASH PRIZE.',
  team='Zindi&rsquo;s standard team rules apply; a maximum size is not printed on this page.',
  eligible='NOT PRINTED. This page has no &ldquo;Who can compete&rdquo; line, unlike every other '
           'Zindi challenge here &mdash; and it is called a University Hackathon, so it may be '
           'restricted to a particular institution.',
  effort='Very light. Four days.',
  difficulty=1,
  deadline_text='Starts 9 September 2026, closes 13 September 2026.',
  deadline='2026-09-13', precision='exact',
  why='It has not started yet, it is four days long, and it is a clean classification task &mdash; '
      'the cheapest possible way to make your first Zindi submission.',
  view='Points only, and the eligibility is not printed, which is the one thing to check before '
       'starting. If it is open, use it as a dry run for the Climate Risk and Health challenge: same '
       'platform, same submission mechanics, nothing at stake.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#f4e2e8', ink='#63233a', rule='#63233a', treatment='t-ticket'),
  tags=['four days','dry run','eligibility not printed','no cash']),

dict(id='crunchdao-structural-break', name='ADIA Lab Structural Break Challenge &mdash; Real-Time Edition',
  host='ADIA Lab', platform='CrunchDAO',
  url='https://hub.crunchdao.com/competitions/structural-break-real-time',
  domain='ai', kind='Quantitative data science competition',
  blurb='Detect structural breaks in real-time time series &mdash; the moment where the process '
        'generating a signal changes character.',
  submit='Not stated. The CrunchDAO page renders its details behind the platform shell and could not '
         'be read without an account.',
  fmt='remote', location='Entirely online',
  travel='Not stated.',
  fee='Not stated',
  prize='$100,000, as listed by ML Contests. The figure is NOT confirmed on CrunchDAO&rsquo;s own '
        'page, which did not render.',
  team='Not stated', eligible='Not stated',
  effort='Moderate to heavy.',
  difficulty=4,
  deadline_text='NOT STATED. Neither the CrunchDAO page nor the ML Contests listing printed a '
                'closing date that could be read.',
  deadline='', precision='none',
  extra='CrunchDAO is one of eight platforms found today that this wall had never named &mdash; the '
        'others are Solafune, ThinkOnward, Antigranular, Bitgrit, CodaLab, Trustii and Hugging Face '
        'competitions. None of the other seven has been harvested yet.',
  why='Change-point detection is the same mathematics as noticing a patient has deteriorated, and '
      'the pot is six figures.',
  view='The weakest-verified card on this wall and it says so: the platform needs an account before '
       'it will show you anything, so the prize is second-hand from an aggregator and there is no '
       'deadline at all. Open it yourself before trusting a single figure here. It is listed because '
       'leaving out a $100,000 competition because a page would not load is exactly the kind of '
       'silent gap you asked me to stop leaving.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#e0f4de', ink='#1e6319', rule='#1e6319', treatment='t-hoard'),
  tags=['unverified figures','account needed','new platform','check it yourself']),

]


BILLS.append(dict(
 id='mhtechin-innovation',
 domain='open',
 kind='National innovation challenge',
 name='MHTECHIN Innovation Challenge 2026',
 host='MHTECHIN',
 platform='Unstop',
 url='https://unstop.com/competitions/mhtechin-innovation-challenge-2026-mhtechin-1715258',
 blurb='A national online innovation competition asking teams to turn an idea into something practical and scalable. Named domains include artificial intelligence, data science, healthcare, cybersecurity, robotics, IoT, sustainability and agritech.',
 submit='Not stated on the record beyond the idea-to-solution framing.',
 fmt='remote',
 location='Online, national',
 travel='None stated.',
 fee='Free.',
 prize='&#8377;5,00,000 first, &#8377;3,00,000 second, &#8377;1,00,000 third.',
 team='<b>TEAM REQUIRED: two to five members.</b> You cannot enter this alone.',
 eligible='The record names undergraduate, postgraduate, engineering, management, law, <b>Medical</b>, arts/commerce/sciences, freshers and experienced professionals, with the sector given as students.',
 effort='Moderate, spread over seven weeks.',
 difficulty=3,
 deadline_text='Opened 10 July 2026, closes <b>31 October 2026, 23:59</b>.',
 deadline='2026-10-31',
 precision='exact',
 why='<b>Fifty-one days of runway</b> &mdash; the longest of anything added today &mdash; real prize money, healthcare named as a domain, and medicine named in the eligibility. This is the shape of thing this wall exists to hand you early rather than late.',
 view='The obstacle is not the work, it is the <b>minimum team of two</b>. You cannot submit this alone, so the first move is finding one person, and seven weeks is enough time to do that properly rather than in a panic. Two honest cautions: the organiser is a private company rather than an institution, and a &#8377;5,00,000 first prize from a company you have not heard of is worth verifying on their own site before you build a plan around the money. The work would still be worth doing.',
 conf='verified',
 checked='2026-09-10',
 theme={'paper': '#fce9dd', 'ink': '#8a3a12', 'rule': '#8a3a12', 'treatment': 't-bulletin'},
 tags=['long runway', 'TEAM REQUIRED', 'medicine named', 'healthcare', 'verify the prize'],
))

BILLS.append(dict(
 id='ies-student-innovation',
 domain='open',
 kind='Idea competition',
 name='Student Innovation &amp; Idea Challenge 2026',
 host='IES University, Bhopal',
 platform='Unstop',
 url='https://unstop.com/competitions/student-innovation-idea-challenge-2026-ies-university-bhopal-1750392',
 blurb='An idea competition for students: register, sit a quiz round, then an interactive challenge, then submit and present an idea that solves a real problem.',
 submit='An idea, presented. The record describes registration, a quiz or assessment round, an interactive challenge, then submission and presentation.',
 fmt='remote',
 location='Online',
 travel='None stated &mdash; the record gives the format as online.',
 fee='Free.',
 prize='The record prints <b>&#8377;20,00,000 against &ldquo;Grand Finale Winners&rdquo;</b> and &#8377;1,000 against a certificate tier, with finalist, popular-choice, campus-ambassador and semi-finalist tiers carrying no amount. <b>Treat that headline figure as unverified.</b>',
 team='Solo. Participation is individual.',
 eligible='Printed literally: &ldquo;Open to undergraduate and postgraduate students.&rdquo; The course list <b>includes <code>bs</code></b>.',
 effort='Light to moderate &mdash; it is an idea and a presentation, not a build.',
 difficulty=2,
 deadline_text='Opened 7 September 2026, closes <b>15 October 2026</b>.',
 deadline='2026-10-15',
 precision='exact',
 why='Thirty-five days of runway, solo, online, free, and open to undergraduates by its own words. The effort is an idea and a presentation rather than a build, which makes it one of the few things here you could do alongside the Gujarat submission rather than instead of it.',
 view='<b>Check the prize before you believe it.</b> A &#8377;20,00,000 grand prize from a private university is an extraordinary claim, and this wall has already published one prize that was fifty-three times too large because it was read off a page nobody opened properly. The competition looks real and the entry cost is nothing; enter it for the practice of framing an idea and presenting it, and confirm the money on IES University&rsquo;s own site before it shapes any decision. Note also it opens with a quiz round, so the first gate is not your idea.',
 conf='verified',
 checked='2026-09-10',
 theme={'paper': '#f5e8d8', 'ink': '#6b4a1d', 'rule': '#6b4a1d', 'treatment': 't-letter'},
 tags=['solo', 'free', 'idea only', 'verify the prize', 'quiz round first'],
))

BILLS.append(dict(
 id='krunch-analytics',
 domain='open',
 kind='Business case competition',
 name='Krunch &mdash; The Analytics Challenge',
 host='Department of Management Studies, IIT Madras',
 platform='Unstop',
 url='https://unstop.com/competitions/krunch-the-analytics-challenge-department-of-management-studies-doms-indian-institute-of-technology-iit-mad-1750484',
 blurb='A business case competition run by IIT Madras&rsquo; management school: analyse a real situation, find the problem, and argue a data-driven answer. A quiz round, a case submission, then a final presentation.',
 submit='Round 1 a quiz on Unstop, round 2 a case study submission, round 3 a final presentation &mdash; the record gives the last round as offline.',
 fmt='hybrid',
 location='Online for rounds 1 and 2; the final presentation is offline',
 travel='<b>The final round is offline</b> and the record does not say where.',
 fee='Free.',
 prize='&#8377;15,000 first, &#8377;10,000 second, &#8377;5,000 third.',
 team='One to three. Printed literally: &ldquo;Team members should be from the same institute.&rdquo;',
 eligible='Printed literally: &ldquo;This event is open to all college students.&rdquo; The course list <b>includes <code>bs</code></b>, which is the IIT Madras degree you are enrolled in.',
 effort='Moderate. Three rounds.',
 difficulty=3,
 deadline_text='Opened 7 September 2026, closes <b>27 September 2026, 23:59</b>.',
 deadline='2026-09-27',
 precision='exact',
 why='It is run by <b>your own institution</b> &mdash; you are an IIT Madras BS student and its course list names that degree &mdash; it is free, and a team of one is allowed, so the same-institute rule costs you nothing.',
 view='<b>Read what this actually is before you enter: it is a business case competition, not a data science one.</b> The record talks about business acumen and strategic decisions under constraint; the analytics is the tool, not the subject. That is worth knowing because a sibling event, the Students&rsquo; Research Conclave, was looked at on 7 September and left off this wall for being management rather than science. This one earns its place on the IIT Madras connection and the fact that structured problem-framing is a genuinely transferable skill &mdash; but it is not research, and I am not going to dress it up as research.',
 conf='verified',
 checked='2026-09-10',
 theme={'paper': '#dfe9e0', 'ink': '#31513a', 'rule': '#31513a', 'treatment': 't-clinic'},
 tags=['IIT Madras', 'your own institute', 'business case', 'free', 'solo allowed'],
))

BILLS.append(dict(
 id='math-o-stellar',
 domain='open',
 kind='Mathematics competition',
 name='Math-O-Stellar',
 host='IIT Bhubaneswar',
 platform='Unstop',
 url='https://unstop.com/hackathons/math-o-stellar-tech-zephyr-40-indian-institute-of-technology-bhubaneswar-1742777',
 blurb='A mathematics competition run as part of Tech Zephyr 4.0 at IIT Bhubaneswar.',
 submit='Not stated on the record.',
 fmt='remote',
 location='Not stated on the record',
 travel='Not stated on the record.',
 fee='Free.',
 prize='&#8377;6,000 winner, &#8377;4,000 first runner-up, &#8377;3,000 second runner-up, plus goodies and a participation certificate.',
 team='One or two.',
 eligible='The record states eligibility as <b>All</b> &mdash; no course, year or institution bar.',
 effort='Light. It is a maths contest, not a project.',
 difficulty=2,
 deadline_text='Opened 22 August 2026, closes <b>29 October 2026, 23:59</b>.',
 deadline='2026-10-29',
 precision='exact',
 why='Forty-nine days of runway, open to anyone, free, and small money against a real IIT&rsquo;s name. Mathematics is the one subject underneath both halves of what you are studying.',
 view='This is on the wall as a low-cost, long-runway thing rather than a priority, and I have rated its prestige accordingly &mdash; a college fest maths contest is not a credential. Take it if you want a deadline to push you into doing some mathematics, which by your own diary is something you keep meaning to do. Nothing about it should displace the Gujarat submission or the DREAM blind test.',
 conf='verified',
 checked='2026-09-10',
 theme={'paper': '#f7eef7', 'ink': '#5c3559', 'rule': '#5c3559', 'treatment': 't-gazette'},
 tags=['long runway', 'open to all', 'mathematics', 'free', 'small money'],
))


BILLS.append(dict(
 id='bharat-innovation-2',
 domain='open',
 kind='Online hackathon',
 name='Bharat Innovation Challenge 2.0',
 host='Bharat Innovation Challenge',
 platform='Devpost',
 url='https://bic.devpost.com/',
 blurb='An India-focused innovation hackathon run on Devpost, with the largest published prize pool of anything added to this wall today.',
 submit='A Devpost project submission.',
 fmt='remote',
 location='Online',
 travel='None stated.',
 fee='Not stated.',
 prize='&#8377;13,30,000 in prizes, with a Grand Champion Team tier at the top.',
 team='Not stated on the page read.',
 eligible='Printed literally in the eligibility list: <b>&ldquo;Ages 13 to 18 only&rdquo;.</b> <b>You are eighteen, so you qualify &mdash; and this is the last year you will.</b>',
 effort='Moderate. Three weeks of submission window.',
 difficulty=3,
 deadline_text='Submission period 9&ndash;30 September 2026. The page prints the deadline as <b>September 30 at 2:30pm EDT</b>, which is about midnight IST that night.',
 deadline='2026-09-30',
 precision='exact',
 why='<b>&#8377;13,30,000, and its eligibility rule is an age band that you are in the last year of.</b> Almost everything else on this wall is open to people years ahead of you; this one is closed to them and open to you, which is the rarest thing a competition can be.',
 view='<b>Of everything added today, act on this one first.</b> The age ceiling is the whole point: at nineteen you are simply not allowed to enter, so a competition you could win against a field capped at eighteen will not come round again. Three weeks is a real window. The page does not state a team rule or an entry fee, so read the rules tab before you build anything, and note the deadline is US Eastern &mdash; 2:30pm EDT is <b>midnight in India</b>, so it is effectively the night of the 30th, not the day.',
 conf='verified',
 checked='2026-09-10',
 theme={'paper': '#f0e4dd', 'ink': '#7a3a1f', 'rule': '#7a3a1f', 'treatment': 't-hoard'},
 tags=['AGE 13-18 ONLY', 'last year you qualify', 'big money', 'india', 'act first'],
))
