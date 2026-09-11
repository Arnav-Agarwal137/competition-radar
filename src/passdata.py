# -*- coding: utf-8 -*-
"""Aggregates THE PASS WALL: entries, ratings, themes, sources, and the assertions.

Same job data.py does for the bill wall, and deliberately the same shape so a
future session does not have to learn two systems. Every assertion here exists
because the corresponding mistake has already happened once on this project:

  - a half-written entry reaching the page  -> required-field check
  - a duplicate id                          -> id check
  - an entry with no rating sinking to the  -> both-directions rating check
    bottom of the very orders he asked for
  - a fee that SAYS free but is filed paid  -> the free-prefix assertion
  - two entries sharing a paper             -> distinct-theme assertion

The theme assertion is new and it matters: he asked twice, on the other wall,
that every item look unlike every other. Generating the palettes is only half
the job; proving no two collide is the other half.
"""
import datetime
import passes as P
import judgement_passes as J

# Same two dates, same opposite rules as data.py - read the note there.
# READ_ON records when a human harvested these sources and must not move.
# TODAY is the countdown baseline and must move on every build; it sat at
# 2026-09-04 until 10 September, which baked a course that closed on the 8th
# as "4 days" and left it in the closing-within-the-week banner.
READ_ON = '2026-09-04'
TODAY = '2026-09-10'

ENTRIES = list(P.PASSES)
CATS = P.CATS

# ---------------------------------------------------------------- integrity

_ids = [e['id'] for e in ENTRIES]
assert len(_ids) == len(set(_ids)), 'duplicate id: %s' % (
    sorted({i for i in _ids if _ids.count(i) > 1}),)

_REQUIRED = ('id name host platform url cat domain blurb mark fmt location travel fee commit '
             'eligible apply starts starts_text deadline deadline_text precision why view '
             'conf checked tags').split()

for e in ENTRIES:
    missing = [f for f in _REQUIRED if f not in e]
    assert not missing, 'entry %s is missing %s' % (e['id'], missing)
    assert e['cat'] in CATS, 'entry %s has unknown category %r' % (e['id'], e['cat'])
    assert e['conf'] in ('verified', 'listing', 'stale'), e['id']
    assert e['fmt'] in ('remote', 'in-person', 'hybrid'), e['id']
    assert e['domain'] in ('med', 'ai', 'research', 'build', 'open'), e['id']
    assert e['precision'] in ('exact', 'listing', 'recurring', 'none'), e['id']
    for datefield in ('starts', 'deadline'):
        v = e[datefield]
        if v:
            datetime.date.fromisoformat(v)   # raises on a malformed date

# A deadline that is EARLIER than nothing and a start that is earlier than the
# deadline are both signs of the two dates having been swapped, which is the one
# error on this page that would actively mislead him.
for e in ENTRIES:
    if e['starts'] and e['deadline']:
        assert e['deadline'] <= e['starts'], (
            'entry %s: you must apply (%s) AFTER it starts (%s) - the dates look swapped'
            % (e['id'], e['deadline'], e['starts']))

# Ratings, asserted in both directions.
_rated, _have = set(J.RANK), {e['id'] for e in ENTRIES}
assert not (_have - _rated), 'entries with no rating: %s' % sorted(_have - _rated)
assert not (_rated - _have), 'ratings for entries that do not exist: %s' % sorted(_rated - _have)
for e in ENTRIES:
    p, l = J.RANK[e['id']]
    assert 1 <= p <= 5 and 1 <= l <= 5, 'rating out of range: %s' % e['id']
    e['prestige'], e['learning'] = p, l

# The free filter is decided from fee.lower().startswith(). An entry whose fee
# text SAYS there is no fee but does not START that way is silently filed as
# paid and vanishes from that filter. This bit six bills at once on the other
# wall; asserting the class rather than fixing instances is the whole lesson.
_FREE_PREFIX = ('free', 'no fee', 'none', 'no cost')
_SAYS_FREE = ('no application fee', 'no entry fee', 'no cost to enter', 'no hidden costs',
              'charges no admission fee', 'complimentary')
for e in ENTRIES:
    f = e['fee'].lower()
    if any(t in f for t in _SAYS_FREE) and not f.startswith(_FREE_PREFIX):
        raise AssertionError(
            'entry %s says it is free but would be filed as paid - start its fee field with '
            '"Free" or reword it: %r' % (e['id'], e['fee'][:80]))

