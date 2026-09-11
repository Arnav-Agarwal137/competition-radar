# -*- coding: utf-8 -*-
"""AI, ML and build bills. Same rules as bills_med.py."""

BILLS = [

dict(id='arc-whitebox', name='ARC White-Box Estimation Challenge 2026',
  host='ARC Prize Foundation', platform='AIcrowd',
  url='https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026',
  domain='ai', kind='Interpretability challenge',
  blurb='Predict, from a neural network&rsquo;s own weights, what its neurons will do &mdash; the '
        'per-neuron activation means &mdash; without running it.',
  submit='Executable Python code as a tarball containing an estimator.py.',
  fmt='remote', location='Entirely online. A NeurIPS workshop is planned for 11&ndash;12 December, TBD.',
  travel='None. Competing does not require attending anything.',
  fee='Free, and the rules say so in capitals: &ldquo;NO PURCHASE, PAYMENT, ENTRY FEE, OR '
      'DONATION IS NECESSARY TO ENTER OR PARTICIPATE IN THIS COMPETITION.&rdquo; ARC is a US '
      '501(c)(3) non-profit and the rules add that donating does not improve your chances.',
  prize='<b>$140,000 across both phases</b>, read off the Official Rules v14. Phase 1: $25,000 / '
        '$10,000 / $5,000. Phase 2: $50,000 / $20,000 / $10,000. Plus $20,000 for Best Algorithmic '
        'Contribution, judged on the idea rather than the leaderboard. The rules add that the '
        'sponsor may raise these or add further prizes at its own discretion. <b>This wall '
        'previously showed $100,000</b> &mdash; it carried the Phase 2 table and the algorithmic '
        'prize and had missed Phase 1 entirely.',
  team='<b>Solo or a team of up to five.</b> Each team appoints a &ldquo;Team Representative&rdquo; to '
       'enter on its behalf, and every member must meet the eligibility bar separately. '
       '<b>Teams must be finalised by 2 October 2026, 23:59 UTC</b> &mdash; the rules call it the Team '
       'Freeze Deadline, after which no new individual or team registrations are accepted at all. '
       'Multiple accounts, and submissions substantially authored by someone else, are violations.',
  eligible='Printed in the Official Rules. You must be <b>at least eighteen and have reached the age '
           'of majority where you live</b>, hold a valid email address for the duration, and have an '
           'active AIcrowd account; you also need internet access and a personal computer. The rules '
           'state the expected background plainly: &ldquo;Participants should have familiarity with '
           'Python and numerical computing sufficient to develop and submit Solutions.&rdquo; '
           'Residents of comprehensively sanctioned jurisdictions are barred from prizes.',
  effort='Heavy, but small and self-contained &mdash; no huge dataset to wrangle.',
  difficulty=4,
  deadline_text='<b>17 October 2026 &mdash; the Phase 2 deadline, when submissions close.</b> Read '
                'off the challenge&rsquo;s own live timeline, which prints the whole run: warm-up '
                '28 May, Phase 1 opened 18 June and <b>closed 10 August</b>, Phase 2 opened 22 '
                'August, submissions close 17 October. Phase 2 is what is live now. One earlier gate '
                'still binds and it is the one to diary: the Official Rules set a <b>Team Freeze on '
                '2 October, 23:59 UTC</b>, after which <b>no new registration is accepted at all</b> '
                '&mdash; so register before then even if you intend to submit later.',
  deadline='2026-10-17', precision='exact',
  extra='A separate $20,000 prize for the best algorithmic contribution, judged apart from the '
        'leaderboard. '
        '<b>DEADLINE CORRECTED 7 September 2026, and it had been a month early.</b> This card said '
        '19 September. A sweep for unread sources found the Official Rules v14 printing a Team Freeze '
        'of 2 October and a Competition Period running &ldquo;through October 31&rdquo; &mdash; two '
        'dates that could not both end the same thing as 19 September. That conflict was left flagged '
        'rather than guessed at, and then settled by opening the challenge&rsquo;s own timeline '
        'widget, which prints <b>17 October</b> against &ldquo;Phase 2 deadline, submissions '
        'close&rdquo;. <b>Had this not been checked, the wall would have retired the card on 19 '
        'September with four weeks still to run</b> &mdash; the failure this wall exists to prevent, '
        'produced by the wall itself.',
  why='A $140,000 pool on AIcrowd rather than Kaggle, which means a far smaller field.',
  view='<b>Six weeks, not sixteen days &mdash; this card was a month out until it was checked.</b> '
       'The Best Algorithmic Contribution prize is the interesting door here: it is judged on the '
       'idea, not the score, which is the same opening the ARC Paper Track offers. If you look at one '
       'ARC thing, compare those two before choosing. <b>Whatever you decide, register before 2 '
       'October</b> &mdash; the team freeze shuts registration entirely, and it arrives a fortnight '
       'before the work is due.',
  conf='verified', checked='2026-09-07',
  theme=dict(paper='#f8f4ec', ink='#8a2b1e', rule='#8a2b1e', treatment='t-stencil'),
  tags=['interpretability','AIcrowd','smaller field']),

dict(id='arc-agi-3', name='ARC Prize 2026 &mdash; ARC-AGI-3',
  host='ARC Prize Foundation', platform='Kaggle',
  url='https://www.kaggle.com/competitions/arc-prize-2026-arc-agi-3',
  domain='ai', kind='Grand challenge',
  blurb='Build an AI capable of fluid intelligence &mdash; solving novel reasoning puzzles it has never seen.',
  submit='A code submission run against unseen tasks.',
  fmt='remote', location='Entirely online', travel='None stated.',
  fee='Free', prize='$850,000', team='Solo or team', eligible='Open.',
  effort='Very heavy. An open research problem, not an exercise.',
  difficulty=5,
  deadline_text='about 2 months to go', deadline='2026-11-03', precision='derived',
  extra='2,738 teams.',
  why='Here because you asked to see the ones above you as well.',
  view='Read it, do not enter it. The prize is that large precisely because nobody has solved it, '
       'and there is no version of the next two months where you do. Knowing what ARC is, and why '
       'it resists everything, is genuinely worth an hour.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#141414', ink='#f0ede6', rule='#e0c341', treatment='t-night'),
  stretch=True, tags=['reasoning','AGI','above you for now']),

dict(id='arc-agi-2', name='ARC Prize 2026 &mdash; ARC-AGI-2',
  host='ARC Prize Foundation', platform='Kaggle',
  url='https://www.kaggle.com/competitions/arc-prize-2026-arc-agi-2',
  domain='ai', kind='Grand challenge',
  blurb='The sibling track to ARC-AGI-3: build an AI capable of novel reasoning.',
  submit='A code submission run against unseen tasks.',
  fmt='remote', location='Entirely online', travel='None stated.',
  fee='Free', prize='$700,000', team='Solo or team', eligible='Open.',
  effort='Very heavy.', difficulty=5,
  deadline_text='about 2 months to go', deadline='2026-11-03', precision='derived',
  extra='1,784 teams &mdash; roughly a thousand fewer than ARC-AGI-3.',
  why='The same reason as its sibling: you asked to see what sits above you.',
  view='Same advice as ARC-AGI-3. If you are going to read one ARC track properly, read this one, '
       'because ARC-AGI-2 is the better-documented benchmark and the write-ups are clearer.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#16171c', ink='#eae7f0', rule='#7b6cff', treatment='t-night'),
  stretch=True, tags=['reasoning','AGI','above you for now']),

dict(id='kaggriculture', name='Kaggriculture',
  host='Kaggle', platform='Kaggle',
  url='https://www.kaggle.com/competitions/kaggriculture',
  domain='ai', kind='Simulation competition',
  blurb='Write an agent that plays a farming simulation and competes against other agents to maximise income.',
  submit='An agent, played head to head against others.',
  fmt='remote', location='Entirely online', travel='None stated.',
  fee='Free', prize='$50,000', team='Solo or team', eligible='Open.',
  effort='Medium. Simulation competitions reward tinkering more than compute.',
  difficulty=3,
  deadline_text='about a month to go', deadline='2026-10-03', precision='derived',
  extra='7,437 teams &mdash; the most crowded thing on this wall.',
  why='Simulation competitions are unusually friendly to a beginner: you can watch your agent play.',
  view='If you want one competition where the feedback loop is fun rather than statistical, this is '
       'it. A clever hand-written rule beats a big model surprisingly often in these. Seven thousand '
       'teams means you will not place &mdash; enter it to learn what an agent loop feels like.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#f7f9ea', ink='#4a6b12', rule='#4a6b12', treatment='t-hoard'),
  tags=['agents','simulation','beginner friendly']),

dict(id='ptcg', name='Pok&eacute;mon PTCG AI Battle Challenge',
  host='The Pok&eacute;mon Company', platform='Kaggle',
  url='https://www.kaggle.com/competitions/pokemon-tcg-ai-battle-challenge-strategy',
  domain='ai', kind='Hackathon',
  blurb='Analyse data and build agentic play for the Pok&eacute;mon Trading Card Game.',
  submit='An agent plus analysis.',
  fmt='remote', location='Entirely online', travel='None stated.',
  fee='Free', prize='$240,000', team='Solo or team', eligible='Open.',
  effort='Medium.', difficulty=3,
  deadline_text='11 days to go, read 3 September 2026', deadline='2026-09-14', precision='derived',
  extra='594 teams.',
  why='A quarter of a million dollars on a card game, which is a fair summary of this field in 2026.',
  view='Eleven days is not enough to do this properly from nothing, and the whole point of this wall '
       'is that I tell you that instead of letting you find out on day nine. Note it, catch the next one.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#fdf3f6', ink='#a8265c', rule='#a8265c', treatment='t-ticket'),
  tags=['agents','game','too late this round']),

dict(id='playground-ev', name='Playground Series &mdash; Predicting EV Purchases',
  host='Kaggle', platform='Kaggle',
  url='https://www.kaggle.com/competitions/playground-series-s6e9',
  domain='ai', kind='Playground practice competition',
  blurb='A monthly tabular-data practice competition. Predict who buys an electric vehicle.',
  submit='A predictions CSV.',
  fmt='remote', location='Entirely online', travel='None.',
  fee='Free', prize='Swag only', team='Solo or team', eligible='Open to everyone.',
  effort='Light. A weekend, honestly less.', difficulty=1,
  deadline_text='about a month to go', deadline='2026-10-03', precision='derived',
  extra='498 teams. A fresh one starts every month, so missing this one costs nothing.',
  why='The on-ramp. Tabular data, a clean metric, nothing at stake but a leaderboard position.',
  view='Start here. Genuinely, before anything else on this wall. One afternoon gets you a working '
       'submission pipeline, and every harder competition here reuses that same pipeline. The fact '
       'that a new one appears monthly means there is no cost to failing at this one.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#eef6fa', ink='#1c6a8a', rule='#1c6a8a', treatment='t-chart'),
  tags=['beginner','tabular','start here']),

dict(id='kaggle-getting-started', name='Kaggle Getting Started &mdash; Titanic and friends',
  host='Kaggle', platform='Kaggle',
  url='https://www.kaggle.com/competitions',
  domain='ai', kind='Permanent practice competitions',
  blurb='Four permanently open teaching competitions: Titanic survival, handwritten digit '
        'recognition, house-price regression and Spaceship Titanic.',
  submit='Predictions. No deadline, no prize, no pressure.',
  fmt='remote', location='Entirely online', travel='None.',
  fee='Free', prize='Knowledge and a rank', team='Solo', eligible='Everyone.',
  effort='An afternoon each.', difficulty=1,
  deadline_text='Ongoing. No deadline, ever.', deadline='', precision='none',
  extra='Titanic alone has 9,622 teams active right now.',
  find='A GROUP of four, so this link opens Kaggle&rsquo;s competition list rather than one page. '
       'Filter it to Getting Started.',
  why='The cheapest possible way to find out whether you like this work at all.',
  view='If the Playground competition above feels like too much, do Titanic first. It is two hours '
       'and it removes the only real barrier, which is never having submitted anything anywhere.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#f5f5f2', ink='#3f3f3a', rule='#7a7a70', treatment='t-letter'),
  tags=['beginner','no deadline','free']),

