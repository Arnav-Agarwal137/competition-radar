# -*- coding: utf-8 -*-
"""Aggregates the bill files and holds the source directory.

Split into bills_med / bills_ai / bills_open only so each file stays readable.
The wall does not care which file an entry came from.
"""
import bills_med, bills_ai, bills_open
import judgement

# TWO DATES OF THE SAME TYPE, WITH OPPOSITE UPDATE RULES. Do not touch one
# thinking you are touching the other - "update the date" is not an instruction
# that identifies either of them.
#
#   READ_ON  is a fact about WHEN A HUMAN HARVESTED THE SOURCES. It appears in
#            the masthead as "sources read 3 Sep 2026" and it MUST NOT MOVE for
#            a rebuild, a re-check, or an added bill. Moving it stamps the page
#            with a freshness it does not have.
#
#   TODAY    is the baseline the baked countdowns are measured from, and it
#            MUST MOVE ON EVERY BUILD. It was left at 2026-09-03 for a week and
#            found on 10 September, when an entry that had closed two days
#            earlier still baked as "4 days" and sat in the closing-this-week
#            banner. Nothing errored and the parity check agreed with the page,
#            because the parity check measures against this same constant - a
#            stale baseline is invisible to a checker that shares it.
#
# In a browser reweather() recomputes every count from data-deadline, so the
# live page self-corrects; the baked values are the no-JS fallback and the
# thing every offline check reads. Both deserve to be right.
READ_ON = '2026-09-03'
TODAY = '2026-09-10'

BILLS = bills_med.BILLS + bills_ai.BILLS + bills_open.BILLS

_ids = [b['id'] for b in BILLS]
assert len(_ids) == len(set(_ids)), 'duplicate bill id: %s' % (
    [i for i in _ids if _ids.count(i) > 1])

# Fields every bill must carry, so a half-written entry cannot reach the wall.
_REQUIRED = ('id name host platform url domain kind blurb submit fmt location travel fee prize '
             'team eligible effort difficulty deadline_text deadline precision why view conf '
             'checked theme tags').split()
for _b in BILLS:
    _missing = [f for f in _REQUIRED if f not in _b]
    assert not _missing, 'bill %s is missing %s' % (_b['id'], _missing)
    assert _b['conf'] in ('verified', 'listing', 'stale'), _b['id']
    assert _b['fmt'] in ('remote', 'in-person', 'hybrid'), _b['id']
    assert 0 <= _b['difficulty'] <= 5, _b['id']

# build.py decides the Free filter chip from fee.lower().startswith(), so a bill
# whose fee text SAYS there is no fee but does not START that way is silently
# filed as paid and disappears from that filter. It happened to six bills at
# once on 3 Sep 2026, including a scholarship whose page prints NO APPLICATION
# FEE in as many words. Fixing the six was not enough - this asserts the class,
# so the next one cannot ship quietly.
# My prestige and learning ratings live in judgement.py, apart from the facts.
# Assert BOTH directions: a bill with no rating would sort as if it were worthless
# and quietly sink to the bottom, and a rating for an id that no longer exists is
# a rename nobody finished.
_rated = set(judgement.RANK)
_have = {b['id'] for b in BILLS}
assert not (_have - _rated), 'bills with no prestige/learning rating: %s' % sorted(_have - _rated)
assert not (_rated - _have), 'ratings for bills that do not exist: %s' % sorted(_rated - _have)
for _b in BILLS:
    _p, _l = judgement.RANK[_b['id']]
    assert 1 <= _p <= 5 and 1 <= _l <= 5, 'rating out of range: %s' % _b['id']
    _b['prestige'], _b['learning'] = _p, _l


_FREE_PREFIX = ('free', 'no fee', 'none')
_SAYS_FREE = ('no application fee', 'no purchase', 'no entry fee', 'no cost to enter')
for _b in BILLS:
    _f = _b['fee'].lower()
    if any(t in _f for t in _SAYS_FREE) and not _f.startswith(_FREE_PREFIX):
        raise AssertionError(
            'bill %s says it is free but would be filed as paid - start its fee '
            'field with "Free" or reword it: %r' % (_b['id'], _b['fee'][:70]))