# ---------------------------------------------------------------- themes
#
# Pass stocks: the paper a real ticket, certificate or membership card is printed
# on. Fourteen bases, then nudged per lap so no two entries share a paper.

_STOCKS = [
    ('#efe2c6', '#3a2c14'),   # manila
    ('#f6dfd8', '#8f1d16'),   # ticket red
    ('#dae7f2', '#123a63'),   # boarding blue
    ('#f7f1de', '#4a3b1e'),   # certificate cream
    ('#dcecdd', '#14432b'),   # security green
    ('#e8e0f0', '#3e2a5c'),   # lilac pass
    ('#f8dee6', '#7a1f42'),   # carbon-copy pink
    ('#d9ecec', '#0f4144'),   # teal card
    ('#e3d3ba', '#4a3520'),   # kraft
    ('#f1f3f1', '#1f2a24'),   # lab white
    ('#f7e6c8', '#6b3a06'),   # amber stub
    ('#dfe3e8', '#232c38'),   # slate pass
    ('#dcefe4', '#16452f'),   # mint chit
    ('#f6e3e0', '#6d2418'),   # rose vellum
]


def _hex(rgb):
    return '#%02x%02x%02x' % tuple(max(0, min(255, int(round(c)))) for c in rgb)


def _rgb(h):
    h = h.lstrip('#')
    return [int(h[i:i + 2], 16) for i in (0, 2, 4)]


def _shift(h, amount):
    """Move a colour towards black (negative) or white (positive) by a fraction."""
    r, g, b = _rgb(h)
    if amount < 0:
        f = 1 + amount
        return _hex((r * f, g * f, b * f))
    return _hex((r + (255 - r) * amount, g + (255 - g) * amount, b + (255 - b) * amount))


for i, e in enumerate(ENTRIES):
    paper, ink = _STOCKS[i % len(_STOCKS)]
    lap = i // len(_STOCKS)
    if lap:
        paper = _shift(paper, -0.045 * lap)      # each lap, slightly deeper stock
        ink = _shift(ink, 0.10 * lap)            # and slightly lighter ink
    e['theme'] = dict(paper=paper, ink=ink, rule=ink, treatment='t-' + e['cat'])

_papers = [e['theme']['paper'] for e in ENTRIES]
assert len(_papers) == len(set(_papers)), (
    'two entries share a paper: %s' % sorted({p for p in _papers if _papers.count(p) > 1}))

# ---------------------------------------------------------------- sources
#
# checked=True means a page was actually opened on 4 September 2026. Sources that
# were opened and turned out to be empty, stale or blocked are recorded as such,
# because "checked and empty" is an answer and "I could not look" is a different
# answer from "there was nothing there".