dict(id='road-barbados-handwriting', name='R.O.A.D. Barbados Historic Handwriting Challenge',
  host='GovTech Barbados', platform='Zindi',
  url='https://zindi.world/competitions/road-barbados-historic-handwriting-challenge',
  domain='ai', kind='OCR competition',
  blurb='Build a model that transcribes handwritten Barbadian historical records &mdash; deeds, wills, '
        'censuses, estate inventories.',
  submit='Predicted transcriptions, scored on weighted Word Error Rate and Character Error Rate.',
  fmt='remote', location='Entirely online',
  travel='None &mdash; it runs entirely on Zindi.',
  fee='No fee is stated anywhere in the rules. Zindi&rsquo;s own terms go the other way on '
      'money: it covers the international transfer fees itself when a prize is under $500.',
  prize='$25,000 total &mdash; $10,000 first, $6,000 second, $4,000 third, '
        'and $5,000 for the top Barbadian entrant',
  team='<b>Maximum team size of 4</b>, printed in the rules. Submissions are capped at <b>5 per day '
       'and 200 overall</b>. One further constraint that shapes the whole entry: <b>you may only use '
       'open-source languages and tools</b>, and Zindi reviews the top 10 solutions when a challenge '
       'ends and may request your code at any point during it.',
  eligible='<b>&ldquo;Who can compete: Open to all&rdquo;</b> &mdash; printed in the rules, with no '
           'restriction by age, country or affiliation. The only bar is conduct: anyone caught '
           'cheating loses prize eligibility for a six-month probation period, and so does any team '
           'carrying them.',
  effort='Medium to heavy. Handwriting OCR is hard but very well-trodden.',
  difficulty=3,
  deadline_text='4 October 2026', deadline='2026-10-04', precision='exact',
  extra='Zindi moved domain from zindi.africa to zindi.world; the old link redirects.',
  why='Thirty-one days, $25,000, open to all, on a platform with a much smaller field than Kaggle.',
  view='The most winnable serious-money competition on this wall for someone at your stage. OCR has '
       'strong off-the-shelf starting points, the separate Barbadian prize takes some of the '
       'strongest competition out of your bracket, and Zindi fields are small. If you enter exactly '
       'one thing here to try to place, make it this.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#fbf4e4', ink='#8a5a1e', rule='#c98a2e', treatment='t-stencil'),
  tags=['OCR','Zindi','most winnable']),

dict(id='amazon-bss', name='Build, Ship, Shape: Amazon Developer Hackathon',
  host='Amazon', platform='Devpost',
  url='https://amazonappdev2026.devpost.com/',
  domain='build', kind='Hackathon',
  blurb='An open-ended Amazon developer hackathon &mdash; build something on their developer stack.',
  submit='A working project plus a demo video.',
  fmt='remote', location='Online', travel='None stated.',
  fee='Free', prize='$138,000', team='Solo or team',
  eligible='Not stated on the listing. Check Amazon&rsquo;s own rules for country eligibility '
           'before you build anything.',
  effort='Medium to heavy.', difficulty=3,
  deadline_text='31 August to 23 October 2026', deadline='2026-10-23', precision='exact',
  extra='984 participants. Managed by Devpost.',
  why='The largest prize pool on this wall with genuine runway &mdash; seven weeks.',
  view='Open-ended briefs suit you, because you pick the problem instead of being handed one, and '
       'you have already shipped a real system this month. The eligibility line is the thing to '
       'check first, not last: Amazon hackathons often exclude countries, and finding that out in '
       'week six would be the exact waste you are trying to avoid.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#fdf6e0', ink='#1a1a17', rule='#1a1a17', treatment='t-hoard'),
  tags=['open ended','big prize','check eligibility first']),

dict(id='ml-empower-3', name='ML Empowerment Build Challenge 3.0',
  host='ML Empowerment Foundation', platform='Devpost',
  url='https://ml-build-challenge-3.devpost.com/',
  domain='ai', kind='Hackathon',
  blurb='Machine learning for social good. Tagged beginner-friendly by the host.',
  submit='A project and a write-up.',
  fmt='remote', location='Online', travel='None stated.',
  fee='Free',
  prize='<b>$1,000 in prizes &mdash; 10 winners at $100 each in cash.</b> CORRECTED 7 September '
        '2026: this wall said $53,500, which was <b>fifty-three times too high</b>.',
  team='Solo or team',
  eligible='Printed on the live page: <b>ages 13+ only, students only</b>, companies and '
           'professional organisations excluded, all countries except the standard exceptions.',
  effort='Medium.', difficulty=2,
  deadline_text='<b>5 October 2026, 5:00pm PDT</b>, read off the live event page on 7 September 2026. '
                'This wall previously said 1 October, taken from the wrong page.',
  deadline='2026-10-05', precision='exact',
  extra='CORRECTED 7 September 2026, and it was wrong three ways at once. <b>The URL pointed at a '
        'dead shell</b> &mdash; <code>ml--build-challenge-3-0.devpost.com</code>, note the double '
        'hyphen, which says &ldquo;This hackathon has ended&rdquo; and whose only listed prize is a '
        'note reading <i>&ldquo;n/a - submit to: ml-build-challenge-3.devpost.com&rdquo;</i>. The '
        'live event is at the single-hyphen address. The $53,500 and the 1 October date both came '
        'off that shell.',
  why='Free, students only, beginner-flagged, and four weeks of runway. <b>The prize is $1,000, not '
      'the $53,500 this wall used to claim</b> &mdash; which changes what it is for, not whether it '
      'is worth doing.',
  view='<b>Still worth entering, for a smaller and more honest reason than the one this card used '
       'to give.</b> It said the prize-to-entrant ratio was the best on the wall; that was built on '
       'a figure fifty-three times too large and it is withdrawn. What is actually here: ten '
       'separate $100 prizes rather than one pot, a students-only field, beginner framing, and a '
       'social-good brief a health project fits. <b>Ten winners is a far better shape for you than '
       'one</b> &mdash; you are not competing for a single top slot. Build the thing you were going '
       'to build anyway and enter it here as well.',
  conf='verified', checked='2026-09-07',
  theme=dict(paper='#eef7f4', ink='#146b5c', rule='#146b5c', treatment='t-riso'),
  tags=['beginner','social good','ten winners','prize corrected']),

dict(id='next-byte-v4', name='Next Byte Hacks: V4',
  host='Next Byte Hacks', platform='Devpost',
  url='https://next-byte-hacks-v4.devpost.com/',
  domain='build', kind='Online student hackathon',
  blurb='A small, open-brief student hackathon on Devpost.',
  submit='A Devpost project submission.',
  fmt='remote', location='Online', travel='None stated.',
  fee='Not stated', prize='$100 in prizes.',
  team='Not stated on the listing.',
  eligible='Listed as open to all on the Devpost index. <b>The individual eligibility block was not '
           'opened</b>, so age, student status and excluded countries are unread here.',
  effort='Light.', difficulty=1,
  deadline_text='30 September 2026, from the Devpost recently-added index read on 7 September 2026.',
  deadline='2026-09-30', precision='listing',
  extra='Added 7 September 2026 by the weekly Devpost sweep. It was the only open Devpost hackathon '
        'with any prize at all that this wall did not already carry &mdash; the other four new ones '
        'are explicitly non-monetary.',
  why='It is on the wall for consistency rather than for the money: the wall already carries several '
      'student hackathons in the $100 to $1,750 range, and leaving this one off would be filtering '
      'on my taste rather than on the rule.',
  view='<b>$100, so this is about having submitted something, not about winning.</b> Three weeks and '
       'an open brief. Only worth it as a second home for a project you are already building for '
       'something bigger &mdash; the same advice as NextStep and COMPSPHERE. If nothing is already '
       'half-built, skip it without regret.',
  conf='listing', checked='2026-09-07',
  theme=dict(paper='#e8eef0', ink='#2f4f5a', rule='#2f4f5a', treatment='t-chart'),
  tags=['tiny prize','students','three weeks','reuse a project']),

dict(id='nextgen-blr', name='Next Gen Hackathon 2026 &mdash; Bengaluru',
  host='RAAIF', platform='Devpost',
  url='https://next-gen-hackathon.devpost.com/',
  domain='build', kind='Hackathon',
  blurb='AR/VR, IoT and machine learning hackathon at Tripura Vasini Palace Grounds, Bengaluru.',
  submit='A built prototype.',
  fmt='in-person', location='Tripura Vasini Palace Grounds, Bengaluru, Karnataka',
  travel='In person in Bengaluru. You are in Karnataka now; this stops being reachable once '
         'counselling relocates you.',
  fee='Free to enter. Travel is yours.', prize='&#8377;50,000', team='Solo or team',
  eligible='Not stated on the listing.',
  effort='Medium.', difficulty=3,
  deadline_text='1 September to 23 October 2026', deadline='2026-10-23', precision='exact',
  extra='Only 10 participants listed so far.',
  why='The one thing on this wall that is physically near you, and it stops being near you soon.',
  view='Ten participants and &#8377;50,000 is an absurd ratio, but read the honest catch: the '
       'deadline is 23 October and your counselling may have moved you by then. Decide this one on '
       'your posting, not on the prize. If you are still in Karnataka in October, go.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#f6eefa', ink='#5c2b7a', rule='#5c2b7a', treatment='t-riso'),
  tags=['in person','Bengaluru','tiny field']),

dict(id='prom-fall', name='Prom Fall Classic',
  host='Prometheus CS', platform='Devpost',
  url='https://prometheus-fall-classic.devpost.com/',
  domain='build', kind='Hackathon',
  blurb='A beginner-friendly education and machine learning hackathon.',
  submit='A project.',
  fmt='remote', location='Online', travel='None stated.',
  fee='Free', prize='$1,500', team='Solo or team',
  eligible='Open. Tagged Beginner Friendly.',
  effort='Light to medium.', difficulty=2,
  deadline_text='31 August to 26 September 2026', deadline='2026-09-26', precision='exact',
  extra='67 participants.',
  why='Small, friendly, three weeks.',
  view='A good first hackathon to finish rather than win. The value is entirely in shipping '
       'something with a deadline attached; the $1,500 is incidental.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#fef4ee', ink='#a84a1e', rule='#a84a1e', treatment='t-ticket'),
  tags=['beginner','small','three weeks']),

dict(id='qiskit-fall', name='Qiskit Fall Fest',
  host='NMIMS Mumbai', platform='Unstop',
  url='https://unstop.com/hackathons/qiskit-fall-fest-mukesh-patel-school-of-technology-management-and-engineering-nmims-mumbai-1748182',
  domain='quantum', kind='Quantum computing event',
  blurb='A quantum computing challenge run on IBM&rsquo;s Qiskit framework, hosted by MPSTME, NMIMS '
        'Mumbai <b>in association with IBM Quantum</b>.',
  submit='Notebooks and challenges.',
  fmt='remote', location='Online', travel='None stated.',
  fee='FREE. The Unstop API returns isPaid false and no registration fee.',
  prize='&#8377;10,000 first, &#8377;5,000 second, &#8377;3,000 third.', team='1 to 4 members',
  eligible='Not stated on the listing &mdash; the eligibility block is empty, which on Unstop means '
           'no filter was set rather than that anyone may enter.',
  effort='Medium, but the learning curve is the point.',
  difficulty=3,
  deadline_text='Registration runs 2 September to <b>24 October 2026, 23:59 IST</b>, read straight '
                'off the Unstop API on 7 September 2026. This replaces a derived 3 October date that '
                'had been computed from the words &ldquo;about 1 month left&rdquo;.',
  deadline='2026-10-24', precision='exact',
  extra='199 registered when read. CORRECTED 7 September 2026: this bill previously carried no direct '
        'link at all &mdash; it opened Unstop&rsquo;s whole hackathon list &mdash; a derived deadline '
        'three weeks early, and &ldquo;prize not stated&rdquo;. The public API returns all three.',
  why='Filed under things you said you would learn anything for &mdash; and it now has a real link, '
      'a real deadline and a real prize.',
  view='Quantum is one of the few fields where an eighteen-year-old and a postdoc are genuinely '
       'closer together, because almost nobody has done it long. Free, seven weeks, teams of up to '
       'four, and IBM&rsquo;s name on it. Worth an evening of curiosity even if you never go back '
       'to it &mdash; and it pairs with DREAM-Q, which is the same subject with a research paper '
       'at the end of it.',
  conf='listing', checked='2026-09-07',
  theme=dict(paper='#171b2e', ink='#cdd6ff', rule='#6f5cff', treatment='t-night'),
  stretch=True, tags=['quantum','free','curiosity']),