# ---------------------------------------------------------------- sources
#
# checked=True means a page was actually opened on the date given and bills on
# this wall came from it (or it was opened and had nothing).
#
# He asked specifically whether foreign platforms were considered. They are, and
# the ones below marked 'not yet' are named rather than quietly omitted, so the
# gap is visible instead of looking like a complete list.

SOURCES = [
 # ---------- harvested, and bills on this wall came from them
 dict(name='Internshala Competitions', url='https://internshala.com/competitions/',
      kind='India-wide student competitions, workshops and internships',
      note='ADDED 7 September 2026 by the first monthly source sweep &mdash; the only genuinely new '
           'source the sweep found, and it had been missed by all forty before it. Free to browse, '
           'India-specific, and it carries dated listings out to September 2027. It surfaced the '
           'IIRS/ISRO student internship and an IEEE PerCom paper call that no other source here '
           'indexes. TREAT IT AS AN AGGREGATOR: its IEEE PerCom card printed a 28 February 2027 '
           'deadline while the body text of the same card gave a paper deadline of 11 September '
           '2026. Open the thing&rsquo;s own page before writing a bill from it.',
      checked=True, region='india'),
 dict(name='Grand Challenge', url='https://grand-challenge.org/challenges/',
      kind='Medical imaging challenges, global',
      note='Re-swept 3 Sep 2026 and it was the richest seam by far: 13 open, ALL TWELVE we did not '
           'have are now on the wall. WARNING: it lists a challenge as &ldquo;Accepting '
           'submissions&rdquo; when only a post-challenge phase is open. PANTHER and ToothFairy3 '
           'both ended in 2025 and still say that. Only the /timeline/ page tells you the truth.',
      checked=True, region='global'),
 dict(name='Devpost', url='https://devpost.com/hackathons?order_by=recently-added',
      kind='Hackathons, global',
      note='Re-swept 3 Sep 2026: 57 open, 18 taken. The listing page renders nothing to a fetcher, '
           'but devpost.com/api/hackathons returns JSON in a browser, and each hackathon page has a '
           '&ldquo;Who can participate&rdquo; block printing age, student status, team rule and the '
           'excluded-country list. ALWAYS sort by recently-added.', checked=True, region='global'),
 dict(name='Unstop', url='https://unstop.com/hackathons?oppstatus=open', kind='India, everything',
      note='Re-swept 3 Sep 2026: 152 hackathons, 412 competitions, 3 scholarships open. CORRECTION '
           'TO AN OLD NOTE &mdash; its search URL IS reachable: '
           'unstop.com/api/public/opportunity/search-result with opportunity, oppstatus, page and '
           'searchTerm returns prize, team size, isPaid and registration close date as JSON. '
           'searchTerm=medical across competitions returns zero, which is an answer, not a gap.',
      checked=True, region='India'),
 dict(name='DrivenData', url='https://www.drivendata.org/competitions/', kind='ML for social good, global',
      note='Re-swept 3 Sep 2026 and it was carrying six we never took, two of them clinical. Its '
           'rules pages are the clearest of any platform here: 18+, no purchase necessary, '
           'OFAC-designated countries excluded, India not among them.', checked=True, region='global'),
 dict(name='EvalAI', url='https://eval.ai/web/challenges/list', kind='Open AI challenges, IIT Hyderabad',
      note='HARVESTED 3 Sep 2026, first time. Its public JSON API '
           '(/api/challenges/challenge/present/approved/public) lists everything in one call. 20 '
           'open, 5 taken. eBay&rsquo;s university competition was rejected &mdash; Canada only. '
           'Fifteen others are permanently-open leaderboards dated 2099.',
      checked=True, region='global'),
 dict(name='Zindi', url='https://zindi.world/competitions', kind='ML competitions, Africa-founded',
      note='Re-swept 10 Sep 2026 THROUGH ITS API, which is the thing that had never been tried: '
           '<b>api.zindi.africa/v1/competitions returns JSON</b> and lists 10 competitions with '
           'rewards and both dates. The old note said &ldquo;use zindi.world, not zindi.africa&rdquo; '
           '&mdash; true of the SITE, and false of the API, which is why this source sat recorded as '
           'a JS shell needing a browser. 10 listed, 5 already here, 3 already closed, 2 are Zindi '
           'points-only university jams. Small fields and real money.',
      checked=True, region='global'),
 dict(name='Kaggle', url='https://www.kaggle.com/competitions', kind='ML competitions, global',
      note='Re-swept 3 Sep 2026 with the browser: 8 active competitions plus the Getting Started '
           'set, and EVERY ONE was already on this wall. Nothing new, which is a clean result '
           'rather than a gap. Sort by NEWEST. A closed competition says Late Submission instead of '
           'Join Competition.', checked=True, region='global'),
 dict(name='DREAM Challenges', url='https://dreamchallenges.org/open-challenges/',
      kind='Biomedical data science, global',
      note='HARVESTED 3 Sep 2026, first time, and it was worth the wait: 3 open, all 3 taken. The '
           'Digital Pen challenge has not launched yet and is open for PRE-REGISTRATION, which is '
           'the single best state a competition can be in for you. Challenge wikis live on '
           'synapse.org and need a real browser plus a ten-second wait to render.',
      checked=True, region='global'),
 dict(name='ML Contests', url='https://mlcontests.com', kind='Aggregator, global',
      note='Re-swept 3 Sep 2026 and it earned its place: 28 listed, and it surfaced NINE '
           'competitions hosted on their own sites that no platform here indexes &mdash; QuantiPhy, '
           'Learn2Design, FAIR Universe, the EUROCONTROL taxi-out challenge, RealPDE and others. It '
           'also named eight platforms this wall had never heard of. CAUTION: it listed the AMD '
           '$1.1M contest as active when registration had closed and the event ran in May.',
      checked=True, region='global'),
 dict(name='HackerEarth Challenges', url='https://www.hackerearth.com/challenges/hackathon/',
      kind='Hackathons and contests, global',
      note='HARVESTED 3 Sep 2026, first time. Only 3 live, but one of them is the biggest rupee '
           'prize on this wall: Schneider Electric&rsquo;s Yuva Yodha at &#8377;45 lakh. Needs a '
           'browser; every listing redirects out to the sponsor&rsquo;s own site, which is where '
           'the real dates and eligibility are.', checked=True, region='global'),
 dict(name='lablab.ai', url='https://lablab.ai/ai-hackathons', kind='Generative AI hackathons, global',
      note='HARVESTED 3 Sep 2026, first time. Returns 403 to a fetcher; fine in a browser. Several '
           'live, 3 taken. Its hackathons are unusually forgiving &mdash; the AssemblyAI one says '
           'outright that you can join at any point in the build window.', checked=True, region='global'),
 dict(name='Major League Hacking', url='https://www.mlh.com/seasons/2027/events',
      kind='Student hackathons, global',
      note='HARVESTED 3 Sep 2026, first time, AND THERE IS A TRAP IN THE URL: the 2026 season ended '
           'in June, so /seasons/2026/ shows only expired events. The live one in September 2026 is '
           'the 2027 SEASON. mlh.io redirects to mlh.com. Global Hack Weeks are digital-only and '
           'free.', checked=True, region='global'),
 dict(name='Codabench', url='https://www.codabench.org', kind='Open competition hosting, global',
      note='FULLY WALKED 10 Sep 2026, and it had never been: <b>1,486 of 1,486 rows</b>, against the '
           '20 this wall had ever seen. The listing needs a login; the API does not. <b>The trap is '
           'in the paginator</b> &mdash; /api/competitions/public/ answers on www.codabench.org, but '
           'the `next` URL it hands back points at codabench-prod.lisn.upsaclay.fr, which does not '
           'answer from here. So page 2 always failed with a connection timeout and read as a flaky '
           'network, when page 1 succeeding every time was the tell. Keep the path, rewrite the host. '
           'End dates and prizes are NOT in the listing row, so each candidate still needs its own '
           '/api/competitions/{id}/ record. 100 survived the filter, 22 were opened, 8 were open, '
           '7 taken.', checked=True, region='global'),
 dict(name='Tianchi', url='https://tianchi.aliyun.com/competition/activeList', kind='Data science, China',
      note='HARVESTED 3 Sep 2026, first time. Real competitions with large prizes and an English '
           'interface, but the competition pages themselves are in Chinese and registering needs an '
           'Alibaba account &mdash; which only he can create. One taken: a Human Phenotype Ontology '
           'concept-recognition task that is a better subject match than most English-language AI '
           'competitions here.', checked=True, region='foreign'),
 dict(name='Buddy4Study', url='https://www.buddy4study.com/scholarships/medical',
      kind='Medical scholarships, India',
      note='HARVESTED 3 Sep 2026, first time, and it produced the best single find of the sweep: '
           'the SBI Platinum Jubilee Asha Scholarship for Medical Students, up to &#8377;2,00,000 a '
           'year, closing 19 September. 13 live medical scholarships. Needs a browser. Scholarships '
           'are not competitions, but the lead-time problem is identical and the money is larger.',
      checked=True, region='India'),
 dict(name='MyGov Innovate India', url='https://innovateindia.mygov.in',
      kind='Indian government challenges',
      note='Re-swept 3 Sep 2026: five open, four already on the wall. The fifth, D.E.S.I.G.N for '
           'BioE3, was re-checked at source and its exclusion CONFIRMED &mdash; classes VI to XII '
           'only, and the prize is a certificate. Still the richest government source, and this is '
           'the category the Gujarat challenge came from.', checked=True, region='India'),
 dict(name='AIcrowd', url='https://www.aicrowd.com/challenges', kind='ML competitions, Switzerland',
      note='Re-swept 3 Sep 2026: 6 &ldquo;active&rdquo;, of which ARC White-Box was already here and '
           'the other five are stale post-challenge rounds &mdash; one shows &ldquo;27087 days '
           'left&rdquo;. Nothing new. Hosts official NeurIPS competitions, so worth rechecking each '
           'cycle.', checked=True, region='global'),

 # ---------- opened, and genuinely empty or blocked. Written down so the gap is
 # ---------- visible instead of looking like something nobody got round to.
 dict(name='Gates Foundation Grand Challenges', url='https://gcgh.grandchallenges.org/challenges',
      kind='Global health funding calls',
      note='CHECKED 3 Sep 2026: NOTHING OPEN. Every call on page one has a deadline already past, '
           'the latest being 21 July 2026. They are also institutional research grants rather than '
           'student competitions. Recheck each quarter.', checked=True, region='global'),
 dict(name='Topcoder', url='https://www.topcoder.com/challenges', kind='Paid challenges, global',
      note='CHECKED 3 Sep 2026: the Active Challenges page renders &ldquo;No challenges found&rdquo; '
           'across development, design, data science and QA. Nothing open at all. Needs a browser; '
           'a fetcher only ever sees &ldquo;Loading Challenges&rdquo;.', checked=True, region='global'),
 dict(name='Analytics Vidhya DataHack', url='https://www.analyticsvidhya.com/datahack',
      kind='Data science hackathons, India',
      note='CHECKED 3 Sep 2026: the old contest listing 301s and then 404s, and the DataHack page '
           'that replaced it shows skill tests and marketing rather than any live competition. '
           'India&rsquo;s Kaggle-alike appears to have stopped running open hackathons.',
      checked=True, region='India'),
 dict(name='event.data.gov.in', url='https://event.data.gov.in', kind='Indian government hackathons',
      note='Re-checked 3 Sep 2026: STILL ENTIRELY CLOSED, exactly as on the first pass. The most '
           'recent was the UIDAI Data Hackathon, which ended 20 January 2026. Nothing live. Check '
           'it anyway &mdash; it is a government hub and things appear without warning.',
      checked=True, region='India'),
 dict(name='Signate', url='https://competition-content.signate.jp/', kind='Data science, Japan',
      note='CHECKED 3 Sep 2026: BLOCKED BY A SIGN-UP WALL. signate.jp/competitions redirects to a '
           'marketing page that states plainly that using the service requires SIGNATE membership, '
           'and the site is entirely in Japanese. I do not create accounts. IF HE WANTS THIS SOURCE '
           'OPENED, HE HAS TO REGISTER HIMSELF.', checked=True, region='foreign'),
 dict(name='Hult Prize', url='https://www.hultprize.org', kind='Student social enterprise, global',
      note='CHECKED 3 Sep 2026: the site prints past winners and headline statistics but NO current '
           'challenge, eligibility, dates or fee. Nothing enterable could be read. Explicitly for '
           'students, campus rounds worldwide, so recheck when the next cycle is announced.',
      checked=True, region='global'),
 dict(name='XPRIZE', url='https://www.xprize.org/prizes', kind='Long-horizon grand challenges, global',
      note='CHECKED 3 Sep 2026: three Active &mdash; Quantum Applications $5M, Water Scarcity $119M, '
           'Healthspan $101M. None prints an open entry window; Quantum&rsquo;s only date is a '
           'wildcard registration that closed 4 March 2026. Multi-year, team-based. Quantum is on '
           'the wall for orientation, flagged as not currently enterable.', checked=True, region='global'),
 dict(name='Devfolio', url='https://devfolio.co/hackathons/open', kind='Hackathons, India-heavy',
      note='CHECKED 3 Sep 2026, first time. One of your brother&rsquo;s three suggestions. Ten '
           'hackathons with applications open, and NINE ARE OFFLINE Indian college events whose city '
           'the listing does not print. Only one is online. Useful finding: Devfolio is an '
           'in-person-hackathon index, not a remote-competition source.', checked=True, region='India'),
 dict(name='Luma', url='https://luma.com/discover', kind='Events and meetups, global',
      note='CHECKED 3 Sep 2026, first time. Another of your brother&rsquo;s suggestions. It is an '
           'event-hosting tool, not a competition index: about 4,000 events under AI, mostly '
           'meetups, WITH NO FILTER FOR COMPETITIONS. Real contests do appear on it &mdash; the '
           'AMD $1.1M speedrun was hosted here &mdash; but only when an organiser happens to choose '
           'it, so it cannot be swept systematically.', checked=True, region='global'),
 dict(name='Partiful', url='https://partiful.com/discover', kind='Social events, global',
      note='CHECKED 3 Sep 2026, first time. The third of your brother&rsquo;s suggestions, and it is '
           'a party-invitation tool: stoop sales, DJ nights, a beer mile. NO COMPETITIONS OF ANY '
           'KIND. Recorded so nobody spends time on it again.', checked=True, region='global'),
 dict(name='Numerai', url='https://numer.ai', kind='Ongoing quant tournament, global',
      note='CHECKED 3 Sep 2026, first time. A continuous tournament with no deadline, no printed '
           'eligibility bar and no entry fee. STAKING CRYPTOCURRENCY IS OPTIONAL AND CAN BURN YOUR '
           'MONEY &mdash; the only source on this wall where taking part can cost you anything.',
      checked=True, region='global'),
 dict(name='NASA Space Apps Challenge', url='https://www.spaceappschallenge.org/2026/',
      kind='Global hackathon, annual',
      note='CHECKED 3 Sep 2026, first time. Registration open for 14&ndash;15 November 2026, all '
           'ages and backgrounds welcome, 450+ local events plus a universal online event. Ten '
           'weeks of notice, which is exactly what this wall is for.', checked=True, region='global'),
 dict(name='Hugging Face competitions', url='https://huggingface.co/competitions',
      kind='ML competitions, global',
      note='NEW SOURCE, found via ML Contests. Checked 3 Sep 2026: the &ldquo;ongoing&rdquo; list is '
           'STALE &mdash; the only open entries are RadNLP 2024 tasks with February 2025 deadlines. '
           'Nothing genuinely live.', checked=True, region='global'),
 dict(name='ThinkOnward', url='https://thinkonward.com/app/c/challenges', kind='Energy data science, global',
      note='NEW SOURCE, found via ML Contests. Checked 3 Sep 2026: Active (0), Upcoming (0), 33 '
           'completed, 4 sandbox. Nothing open. Energy and subsurface data, so a narrow fit anyway.',
      checked=True, region='global'),
 dict(name='CrunchDAO', url='https://hub.crunchdao.com/competitions', kind='Quantitative competitions, global',
      note='NEW SOURCE, found via ML Contests, which lists two CrunchDAO competitions at $100,000 '
           'and $52,000. Checked 3 Sep 2026: THE PAGES DO NOT RENDER WITHOUT AN ACCOUNT, so the '
           'structural-break bill on this wall carries an aggregator&rsquo;s figures and no '
           'deadline. Highest-value unopened source found today.', checked=True, region='global'),
 dict(name='CodaLab', url='https://codalab.lisn.upsaclay.fr/competitions/',
      kind='Academic competition hosting, global',
      note='NEW SOURCE, found via ML Contests. Checked 3 Sep 2026: hundreds of listings, but the '
           'index is dominated by past deadlines and some entries carry absurd end dates (one reads '
           '2035). Nothing can be trusted from the index alone; each competition needs its own page. '
           'A next-time job, and a large one.', checked=True, region='global'),
 dict(name='Solafune', url='https://community.solafune.com/', kind='Satellite and geospatial, Japan',
      note='NEW SOURCE, found via ML Contests. Checked 3 Sep 2026: solafune.com/competitions is a '
           '404 and the community site lists no competitions on its landing page. English '
           'interface. Nothing readable without going further in.', checked=True, region='foreign'),
 dict(name='Bitgrit', url='https://bitgrit.com/competition/', kind='Data science competitions, Japan',
      note='NEW SOURCE, found via ML Contests. Checked 3 Sep 2026: bitgrit.net 301s to bitgrit.com, '
           'and the competition page describes the platform but lists no open competitions &mdash; '
           'it sends you to a sign-in.', checked=True, region='foreign'),
 dict(name='Antigranular', url='https://www.antigranular.com/competitions',
      kind='Privacy-preserving data science, global',
      note='Re-read 10 Sep 2026 with the right instrument, and the verdict stands. The 3 Sep note '
           'said the sections render as empty placeholders; the first re-check reported &ldquo;no '
           'data&rdquo; only because it looked for __NEXT_DATA__, and this is a Next.js '
           '<b>app-router</b> page whose data lives in the RSC flight payload instead. Decoded, that '
           'payload is 37,863 bytes and contains <b>no slug, no deadline, no prize and no '
           'competition name</b> &mdash; the list really is fetched after sign-in. Differential '
           'privacy on sensitive data would suit clinical work well, so it stays on the list, but it '
           'needs an account rather than a better reader.', checked=True, region='global'),
 dict(name='Trustii', url='https://app.trustii.io', kind='Healthcare ML competitions, France',
      note='OPENED PROPERLY 10 Sep 2026, and the answer is an account. app.trustii.io serves the '
           '<b>same 1,724-byte shell for every path INCLUDING its 404s</b>, so no path probe there '
           'can mean anything &mdash; which is why this looked like a dead end. Its Angular bundle '
           'names exactly one API, api-trustii-v2.azurewebsites.net/api, and on that API '
           '<b>/datasets returns 401 authentification_required while every other route returns '
           '&ldquo;Route not found&rdquo;</b>. That is a real answer: the listing exists and is '
           'behind a login. The marketing site is a 699 KB Wix page that renders 1,807 characters of '
           'text and names no challenge. <b>Nothing further is readable without an account, and I do '
           'not create accounts.</b> It is still explicitly healthcare &mdash; if you want this seam, '
           'signing up yourself is the one step that opens it.', checked=True, region='foreign'),

 # ---------- carried from the first pass, still true
 dict(name='ICMR', url='https://www.icmr.gov.in', kind='Medical research funding, India',
      note='STS, SHINE and the NMC education research grants. Annual cycles &mdash; the reason this '
           'wall carries closed entries. The STS page the ICMR bill links to was re-checked on '
           '3 Sep 2026 and returns 200.', checked=True, region='India'),
 dict(name='Smart India Hackathon', url='https://sih.gov.in', kind='India, national',
      note='Ministry-run, needs a college SPOC to nominate you &mdash; which means it depends '
           'entirely on which college you end up at.', checked=True, region='India'),
 dict(name='Mozilla Data Collective', url='https://competitions.mozilladatacollective.com/',
      kind='Open data competitions, global',
      note='NEW SOURCE, found through DrivenData&rsquo;s listing. Runs the Lost in Transcription ASR '
           'competition at $20,000. Small, and worth watching because Mozilla&rsquo;s data work is '
           'consistently open-licensed.', checked=True, region='global'),
]