SOURCES = [
 dict(name='Common Fellowship Portal (fellowships.gov.in)', url='https://fellowships.gov.in/',
      kind='Government of India fellowships &mdash; DST, DBT and CSIR in one place',
      region='india', checked=True,
      note='ADDED 7 September 2026 by the first monthly source sweep. Live and current &mdash; the '
           'announcements panel carried items dated 25.08.2026 when it was opened. It is the single '
           'front door to fellowships from the Departments under the Ministry of Science and '
           'Technology, with an eligibility calculator and a profile that auto-fills applications, '
           'and ICMR, UGC and AICTE are stated as coming. <b>NOTHING FROM IT IS ON THIS WALL, and '
           'that is deliberate: it prints, in its own words, that it is for &ldquo;PhD and '
           'Post-Doctoral researchers&rdquo;.</b> It is recorded here so that the session that '
           'needs it &mdash; six or seven years from now &mdash; does not have to find it again. '
           'It also refuses a plain fetcher, which returns only the page heading; use a browser.'),
 dict(name='IndiaBioscience &mdash; Events', url='https://indiabioscience.org/events',
      kind='Indian life-science events, workshops, conferences', region='india', checked=True,
      note='The best single aggregator for Indian life science, and it prints registration '
           'deadlines on the listing itself, which almost nothing else does. Its own category '
           'filters (workshop / conference / seminar / webinar / meeting / competition) are close '
           'to the categories on this page. <b>It sits behind Cloudflare</b> and refuses a plain '
           'fetcher with HTTP 403; a real browser gets the &ldquo;Just a moment&hellip;&rdquo; '
           'interstitial, and working around bot detection is off limits. <b>Re-swept 10 September '
           '2026 through the one door it leaves open: /sitemap.xml answers 200 and was regenerated '
           'THAT DAY</b>, which settles the only question a 403 leaves hanging &mdash; the source is '
           'alive and updating, not abandoned. It publishes <b>79 sub-sitemaps, thirteen of them '
           'events</b>, roughly 1,300 event pages, newest first. What that sweep could NOT do is read '
           'any of them: every leaf page 403s too. So this source is <b>ENUMERATED BUT UNREAD</b> '
           '&mdash; I know what is on it and cannot open a single item, which is &ldquo;could not '
           'look&rdquo;, not &ldquo;found nothing&rdquo;. Nothing has been taken from it, because a '
           'URL slug carries no date, no fee and no eligibility and inventing those is how a '
           'competition that had closed eleven weeks earlier once reached the sister wall. '
           '<b>Leads worth your own browser, all posted since August 2026:</b> the 19th Young '
           'Investigators Meeting 2027; CuttingGardens 2026 at IIT Mandi, a global EEG conference; '
           'IndiBioCom 2026, the first Indian conference on bioinformatics; a fifteen-day certified '
           'internship on AI in bioinformatics; the 4th Winter School on Biomedical Optics; and the '
           'Ashoka Quantitative Microscopy Course 2027.'),
 dict(name='NCBS Bengaluru &mdash; Events', url='https://www.ncbs.res.in/events',
      kind='Courses, workshops, symposia and annual talks', region='bengaluru', checked=True,
      note='Fifteen dated items through to March 2027, and the richest single seam for hands-on '
           'laboratory training anywhere near him. The listing prints titles and dates and '
           '<b>nothing else</b> &mdash; no fee, no eligibility, no venue, no application deadline &mdash; '
           'so every entry taken from it is amber. <b>On the second sweep the Bangalore Microscopy Course site '
           'was opened and settled it</b>: 24 participants and 2 observers by competitive '
           'selection, applications need a CV, a write-up and a letter of recommendation from a '
           'supervisor, and <b>the 2026 selected list is already published</b> &mdash; so that '
           'entry moved from &ldquo;probably too late, my reading&rdquo; to closed, as a fact. The '
           'flow cytometry and CIFF course pages are on <code>ciff.ncbs.res.in</code>, which the '
           'browser tool is not permitted to open, so those two remain amber.'),
 dict(name='ICTS-TIFR &mdash; Upcoming programmes',
      url='https://www.icts.res.in/programs/upcoming',
      kind='Schools, workshops and discussion meetings in the physical sciences', region='bengaluru',
      checked=True,
      note='Eighteen programmes, and unusually <b>every one prints its application deadline</b>. '
           'Deadlines run three to four months ahead of the event, which is exactly the lead time '
           'this project exists to capture. <b>On the second sweep the four individual programme '
           'pages were opened, and they changed three of the four entries.</b> The listing prints '
           'no eligibility at all; the programme pages do, and it is restrictive: '
           '&ldquo;PhD students and postdoctoral researchers&rdquo;, &ldquo;researchers, postdocs, '
           'and senior graduate students&rdquo;, &ldquo;active researchers (PhD, postdoctoral and '
           'faculty levels)&rdquo;. Only <i>Modelling Water Across Scales</i> prints that '
           '&ldquo;a limited number of advanced undergraduates may be considered&rdquo;. One entry '
           'was removed outright as a result, and the Winter School stopped being described as a '
           'missed opportunity &mdash; he was never eligible for it. Accommodation is provided for '
           'outstation participants on all of them.'),
 dict(name='Science Gallery Bengaluru', url='https://bengaluru.sciencegallery.com/',
      kind='Free exhibitions, programmes, mediator and extern roles', region='bengaluru',
      checked=True,
      note='<b>The domain in his diary note, scigalleryblr.org, does not resolve at all.</b> The '
           'real one is bengaluru.sciencegallery.com. Everything is free &mdash; the site prints '
           '&ldquo;charges no admission fee. Every exhibition, every programme, every season&rdquo;. '
           'Its Open Calls page carried only closed calls on 4 September 2026, and the mediator page '
           'prints no eligibility and no application route.'),
 dict(name='IISc &mdash; Upcoming events',
      url='https://www.iisc.ac.in/news-events/events-upcoming/',
      kind='Lectures, conferences and training programmes', region='bengaluru', checked=True,
      note='Five dated items. <b>Use this URL and not iisc.ac.in/events/</b> &mdash; that second '
           'page renders perfectly, is well laid out, carries thirty-nine dated events, and every '
           'single one of them is from 2016. It is the best example on this whole project of a '
           'listing that looks alive and is not.'),
 dict(name='Science Academies&rsquo; Fellowship portal',
      url='https://webjapps.ias.ac.in/fellowship2026/index.html',
      kind='The IASc-INSA-NASI summer research fellowship', region='india', checked=True,
      note='Names <b>MCI</b> &mdash; the medical council &mdash; in its own eligibility text, which '
           'is why it is the most important annual item on this page for him. Announced around '
           'October, closes end of January. The 2026 round has gone; the 2027 round opens next month.'),
 dict(name='Google Summer of Code', url='https://summerofcode.withgoogle.com/get-started',
      kind='Paid open source contribution programme', region='global', checked=True,
      note='Eligibility prints as 18+, &ldquo;a student or an open source beginner&rdquo;, and '
           'resident of a non-embargoed country. He clears all three. Applications are in March; '
           'the 2027 dates are not published yet and no date has been invented for them here.'),
 dict(name='SPAR &mdash; Supervised Program for Alignment Research', url='https://sparai.org/',
      kind='Remote AI-safety research mentorship', region='global', checked=True,
      note='Prints, in its own words, that it does not require previous research experience and '
           'that many mentees have none. Free, remote, part-time, and explicitly open to '
           'undergraduates. Spring 2027 applications open around December.'),
 dict(name='Outreachy', url='https://www.outreachy.org/',
      kind='Paid remote open source internships', region='global', checked=True,
      note='$7,000 stipend, three months. Eligibility is self-assessed against under-representation '
           'in your own country and is deliberately left for him to judge rather than judged here. '
           'Next window around February 2027.'),
 dict(name='BlueDot Impact', url='https://bluedot.org/',
      kind='Free cohort courses on AI safety and AI governance', region='global', checked=True,
      note='Two courses taken. The two-hour Future of AI course is free and states an '
           '&ldquo;industry-recognised certificate&rdquo;; the Technical AI Safety course is '
           'pay-what-you-want and its page prints &ldquo;Apply by 6 Sep&rdquo; <b>without a year</b>.'),
 dict(name='RSNA &mdash; Discounted membership rates',
      url='https://www.rsna.org/membership/discounted-membership-rates',
      kind='International radiology society membership', region='global', checked=True,
      note='Members-in-Training is printed as <b>$0</b> and names medical students. The catch is the '
           'application route: it needs a verification form signed by a dean, so it is unusable '
           'until MBBS actually starts.'),
 dict(name='Cohere Labs Open Science Community', url='https://cohere.com/research/open-science',
      kind='Open machine-learning research community', region='global', checked=True,
      note='Free, 5,000+ members, application status shown as Open and reviewed weekly. Explicitly '
           'welcomes people with no institutional affiliation. Co-authorship is NOT promised on the '
           'page and is not claimed here.'),
 dict(name='ML Collective', url='https://mlcollective.org/',
      kind='Non-profit ML research community, reading group, free compute', region='global',
      checked=True,
      note='&ldquo;A research home for you regardless of your affiliation, employer, or '
           'background&rdquo; &mdash; the single most relevant sentence found all day. Weekly '
           'reading group, office hours, open collaborations, no application printed.'),
 dict(name='PREreview', url='https://prereview.org/',
      kind='Open preprint peer review, aimed at early-career researchers', region='global',
      checked=True,
      note='The only route on this page into peer review itself, which normally needs a doctorate. '
           'Free, permanently open, and it runs training and live-review sessions so it need not be '
           'done blind.'),
 dict(name='Zooniverse', url='https://www.zooniverse.org/projects',
      kind='Citizen science across eleven disciplines including medicine', region='global',
      checked=True,
      note='Medicine is one of its listed disciplines; live biomedical projects include Monkey '
           'Health Explorer (white blood cell types) and Etch A Cell. No deadlines. Whether '
           'volunteers are credited on papers is not printed on the projects page.'),
 dict(name='Foldit', url='https://fold.it/', kind='Protein-folding citizen science game',
      region='global', checked=True,
      note='Free, no deadline. Whether players have been credited as authors is not printed on the '
           'page that was opened, and is therefore not claimed.'),
 dict(name='Emergent Ventures (Mercatus Center)', url='https://www.mercatus.org/emergent-ventures',
      kind='Rolling micro-grants for early, ambitious projects', region='global', checked=True,
      note='Minimum age 13, applications open year-round, and a dedicated India track selected from '
           'a dropdown. The one item here with no window to miss &mdash; which makes it a thing to '
           'apply to when a project exists, not now. <b>Re-checked 10 September 2026 and it could '
           'not be read:</b> mercatus.org answers 403 to a plain fetcher, to a full browser header '
           'set, and on every published feed and sitemap path tried; a real Chrome tab timed out '
           'twice. That is the site declining automated clients &mdash; a fact about how it treats '
           'scripts, and <b>not</b> evidence that the programme has stopped. Nothing above has been '
           'changed on its account; confirm the details yourself before applying.'),
 dict(name='SWAYAM / NPTEL', url='https://swayam.gov.in/',
      kind='India&rsquo;s national online course platform, IIT and IISc taught', region='india',
      checked=True,
      note='Free to learn, paid proctored exam, and credits that transfer into a degree &mdash; '
           'which matters because he is already an IITM BS student. <b>The exam fee and the exact '
           'semester windows are not printed on the homepage</b> and onlinecourses.nptel.ac.in '
           'returned almost nothing to a fetcher and is not reachable by the browser tool here.'),
 dict(name='OpenWHO', url='https://openwho.org/channels',
      kind='World Health Organization online courses', region='global', checked=True,
      note='Reached only partially: openwho.org and /courses return 404 or an empty body to a '
           'fetcher, and /channels shows most channels as &ldquo;Public, Restricted&rdquo; with the '
           'Community First Aid Response Course as &ldquo;Public, Open&rdquo;. <b>The certificate '
           'policy could not be confirmed</b> and no claim about it is made.'),
 dict(name='MLH Fellowship', url='https://fellowship.mlh.com/',
      kind='Twelve-week remote open source programme with a stipend', region='global', checked=True,
      note='The programme page prints the shape and the stipend but <b>not the eligibility</b>, '
           'which lives on the FAQ. Recorded as unread rather than guessed.'),
 dict(name='GitHub Campus Experts', url='https://githubcampus.expert/',
      kind='Campus community leadership programme', region='global', checked=True,
      note='<b>Opened and unreadable.</b> The public site lists current experts and their events; '
           'the Apply link redirects to a GitHub OAuth sign-in, so eligibility, deadlines and '
           'benefits are all behind a login. This is &ldquo;I could not look&rdquo;, not &ldquo;I '
           'found nothing&rdquo;, and the entry says so.'),
 dict(name='Microsoft Learn Student Ambassadors', url='https://mvp.microsoft.com/en-US/studentambassadors',
      kind='Campus ambassador programme', region='global', checked=True,
      note='Same as GitHub&rsquo;s: the public pages are marketing and the terms are behind a '
           'sign-in. The Get Started page rendered only navigation and a footer.'),
 dict(name='TIFR &mdash; Summer research', url='https://www.tifr.res.in/academics/summer_program.php',
      kind='Directory of summer programmes across TIFR centres', region='india', checked=True,
      note='<b>Checked and it is not a source.</b> It is a page of links to each centre&rsquo;s own '
           'programme &mdash; no eligibility, no stipend, no deadline of its own. Each centre has to '
           'be opened separately, and that has not been done.'),


 # ---------- opened on the second sweep, 4 September 2026
 dict(name='NIDA Clinical Trials Network &mdash; Good Clinical Practice',
      url='https://gcp.nidatraining.org/',
      kind='Free Good Clinical Practice certification', region='global', checked=True,
      note='Filled the certification category that the first build had to leave empty. Twelve '
           'modules on ICH GCP principles and the US Code of Federal Regulations, '
           '&ldquo;self-paced and takes approximately six hours&rdquo;, quizzes at 80% to pass, '
           'federally funded so no fee is shown, and anyone may register. The certificate expires '
           'after three years within the CTN.'),
 dict(name='80,000 Hours &mdash; one-to-one advising', url='https://80000hours.org/speak-with-us/',
      kind='Free career advising calls', region='global', checked=True,
      note='Free, rolling, one-to-one video calls, and students are named explicitly. They select, '
           'and they reply &ldquo;within about two weeks&rdquo;. Comes with a stated worldview '
           'attached - heavily oriented to AI risk - which the card says rather than hides.'),
 dict(name='Cureus Journal of Medical Science', url='https://www.cureus.com/',
      kind='Peer-reviewed medical journal, Springer Nature backed', region='global', checked=True,
      note='Home page opened; <b>the pricing and author-guide pages return 403 and the domain is '
           'blocked to the browser tool</b>, so the fee terms are recorded as unconfirmed. The home '
           'page states an average cost of $400 and that &ldquo;nearly one-third of authors publish '
           'for free&rdquo; without saying what qualifies.'),
 dict(name='Effective Thesis', url='https://effectivethesis.org/',
      kind='Research-direction coaching for students', region='global', checked=True,
      note='<b>Checked and left off, deliberately.</b> It runs 1:1 advising and cohort programmes, '
           'but the cohorts are aimed at students &ldquo;heading into their final year&rdquo; and '
           'master&rsquo;s students, its next intakes had closed, and no price is printed anywhere. '
           'Too many unknowns to put on a wall whose whole promise is that nothing is inferred.'),
 dict(name='TRREE &mdash; research ethics e-learning', url='https://elearning.trree.org/',
      kind='Research ethics training and certification', region='global', checked=True,
      note='<b>Checked and left off.</b> Genuinely relevant - modules on research ethics, informed '
           'consent and Good Clinical Practice, with country frameworks for 17+ nations including '
           'India. But the home page prints neither the price nor what the certificate is, and the '
           'GCP entry already covers this ground with both stated. Worth opening properly next '
           'time.'),

 # ---------- named, NOT yet opened. The gap is visible on purpose.
 dict(name='JNCASR &mdash; fellowships and extension programmes',
      url='https://www.jncasr.ac.in/fandeprogrammes',
      kind='Summer research fellowships and student programmes, Bengaluru', region='bengaluru',
      checked=True,
      note='<b>The find of the second sweep, and it was on the unopened list the first time.</b> '
           'JNCASR runs eleven programmes; the one that matters is <b>SRFP</b>, whose eligibility '
           'text names MBBS outright &mdash; &ldquo;I/II/III year of MBBS/BVSc (4 years) can '
           'apply&rdquo;. Rs 10,000 a month for two months, train fare covered, in Bengaluru. Its '
           'siblings do NOT fit: POBE is &ldquo;1st year of the three-year or four-year B.Sc '
           'programme only&rdquo;, GRIP names MBBS but wants final-year students, and NE-SRF names '
           'MBBS but only for the seven North-Eastern states. Applications ran 22 Dec 2025 &ndash; '
           '31 Jan 2026, so the next window opens around late December 2026.'),
 dict(name='IISER Pune &mdash; Summer Student Programme',
      url='https://www.iiserpune.ac.in/SummerStudentProgrammes',
      kind='Summer research for external students', region='india', checked=True,
      note='<b>Another wrong address, not a dead source.</b> This was marked &ldquo;guessed URL '
           'returned 404, not opened&rdquo; through two builds. The real path is '
           '<code>/SummerStudentProgrammes</code>, and the programme&rsquo;s own portal at '
           '<code>sites.iiserpune.ac.in/~rathreya/sspc/</code> prints the eligibility and the '
           'money verbatim: 2nd to 4th year B.Sc/B.Tech/B.E or equivalent, 60% overall, a free '
           'hostel room, and no help at all with travel or the roughly Rs. 6000 a month mess '
           'bill. <b>One entry taken.</b> The 2026 round is closed; SSPC-2027 should open around '
           'February 2027.'),
 dict(name='IUSSTF &mdash; Khorana and S.N. Bose Scholars', url='https://iusstf.org/khorana-program-for-scholars',
      kind='Funded research placements in the United States for Indian undergraduates',
      region='india', checked=True,
      note='<b>It was never down. The domain was wrong.</b> This sat on the unopened list through '
           'two builds as <code>indousstf.org</code>, which resets the connection to a fetcher and '
           'to a real browser alike. The site is <b>iusstf.org</b>, and it answered first time. '
           'That is the second host-name failure on this page, after www.ijms.info - and the rule '
           'about it had already been written into the global rules that morning. <b>Khorana names '
           'MBBS in its eligibility list</b> and excludes first-year students; it pays airfare, '
           'stipend and insurance for 10-12 weeks in the United States. <b>S.N. Bose was checked '
           'and ruled out</b>: its disciplines exclude medicine and biology, it points such '
           'applicants at Khorana, and WINStep Forward says it is currently on hold.'),
 dict(name='EMBO &mdash; courses and workshops',
      url='https://www.embo.org/conferences-training/courses-workshops/',
      kind='European molecular biology courses, workshops and fellowships', region='global',
      checked=True,
      note='<b>Swept properly, and it yielded nothing he can act on &mdash; which is an answer, '
           'not a failure.</b> The 404 was a wrong path; the real page is live. Its event portal '
           'is <code>events.embo.org</code> (<code>meetings.embo.org</code> redirects there) and '
           '<b>it serves an incomplete certificate chain</b>, so every ordinary fetcher reports '
           'a certificate error and looks like a dead host. EMBO&rsquo;s own 2026 events poster '
           'lists four Indian events, two of them in Bengaluru. The nearest, the EMBO Workshop '
           'on molecular mechanisms of developmental and regenerative biology at BRIC-inStem '
           'Bangalore on 25&ndash;27 November 2026, was opened at source: <b>abstracts closed 31 '
           'July 2026 and registration closed 30 August 2026</b>, five days before this sweep. '
           'The &ldquo;India | EMBO Lecture Courses&rdquo; scheme is <b>for organisers applying '
           'for funding</b>, not for students attending, and it describes its audience as PhD '
           'students and postdocs. No 2027 participant listings are published yet. <b>Nothing '
           'added; worth re-sweeping in the new year.</b>'),
 dict(name='CITI Program &mdash; GCP for independent learners',
      url='https://about.citiprogram.org/course/good-clinical-practice-basic-ich/',
      kind='Research ethics and good clinical practice certification', region='global',
      checked=True,
      note='<b>Opened, and deliberately not used.</b> The course page is live and current &mdash; '
           'its CME designation period runs to 31 May 2027 &mdash; and anyone may register as an '
           'independent learner without an institution. But it prints '
           '<b>&ldquo;$129 per person&rdquo;</b> for the same GCP credential this wall already '
           'carries <b>free</b> from the NIDA Clinical Trials Network. Adding it would have put a '
           'roughly Rs. 11,000 version of a thing he can already get for nothing on the same '
           'page. Recorded here so no future session pays for it by mistake. The research-ethics '
           'category is no longer empty either way.'),
 dict(name='ISCB &mdash; student membership',
      url='https://www.iscb.org/membership-details/individual-membership-details',
      kind='International Society for Computational Biology', region='global', checked=True,
      note='&ldquo;Membership URL returned 404. Not chased&rdquo; &mdash; and the real one was two '
           'clicks away. It prints the four student tiers and their prices outright, so the '
           'entry taken from it is verified rather than amber. <b>One entry taken.</b> The '
           'benefits page is worth reading beside it: travel fellowships to ISCB conferences, '
           'ECCB, PSB and RECOMB are the part with real value for him. Caveat recorded on the '
           'card: the page&rsquo;s newest visible year is 2022, so the dues calculator is the '
           'authority on price, not these numbers.'),
 dict(name='International Journal of Medical Students', url='https://ijms.info/',
      kind='A journal whose authors are medical students', region='global', checked=True,
      note='<b>An entire category was missing because of four characters.</b> '
           '<code>www.ijms.info</code> refuses the connection &mdash; twice to a fetcher and once '
           'in a real browser &mdash; and the bare <code>ijms.info</code> answers instantly. '
           'Diamond Open Access: no submission fee, no processing charge, no publication fee, and '
           'at least one author must be a current medical student or a doctor within three years of '
           'graduating. Rolling submissions, no issue deadlines. <b>Check the host, not just the '
           'URL, before recording a source as dead.</b>'),
 dict(name='IISc Open Day', url='https://openday.iisc.ac.in/',
      kind='Annual campus-wide public open day', region='bengaluru', checked=True,
      note='Opened on the second sweep. Prints &ldquo;Entry to the Open Day at IISc is free&rdquo; '
           'and gives the 2026 date as Saturday 7 March, 9am&ndash;5pm &mdash; which has passed. '
           'Annual and early March, so it is carried as a returning item with no 2027 date invented '
           'for it.'),
]