dict(id='global-mesh', name='Global Mesh AI &amp; Swarm Robotics Challenge 2026',
  host='Vidya Sanskar Public School', platform='Unstop',
  url='https://unstop.com/hackathons/global-mesh-ai-swarm-robotics-challenge-2026-build-open-source-edge-systems-vidya-sanskar-public-school-1747770',
  domain='ai', kind='Open source challenge',
  blurb='Build open-source edge systems combining AI and swarm robotics &mdash; the listing calls it '
        'a &ldquo;Decentralized Mesh Protocol Hackathon&rdquo; and names dynamic node routing, swarm '
        'network optimisation, testing and documentation as the work.',
  submit='Contributions to an open-source project. Contribution-based rather than a single build.',
  fmt='remote', location='Online', travel='None stated.',
  fee='FREE. The Unstop API returns isPaid false.',
  prize='&#8377;10,000 winner, &#8377;5,000 runner-up, &#8377;2,500 second runner-up, and '
        '<b>&#8377;1,000 each for ranks 4 to 30</b> &mdash; so twenty-seven places pay something.',
  team='1 to 3 members',
  eligible='Printed on the listing: &ldquo;Open to all students, open-source enthusiasts, and '
           'developers (undergraduate, post-graduate, and school students)&rdquo;.',
  effort='Medium to heavy. The listing names C++ and IoT/robotics.', difficulty=4,
  deadline_text='Final submission <b>30 September 2026, 23:59 IST</b>, read off the Unstop API on '
                '7 September 2026. Winners announced after 5 October. This replaces a derived '
                '29 September date.',
  deadline='2026-09-30', precision='exact',
  extra='41 registered when read. CORRECTED 7 September 2026: this bill previously had no direct '
        'link and no prize. Both are now read from the source, and the prize table is the '
        'interesting part &mdash; the tail pays.',
  why='Edge systems is the same architectural argument you already made in the Gujarat project: '
      'process where the data is, do not ship it all to one place.',
  view='You have genuinely done this once, with real measurements behind it. That is a rarer '
       'starting position than it sounds. And the prize table changes the calculation: it is not '
       'winner-take-all, <b>ranks 4 to 30 are still paid</b>, against 41 entrants. The host is a '
       'school, so calibrate the prestige down &mdash; but the odds are better than anything else '
       'on this wall.',
  conf='listing', checked='2026-09-07',
  theme=dict(paper='#eff3f7', ink='#2b4763', rule='#2b4763', treatment='t-chart'),
  tags=['edge','robotics','you have done this']),


dict(id='dr-docbench', name='Dr.DocBench Challenge',
  host='DocInsights 2026 workshop, co-located with EMNLP 2026', platform='EvalAI',
  url='https://eval.ai/web/challenges/challenge-page/2717/overview',
  domain='ai', kind='Academic shared task',
  blurb='Expert-level document parsing: recognition, layout understanding and structured extraction '
        'together, on difficulty-aware data chosen around the cases where strong document parsers '
        'already fail.',
  submit='One .zip archive with a prediction for every released evaluation page. JSONL and Markdown '
         'files must be UTF-8 without a byte-order mark, and prediction identifiers must match the '
         'subject, document ID and page number exactly.',
  fmt='remote', location='Online. The workshop is at EMNLP 2026 in Budapest, Hungary.',
  travel='Not stated for competing.',
  fee='Not stated', prize='Not stated on the challenge page',
  team='Not stated. Top-ranked teams must submit a technical report describing their system.',
  eligible='&ldquo;The challenge is open to researchers and teams worldwide.&rdquo; All external '
           'training data, models and resources must be disclosed.',
  effort='Moderate to heavy. Document AI is fiddly rather than deep.',
  difficulty=3,
  deadline_text='10 August to 10 October 2026 at 12:59:59 PM UTC. Public Validation is the only '
                'participant-facing phase and allows 3 submissions per day.',
  deadline='2026-10-10', precision='exact',
  why='Document parsing is the least glamorous and most immediately useful skill in applied AI, and '
      'this one is explicitly open worldwide with the rules printed in full.',
  view='Five weeks, an open-to-all rule, and a clean zip submission. If you want an academic shared '
       'task on your record without a container to build, this is the easiest one here.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#e1f1df', ink='#1f7a12', rule='#1f7a12', treatment='t-gazette'),
  tags=['document AI','EMNLP','open worldwide','zip submission']),

dict(id='perception-test', name='Perception Test Challenge 2025 &mdash; Multiple-choice videoQA',
  host='Google DeepMind', platform='EvalAI',
  url='https://eval.ai/web/challenges/challenge-page/2547/overview',
  domain='ai', kind='Benchmark challenge',
  blurb='A benchmark built to test the perception and reasoning of multimodal video models. Task 1 '
        'is multiple-choice video question answering.',
  submit='A single JSON file answering every question in the dataset split, in the required format. '
         'A baseline notebook (mc_vqa.ipynb) shows how to download the data and produce it.',
  fmt='remote', location='Entirely online',
  travel='None stated at any stage.',
  fee='Not stated', prize='Not stated on the EvalAI page',
  team='Not stated',
  eligible='Not stated on the EvalAI page; it links to a separate terms page.',
  effort='Light to moderate if you start from the baseline notebook.',
  difficulty=3,
  deadline_text='Open since 1 July 2025, closing 6 October 2026 at 23:59.',
  deadline='2026-10-06', precision='exact',
  extra='Run by DeepMind, which is why the baseline tooling is unusually good.',
  why='A DeepMind benchmark with a working baseline notebook is a free, guided introduction to '
      'multimodal models.',
  view='Treat it as a tutorial with a leaderboard. Run the baseline, change one thing, resubmit. '
       'Five weeks is plenty for that, and the notebook does the tedious half for you.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#e0dcf1', ink='#43377a', rule='#43377a', treatment='t-chart'),
  tags=['video','DeepMind','baseline provided','tutorial-shaped']),

dict(id='lost-in-transcription', name='Lost in Transcription &mdash; ASR for Underserved Languages',
  host='Mozilla Data Collective', platform='Mozilla Data Collective',
  url='https://competitions.mozilladatacollective.com/competitions/group/lost-in-transcription/',
  domain='ai', kind='Speech recognition competition',
  blurb='Build speech recognition for real bilingual conversation across three language pairs '
        '&mdash; Spanish-English, Spanish-Nahuatl and Indonesian-Javanese &mdash; where speakers '
        'switch between languages mid-sentence.',
  submit='Transcriptions scored against references by word error rate.',
  fmt='remote', location='Entirely online',
  travel='None stated at any stage.',
  fee='Not stated',
  prize='$20,000 total. Per track: $4,000 first, $2,000 second. Plus a $2,000 bonus for the best '
        'average across all three tracks.',
  team='Not stated', eligible='Not stated on the competition page',
  effort='Heavy. Code-switched speech is one of the harder ASR problems.',
  difficulty=4,
  deadline_text='The page showed &ldquo;3 weeks&rdquo; left when read on 3 September 2026; '
                'DrivenData&rsquo;s listing says mid-September. NO EXACT DATE IS PRINTED, so the '
                'date on this card is computed from &ldquo;3 weeks&rdquo; and could be days out.',
  deadline='2026-09-24', precision='derived',
  extra='Code-switching &mdash; changing language mid-sentence &mdash; is how most of urban India '
        'actually speaks, which is why no Indian language ASR system handles it well.',
  why='The one competition here whose core problem you hear spoken around you every day.',
  view='Three weeks and a hard modelling problem, so not winnable cold. Worth opening for the data '
       'alone: code-switched speech corpora are rare and this one is public.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#f1e4d9', ink='#7a502b', rule='#7a502b', treatment='t-ticket'),
  tags=['speech','code-switching','derived date','real money']),

dict(id='whats-up-docs', name='What&rsquo;s Up, Docs? Document Summarization with LLMs',
  host='DrivenData', platform='DrivenData',
  url='https://www.drivendata.org/competitions/297/whats-up-docs/',
  domain='ai', kind='Practice competition',
  blurb='Summarise documents with large language models, as a practice competition with no prize '
        'and no real clock.',
  submit='Predictions in the format specified on the competition site.',
  fmt='remote', location='Entirely online',
  travel='None stated at any stage.',
  fee='Not stated &mdash; this competition&rsquo;s own page was not opened individually.',
  prize='None. Listed as Practice.',
  team='Not stated',
  eligible='Not opened individually; DrivenData&rsquo;s standard practice rules are 18 or over and '
           'OFAC-designated countries excluded.',
  effort='Light.',
  difficulty=2,
  deadline_text='Listed as about 7 months left on the DrivenData competitions page.',
  deadline='', precision='none',
  why='An LLM task with no stakes, on the platform whose rules are the clearest of any here.',
  view='Filler, and I am saying so. Useful only if you want a third practice run after DengAI and '
       'Flu Shot Learning. Do not let it displace anything with a deadline.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#f2fbf9', ink='#134c3e', rule='#134c3e', treatment='t-hoard'),
  tags=['LLM','practice','filler','no clock']),

dict(id='gatewayhacks-2026', name='GatewayHacks 2026 &mdash; Software &amp; AI',
  host='GatewayHacks', platform='Devpost',
  url='https://gatewayhacks-2026.devpost.com/',
  domain='ai', kind='Online hackathon',
  blurb='Build software, apps and AI &ldquo;that open doors to a better future&rdquo;. The prize '
        'pool is mostly credits and sponsor awards rather than cash, on top of the placed prizes.',
  submit='A Devpost project submission.',
  fmt='remote', location='Online',
  travel='None stated at any stage.',
  fee='Not stated',
  prize='$814,585 total across all prizes &mdash; placed prizes plus sponsor awards including 100 '
        'free .xyz domains, Momen credits, $299 Tin Computer credits for the first 100 teams and '
        '$1,000 Adaption credits.',
  team='Not stated in the eligibility block',
  eligible='Ages 13 and over; STUDENTS ONLY; companies and professional organisations excluded; all '
           'countries and territories except the standard exceptions.',
  effort='Moderate. A month-long online build.',
  difficulty=2,
  deadline_text='Submission period 1 September to 2 October 2026. Deadline 2 October 2026 at '
                '12:00am EDT.',
  deadline='2026-10-02', precision='exact',
  extra='The headline figure is inflated by credit-based sponsor prizes; read the prize list before '
        'believing the number.',
  why='Students only, all countries, a month of runway, and no theme restriction &mdash; you can '
      'submit something medical and it still qualifies.',
  view='The largest prize number on the wall is mostly credits, and I would rather say that than let '
       'the figure do the work. Still worth entering: a month is real time, the field is students '
       'rather than professionals, and a project built here can be reused for three other bills on '
       'this wall.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#fbeffb', ink='#4c0b4a', rule='#4c0b4a', treatment='t-riso'),
  tags=['students only','month long','prize is mostly credits','reusable']),

dict(id='revenuecat-shipaton', name='RevenueCat Shipaton 2026',
  host='RevenueCat', platform='Devpost',
  url='https://revenuecat-shipaton-2026.devpost.com/',
  domain='build', kind='Online hackathon',
  blurb='Ship a real app. RevenueCat runs the payments layer, and the Shipaton rewards apps that '
        'actually get released rather than demos.',
  submit='A Devpost project submission.',
  fmt='remote', location='Online',
  travel='None stated at any stage.',
  fee='Not stated', prize='$740,000 in prizes',
  team='Not stated in the eligibility block',
  eligible='Ages 13 to 99 only. SPECIFIC COUNTRIES AND TERRITORIES ARE EXCLUDED and the page does '
           'not print the list &mdash; open the full rules and check India before you build anything.',
  effort='Heavy. Shipping a real app to a store is weeks of work, not a weekend.',
  difficulty=4,
  deadline_text='Submission period 31 July to 1 October 2026. Deadline 30 September 2026 at 11:45pm '
                'PDT.',
  deadline='2026-09-30', precision='exact',
  why='The second largest pot on the wall and it is real cash rather than credits.',
  view='Check the excluded-country list FIRST. The page hides it behind &ldquo;View full '
       'rules&rdquo;, and a month of building only to find you were never eligible is the worst '
       'possible outcome. If India is clear, this is serious money for a real product &mdash; but it '
       'wants a shipped app, which is a bigger commitment than anything else here.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#f6fbec', ink='#3e4c22', rule='#3e4c22', treatment='t-stencil'),
  tags=['big money','ship a real app','CHECK ELIGIBILITY','heavy']),

dict(id='gibc-v2', name='Global Innovation Build Challenge V2',
  host='Global Innovation Build Challenge', platform='Devpost',
  url='https://gibc-v2.devpost.com/',
  domain='build', kind='Online hackathon',
  blurb='An open-ended global build challenge run through Devpost.',
  submit='A Devpost project submission.',
  fmt='remote', location='Online',
  travel='None stated at any stage.',
  fee='Not stated', prize='$156,525 in prizes',
  team='Not stated in the eligibility block',
  eligible='Ages 13 and over; students only; companies and professional organisations excluded; all '
           'countries and territories except the standard exceptions.',
  effort='Moderate.',
  difficulty=2,
  deadline_text='Submission period 11 July to 21 September 2026. Deadline 21 September 2026 at '
                '11:45pm CST.',
  deadline='2026-09-21', precision='exact',
  why='Students only and open to all countries, with a six-figure pool.',
  view='Eighteen days. Enterable if you already have something half-built &mdash; and if you enter '
       'GatewayHacks too, the same project may well satisfy both. Check each set of rules on reuse '
       'before doing that.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#e9effb', ink='#1b2d4c', rule='#1b2d4c', treatment='t-bulletin'),
  tags=['students only','open ended','reusable project']),

dict(id='agentic-cinema', name='Agentic Cinema: The Blockbuster Hackathon',
  host='Agentic Cinema', platform='Devpost',
  url='https://agentic-cinema.devpost.com/',
  domain='ai', kind='Online hackathon',
  blurb='Build agentic AI systems for film and video production.',
  submit='A Devpost project submission.',
  fmt='remote', location='Online',
  travel='None stated at any stage.',
  fee='Not stated', prize='$75,000 in prizes',
  team='Not stated in the eligibility block',
  eligible='Above the legal age of majority in your country of residence. SPECIFIC COUNTRIES ARE '
           'EXCLUDED &mdash; the list is printed on the page and includes Afghanistan, Antarctica, '
           'Belarus, Brazil, China, Crimea, Cuba and others. INDIA IS NOT ON THE PRINTED LIST.',
  effort='Moderate.',
  difficulty=3,
  deadline_text='Submission period 27 July to 9 September 2026. Deadline 9 September 2026 &mdash; that window has CLOSED. Kept on the wall because Devpost hackathons of this shape recur.',
  deadline='2026-09-09', precision='exact',
  why='$75,000 and India is clear on the excluded list, which I checked rather than assumed.',
  view='Six days. Too short unless you already have an agent pipeline you can point at video. Listed '
       'because you asked for the borderline ones rather than my filtering, and because the '
       'eligibility check came back clean.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#fbe5e7', ink='#4c1318', rule='#4c1318', treatment='t-ticket'),
  tags=['agents','video','India eligible','very short']),

dict(id='nebius-nvidia', name='Nebius x NVIDIA Global AI Hackathon',
  host='Nebius with NVIDIA', platform='Devpost',
  url='https://nebiusglobalaihackathon.devpost.com/',
  domain='ai', kind='Online hackathon',
  blurb='A global AI hackathon run by Nebius with NVIDIA.',
  submit='A Devpost project submission.',
  fmt='remote', location='Online',
  travel='None stated at any stage.',
  fee='Not stated', prize='$50,000 in prizes',
  team='Not stated in the eligibility block',
  eligible='Above the legal age of majority in your country of residence; ALL countries and '
           'territories except the standard exceptions. Not restricted to students.',
  effort='Moderate.',
  difficulty=3,
  deadline_text='Submission period 26 August to 30 October 2026. Deadline 30 October 2026 at '
                '10:00am PDT.',
  deadline='2026-10-30', precision='exact',
  why='EIGHT WEEKS of runway, $50,000, open to everyone, backed by NVIDIA. This is the shape of '
      'competition this wall exists to find &mdash; large, open, and caught early.',
  view='Take this one seriously. The runway is the longest of any cash hackathon here, which means '
       'you can learn the stack, build, test, and still submit unhurried. If you only commit to one '
       'AI hackathon this autumn, commit to this.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#e2fbe7', ink='#0f6321', rule='#0f6321', treatment='t-gazette'),
  tags=['NVIDIA','eight weeks','open to all','commit to this']),

dict(id='agents-for-humans', name='Agents for Humans Hackathon',
  host='Agents for Humans', platform='Devpost',
  url='https://agentsforhumans.devpost.com/',
  domain='ai', kind='Online hackathon',
  blurb='Build AI agents that do something useful for people.',
  submit='A Devpost project submission.',
  fmt='remote', location='Online',
  travel='None stated at any stage.',
  fee='Not stated', prize='$40,000 in prizes',
  team='Not stated in the eligibility block',
  eligible='Above the legal age of majority in your country of residence. SPECIFIC COUNTRIES ARE '
           'EXCLUDED &mdash; the printed list includes Argentina, Australia, Belarus, Brazil, '
           'Crimea, Cuba and others. INDIA IS NOT ON THE PRINTED LIST.',
  effort='Moderate.',
  difficulty=3,
  deadline_text='Submission period 10 August to 14 September 2026. Deadline 14 September 2026 at '
                '5:00pm PDT.',
  deadline='2026-09-14', precision='exact',
  why='$40,000, agents, and India clears the excluded list.',
  view='Eleven days. Enterable if you build the kind of agent you already use Claude to build. A '
       'health-admin agent would fit the brief and reuse straight into Hack2Heal.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#f4f0f9', ink='#482d63', rule='#482d63', treatment='t-riso'),
  tags=['agents','India eligible','short','reusable']),

dict(id='univabio', name='UnivaBio',
  host='UnivaBio', platform='Devpost',
  url='https://univabio.devpost.com/',
  domain='ai', kind='Online hackathon',
  blurb='A biology-themed build challenge run through Devpost.',
  submit='A Devpost project submission.',
  fmt='remote', location='Online',
  travel='None stated at any stage.',
  fee='Not stated', prize='$38,245 in prizes',
  team='Not stated in the eligibility block',
  eligible='Ages 13 and over; STUDENTS ONLY; companies and professional organisations excluded; all '
           'countries and territories except the standard exceptions.',
  effort='Moderate.',
  difficulty=3,
  deadline_text='Submission period 7 August to 6 October 2026. Deadline 6 October 2026 at 11:45pm EDT.',
  deadline='2026-10-06', precision='exact',
  why='Biology plus students only plus a month of runway plus real cash. On subject match alone this '
      'is the best Devpost entry on the wall for you.',
  view='Enter this. Five weeks, a field limited to students, a subject you are about to study full '
       'time, and $38,000 on the table. Of the eighteen Devpost hackathons taken today, this is the '
       'one where being a medical student is an advantage rather than an irrelevance.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#f9f6ed', ink='#635623', rule='#635623', treatment='t-clinic'),
  tags=['biology','students only','five weeks','enter this']),

dict(id='ai-builders-2026', name='AI Builders Hackathon',
  host='AI Builders', platform='Devpost',
  url='https://ai-builders-hackathon-2026.devpost.com/',
  domain='ai', kind='Online hackathon',
  blurb='An open AI build hackathon run through Devpost.',
  submit='A Devpost project submission.',
  fmt='remote', location='Online',
  travel='None stated at any stage.',
  fee='Not stated', prize='$33,900 in prizes',
  team='Not stated in the eligibility block',
  eligible='Above the legal age of majority in your country of residence; students only; companies '
           'and professional organisations excluded; all countries except the standard exceptions.',
  effort='Moderate.',
  difficulty=2,
  deadline_text='Submission period 21 August to 15 September 2026. Deadline 15 September 2026.',
  deadline='2026-09-15', precision='exact',
  why='Students only, open to all countries, and a fortnight of runway.',
  view='Twelve days. A reasonable second entry if you are already building something for another '
       'bill here. On its own it would be a rush.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#e9f7f9', ink='#195d63', rule='#195d63', treatment='t-bulletin'),
  tags=['students only','fortnight','second entry']),

dict(id='opencv-2026', name='OpenCV AI Competition 2026, powered by AWS',
  host='OpenCV with AWS', platform='Devpost',
  url='https://opencv26.devpost.com/',
  domain='ai', kind='Online competition',
  blurb='The OpenCV foundation&rsquo;s annual AI competition, run on Devpost and backed by AWS.',
  submit='A Devpost project submission.',
  fmt='remote', location='Online',
  travel='None stated at any stage.',
  fee='Not stated', prize='$20,250 in prizes',
  team='Not stated in the eligibility block',
  eligible='Above the legal age of majority in your country of residence; all countries and '
           'territories except the standard exceptions.',
  effort='Moderate to heavy. Computer vision projects need real data.',
  difficulty=3,
  deadline_text='Submission period 26 August to 27 October 2026. Deadline 27 October 2026.',
  deadline='2026-10-27', precision='exact',
  extra='OpenCV is the library nearly all applied computer vision is built on, including most of the '
        'medical imaging entries on this wall.',
  why='Almost two months of runway, open to everyone, and run by the organisation whose library you '
      'would use for any imaging project anyway.',
  view='A strong second choice after Nebius. Long runway, no student restriction, and a computer '
       'vision project here is directly reusable for the Grand Challenge imaging bills. Build one '
       'thing, enter it twice.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#f9e6f2', ink='#630f43', rule='#630f43', treatment='t-chart'),
  tags=['computer vision','OpenCV','two months','reusable']),

dict(id='call-e', name='CALL-E: Your Code Is Calling',
  host='CALL-E', platform='Devpost',
  url='https://call-e.devpost.com/',
  domain='ai', kind='Online hackathon',
  blurb='A voice and telephony themed AI hackathon run through Devpost.',
  submit='A Devpost project submission.',
  fmt='remote', location='Online',
  travel='None stated at any stage.',
  fee='Not stated', prize='$10,000 in prizes',
  team='Not stated in the eligibility block',
  eligible='Not read individually &mdash; taken from the Devpost listing, which does not print the '
           'eligibility block in the API response.',
  effort='Moderate.',
  difficulty=3,
  deadline_text='Submission period 23 July to 14 September 2026. Deadline 14 September 2026.',
  deadline='2026-09-14', precision='exact',
  why='Voice agents are the one AI product category where a medical use case &mdash; triage calls, '
      'appointment handling &mdash; is obvious and underbuilt.',
  view='Eleven days, and I have not opened its eligibility block, so check that before starting. A '
       'voice triage demo would fit both this and Hack2Heal, which is the only reason it is worth '
       'the rush.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#eaf9e3', ink='#4d7a37', rule='#4d7a37', treatment='t-ticket'),
  tags=['voice','eligibility not read','short','medical angle']),

dict(id='assemblyai-voice', name='AssemblyAI Voice Agent Hackathon',
  host='lablab.ai with AssemblyAI', platform='lablab.ai',
  url='https://lablab.ai/ai-hackathons/assemblyai-voice-agent-hackathon',
  domain='ai', kind='Online hackathon',
  blurb='A month-long online challenge to build voice agents on AssemblyAI. The page makes a point '
        'of saying you can join at any time in the window &mdash; registration stays open for the '
        'whole build period, so starting halfway through is expected rather than penalised.',
  submit='A project built on AssemblyAI, submitted through lablab.ai. The guidelines list what the '
         'entry must contain: project title, a short and a long description, technology and category '
         'tags, a cover image and a video presentation.',
  fmt='remote', location='&ldquo;Fully online hackathon. Join and build from anywhere in the world.&rdquo;',
  travel='None stated at any stage.',
  fee='No fee is stated anywhere on the page. What joining requires is registration in two '
      'places, and the guidelines are explicit that <b>both</b> are needed: the lablab.ai platform '
      'and the lablab.ai Discord server.',
  prize='$10,000 prize pool &mdash; <b>$5,000 cash and $5,000 in AssemblyAI credits</b>. Worth '
        'reading as two halves rather than one number: only half of it is money.',
  team='<b>Teams of 1 to 6 people</b>, printed in the guidelines. You may enter alone, and the page '
       'points solo entrants at the dashboard and Discord to find teammates.',
  eligible='<b>&ldquo;Everyone is welcome to participate, regardless of previous AI or coding '
           'experience&rdquo;</b> &mdash; printed in the guidelines, and about as open as this wall '
           'gets. The only caveats are in the small print: submissions must be original and '
           'MIT-compliant, prize distribution may take up to 90 days, and lablab reserves the right '
           'to change or cancel the rules, prizes and terms.',
  effort='Light to moderate. Voice agents are mostly plumbing.',
  difficulty=2,
  deadline_text='1 to 30 September 2026.',
  deadline='2026-09-30', precision='exact',
  why='Explicitly designed so that joining late is fine, which is rare and exactly right for someone '
      'whose month is about to be taken over by counselling and a move.',
  view='The most forgiving entry on the wall. Four weeks, join whenever, plumbing rather than '
       'research, half the prize in cash. If your September gets eaten by the move, this is the one '
       'you can still pick up in the last week and submit something real to.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#e0e1f9', ink='#2b2e7a', rule='#2b2e7a', treatment='t-stencil'),
  tags=['voice','join late is fine','forgiving','cash']),

dict(id='amd-lablab-academy', name='Lablab x AMD AI Academy Challenge',
  host='lablab.ai with AMD', platform='lablab.ai',
  url='https://lablab.ai/ai-hackathons/amd-lablab-ai-academy-challenge',
  domain='ai', kind='Three-month developer programme',
  blurb='&ldquo;Learn. Build. Share. Grow.&rdquo; A three-month AMD-powered developer growth and '
        'community programme rather than a single hackathon.',
  submit='A project, submitted through lablab.ai as a concept, prototype and pitch with a video. The '
         'programme showcases finished entries alongside the technology each used &mdash; the ones on '
         'the page are built on <b>AMD ROCm and the AMD Developer Cloud</b>, which is the hardware '
         'this whole thing exists to get you onto. The submission deadline is shown on the page in '
         'local time: <b>2 December, 12:30 AM IST</b>.',
  fmt='remote', location='Online',
  travel='None stated at any stage.',
  fee='No fee is stated anywhere on the page. The AMD AI Academy learning pathway it is built '
      'around is the free starting point participants are told to use.',
  prize='<b>$5,000 prize pool</b>, printed on the page. Alongside it the programme offers things it '
        'weights just as heavily: early registration for AMD developer events, and <b>project '
        'recognition</b> &mdash; a potential showcase on AMD social channels or at an AMD developer '
        'event.',
  team='OPEN TO INDIVIDUAL PARTICIPANTS ONLY &mdash; stated on the listing, in those words. There is '
       'no team option at all, which is unusual on this platform.',
  eligible='No restriction by age, country or background is printed. What the page does state is who '
           'it is aimed at, and it is unusually direct: it is <b>&ldquo;geared towards beginners who '
           'are curious about the inner workings of AI and want hands-on GPU experience&rdquo;</b>, '
           'working through the AMD AI Academy learning pathway.',
  effort='Spread over three months by design.',
  difficulty=2,
  deadline_text='1 September to 1 December 2026.',
  deadline='2026-12-01', precision='exact',
  why='Three months, individuals only, and structured as learning rather than a sprint. The longest '
      'runway of any AI entry here.',
  view='This is a course with a scoreboard, and that suits how you actually learn. No team to '
       'coordinate, three months to work through it, and it runs straight through the period when '
       'you will be settling into a new city.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#f6f0ed', ink='#7a361f', rule='#7a361f', treatment='t-letter'),
  tags=['three months','individuals only','structured learning']),

dict(id='wearedevelopers', name='WeAreDevelopers Hackathon',
  host='WeAreDevelopers with lablab.ai', platform='lablab.ai',
  url='https://lablab.ai/ai-hackathons/wearedevelopers-hackathon',
  domain='ai', kind='Hybrid hackathon',
  blurb='&ldquo;Turn an idea into a working AI project.&rdquo;',
  submit='Not stated on the listing.',
  fmt='hybrid', location='Listed as Hybrid on lablab.ai. The on-site location is not stated on the listing.',
  travel='Not stated. Being hybrid, an on-site component exists but its terms were not printed.',
  fee='Not stated', prize='Not stated on the listing',
  team='Not stated', eligible='Not stated on the listing',
  effort='Light. A one-week hackathon.',
  difficulty=2,
  deadline_text='18 to 25 September 2026.',
  deadline='2026-09-25', precision='exact',
  why='Included because it is open and online-enterable, and you asked to see the borderline ones.',
  view='Thin: no prize, no eligibility and no venue printed on the listing. Open the page before '
       'spending anything on it. If the hybrid part turns out to be Europe-only in person, skip it.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#eaf6f1', ink='#127a4b', rule='#127a4b', treatment='t-hoard'),
  tags=['hybrid','thin listing','check before entering']),

dict(id='quantiphy', name='QuantiPhy &mdash; Quantitative Physical Reasoning from Video',
  host='Stanford, at NeurIPS 2026', platform='quantiphy.stanford.edu',
  url='https://quantiphy.stanford.edu/competition/index.html',
  domain='ai', kind='NeurIPS competition',
  blurb='Build vision-language models that estimate physical quantities &mdash; sizes, velocities, '
        'accelerations &mdash; directly from video, across microscopic, macroscopic and '
        'astronomical scales. It tests whether a prediction is grounded in what is visible or merely '
        'memorised.',
  submit='A single .csv matching the reference template, with numerical predictions in the required '
         'units for every test instance. The evaluation server scores it automatically.',
  fmt='remote', location='Online. The NeurIPS workshop is 11&ndash;12 December 2026.',
  travel='Not stated for competing. Winners get an oral, spotlight or poster slot.',
  fee='Not stated on the competition page.',
  prize='Per track: $1,000 and an oral presentation for first, $500 and a spotlight for second, $250 '
        'and a poster for third.',
  team='Teams of up to five members. One team per person, per track.',
  eligible='Organisers and direct collaborators are not eligible for prizes. No other restriction '
           'stated.',
  effort='Moderate. The submission is a CSV, which keeps the engineering light.',
  difficulty=3,
  deadline_text='Launched late June 2026, development phase July to September, FINAL SUBMISSION '
                'DEADLINE 23 October 2026 at 23:59 AoE.',
  deadline='2026-10-23', precision='exact',
  extra='Estimating a size or a velocity from an image is exactly what a radiologist does with a '
        'scale bar, and what a microscopist does all day.',
  why='A NeurIPS competition with a CSV submission, printed team rules, printed prizes and seven '
      'weeks of runway. Almost nothing on this wall is this clearly specified.',
  view='Strong candidate. The presentation slot is worth more than the $1,000 &mdash; a poster at a '
       'NeurIPS workshop is a real academic credential and you are eighteen. Seven weeks, five-person '
       'teams allowed, and no container to build.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#f4e7f6', ink='#70377a', rule='#70377a', treatment='t-gazette'),
  tags=['NeurIPS','CSV submission','academic credential','well specified']),

dict(id='learn2design', name='Learn2Design 2026 &mdash; Gravitational Wave Detector Design',
  host='SPRIN-D', platform='learn2design2026.com',
  url='https://www.learn2design2026.com/',
  domain='research', kind='Optimisation competition',
  blurb='Submit optimisation ALGORITHMS, not fixed designs. Your algorithm has a four-hour budget to '
        'tune roughly 200 continuous parameters of a gravitational-wave detector topology, inside a '
        'differentiable simulator.',
  submit='One algorithm class: a single .py file plus an optional requirements.txt and any extra '
         'files, packaged as one zip.',
  fmt='remote', location='Entirely online',
  travel='Not stated.',
  fee='Not stated',
  prize='&euro;25,000 total pool, sponsored by SPRIN-D, for the top-performing methods on hidden '
        'topologies. The split is not stated.',
  team='Not stated', eligible='No eligibility restriction is printed anywhere on the competition site. Neither is team size or a fee &mdash; the page carries the prize and the task and very little else.',
  effort='Moderate. The physics is inside the simulator; you are writing an optimiser.',
  difficulty=4,
  deadline_text='Submissions open now, public leaderboard from August. Submission deadline 15 '
                'October 2026.',
  deadline='2026-10-15', precision='exact',
  extra='Scored as the average best loss over 10 hidden topologies &mdash; lower is better.',
  why='You do not need to understand gravitational wave physics to compete. The simulator holds the '
      'physics; the competition is pure optimisation. That is an unusually clean separation.',
  view='Six weeks and one Python file. The barrier is far lower than the subject sounds, which is '
       'exactly the kind of mismatch worth exploiting. Read the scoring rule twice before starting.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#f4f6e4', ink='#464c1b', rule='#464c1b', treatment='t-chart'),
  tags=['optimisation','physics','one python file','lower barrier than it looks']),

dict(id='fair-universe', name='FAIR Universe &mdash; Weak Lensing Uncertainty Challenge',
  host='US Department of Energy / Lawrence Berkeley National Laboratory', platform='Codabench',
  url='https://fair-universe.lbl.gov/',
  domain='research', kind='NeurIPS competition',
  blurb='Phase 2 asks for out-of-distribution detection: given mock weak-lensing convergence maps, '
        'work out which test data has drifted away from the simulations the model was trained on.',
  submit='Algorithms and methods for analysing the convergence maps and flagging divergence from the '
         'training distribution.',
  fmt='remote', location='Entirely online',
  travel='Not stated.',
  fee='Not stated', prize='<b>Monetary prizes are confirmed but no amount is published.</b> The site says Phase 1 final submissions carry monetary prizes and points at a Winners page; no figure appears anywhere on the challenge site itself.',
  team='Not stated', eligible='Not stated on the page',
  effort='Moderate to heavy.',
  difficulty=4,
  deadline_text='&ldquo;The competition is now open for submission until 11:59 PM October 11th 2026 '
                '(UTC).&rdquo;',
  deadline='2026-10-11', precision='exact',
  extra='Knowing when a model is being asked about data unlike anything it was trained on is the '
        'same problem as knowing when a diagnostic model is out of its depth.',
  why='Out-of-distribution detection is the single most transferable idea in this list &mdash; it is '
      'what stops a medical model confidently misreading a scan it has never seen the like of.',
  view='Enter it for the technique, not the subject. Five weeks. Even reading the task description '
       'carefully will change how you think about every other model on this wall.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#e1edf6', ink='#13344c', rule='#13344c', treatment='t-bulletin'),
  tags=['out of distribution','NeurIPS','transferable idea','DOE']),

dict(id='prc-taxi-out', name='PRC Data Challenge 2026 &mdash; Aircraft Taxi-Out Time',
  host='EUROCONTROL Performance Review Commission', platform='prc-data-challenge-2026',
  url='https://prc-data-challenge-2026.netlify.app/',
  domain='ai', kind='Applied data science competition',
  blurb='Predict the taxi-out time of flights at ten major European airports, trained on every '
        'airport movement in 2025 and tested on January and July 2026.',
  submit='Predictions for the test movements, ranked by root mean squared error.',
  fmt='remote', location='Entirely online',
  travel='Not stated.',
  fee='Not stated',
  prize='&ldquo;The combined prize amount for the first 3 teams is 5000 EUR&rdquo;. The split is not '
        'stated.',
  team='Not stated',
  eligible='The page directs you to its eligibility page; teams from sanctioned countries are '
           'excluded. India is not a sanctioned country.',
  effort='Light to moderate. Tabular regression on a large but ordinary dataset.',
  difficulty=2,
  deadline_text='Competition period 1 September to 11 October 2026, closing at 23:59:59 CET.',
  deadline='2026-10-11', precision='exact',
  extra='It started two days before you read this &mdash; caught at the beginning rather than the end.',
  why='A tabular regression problem with real money, started this week, from an organisation with no '
      'reason to run a rigged contest. The most straightforwardly winnable non-medical entry here.',
  view='Good technical practice with a real prize. Five and a half weeks, no container, no GPU '
       'needed, and the whole problem is feature engineering &mdash; which is the skill that '
       'transfers to every tabular medical dataset you will ever meet.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#f6dde4', ink='#4c0b1e', rule='#4c0b1e', treatment='t-ticket'),
  tags=['tabular','caught early','no GPU needed','winnable']),

dict(id='zindi-bias-bounty', name='Bias Bounty Mapping Equity Challenge',
  host='Zindi', platform='Zindi',
  url='https://zindi.world/competitions/bias-bounty-mapping-equity-challenge',
  domain='research', kind='Data science competition',
  blurb='Are the communities most exposed to climate risk also the least well mapped? Open map data '
        'underpins emergency dispatch, evacuation routing and disaster relief, and its coverage is '
        'uneven. The challenge is to find and evidence that bias.',
  submit='Submissions through Zindi, 10 per day and 300 overall.',
  fmt='remote', location='Entirely online',
  travel='None stated at any stage.',
  fee='Free. Open-source tools only.',
  prize='$4,500 first, $2,500 second, $1,500 third, plus $1,000 for Best Bias Discovery and a prize '
        'for most impactful coverage.',
  team='Maximum team size 4.',
  eligible='&ldquo;Open to all.&rdquo;',
  effort='Moderate. Geospatial analysis rather than heavy modelling.',
  difficulty=3,
  deadline_text='Opened 28 August 2026, closes 1 November 2026.',
  deadline='2026-11-01', precision='exact',
  extra='The Best Bias Discovery prize rewards a finding rather than a leaderboard position, which '
        'is a different game entirely.',
  why='Two months of runway and a $1,000 side prize that goes to whoever finds the most interesting '
      'thing, not whoever tunes the best model. That is a category you can genuinely win.',
  view='Aim at Best Bias Discovery. Emergency dispatch and evacuation routing in badly mapped areas '
       'is a public health problem, and an Indian city you know well is a legitimate case study. '
       'This rewards insight over compute, which is your actual advantage.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#ebf4eb', ink='#224c23', rule='#224c23', treatment='t-riso'),
  tags=['geospatial','insight over compute','two months','winnable side prize']),

dict(id='zindi-drought', name='A Step Ahead of Drought &mdash; Forecasting Global Water Storage',
  host='ITU', platform='Zindi',
  url='https://zindi.world/competitions/one-step-ahead-of-drought-forecasting-global-water-storage-challenge',
  domain='research', kind='Data science competition',
  blurb='Predict how much water will be on the Earth&rsquo;s surface next month. Droughts are '
        'slow-moving crises, and early warning is the whole value.',
  submit='Submissions through Zindi, 5 per day and 200 overall.',
  fmt='remote', location='Entirely online',
  travel='None stated at any stage.',
  fee='Free. Open-source tools only.',
  prize='&euro;1,000 first, &euro;600 second, &euro;400 third, plus 5,000 Zindi points.',
  team='Maximum team size 4.',
  eligible='&ldquo;Open to all.&rdquo;',
  effort='Moderate. Time series forecasting on satellite-derived data.',
  difficulty=3,
  deadline_text='Opened 9 July 2026, closes 14 September 2026.',
  deadline='2026-09-14', precision='exact',
  why='ITU-run, open to all, and 5,000 Zindi points is a large ranking move for a small field.',
  view='Eleven days, so the prize is out of reach. The points are not: Zindi ranking is cumulative '
       'and it is what gets you noticed for the invited challenges later. A modest submission here '
       'is worth more than nothing.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#ebe8f4', ink='#2a1b4c', rule='#2a1b4c', treatment='t-chart'),
  tags=['time series','ITU','points matter','short']),

dict(id='nextstep-hacks', name='NextStep Hacks 2026',
  host='NextStep', platform='Devpost',
  url='https://nextstep2026.devpost.com/',
  domain='build', kind='Online hackathon',
  blurb='A student hackathon run through Devpost.',
  submit='A Devpost project submission.',
  fmt='remote', location='Online',
  travel='None stated at any stage.',
  fee='Not stated', prize='$1,750 in prizes',
  team='Not stated in the eligibility block',
  eligible='Ages 13 and over; students only; companies and professional organisations excluded.',
  effort='Light.',
  difficulty=1,
  deadline_text='Submission period 21 August to 13 September 2026. Deadline 13 September 2026.',
  deadline='2026-09-13', precision='exact',
  why='Small, student-only, and a real submission you can point at.',
  view='Ten days and a small pot. Worth it only as a place to submit something you have already '
       'built for a bigger bill. Do not start from scratch here.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#f4ede5', ink='#634519', rule='#634519', treatment='t-stencil'),
  tags=['students only','small','reuse a project']),

dict(id='hyperbloom-sept', name='Hyperbloom September &mdash; AI/ML',
  host='Hyperbloom', platform='Devpost',
  url='https://hyperbloom-september.devpost.com/',
  domain='ai', kind='Online hackathon',
  blurb='A monthly AI and machine learning hackathon run through Devpost.',
  submit='A Devpost project submission.',
  fmt='remote', location='Online',
  travel='None stated at any stage.',
  fee='Not stated', prize='$710 in prizes',
  team='Not stated in the eligibility block',
  eligible='Above the legal age of majority in your country of residence; students only; companies '
           'and professional organisations excluded; all countries except the standard exceptions.',
  effort='Light.',
  difficulty=1,
  deadline_text='Submission period 25 August to 14 September 2026. Deadline 14 September 2026.',
  deadline='2026-09-14', precision='exact',
  extra='It runs monthly, so missing this one means the October edition exists.',
  why='Monthly cadence matters more than the prize: a recurring hackathon is one you can plan for '
      'rather than stumble on.',
  view='Small money, eleven days. Its real value is that it repeats &mdash; note the pattern and aim '
       'at the October edition with something prepared.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#e2f4f1', ink='#0f6359', rule='#0f6359', treatment='t-hoard'),
  tags=['monthly','small','plan for the next one']),

dict(id='prom-virgo', name='Prom Virgo Challenge',
  host='Prometheus', platform='Devpost',
  url='https://virgo.devpost.com/',
  domain='ai', kind='Online hackathon',
  blurb='A design and machine learning challenge from the Prometheus series, which runs several '
        'hackathons a month on Devpost.',
  submit='A Devpost project submission.',
  fmt='remote', location='Online',
  travel='None stated at any stage.',
  fee='Not stated', prize='$1,500 in cash prizes, plus 2 non-cash prizes',
  team='Not stated in the eligibility block',
  eligible='Ages 13 and over; students only; companies and professional organisations excluded; all '
           'countries except the standard exceptions.',
  effort='Light.',
  difficulty=2,
  deadline_text='Submission period 31 August to 19 September 2026. Deadline 19 September 2026.',
  deadline='2026-09-19', precision='exact',
  extra='Prometheus also runs Prom Fall Classic (already on this wall) and monthly SPEED challenges.',
  why='Beginner-friendly, students only, and part of a series that runs continuously &mdash; so it '
      'is a standing option rather than a one-off.',
  view='Sixteen days for $1,500 in a small student field. This is the most realistic small-money '
       'entry on the wall. Prometheus runs these constantly, so treat the series as a recurring '
       'opportunity rather than this single instance.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#f4def0', ink='#632d5a', rule='#632d5a', treatment='t-riso'),
  tags=['beginner friendly','recurring series','realistic']),

dict(id='compsphere-12', name='COMPSPHERE 12',
  host='COMPSPHERE', platform='Devpost',
  url='https://compsphere12.devpost.com/',
  domain='build', kind='Online hackathon',
  blurb='A student computing hackathon run through Devpost.',
  submit='A Devpost project submission.',
  fmt='remote', location='Online',
  travel='None stated at any stage.',
  fee='Not stated', prize='$1,247 in prizes',
  team='Not stated in the eligibility block',
  eligible='AGES 15 TO 25 ONLY; students only; companies and professional organisations excluded; '
           'all countries except the standard exceptions. You are 18, so you qualify.',
  effort='Light.',
  difficulty=1,
  deadline_text='Submission period 3 August to 17 September 2026. Deadline 18 September 2026.',
  deadline='2026-09-17', precision='exact',
  why='A hard age ceiling of 25 is unusual and it works in your favour &mdash; the field cannot '
      'contain career engineers.',
  view='Fourteen days, small money, genuinely young field. Same advice as NextStep: enter it with '
       'something you have already built.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#e8f4db', ink='#456323', rule='#456323', treatment='t-ticket'),
  tags=['age capped at 25','students only','small','reuse a project']),

dict(id='galuxium-nexus', name='Galuxium Nexus V2',
  host='Galuxium', platform='Devpost',
  url='https://galuxium-nexus-v2-29411.devpost.com/',
  domain='build', kind='Online hackathon',
  blurb='An open build challenge run through Devpost.',
  submit='A Devpost project submission.',
  fmt='remote', location='Online',
  travel='None stated at any stage.',
  fee='Not stated', prize='$2,944 in prizes',
  team='Not stated in the eligibility block',
  eligible='Above the legal age of majority in your country of residence; students only; companies '
           'and professional organisations excluded; all countries except the standard exceptions.',
  effort='Light to moderate.',
  difficulty=2,
  deadline_text='Submission period 15 July to 31 October 2026. Deadline 31 October 2026.',
  deadline='2026-10-31', precision='exact',
  why='Nearly two months of runway for a small student hackathon, which is unusual &mdash; most give '
      'you two weeks.',
  view='Low stakes, long runway, students only. A good place to park a project you build for '
       'something else, since it stays open until the end of October.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#e9ebf1', ink='#192b63', rule='#192b63', treatment='t-bulletin'),
  tags=['students only','long runway','low stakes']),

dict(id='ai-content-engine', name='AI Content Engine Hackathon',
  host='Devpost community', platform='Devpost',
  url='https://ai-content-engine-hacks.devpost.com/',
  domain='ai', kind='Online hackathon',
  blurb='A beginner-friendly, open-ended AI and machine learning hackathon.',
  submit='A Devpost project submission.',
  fmt='remote', location='Online',
  travel='None stated at any stage.',
  fee='Not stated', prize='$2,000 in prizes',
  team='Not stated in the eligibility block',
  eligible='Not read individually &mdash; the Devpost API does not return the eligibility block.',
  effort='Light.',
  difficulty=1,
  deadline_text='Submission period 1 to 8 September 2026. Deadline 8 September 2026 &mdash; that window has CLOSED.',
  deadline='2026-09-08', precision='exact',
  why='Beginner-flagged with $2,000 and 84 registrants, which is a very small field for that money.',
  view='FIVE DAYS. Only worth it if you can build something in a weekend, which for an open-ended '
       'beginner-friendly brief you can. The small field is the whole argument.',
  conf='listing', checked='2026-09-03',
  theme=dict(paper='#f1e6e5', ink='#7a1712', rule='#7a1712', treatment='t-stencil'),
  tags=['beginner friendly','tiny field','five days','weekend build']),

dict(id='rice-urban', name='Rice University Urban Sustainability Hackathon',
  host='Rice University', platform='Devpost',
  url='https://rice-urban-sustainability.devpost.com/',
  domain='build', kind='Online hackathon',
  blurb='An urban sustainability hackathon run online by Rice University.',
  submit='A Devpost project submission.',
  fmt='remote', location='Online',
  travel='None stated at any stage.',
  fee='Not stated', prize='$17,500 in prizes',
  team='TEAM REQUIRED: 2 to 6 members. You cannot enter this alone.',
  eligible='AGES 18 AND OVER; COLLEGE STUDENTS ONLY; companies and professional organisations '
           'excluded.',
  effort='Moderate.',
  difficulty=3,
  deadline_text='Submission period 23 June to 18 September 2026. Deadline 18 September 2026.',
  deadline='2026-09-18', precision='exact',
  why='$17,500, online, college students only &mdash; and you will be a college student.',
  view='The team requirement is the obstacle, not the work: a minimum of two means you need at least '
       'one other person before you can submit at all. If you have someone from the IIT Madras '
       'programme who would join, this is worth the fifteen days. If not, it is closed to you and I '
       'would rather say so on the card than let you find out at the submission form.',
  conf='verified', checked='2026-09-03',
  theme=dict(paper='#e2f1e7', ink='#377a4e', rule='#377a4e', treatment='t-gazette'),
  tags=['college students only','TEAM REQUIRED','good money','need a partner']),

]


BILLS.append(dict(
 id='gopwnit-ctf',
 domain='build',
 kind='Capture the Flag',
 name='GopwnIt CTF',
 host='Gopwnit',
 platform='Unstop',
 url='https://unstop.com/hackathons/gopwnit-ctf-gopwnit-1745426',
 blurb='An online Capture The Flag competition &mdash; hidden flags, points for each one solved, and a leaderboard. Runs on a single day, 10 October 2026.',
 submit='Flags, found during the event and entered against each challenge.',
 fmt='remote',
 location='Online',
 travel='None.',
 fee='Free.',
 prize='Not stated. The record carries no prize table at all &mdash; do not assume there is money in it.',
 team='SOLO ONLY. Printed literally: &ldquo;No team required. This is a completely solo competition.&rdquo;',
 eligible='Printed literally: &ldquo;The competition is open to everyone.&rdquo; The record names students, working professionals, cybersecurity enthusiasts, developers, ethical hackers, researchers and independent learners, and states there is no restriction by college. <b>Nothing here excludes you.</b>',
 effort='One day, plus whatever preparation you choose.',
 difficulty=2,
 deadline_text='Registration opened 27 August 2026 and closes <b>5 October 2026</b>. The CTF itself runs on 10 October 2026.',
 deadline='2026-10-05',
 precision='exact',
 why='It is the second CTF on this wall and the more open of the two: solo, free, no college requirement, and 656 people already registered. A CTF is one of the few things where you can measure yourself against strangers in an evening and nobody asks what you are enrolled in.',
 view='Do this one. It costs a registration and a Saturday, the entry bar is a stated zero, and security is the branch of computing that rewards curiosity over coursework more than any other. Be clear-eyed about the reward: <b>no prize is published</b>, so treat it as practice and a leaderboard position, not as money. Try a few beginner challenges on any public CTF site first so the format is not new on the day.',
 conf='verified',
 checked='2026-09-10',
 theme={'paper': '#e7eaf3', 'ink': '#2b3556', 'rule': '#2b3556', 'treatment': 't-stencil'},
 tags=['free', 'solo', 'security', 'open to everyone', 'no prize stated'],
))

BILLS.append(dict(
 id='snapdragon-ai-lab',
 domain='ai',
 kind='Corporate AI build challenge',
 name='Snapdragon&#174; AI Lab Build &amp; Present Challenge',
 host='Qualcomm',
 platform='Unstop',
 url='https://unstop.com/competitions/crp-snapdragon-ai-lab-build-present-challenge-qualcomm-1748893',
 blurb='Submit an AI use-case proposal built for, or intended to be optimised for, Snapdragon-powered HP PCs, drawing models from Qualcomm AI Hub or other open-source platforms.',
 submit='A proposal. It may be newly created, or an existing project <b>significantly modified</b> to add AI models &mdash; the record says so in those words.',
 fmt='remote',
 location='Online, India',
 travel='None stated.',
 fee='Free.',
 prize='Awards are listed for 1st, 2nd, 3rd and 4th and for all participants, but <b>every cash figure is blank on the record</b>. Not stated.',
 team='Solo. Team size is one.',
 eligible='Printed literally: &ldquo;Residents of the Republic of India who are 18 years of age or above may participate.&rdquo; <b>You clear both.</b> Excluded: individuals residing outside India, anyone affiliated with government agencies or state-owned entities, restricted persons, and organisations involved in running the challenge.',
 effort='Moderate. It is a proposal, not a shipped product.',
 difficulty=3,
 deadline_text='Opened 4 September 2026, closes <b>30 September 2026, 23:59</b>.',
 deadline='2026-09-30',
 precision='exact',
 why='Qualcomm is a name that means something, it is open to any 18-year-old resident in India with no college requirement at all, and 2,777 people have registered &mdash; which tells you the bar to enter is genuinely low even if the bar to win is not.',
 view='The catch is the hardware: it wants solutions for Snapdragon-powered PCs and you do not have one. Read the wording before you decide it is closed to you &mdash; it accepts work <b>&ldquo;intended to be optimized for&rdquo;</b> that platform, which is a proposal, not a benchmark. Three weeks is enough for one honest use case written up properly. And note the prizes: the record lists four award tiers and <b>no amounts</b>, so do not enter this for the money until you have seen a number.',
 conf='verified',
 checked='2026-09-10',
 theme={'paper': '#e4f2fa', 'ink': '#123f63', 'rule': '#123f63', 'treatment': 't-chart'},
 tags=['qualcomm', 'free', 'india only', '18+', 'prize not stated'],
))

BILLS.append(dict(
 id='quantumxpo',
 domain='research',
 kind='Quantum project expo',
 name='QuantumXpo',
 host='RGUKT&ndash;IIIT Nuzvid',
 platform='Unstop',
 url='https://unstop.com/hackathons/quantumxpo-rajiv-gandhi-university-of-knowledge-technologies-rgukt-iiit-nuzvid-1752247',
 blurb='Build something with Qiskit that applies quantum computing to a real problem, and present it. An abstract, a demo video, and a repository link if you have one.',
 submit='An abstract on the organisers&rsquo; template, plus a short video explaining the problem, the approach, the method and the quantum implementation. A GitHub link if one exists.',
 fmt='remote',
 location='Online',
 travel='None stated.',
 fee='Free.',
 prize='Not stated. The record lists no prizes.',
 team='One to three.',
 eligible='The record states eligibility as <b>All</b> &mdash; no course, year or institution bar of any kind.',
 effort='A fortnight, if you are learning Qiskit from zero.',
 difficulty=4,
 deadline_text='Opened 10 September 2026, closes <b>30 September 2026</b>.',
 deadline='2026-09-30',
 precision='exact',
 why='<b>Fourteen people had registered when this was read.</b> That is the smallest field of anything on this wall, it is open to literally anyone, and Qiskit is free and runs on a simulator on your own laptop. The DREAM-Q challenge on this wall is the serious quantum door and it is years above you; this is the one where you could actually submit something.',
 view='Take this if you want to find out whether quantum interests you, and take it precisely because almost nobody has entered. Qiskit&rsquo;s own tutorials will get you to a working toy circuit in an evening, and the submission is an abstract and a video rather than a trained model. Be honest about what it is worth: <b>a university expo with no published prize and no name recognition</b>. The value is the thing you learn and a project you can point at, not the line on a CV.',
 conf='verified',
 checked='2026-09-10',
 theme={'paper': '#f2e9f7', 'ink': '#4a2a6b', 'rule': '#4a2a6b', 'treatment': 't-riso'},
 tags=['quantum', 'qiskit', 'tiny field', 'open to all', 'free'],
))

BILLS.append(dict(
 id='codexnovas-innovathon',
 domain='ai',
 kind='Online hackathon',
 name='Code-X-Novas Innovathon 2026',
 host='Code-X-Novas',
 platform='Unstop',
 url='https://unstop.com/hackathons/code-x-novas-innovathon-2026-national-software-ai-hackathon-code-x-novas-1737822',
 blurb='A national online software and AI hackathon run by a private technology company.',
 submit='Not stated on the record beyond the hackathon format.',
 fmt='remote',
 location='Online',
 travel='None &mdash; the record states the mode is online.',
 fee='Free.',
 prize='1st, 2nd and 3rd are listed with <b>no amounts against any of them</b>. Not stated.',
 team='One to three.',
 eligible='The record names, among others, <b>Medical</b> students explicitly, alongside undergraduate, postgraduate, engineering, management, law, arts/commerce/sciences, freshers and experienced professionals. <b>Medicine being named outright is rare and is why this is here.</b>',
 effort='A weekend.',
 difficulty=2,
 deadline_text='Opened 16 August 2026, closes <b>30 September 2026</b>.',
 deadline='2026-09-30',
 precision='exact',
 why='Its eligibility list names medical students by name, which almost no hackathon does, and 988 people have registered. Online, free, teams of up to three.',
 view='A reasonable first hackathon, and I would rate it no higher than that. The organiser is a private company rather than an institution, <b>no prize amount is published against any of the three ranks</b>, and the listing is mostly about the company. Enter it to practise shipping something in a weekend and to have a finished project, not for the name. If you only have room for one thing closing on 30 September, the Qualcomm one carries more weight.',
 conf='verified',
 checked='2026-09-10',
 theme={'paper': '#e9f3ec', 'ink': '#2c5c43', 'rule': '#2c5c43', 'treatment': 't-ticket'},
 tags=['medicine named', 'free', 'online', 'prize not stated'],
))

BILLS.append(dict(
 id='namma-space',
 domain='ai',
 kind='Technical competition',
 name='Namma Space &mdash; Techfest, IIT Bombay',
 host='Indian Institute of Technology Bombay',
 platform='Unstop',
 url='https://unstop.com/competitions/namma-space-techfest-iit-bombay-1749529',
 blurb='Reconstruct an indoor space in 3D, build a web viewer you can roam it in, add searchable points of interest and obstacle-aware pathfinding &mdash; then do it live on a venue you are handed at IIT Bombay.',
 submit='Round 1: a technical abstract, a web viewer proof of concept, a code repository and a 3&ndash;5 minute roaming video. Round 2: the upgraded platform with POI search and pathfinding, and a video. Round 3: on-site capture at IIT Bombay, then a ten-minute live pitch and technical Q&amp;A.',
 fmt='hybrid',
 location='Online for rounds 1 and 2; the finale is on the IIT Bombay campus, Mumbai',
 travel='<b>The finale is in Mumbai.</b> Rounds 1 and 2 are online; round 3 is two days on campus.',
 fee='Free.',
 prize='&#8377;1,50,000 prize pool for the top three.',
 team='One to four.',
 eligible='The record lists undergraduate and postgraduate students across engineering, management, and arts/commerce/sciences, and its course list <b>includes <code>bs</code></b> &mdash; the shape of your IIT Madras degree. No year-of-study bar is stated.',
 effort='Heavy. Three rounds across a month, and the last one is in person.',
 difficulty=4,
 deadline_text='Opened 3 September 2026, closes <b>30 September 2026</b>.',
 deadline='2026-09-30',
 precision='exact',
 why='It is Techfest at IIT Bombay, which is a name that carries, the money is real, and the course list names the <code>bs</code> degree you actually hold. The subject &mdash; 3D reconstruction and spatial search &mdash; is computer vision, which is the half of AI closest to medical imaging.',
 view='<b>This is the most technically serious thing added today and the least likely to fit your September.</b> Round 1 alone wants a working web viewer and a code repository, and the finale is two days in Mumbai during the fortnight before your Gujarat submission. I am putting it on the wall because you asked for the borderline to be shown rather than filtered out, and because the eligibility genuinely includes you. Read round 1 and decide honestly whether you have the weeks; if not, this runs every year.',
 conf='verified',
 checked='2026-09-10',
 theme={'paper': '#eef0e2', 'ink': '#4c5320', 'rule': '#4c5320', 'treatment': 't-hoard'},
 tags=['IIT Bombay', 'techfest', 'computer vision', 'travel needed', 'heavy'],
))


BILLS.append(dict(
 id='hacksprint-devpost',
 domain='build',
 kind='Online hackathon',
 name='HackSprint',
 host='HackSprint organisers',
 platform='Devpost',
 url='https://hacksprint.devpost.com/',
 blurb='An online hackathon on Devpost with a published rupee prize pool, running through September into early October.',
 submit='A Devpost project submission.',
 fmt='remote',
 location='Online',
 travel='None stated.',
 fee='Not stated.',
 prize='&#8377;3,00,000 in prizes.',
 team='Not stated on the page read.',
 eligible='Printed literally in the eligibility list: <b>&ldquo;Above legal age of majority in country of residence&rdquo;.</b> In India that is eighteen, and you are eighteen.',
 effort='Moderate.',
 difficulty=3,
 deadline_text='Submission period 9 September to 5 October 2026. The page prints the deadline as <b>October 05 at 2:15am EDT</b>.',
 deadline='2026-10-05',
 precision='exact',
 why='&#8377;3,00,000, online, and its only stated eligibility rule is being of legal age &mdash; which you now are. Four weeks of runway.',
 view='A straightforward one: no age ceiling, no institution requirement, no travel, and a month to build. The page states neither a fee nor a team rule, which are the two things worth reading the rules tab for before you start. Take it if you want a second Devpost submission alongside the Bharat challenge &mdash; the two windows overlap almost exactly, and one project rarely fits two briefs, so choose rather than split yourself.',
 conf='verified',
 checked='2026-09-10',
 theme={'paper': '#e2ece0', 'ink': '#33502f', 'rule': '#33502f', 'treatment': 't-ticket'},
 tags=['18+', 'free to enter', 'india money', 'online', 'overlaps Bharat'],
))

BILLS.append(dict(
 id='techcommons-v2',
 domain='build',
 kind='Online hackathon',
 name='TechCommons Hacks V2 &mdash; Hacks to Inspire',
 host='TechCommons',
 platform='Devpost',
 url='https://techcommons-hacks-v2.devpost.com/',
 blurb='A short online hackathon on Devpost for teenagers and very young adults.',
 submit='A Devpost project submission.',
 fmt='remote',
 location='Online',
 travel='None stated.',
 fee='Not stated.',
 prize='$6,300 in prizes.',
 team='Not stated on the page read.',
 eligible='Printed literally in the eligibility list: <b>&ldquo;Ages 13 to 20 only&rdquo;.</b> You qualify, and unlike the Bharat challenge you will still qualify for two more years.',
 effort='Light &mdash; it is a one-week window.',
 difficulty=2,
 deadline_text='Submission period 10&ndash;17 September 2026. The page prints the deadline as <b>September 17 at 3:00am EDT</b>.',
 deadline='2026-09-17',
 precision='exact',
 why='An age-capped field again, which is where your odds are best, and $6,300 against a one-week build. It is on the wall despite the short runway because the whole submission window is only a week long &mdash; this is not a deadline you missed, it is the shape of the thing.',
 view='<b>Seven days, and you are four days from a Gujarat submission.</b> I am putting it up because you asked for the borderline to be shown rather than filtered out, and because an age-capped hackathon is genuinely winnable &mdash; but the honest read is that this collides with the one deadline that actually matters this fortnight. Skip it unless Gujarat is finished early, and note that TechCommons appears to run these repeatedly, so a V3 is likely.',
 conf='verified',
 checked='2026-09-10',
 theme={'paper': '#f3e6ee', 'ink': '#6b2d4d', 'rule': '#6b2d4d', 'treatment': 't-riso'},
 tags=['AGE 13-20 ONLY', 'one week only', 'clashes with Gujarat', 'small money'],
))


BILLS.append(dict(
 id='slm-medical-advice',
 domain='med',
 kind='Small language model challenge',
 name='Domain-Specific SLM Challenge &mdash; Medical Advice track',
 host='TRI AI',
 platform='Codabench',
 url='https://www.codabench.org/competitions/17431/',
 blurb='Build a <b>small</b> language model for clinical decision support &mdash; interpreting symptoms and synthesising medical literature &mdash; with, in the organisers&rsquo; words, &ldquo;strict safety and evidence-based guardrails&rdquo;. The point is that a large model is too bulky, too expensive and too generic for a high-stakes narrow domain.',
 submit='A <b>.jsonl file of your model&rsquo;s generated answers</b> to a hidden set of prompts &mdash; not the model itself. Scoring is hybrid: <b>BERTScore 40%</b> for semantic similarity against the reference, and <b>an LLM-as-a-judge at 60%</b>, a GPT-4o-mini evaluator scoring factual accuracy and safety guardrails. Ten submissions per day.',
 fmt='remote',
 location='Online, on Codabench',
 travel='None.',
 fee='Free to enter, but <b>you supply your own compute</b> &mdash; the terms say participants are responsible for their own GPUs or cloud instances, and Codabench is used only for evaluation.',
 prize='<b>Certificates of Excellence.</b> That is the whole reward string; no cash is mentioned.',
 team='Not stated. The terms say &ldquo;participant/team&rdquo; but print no size limit.',
 eligible='No age, country or institution restriction is printed. The description says the track &ldquo;aims for students&rdquo;, which is a statement of intent rather than a rule. Two hard conditions do bind you: the model must be <b>trained by you</b> &mdash; submitting raw ChatGPT output as your own is disqualifying &mdash; and <b>no PII or PHI</b> may appear in your training data or submissions.',
 effort='Moderate. Fine-tuning a small model is a laptop-and-Colab job, not a cluster job.',
 difficulty=3,
 deadline_text='One phase, printed on the record: Main Competition Phase <b>8 July to 31 December 2026</b>.',
 deadline='2026-12-31',
 precision='exact',
 why='<b>Of everything found on this platform today, this is the one you could actually finish.</b> It is medicine, it is language models, the submission is a text file rather than a container, and there were <b>seven registered participants and zero submissions</b> when the record was read. A field that empty does not stay empty, but it is empty now.',
 view='<b>Take this one.</b> Three and a half months, no institution required, no data-access gate, and the whole submission is a .jsonl of generated answers &mdash; which means the hard part is genuinely the modelling and not the plumbing. Read how it is scored before you build anything: sixty per cent of your mark comes from an LLM judging factual accuracy and <b>safety guardrails</b>, so a model that answers confidently and wrongly will score worse than one that hedges correctly. That is a real lesson about clinical language models and it is worth more than the certificate. One caution the organisers print themselves and mean: these outputs are for research only and are never medical advice.',
 conf='verified',
 checked='2026-09-10',
 theme={'paper': '#eef4fb', 'ink': '#1d3f6b', 'rule': '#1d3f6b', 'treatment': 't-letter'},
 tags=['small language models', 'clinical', 'empty field', 'finishable', 'no institution needed'],
))

BILLS.append(dict(
 id='bioml-local-rank',
 domain='med',
 kind='Biomedical ontology matching',
 name='BioML 2026 &mdash; Local Equivalence Ranking',
 host='OAEI Bio-ML track',
 platform='Codabench',
 url='https://www.codabench.org/competitions/17423/',
 blurb='Given a medical concept from one terminology and a frozen pool of 100 candidates from another, rank them best-first &mdash; across three pairs: <b>NCIT&ndash;DOID, SNOMED&ndash;FMA and SNOMED&ndash;NCIT</b>. This is the machinery that lets one hospital&rsquo;s records be read by another&rsquo;s system.',
 submit='Prediction files only &mdash; <b>no participant code is executed</b>. A ranking per pair, scored with MRR and Hits@1/5/10, macro-averaged across the three pairs. A scoring kit (validate_ranking.py, score_local.py) is provided so you can self-score before submitting.',
 fmt='remote',
 location='Online, on Codabench',
 travel='None.',
 fee='Free. No entry fee is printed.',
 prize='Not stated. The record carries no reward string. Leaderboard scores and system names may be published on the project site and in the OAEI results.',
 team='Not stated on the record.',
 eligible='<b>THE LICENCE IS THE GATE, and it is printed plainly:</b> the data derives from NCIT, MONDO, DOID, FMA and from UMLS/SNOMED CT, and &ldquo;SNOMED CT and UMLS-derived material is <b>restricted</b>: you must hold the relevant SNOMED CT Affiliate / UMLS Metathesaurus licence to access the gated portions, and you may not redistribute them.&rdquo; No age, country or institution rule is printed beyond that.',
 effort='Moderate. Ranking with embeddings; the ontologies are the hard part, not the model.',
 difficulty=4,
 deadline_text='One phase: Evaluation (2026), <b>12 July to 30 September 2026</b>.',
 deadline='2026-09-30',
 precision='exact',
 why='This wall already carries a SNOMED CT challenge, and this is the same world seen from the research side: how two medical vocabularies are made to agree. It is also unusually gentle mechanically &mdash; you upload a ranking file, nothing of yours is executed.',
 view='<b>Settle the licence question before anything else.</b> The terms require a SNOMED CT Affiliate or UMLS licence for the gated parts, and whether you already have access through a national or institutional route is exactly the sort of thing worth asking rather than assuming &mdash; India is a SNOMED International member country, but I am not going to state on this wall what your particular access is when the page does not. Three weeks of runway, a three-entrant field, and a scoring kit you can run offline. If the licence clears, this is cheap to try.',
 conf='verified',
 checked='2026-09-10',
 theme={'paper': '#eae6f4', 'ink': '#3b2c66', 'rule': '#3b2c66', 'treatment': 't-stencil'},
 tags=['SNOMED CT', 'ontologies', 'licence gate', 'no code executed', 'tiny field'],
))

BILLS.append(dict(
 id='bioml-global-align',
 domain='med',
 kind='Biomedical ontology matching',
 name='BioML 2026 &mdash; Global Equivalence Alignment',
 host='OAEI Bio-ML track',
 platform='Codabench',
 url='https://www.codabench.org/competitions/17424/',
 blurb='The harder half of the same task: instead of ranking 100 candidates for one concept, produce a <b>complete alignment</b> between two whole medical ontologies &mdash; every mapping you believe holds, across NCIT&ndash;DOID, SNOMED&ndash;FMA and SNOMED&ndash;NCIT.',
 submit='One OAEI Alignment file per ontology pair, as <b>RDF/XML or TSV</b>. Scored semi-supervised against a hidden test slice: repaired coherence-aware precision/recall/F1 is the headline, standard P/R/F1 auto-scores in-container, and reasoner-based Global Coherence is reported separately on the track website. A public refs_equiv/train.tsv of positive mappings is given for each pair.',
 fmt='remote',
 location='Online, on Codabench',
 travel='None.',
 fee='Free. No entry fee is printed.',
 prize='Not stated. No reward string on the record.',
 team='Not stated on the record.',
 eligible='Identical to the Local Ranking task, and the same gate: NCIT, MONDO, DOID and FMA are open, while <b>SNOMED CT and UMLS-derived material is restricted and needs the relevant SNOMED CT Affiliate or UMLS Metathesaurus licence</b>. Nothing else is restricted on the page.',
 effort='Heavy. A full alignment is a much larger object than a ranked list, and coherence is scored.',
 difficulty=5,
 deadline_text='One phase: Evaluation (2026), <b>12 July to 30 September 2026</b>.',
 deadline='2026-09-30',
 precision='exact',
 why='It is the same subject as its sibling task and the same three weeks, but it is where the interesting idea lives: your alignment is scored for <b>logical coherence</b>, not just accuracy. Two mappings can each look right and together imply something medically impossible, and a reasoner will find it.',
 view='<b>Do not take both.</b> They share data, a deadline and a licence gate, and this one is markedly harder &mdash; eight entrants against three, and twenty-one submissions against three. If the SNOMED licence clears and you want to try the pair, start with Local Ranking to learn the data format and only come here if there is time left, which in three weeks there will not be. Worth reading either way for the coherence idea alone.',
 conf='verified',
 checked='2026-09-10',
 theme={'paper': '#f2f6e8', 'ink': '#46521f', 'rule': '#46521f', 'treatment': 't-riso'},
 tags=['SNOMED CT', 'ontologies', 'coherence', 'licence gate', 'harder sibling'],
))

BILLS.append(dict(
 id='fusion-equilibrium',
 domain='research',
 kind='Physics machine learning challenge',
 name='Fusion Equilibrium Challenge (NeurIPS 2026)',
 host='Fusion Equilibrium Challenge organisers',
 platform='Codabench',
 url='https://www.codabench.org/competitions/17739/',
 blurb='Reconstruct a fusion reactor&rsquo;s magnetic state &mdash; the 2-D poloidal flux map, the plasma boundary and the equilibrium scalars &mdash; from <b>non-magnetic diagnostics alone</b>, on the DIII-D tokamak, and then zero-shot on a different machine, MAST.',
 submit='Full-resolution predictions against the public test fold, five submissions a day and 100 in total, under a 15 GB platform quota. For the Final phase your single highest-scoring Development entry is the basis for ranking, with a few confirmation submissions allowed and the leaderboard hidden until close.',
 fmt='remote',
 location='Online, on Codabench',
 travel='None.',
 fee='Free. No entry fee is printed.',
 prize='<b>Not stated as an amount</b>, but prizes exist: the terms set conditions for &ldquo;the top three teams in each award category&rdquo; to receive one &mdash; source released under an OSI-approved licence and a 1&ndash;2 page methods report, before prizes are paid. The record carries no reward string, so the value is genuinely unprinted rather than unread.',
 team='Not stated as a size. The terms are written in terms of teams throughout.',
 eligible='No age, country or institution restriction is printed. Organising-team members with access to the hidden ground truth are excluded from prizes. All participants are bound by the <b>NeurIPS Code of Conduct</b>. External public datasets and pre-trained models are allowed but must be disclosed in the methods report.',
 effort='Heavy, and in physics you have not touched.',
 difficulty=5,
 deadline_text='Two phases: Development <b>27 July to 18 October 2026</b>, then the blind Final <b>19 to 26 October 2026</b>.',
 deadline='2026-10-26',
 precision='exact',
 why='<b>The NeurIPS name is the reason, and the dataset licence is the second reason.</b> A competition run at the largest machine-learning conference in the world carries weight that a college fest cannot, and the data is CC BY 4.0 &mdash; yours to keep and publish on afterwards, with attribution. 151 people have made 469 submissions, so this one is real.',
 view='<b>This is not medicine and I am not pretending it is.</b> It is on the wall because it is the most prestigious thing found on this platform and because zero-shot transfer &mdash; train on one machine, be scored on a different one &mdash; is a genuinely important idea you will meet again the moment a clinical model trained at one hospital is asked to work at another. That is the transferable lesson. As an entry, six weeks against 151 established teams in plasma physics is not a fight worth picking in your first MBBS term. Read the task and the terms; skip the leaderboard.',
 conf='verified',
 checked='2026-09-10',
 theme={'paper': '#f5ece0', 'ink': '#6b4423', 'rule': '#6b4423', 'treatment': 't-hoard'},
 tags=['NeurIPS', 'plasma physics', 'zero-shot transfer', 'CC BY 4.0', 'stretch'],
))
