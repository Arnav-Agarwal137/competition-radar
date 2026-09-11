# -*- coding: utf-8 -*-
"""THE PASS WALL - entries for the second page.

A separate page from the bill wall, on his instruction of 4 September 2026:
*"a different web page entirely forget i said to add this to bill wall"*.

WHAT BELONGS HERE, and how it differs from a bill:
A bill is a competition - you enter it, you might win. A PASS is a way IN. Every
entry here hands you something you keep: a seat for one night, a certificate, a
cohort, a membership, a title, a byline, a mentor. The face question is not
"what do I win" but "what does this leave behind that somebody else can see".

THE RULE THAT SHAPES THE PAGE, from diary 0004:
    A bill that never expires is a bill that trains you to ignore bills.
So the objects here are NOT all the same object. Five of the categories have no
deadline at all, and they must not wear the deadline treatment.

EVERY VALUE BELOW is what a page printed on 4 September 2026, or the literal
words "Not stated". Nothing is inferred. Banned words, per the project rules:
suggests, likely, probably, commonly, appears to, would normally.

FIELDS
  starts / starts_text  the date the thing HAPPENS (a talk, a course, a school).
  deadline / deadline_text  the date you must APPLY BY, if there is one.
Those are different dates and conflating them is how a wall lies. A talk has a
start and no deadline; a fellowship has a deadline and its dates come later.
`mark` is what you walk away holding - it goes on the face, where the bill wall
puts the prize.
"""

# ---------------------------------------------------------------- categories
#
# The category sweep IS the deliverable. He said, verbatim: "i just dont know
# what other categories are there check em all". Thirteen kinds of object, each
# one genuinely different in what it costs, what it leaves, and how its date
# behaves. `dated` says whether the object has a clock on it at all.

CATS = {
 'lecture':    dict(label='Talk',           form='ticket stub',      dated=True,
                    note='Free, one evening, no credential. Its only value is that you were in the room.'),
 'workshop':   dict(label='Workshop',       form='enrolment slip',   dated=True,
                    note='Hands-on, days to weeks, usually an application and a fee. You come out able to do a thing.'),
 'school':     dict(label='School',         form='admission card',   dated=True,
                    note='Summer or winter school. A cohort you were selected into, weeks long, months of notice.'),
 'fellowship': dict(label='Fellowship',     form='sealed letter',    dated=True,
                    note='You do real research with a named guide, usually paid. The strongest thing on this page.'),
 'course':     dict(label='Course',         form='certificate',      dated=True,
                    note='Taught online, ends in a credential you can show.'),
 'conf':       dict(label='Conference',     form='delegate badge',   dated=True,
                    note='You attend, and if you submit an abstract you present. A poster is a citable thing.'),
 'member':     dict(label='Membership',     form='membership card',  dated=False,
                    note='A society lists you as a member. Often free for students and permanently open.'),
 'badge':      dict(label='Ambassadorship', form='enamel badge',     dated=True,
                    note='A title you hold for a term, with a company or foundation behind it.'),
 'community':  dict(label='Community',      form='open handbill',    dated=False,
                    note='You join and start contributing. No form, no date, no gatekeeper.'),
 'review':     dict(label='Peer review',    form='reviewer stamp',   dated=False,
                    note='You review other people&rsquo;s work under your own name. Permanently open.'),
 'citizen':    dict(label='Citizen science',form='tally sheet',      dated=False,
                    note='Real data, real projects, no credential and no deadline. Contribution, not selection.'),
 'grant':      dict(label='Grant',          form='cheque stub',      dated=False,
                    note='Money for your own idea. Rolling - you apply when you have something to say.'),
 'role':       dict(label='Role',           form='staff pass',       dated=True,
                    note='An actual position - intern, extern, mediator. A reference at the end of it.'),
 'cert':       dict(label='Certification',  form='stamped credential', dated=False,
                    note='A specific named credential the field already recognises, with an expiry date on it. Not a course certificate - a qualification.'),
 'publish':    dict(label='Publishing',     form='galley proof',     dated=False,
                    note='A byline. Somewhere that will actually print a medical student, year-round, with no cohort to be selected into.'),
 'mentor':     dict(label='Mentorship',     form='calling card',     dated=False,
                    note='The product is a person, not a course. You are matched with someone who has done it and they talk to you.'),
}

# ---------------------------------------------------------------- the passes

PASSES = []

# ============================ FELLOWSHIPS ===================================
# The heaviest category for him, and the one he is most likely to miss, because
# every one of them opens once a year and closes quietly.

PASSES.append(dict(
 id='srfp-science-academies', cat='fellowship', domain='research',
 name='Science Academies&rsquo; Summer Research Fellowship',
 host='Indian Academy of Sciences, INSA and NASI, jointly',
 platform='ias.ac.in fellowship portal',
 url='https://webjapps.ias.ac.in/fellowship2026/index.html',
 blurb='Two months of real research with an assigned guide at an Indian research institution, '
       'paid, arranged by the three national science academies together.',
 mark='Two months in a named lab, a guide who knows your work, and a report. The standard first '
      'research line on an Indian science CV.',
 fmt='in-person', location='At your assigned guide&rsquo;s institution, anywhere in India',
 travel='Round trip train fare is included. The page prints '
        '&ldquo;entitled round trip train fare and a monthly fellowship to meet their living '
        'expenses at the place of work&rdquo;. The amount is Not stated on the page.',
 fee='Free to apply. No fee is printed anywhere on the application instructions.',
 commit='Two months. The page prints &ldquo;The selected candidate should work with the assigned '
        'guide for two months any time during the calendar year&rdquo;, so it need not be summer.',
 eligible='Printed literally: &ldquo;Applications are invited from motivated students and teachers '
          'from all universities and colleges affiliated to UGC/AICTE/<b>MCI</b>/Accredited '
          'Institutions/Private Universities.&rdquo; MCI is the medical council, so medical '
          'colleges are named in the eligibility text. The index page prints no year-of-study bar.',
 apply='Online only, through any one of the three academies&rsquo; websites: ias.ac.in, '
       'insaindia.res.in or nasi.org.in. You name the subject and can name preferred guides.',
 starts='', starts_text='Two months of your choosing, within the calendar year.',
 deadline='', deadline_text='The 2026 round closed on 31 January 2026. The programme is announced '
          '&ldquo;around October&rdquo; with selections &ldquo;February&ndash;March&rdquo;, so the '
          '2027 round should open next month. The exact 2027 date is Not stated yet.',
 precision='recurring', recurring=True,
 why='This is the one thing on this page most worth putting a reminder against. It is annual, it '
     'names medical colleges in its own eligibility text, it pays, and it ends with you having done '
     'two months of supervised research before most of your MBBS cohort has done any. You cannot '
     'apply today. You can be ready the week it opens.',
 view='Do not wait for the announcement to find you. Put a reminder on 1 October 2026 and check all '
      'three academy sites. The application asks for a subject and preferred guides, which means the '
      'useful preparation is deciding what you actually want to work on and reading two or three '
      'people whose labs do it. That is a weekend of work that raises your odds enormously, and it '
      'is the sort of thing that never happens if you start it in January.',
 conf='verified', checked='2026-09-04',
 tags=['annual', 'paid', 'research', 'medicine eligible', 'india'],
))

PASSES.append(dict(
 id='jncasr-srfp', cat='fellowship', domain='med',
 name='JNCASR Summer Research Fellowship',
 host='Jawaharlal Nehru Centre for Advanced Scientific Research, Bengaluru',
 platform='jncasr.ac.in fellowships and extension programmes',
 url='https://www.jncasr.ac.in/academic/fandeprogrammes/srfp',
 blurb='Two paid months of research at JNCASR in Bengaluru, working with a faculty member. Running '
       'since 1990; the centre says around 2,500 students have been through it.',
 mark='Two months in a real lab at a national research centre, a faculty supervisor who has watched '
     'you work, and the reference that comes with that.',
 fmt='in-person', location='JNCASR, Jakkur, Bengaluru',
 travel='Bengaluru for two continuous months. Train fare is covered &mdash; the page prints second '
        'sleeper class by the shortest route.',
 fee='Free to apply.',
 commit='Printed literally: &ldquo;2 continuous months&rdquo;.',
 eligible='<b>MBBS is named explicitly, which is rare and is why this is here.</b> The Life Sciences '
          'section prints: &ldquo;I/II/III year of MBBS/BVSc (4 years) can apply&rdquo;, and the '
          'Chemical Biology section prints &ldquo;I/II/III/IV year of MBBS (5 years) can '
          'apply&rdquo;. So a first-year MBBS student qualifies from the year he starts.',
 apply='Online application through the JNCASR site during the winter window.',
 starts='', starts_text='Two continuous months, over the summer.',
 deadline='', deadline_text='SRFP-2026 ran &ldquo;from 22nd Dec. 2025 to 31st Jan. 2026&rdquo; and '
          'has closed. The 2027 window should open around late December 2026; <b>the exact date is '
          'Not stated yet</b> and none has been invented here.',
 precision='recurring', recurring=True,
 extra='Its sibling programme POBE is <b>not</b> open to you &mdash; that one prints '
       '&ldquo;1st year of the three-year or four-year B.Sc programme only&rdquo;. JNCASR also runs '
       'GRIP, which names MBBS but for final-year students, and NE-SRF, which names MBBS but only '
       'for the seven North-Eastern states. SRFP is the one that fits.',
 why='Stipend of Rs 10,000 a month, two months, at a national research centre <b>in the city your '
     'brother lives in</b>, and its eligibility text names MBBS students in their first year by '
     'name. Of everything on this wall, this is the one with the best ratio of prestige to how '
     'plausibly you get it.',
 view='<b>Put a reminder on 15 December 2026.</b> That is the single most useful sentence on this '
      'page. The window is roughly 22 December to 31 January and it will not announce itself to '
      'you. Between now and then the preparation that matters is picking two or three JNCASR '
      'faculty whose work you can actually describe, because the application asks what you want to '
      'work on. Do that in November, not in January.',
 conf='verified', checked='2026-09-04',
 tags=['bengaluru', 'annual', 'paid', 'mbbs named', 'do the reminder'],
))

PASSES.append(dict(
 id='gsoc', cat='fellowship', domain='ai',
 name='Google Summer of Code',
 host='Google Open Source', platform='summerofcode.withgoogle.com',
 url='https://summerofcode.withgoogle.com/get-started',
 blurb='A paid, remote programme where you spend a summer writing code for an established open '
       'source project with a mentor from that project.',
 mark='A shipped contribution to a real, public codebase, a named mentor, and a line every '
      'engineer recognises on sight.',
 fmt='remote', location='Entirely online, from wherever you are',
 travel='None.',
 fee='Free to apply.',
 commit='A summer. The programme offers different project sizes; the page does not print the hours.',
 eligible='Printed literally: &ldquo;Must be at least 18 years old at time of registration.&rdquo; / '
          '&ldquo;Must be a student or an open source beginner.&rdquo; / &ldquo;Must be a resident '
          'of a country not currently embargoed by the United States.&rdquo; '
          'You are 18, you are a student, and India is not embargoed &mdash; you qualify on all three.',
 apply='Pick an organisation from the published list, talk to them on their own channels first, '
       'then submit a project proposal during the contributor application window.',
 starts='', starts_text='Coding runs over the northern summer.',
 deadline='', deadline_text='The 2026 contributor window was 16&ndash;31 March. The 2027 dates are '
          'Not stated yet; the timeline page says applications are typically in March with a '
          'fifteen-day window.',
 precision='recurring', recurring=True,
 why='It is the single best-known open source programme in the world, it explicitly welcomes '
     '&ldquo;open source beginners&rdquo;, and you are exactly old enough this year. For the IIT '
     'Madras data science half of your life it is worth more than any certificate you could buy.',
 view='The application is not the hard part &mdash; the hard part is that accepted proposals almost '
      'always come from people who have already had a patch merged and talked to the maintainers. '
      'That means the useful work happens in January and February, not in March. If you want this, '
      'pick one organisation over the winter and start being useful to it. The stipend is real but '
      'the mentor is the thing you are actually buying.',
 conf='verified', checked='2026-09-04',
 tags=['annual', 'paid', 'open source', 'remote', '18+'],
))

PASSES.append(dict(
 id='spar', cat='fellowship', domain='ai',
 name='SPAR &mdash; Supervised Program for Alignment Research',
 host='SPAR', platform='sparai.org', url='https://sparai.org/',
 blurb='A part-time, fully remote research fellowship pairing people who want to do AI safety '
       'research with mentors already doing it.',
 mark='A research project done under a named mentor, and a body of work you can point at.',
 fmt='remote', location='Fully virtual. The page prints &ldquo;SPAR is fully virtual and our '
     'mentees join from all over the world.&rdquo;',
 travel='None.',
 fee='Free to take part, and unpaid. Printed literally: &ldquo;We cover approved project expenses, '
     'including compute and access to APIs and LLMs, but do not personally compensate mentors or '
     'mentees.&rdquo; It calls itself &ldquo;a volunteer research program&rdquo;.',
 commit='Part-time, across a research period of about three months.',
 eligible='Printed literally: &ldquo;The program is open to undergraduate, graduate/PhD students, '
          'and professionals of different experience levels&rdquo;, and &ldquo;We don&rsquo;t '
          'require previous research experience, and many mentees have none.&rdquo;',
 apply='An online mentee application in each cohort&rsquo;s window, choosing projects to apply to.',
 starts='2026-09-14', starts_text='The Fall 2026 research period runs 14 September 2026 &ndash; 14 December 2026.',
 deadline='', deadline_text='Fall 2026 applications ran 28 July &ndash; 18 August and decisions land '
          '7 September &mdash; that window has closed. The page prints that Spring 2027 applications '
          '&ldquo;open around December&rdquo;. The exact date is Not stated.',
 precision='recurring', recurring=True,
 why='It says in its own words that it does not require previous research experience and that many '
     'of its mentees have none. That sentence is rarer than it sounds, and it is aimed straight at '
     'where you are: interested, capable, and with nothing on paper yet.',
 view='This is the most winnable serious research mentorship on this page, and it costs you nothing '
      'but hours. Unpaid is a real cost &mdash; but you are not choosing between this and a salary, '
      'you are choosing between this and reading about AI on your own. Set a reminder for the start '
      'of December. Between now and then, the useful thing is to be able to say what you actually '
      'want to work on.',
 conf='verified', checked='2026-09-04',
 tags=['remote', 'mentored', 'unpaid', 'ai safety', 'undergraduates'],
))

PASSES.append(dict(
 id='outreachy', cat='fellowship', domain='ai',
 name='Outreachy', host='Software Freedom Conservancy', platform='outreachy.org',
 url='https://www.outreachy.org/',
 blurb='Paid, remote, three-month internships in open source, aimed at people who face '
       'under-representation in tech in their own country.',
 mark='A paid internship, a mentor, public contributions, and an alumni network that hires.',
 fmt='remote', location='Remote, worldwide',
 travel='None.',
 fee='Free to apply.',
 commit='Three months, full time during the internship.',
 eligible='Printed literally: &ldquo;Anyone who faces under-representation, systemic bias or '
          'discrimination in the technology industry of their country is invited to apply&rdquo;, '
          'and there is &ldquo;no list of groups that are eligible or ineligible for Outreachy&rdquo;. '
          '<b>This is self-assessed and I am not going to assess it for you</b> &mdash; read their '
          'eligibility page yourself and answer it honestly.',
 apply='An initial application, then a contribution period with a mentoring organisation, then a '
       'final application.',
 starts='', starts_text='The December 2026 internship runs early December 2026 to early March 2027.',
 deadline='', deadline_text='December 2026 applications ran &ldquo;early August to mid August&rdquo; '
          '&mdash; closed. The May 2026 round closed 13 February 2026, so the next window is around '
          'February 2027. The exact date is Not stated.',
 precision='recurring', recurring=True,
 why='$7,000 for three months of remote open source work with a mentor, and it is one of the very '
     'few programmes of its kind that takes complete beginners seriously.',
 view='The stipend is printed as $7,000 USD total, which is real money. The eligibility question is '
      'yours to answer and I have deliberately not answered it for you. If it does apply to you, the '
      'contribution period is the whole game &mdash; people are selected on what they actually did '
      'during it, not on the application form.',
 conf='verified', checked='2026-09-04',
 tags=['paid', 'remote', 'open source', 'annual'],
))

PASSES.append(dict(
 id='mlh-fellowship', cat='fellowship', domain='build',
 name='MLH Fellowship', host='Major League Hacking', platform='fellowship.mlh.com',
 url='https://fellowship.mlh.com/',
 blurb='A twelve-week remote programme, described on its own page as an internship alternative, '
       'building open source software in a small pod with engineers from established companies.',
 mark='Twelve weeks of reviewed, shipped code and a pod of peers. An internship-shaped thing on '
      'your record without an internship.',
 fmt='remote', location='Fully remote',
 travel='None.',
 fee='Free to apply. Paid: the page prints &ldquo;We offer fellows an educational stipend to help '
     'offset expenses while they participate in the program.&rdquo; The amount is Not stated on the page.',
 commit='Twelve weeks.',
 eligible='Not stated on the page I opened. Age, student status and country rules are held on their '
          'FAQ and application pages, which I did not open. <b>Check before counting on it.</b>',
 apply='An online application. The page says &ldquo;Apply today to be considered for our upcoming '
       'start dates&rdquo; without printing those dates.',
 starts='', starts_text='Rolling batches. Specific start dates are Not stated on the page.',
 deadline='', deadline_text='No deadline is printed. Applications are described as open for upcoming '
          'start dates.',
 precision='none',
 why='It is the closest thing to a software internship that does not require you to already have '
     'had a software internship, and it is remote, which matters when you are about to be tied to a '
     'medical college timetable.',
 view='I could not read the eligibility, and I am not going to guess it &mdash; that is exactly the '
      'kind of gap that wastes a week. Ten minutes on their FAQ settles whether this is even open to '
      'you. Do that before you spend any time on the application.',
 conf='listing', checked='2026-09-04',
 tags=['remote', 'stipend', 'open source', 'terms unread'],
))

PASSES.append(dict(
 id='icts-ltvsp', cat='fellowship', domain='research',
 name='ICTS Long Term Visiting Students Programme',
 host='International Centre for Theoretical Sciences, TIFR', platform='icts.res.in',
 url='https://www.icts.res.in/opportunities/academic/ltvsp/2026',
 blurb='One or two full semesters at ICTS Bengaluru working on a research project with an ICTS '
       'faculty member, with a stipend and a room.',
 mark='A semester or a year of research at a TIFR centre, and a faculty member who can write about '
      'you from having watched you work.',
 fmt='in-person', location='ICTS-TIFR campus, Hesaraghatta, Bengaluru',
 travel='You live there. Accommodation is provided.',
 fee='Free to apply. Selected candidates receive stipends and accommodation; amounts Not stated on '
     'the page.',
 commit='One or two semesters &mdash; this is a full-time commitment, not a side project.',
 eligible='Printed literally: &ldquo;Master&rsquo;s/ Integrated Master&rsquo;s/ Bachelor&rsquo;s '
          'students of science, mathematics and engineering, who are <b>entering the final year, in '
          'their final year or have recently completed their program</b>.&rdquo; '
          'You are at the start of your degrees, not the end, so this is a future item, not a now item.',
 apply='Online, with a CV, academic records and at least two referees. Referees have their own later '
       'deadline.',
 starts='', starts_text='Typically begins in August, and the page says the start is flexible.',
 deadline='', deadline_text='The 2026 round closed 15 January 2026, with referee letters due '
          '30 January and decisions in mid-April. The 2027 dates are Not stated yet.',
 precision='recurring', recurring=True,
 why='It is on this wall for the same reason ICMR-STS is on the other one: it comes round every '
     'year, and a page that only showed what is open today would never tell you it exists. By the '
     'time you are eligible you will have needed two years of notice.',
 view='You are not eligible yet and I am not going to pretend otherwise &mdash; the eligibility text '
      'says final year or recently completed. Keep it on the wall as a thing you are walking '
      'towards. The part worth acting on now is that ICTS is twenty minutes from where your brother '
      'lives and runs public programmes you can simply attend.',
 conf='verified', checked='2026-09-04',
 tags=['annual', 'stipend', 'bengaluru', 'not yet eligible'],
))

# ============================ SCHOOLS =======================================

PASSES.append(dict(
 id='icts-living-matter', cat='school', domain='research',
 name='Multiscale flows and self-organisation in living matter',
 host='ICTS-TIFR', platform='icts.res.in discussion meeting page',
 url='https://www.icts.res.in/discussion-meeting/mfso',
 blurb='A discussion meeting on the physics of living material &mdash; how flows and structure '
       'organise themselves inside tissue and cells.',
 mark='A week inside a research meeting, in a room with the people who write the papers.',
 fmt='in-person', location='Madhava Lecture Hall, ICTS Bengaluru',
 travel='Bengaluru for six days. Printed on the page: &ldquo;Accommodation will be provided for '
        'outstation participants at our on campus guest house.&rdquo;',
 fee='Not stated on the programme page.',
 commit='Six days, 1&ndash;6 March 2027.',
 eligible='Printed literally on the programme page: &ldquo;The school is primarily meant for '
          '<b>researchers, postdocs, and senior graduate students</b> working broadly in active '
          'matter and biological fluid mechanics.&rdquo; <b>That is not you, and the page says so '
          'plainly.</b>',
 apply='Through the programme&rsquo;s own ICTS page, before the deadline.',
 starts='2027-03-01', starts_text='1&ndash;6 March 2027',
 deadline='2027-02-15', deadline_text='15 February 2027, printed on the programme page',
 precision='exact',
 why='It is the closest ICTS programme to medicine &mdash; living matter, tissue, '
     'self-organisation &mdash; and it is fifteen minutes from where your brother lives.',
 view='<b>You are not eligible and I am not going to soften that.</b> I opened the page and it '
      'names researchers, postdocs and senior graduate students. It stays on the wall for one '
      'reason: it shows you what the ceiling of this building looks like, and it is a subject you '
      'could genuinely be applying to in six or seven years. Read the programme description for '
      'the vocabulary, not the application form.',
 conf='verified', checked='2026-09-04',
 tags=['bengaluru', 'biophysics', 'researchers only', 'not eligible yet'], stretch=True,
))

PASSES.append(dict(
 id='icts-winter-biophysics', cat='school', domain='research',
 name='ICTS Winter School on Biological Physics',
 host='ICTS-TIFR', platform='icts.res.in programme page',
 url='https://www.icts.res.in/program/wsbp',
 blurb='A twelve-day winter school on biological physics, over the turn of the year, at ICTS '
       'Bengaluru.',
 mark='A named winter school on your record, and twelve days of taught material you cannot get '
      'from a textbook.',
 fmt='in-person', location='Madhava Lecture Hall, ICTS Bengaluru',
 travel='Bengaluru, residential across the new year. The page prints that accommodation is provided '
        'for outstation participants, and that &ldquo;There may be limited travel support for '
        'participants from India.&rdquo;',
 fee='Not stated on the programme page.',
 commit='Twelve days, 21 December 2026 &ndash; 1 January 2027.',
 eligible='Printed literally: <b>&ldquo;PhD students and postdoctoral researchers&rdquo;</b> with '
          'backgrounds in physics, mathematics or engineering. It adds that applicants need '
          '&ldquo;a demonstrated interest in, but not necessarily any formal exposure to, '
          'biology&rdquo;. <b>Undergraduates are not named.</b>',
 apply='Through the programme&rsquo;s ICTS page.',
 starts='2026-12-21', starts_text='21 December 2026 &ndash; 1 January 2027',
 deadline='2026-08-31', deadline_text='31 August 2026 &mdash; four days before this wall was built. '
          'It is on the wall precisely because it is shut.',
 precision='exact', recurring=True,
 why='It is the ICTS programme nearest your subject, and it teaches the physics under the biology. '
     'It is here as a marker of a route, not as a thing you lost.',
 view='<b>I got this one wrong on the first build and am correcting it.</b> I wrote that its 31 '
      'August closing was &ldquo;the Gujarat wound happening again&rdquo;. It was not. When I opened '
      'the page itself, the eligibility reads <i>PhD students and postdoctoral researchers</i> '
      '&mdash; you could not have applied whether you had known about it or not. That is a real '
      'difference and you should not carry a regret you were never owed. What stays true is the '
      'mechanics: ICTS deadlines run three to four months ahead of the event, so their listing is '
      'worth a look every couple of months, permanently.',
 conf='verified', checked='2026-09-04',
 tags=['bengaluru', 'biophysics', 'phd level', 'annual', 'i was wrong'],
))

# REMOVED 4 Sep 2026, second pass: "Theory of Tidal Deformation" (ICTS, 23-27 Nov
# 2026). On the first build its eligibility was "Not stated on the listing" and it
# was kept under the include-the-borderline rule. Opening its own page settled it:
# "The meeting is aimed at active researchers (PhD, postdoctoral and faculty
# levels)" - gravitational-wave physics, for researchers, in a field with no
# connection to either of his degrees. That is not borderline any more, it is
# plainly irrelevant, and the rules say only the plainly irrelevant is left off.
# `icts-living-matter` already does the job of showing what ICTS is.

PASSES.append(dict(
 id='icts-water', cat='school', domain='research',
 name='Modelling Water Across Scales',
 host='ICTS-TIFR', platform='icts.res.in programme page',
 url='https://www.icts.res.in/program/mwas',
 blurb='A two-week programme on modelling water from the molecular scale upward &mdash; the physics '
       'and chemistry underneath every biological process you will be taught.',
 mark='Two weeks of a taught research programme at a TIFR centre, and the only ICTS door on this '
      'wall that is open to an undergraduate at all.',
 fmt='in-person', location='Ramanujan Lecture Hall, ICTS Bengaluru',
 travel='Bengaluru for twelve days. Printed on the page: &ldquo;Accommodation will be provided for '
        'outstation participants at our on-campus guest house.&rdquo;',
 fee='Not stated on the programme page.',
 commit='Twelve days, 15&ndash;26 March 2027.',
 eligible='Printed literally: &ldquo;The program is primarily intended for graduate students, '
          'postdoctoral researchers, and early-career faculty&rdquo; &mdash; <b>and then, crucially, '
          'that &ldquo;a limited number of advanced undergraduates may be considered&rdquo;</b>, '
          'with expected background in statistical mechanics, quantum mechanics and computational '
          'methods. That is a narrow door, but it is a real one, and it is the only one of the four '
          'ICTS entries here that has it.',
 apply='Through the programme&rsquo;s ICTS page, before 25 November 2026.',
 starts='2027-03-15', starts_text='15&ndash;26 March 2027',
 deadline='2026-11-25', deadline_text='25 November 2026, printed on the programme page',
 precision='exact',
 why='<b>It is the one ICTS programme on this wall you could actually apply to.</b> I opened all '
     'four pages: the other three name researchers, postdocs and PhD students and stop there. This '
     'one says advanced undergraduates may be considered. Water across scales is also genuinely '
     'upstream of biochemistry, so it is not a stretch subject-wise, only level-wise.',
 view='Worth taking seriously precisely because the door exists. Be clear-eyed: it wants statistical '
      'mechanics, quantum mechanics and computational methods, and you have none of those yet. You '
      'have <b>eleven weeks</b> until the deadline, which is enough to read one review on water '
      'structure and decide honestly whether you would follow a word of it. If the answer is no, '
      'that is a useful no &mdash; and the programme runs again.',
 conf='verified', checked='2026-09-04',
 tags=['bengaluru', 'physical chemistry', 'undergraduates considered', 'the open ICTS door'],
 stretch=True,
))

# ============================ WORKSHOPS =====================================

PASSES.append(dict(
 id='embo-indiabio-oct', cat='course', domain='research',
 name='EMBO&ndash;IndiaBioscience Online Courses 2026',
 host='IndiaBioscience and EMBO', platform='indiabioscience.org/events',
 url='https://indiabioscience.org/events/embo-indiabioscience-online-courses-2026',
 blurb='A series of four curated courses for the Indian life-science community. <b>The October one '
       'is &ldquo;Starting Your Own Lab&rdquo;</b> &mdash; three afternoons on how a new principal '
       'investigator sets up a laboratory, allocates resources, hires and builds a team culture.',
 mark='EMBO&rsquo;s name against a course you completed. Whether a certificate is issued is Not '
      'stated on the event page.',
 fmt='remote', location='Online',
 travel='None.',
 fee='Not stated on the event page.',
 commit='Three afternoons, 28&ndash;30 October 2026. Day 3 runs 12:30&ndash;16:30 IST.',
 eligible='<b>Printed on the event page: the course is &ldquo;targeted at junior group leaders&rdquo;.</b> '
          'Its own description opens &ldquo;Having navigated a PhD and a postdoc, junior group '
          'leaders face a new and exciting challenge: setting up their own laboratory and leading a '
          'team.&rdquo; <b>That is not you and will not be for a decade.</b>',
 apply='An application form run jointly by EMBO and IndiaBioscience, linked from the event page as '
       '&ldquo;Apply Online&rdquo;.',
 starts='2026-10-28', starts_text='28&ndash;30 October 2026',
 deadline='2026-09-08', deadline_text='8 September 2026, printed on the event page as '
          '&ldquo;Registrations/applications deadline 08 September&rdquo;. Re-read at source on '
          '7 September 2026 and still open.',
 precision='exact',
 why='It stays on the wall <b>as a correction, not as a recommendation</b>. It was rated highly here '
     'on 4 September on the strength of a listing that printed a deadline and nothing else &mdash; '
     'no eligibility, no description. Opening the event page answered both, and the answer is that '
     'this course is for people running their own laboratories.',
 view='<b>Do not apply, and do not feel you missed it.</b> This is the one thing on either wall that '
      'was recommended to you without anybody having read what it was, and the deadline landing '
      'tomorrow is exactly how that kind of mistake gets acted on. The lesson is worth more than the '
      'course: <b>a listing that prints a deadline and nothing else is a listing, not a source</b>, '
      'and this wall marks those amber for a reason. EMBO does run things you could take &mdash; '
      'the series has four courses and this is only the October one &mdash; so watch the same page '
      'for the fellowship-writing and scientific-writing courses instead.',
 conf='verified', checked='2026-09-07',
 tags=['online', 'embo', 'not for you', 'group leaders only', 'corrected'],
))

PASSES.append(dict(
 id='blr-microscopy-16', cat='workshop', domain='research',
 name='16th Bangalore Microscopy Course',
 host='NCBS Bangalore', platform='ncbs.res.in/events',
 url='https://www.ncbs.res.in/BangaloreMicroscopyCourse/2026/home',
 blurb='An eight-day hands-on microscopy course at NCBS &mdash; the sixteenth time it has run, which '
       'tells you it is an institution rather than an experiment.',
 mark='Hands-on time on real microscopes at NCBS, and a course that microscopy people recognise.',
 fmt='in-person', location='NCBS, Bellary Road, Bengaluru',
 travel='Bengaluru, eight days.',
 fee='Not stated on the course site.',
 commit='Eight days, 20&ndash;27 September 2026.',
 eligible='No formal eligibility rule is printed. What the course site does print: '
          '&ldquo;24 participants and 2 observers will be selected through a competitive selection '
          'process&rdquo;, and &ldquo;International applications are entertained from across the '
          'globe&rdquo;. <b>The published list of those selected for 2026 is entirely people at '
          'research institutions</b> &mdash; IISc, TIFR, IISER Bhopal, ACTREC &mdash; which is a '
          'fact about this year&rsquo;s intake, not a stated rule.',
 apply='By application with a CV, a short write-up on how the course would help your research, and '
       '&ldquo;at least on[e] letter of recommendation (preferably from your supervisor)&rdquo;.',
 starts='2026-09-20', starts_text='20&ndash;27 September 2026',
 deadline='', deadline_text='No deadline date is printed, because it has passed: '
          '<b>the course site has already published its list of selected applicants for 2026.</b> '
          'Applications are closed.',
 # precision='recurring', NOT 'none'. With 'none' this card ran its clock off
 # the COURSE START date instead of an application deadline, and stamped
 # itself "THIS MONTH - in 16 days" for a course whose applications have
 # demonstrably closed. Two true fields, one false impression. An entry that
 # is shut must never wear an open-looking stamp, whichever date it carries.
 precision='recurring', recurring=True,
 why='Sixteen editions in, at NCBS, in the city you are visiting, and it takes applications from '
     'anywhere in the world. Twenty-six places a year for hands-on time on real microscopes.',
 view='<b>Closed &mdash; and this time that is a fact, not my guess: the selected applicants for '
      '2026 are published on the site.</b> Two things to take from it. It needs a letter of '
      'recommendation from a supervisor, which means it is not really available to you until you '
      'have one. And it runs annually with applications closing months ahead, so the useful action '
      'is a reminder around March 2027 to watch for the 17th course&rsquo;s call.',
 conf='verified', checked='2026-09-04',
 tags=['bengaluru', 'ncbs', 'hands-on', 'annual', 'closed for 2026', 'needs a supervisor'],
))

PASSES.append(dict(
 id='ncbs-flow-cytometry', cat='workshop', domain='med',
 name='BD&ndash;NCBS Hands-on Basic Flow Cytometry Course',
 host='BD&ndash;NCBS Centre of Excellence', platform='ncbs.res.in/events',
 url='https://www.ncbs.res.in/research-facilities/ciff-course',
 blurb='Three days of hands-on basic flow cytometry at NCBS, run with BD, whose machines are the '
       'ones actually sitting in hospital labs.',
 mark='A hands-on flow cytometry course &mdash; a technique you will meet again in haematology and '
      'immunology, taught on the equipment the field uses.',
 fmt='in-person', location='NCBS, Bengaluru',
 travel='Bengaluru, three days.',
 fee='Not stated on the NCBS events listing.',
 commit='Three days, 13&ndash;15 October 2026.',
 eligible='Not stated on the NCBS events listing.',
 apply='Through the CIFF course page linked from the NCBS events listing.',
 starts='2026-10-13', starts_text='13&ndash;15 October 2026',
 deadline='', deadline_text='No application deadline is printed on the listing. Open the CIFF course '
          'page for the real one.',
 precision='none',
 why='Flow cytometry is one of the few lab techniques that runs straight through immunology, '
     'haematology and oncology &mdash; the parts of medicine you will meet whether you go looking '
     'for them or not. Three days is a small price for being the person in the room who has actually '
     'operated one.',
 view='This is the most directly medical hands-on course on the wall and it is six weeks away, which '
      'means the application may still be open. That makes it worth a click today rather than a '
      'bookmark. The listing prints nothing about fees or eligibility, so go and find out &mdash; '
      'and if it is open only to postgraduates, ask anyway, because these courses often keep a '
      'couple of places for keen undergraduates.',
 conf='listing', checked='2026-09-04',
 tags=['bengaluru', 'ncbs', 'immunology', 'hands-on', 'medicine'],
))

PASSES.append(dict(
 id='ncbs-ciff-microscopy', cat='workshop', domain='research',
 name='CIFF Microscopy Course',
 host='Central Imaging and Flow Facility, NCBS', platform='ncbs.res.in/events',
 url='https://www.ncbs.res.in/research-facilities/ciff-course',
 blurb='A three-day microscopy course run by the NCBS imaging facility itself.',
 mark='Hands-on imaging training at an NCBS core facility.',
 fmt='in-person', location='NCBS, Bengaluru',
 travel='Bengaluru, three days.',
 fee='Not stated on the NCBS events listing.',
 commit='Three days, 3&ndash;5 November 2026.',
 eligible='Not stated on the NCBS events listing.',
 apply='Through the CIFF course page.',
 starts='2026-11-03', starts_text='3&ndash;5 November 2026',
 deadline='', deadline_text='No application deadline is printed on the listing.',
 precision='none',
 why='The smaller, more frequent sibling of the big Bangalore Microscopy Course, and therefore the '
     'more realistic one to actually get into.',
 view='Two months out, three days long, and run by the facility rather than as a flagship course &mdash; '
      'which usually means less competition. If you want one imaging course this year, this is the '
      'more gettable of the two on this wall.',
 conf='listing', checked='2026-09-04',
 tags=['bengaluru', 'ncbs', 'imaging', 'hands-on'],
))

PASSES.append(dict(
 id='zebrafish-sathyabama', cat='workshop', domain='med',
 name='Zebrafish Animal Model in Biomedical Research',
 host='Sathyabama Institute of Science and Technology', platform='indiabioscience.org/events',
 url='https://indiabioscience.org/events',
 blurb='A four-day workshop on using zebrafish as a model organism &mdash; in vivo and molecular '
       'approaches &mdash; in Chennai.',
 mark='A hands-on animal-model workshop, which is the sort of thing that is genuinely hard to get '
      'as an undergraduate.',
 fmt='in-person', location='Chennai, Tamil Nadu',
 travel='Chennai, four days.',
 fee='Not stated on the IndiaBioscience listing.',
 commit='Four days, 23&ndash;26 September 2026.',
 eligible='Not stated on the IndiaBioscience listing.',
 apply='Registration through the host institute; the listing prints only the deadline.',
 starts='2026-09-23', starts_text='23&ndash;26 September 2026',
 deadline='2026-09-20', deadline_text='20 September 2026, printed on the IndiaBioscience listing as '
          '&ldquo;Registration deadline 20 September&rdquo;',
 precision='listing',
 why='Model organisms are how biomedical research is actually done, and almost nobody gets to touch '
     'one before postgraduate work. Sixteen days to decide.',
 view='Chennai is a real cost in time and money and you are about to move for MBBS, so weigh it '
      'honestly. But note what it is: a lab technique workshop open to outsiders, with a printed '
      'deadline, three weeks out. If the fee is modest and the timing works, this is exactly the '
      'sort of thing that later turns into a project.',
 conf='listing', checked='2026-09-04',
 tags=['chennai', 'wet lab', 'model organism', 'closing'],
))

PASSES.append(dict(
 id='invitro-cancer-sathyabama', cat='workshop', domain='med',
 name='In Vitro Cancer Cell Culture Techniques',
 host='Sathyabama Institute of Science and Technology', platform='indiabioscience.org/events',
 url='https://indiabioscience.org/events',
 blurb='A two-day hands-on workshop on culturing cancer cells in vitro.',
 mark='Cell culture at the bench &mdash; the entry skill for almost all wet-lab cancer research.',
 fmt='in-person', location='Chennai, Tamil Nadu',
 travel='Chennai, two days.',
 fee='Not stated on the IndiaBioscience listing.',
 commit='Two days, 17&ndash;18 September 2026.',
 eligible='Not stated on the IndiaBioscience listing.',
 apply='Registration through the host institute.',
 starts='2026-09-17', starts_text='17&ndash;18 September 2026',
 deadline='', deadline_text='No registration deadline is printed on the listing for this one, unlike '
          'the zebrafish workshop from the same institute.',
 precision='none',
 why='Two days, one skill, and that skill is the door into cancer biology labs.',
 view='Shorter and cheaper than the zebrafish workshop from the same place, and the technique is '
      'more broadly useful. If you were going to make one trip to Chennai, and the dates work, this '
      'is the better value of the two &mdash; though you could ask whether they will take you for both.',
 conf='listing', checked='2026-09-04',
 tags=['chennai', 'wet lab', 'oncology', 'hands-on'],
))

PASSES.append(dict(
 id='ncbs-collab-projects', cat='workshop', domain='research',
 name='Managing Large Collaborative Research Projects',
 host='NCBS Bangalore', platform='ncbs.res.in/events',
 url='https://www.ncbs.res.in/events/workshop-lcpm2026',
 blurb='A five-day workshop on how large, multi-institution research projects are actually run &mdash; '
       'the second time it has been held.',
 mark='Training in research project management, which is a real and rare thing to have.',
 fmt='in-person', location='NCBS, Bengaluru',
 travel='Bengaluru, five days.',
 fee='Not stated on the NCBS events listing.',
 commit='Five days, 12&ndash;16 October 2026.',
 eligible='Not stated on the NCBS events listing.',
 apply='Through the workshop page linked from the NCBS events listing.',
 starts='2026-10-12', starts_text='12&ndash;16 October 2026',
 deadline='', deadline_text='No application deadline is printed on the listing.',
 precision='none',
 why='Almost nobody is taught how research is organised, only how it is done. That gap is where a '
     'lot of good projects die.',
 view='Probably aimed above you &mdash; people who manage collaborations tend to be postdocs and PIs '
      '&mdash; and I have flagged it as a stretch rather than pretend otherwise. Worth one look at '
      'the page to see whether they take observers.',
 conf='listing', checked='2026-09-04',
 tags=['bengaluru', 'ncbs', 'research skills'], stretch=True,
))

# ============================ COURSES =======================================

PASSES.append(dict(
 id='bluedot-future-of-ai', cat='course', domain='ai',
 name='Future of AI', host='BlueDot Impact', platform='bluedot.org',
 url='https://bluedot.org/courses/future-of-ai',
 blurb='A short, self-paced online course on where AI is going and what it means, aimed at people '
       'with no technical background at all.',
 mark='Printed literally: an &ldquo;Industry-recognised certificate upon completion showing '
      'you&rsquo;re informed about AI&rsquo;s future&rdquo;.',
 fmt='remote', location='Online, self-paced',
 travel='None.',
 fee='Free. Printed literally: &ldquo;Completely free. No hidden costs.&rdquo;',
 commit='Printed literally: &ldquo;About 2 hours total&rdquo;. Can be done in one sitting.',
 eligible='Printed literally: &ldquo;No prerequisites. No technical knowledge required.&rdquo;',
 apply='No application and no cohort. You start it.',
 starts='', starts_text='Start whenever you like &mdash; there is no cohort to wait for.',
 deadline='', deadline_text='No deadline. Permanently open.',
 precision='none',
 why='Two hours, free, a certificate at the end, no application, no waiting. There is no other item '
     'on this page with a cost-to-credibility ratio anywhere near this.',
 view='Do this one. Today, if you want. It is the single lowest-friction thing on the wall: two '
      'hours, no gatekeeper, and it ends with something you can point at. It will not make you an AI '
      'researcher and it does not pretend to &mdash; but it is the honest first rung, and finishing '
      'it also makes the harder BlueDot course legible to you.',
 conf='verified', checked='2026-09-04',
 tags=['free', 'online', 'certificate', 'no deadline', 'today'],
))

PASSES.append(dict(
 id='bluedot-agi-strategy', cat='course', domain='ai',
 name='AGI Strategy', host='BlueDot Impact', platform='bluedot.org',
 url='https://bluedot.org/courses/agi-strategy',
 blurb='Twenty-five hours, in a cohort of about eight with an AI safety expert facilitating, on what '
       'is actually happening with AI development, what the good and bad outcomes could be, and what '
       'could be done to steer it. BlueDot&rsquo;s own stated entry point to the whole field.',
 mark='<b>A digital certificate.</b> Printed literally: &ldquo;Participants who complete the course '
      'receive a digital certificate they can share on LinkedIn or with employers.&rdquo; Plus the '
      'cohort, and an alumni network the page says now works at Anthropic, DeepMind and UK AISI.',
 fmt='remote', location='Online, cohort-based, Zoom discussions',
 travel='None. Printed on the page: &ldquo;We run discussions across a wide range of timezones.&rdquo;',
 fee='Free, pay-what-you-want. The FAQ asks &ldquo;Is it really free?&rdquo; and answers, in full, '
     '&ldquo;Yes.&rdquo;',
 commit='Printed literally: &ldquo;Intensive (~5 days at ~5h/day) or part-time (~5 weeks at '
        '~5h/week). Same content, different pace.&rdquo; Each unit is 3 hours of reading and writing '
        'plus a 2-hour discussion with about eight peers.',
 eligible='<b>Printed literally, and it is the reason this is on your wall: &ldquo;We don&rsquo;t '
          'care about your CV. We care about what you&rsquo;ll do next.&rdquo;</b> The page names '
          'three audiences &mdash; domain experts redirecting their skills, people heading into '
          'safety or governance roles, and &ldquo;newcomers who are serious about making big '
          'moves&rdquo; &mdash; then adds &ldquo;Not sure you fit? Apply anyway&rdquo;, noting that '
          'recent cohorts included &ldquo;teachers, lawyers, engineers, and community organisers&rdquo;.',
 apply='An application form, then you are placed in a cohort that fits your timezone.',
 starts='2026-09-21', starts_text='Next intensive runs <b>21&ndash;25 September 2026</b>. Later '
        'cohorts: intensives 12&ndash;16 October and 26&ndash;30 October; part-time 12 October to '
        '15 November, and 16 November to 20 December.',
 deadline='2026-09-13', deadline_text='<b>Applications close 13 September 2026 at 23:59 UTC</b> for '
          'the 21&ndash;25 September intensive, printed on the course page&rsquo;s own schedule. If '
          'that week is impossible the next gates are 4 October and 18 October &mdash; <b>this one '
          'does not have to be caught first time.</b>',
 precision='exact',
 why='<b>This is the answer to the thing you told me to remember &mdash; that you have no LinkedIn, '
     'no prior achievements and nothing to put on an application that asks for them.</b> BlueDot '
     'prints on the page that they do not care about your CV. Free, remote, ends in a certificate, '
     'and it is the stated prerequisite for the Technical AI Safety course already on this wall.',
 view='<b>Of everything on either wall, this is the one I would have you do first.</b> Not because '
      'it is the most prestigious &mdash; it is not &mdash; but because it is the only thing here '
      'that hands somebody with an empty record a real, dated, named credential for nothing, and '
      'says in writing that the empty record is not a problem. Five days at five hours is a hard '
      'week; the part-time option exists for exactly that and starts in October. Pick the pace '
      'honestly, then apply. And if you miss the 13th, take the 4 October gate &mdash; missing a '
      'rolling deadline costs three weeks, not the opportunity.',
 conf='verified', checked='2026-09-07',
 tags=['free', 'certificate', 'no cv needed', 'start here', 'ai safety'],
))

PASSES.append(dict(
 id='bluedot-technical-ai-safety', cat='course', domain='ai',
 name='Technical AI Safety', host='BlueDot Impact', platform='bluedot.org',
 url='https://bluedot.org/courses/technical-ai-safety',
 blurb='A cohort-based course surveying the open problems in AI alignment, interpretability, '
       'evaluations and control &mdash; run either as an intensive week or part-time over six weeks.',
 mark='A cohort course in a field with very few formal entry routes, and the people in your cohort.',
 fmt='remote', location='Online, cohort-based',
 travel='None.',
 fee='Free, on a pay-what-you-want basis. Printed literally: &ldquo;This course is freely '
     'available and operates on a &lsquo;pay-what-you-want&rsquo; model.&rdquo;',
 commit='Printed literally: &ldquo;Intensive (~6 days at ~5h/day) or part-time (~6 weeks at '
        '~5h/week)&rdquo;.',
 eligible='Aimed at researchers with ML or CS backgrounds, experienced engineers, and '
          '&ldquo;high-potential early-career professionals&rdquo;. The page also prints: '
          '&ldquo;Don&rsquo;t fit these perfectly? Apply anyway.&rdquo;',
 apply='An application, then a cohort.',
 starts='', starts_text='Cohort start date is Not stated on this page. The courses index lists dated '
        'cohorts for the sibling courses, so check there.',
 deadline='2026-09-27', deadline_text='<b>27 September 2026.</b> The page prints &ldquo;Apply by 27 '
          'Sep&rdquo;, read at source on 7 September 2026. <b>This wall previously said 6 September '
          'and showed the course as shut.</b> It was not shut: BlueDot runs rolling cohorts and the '
          'date on the page simply rolls forward, so a date read once and left alone goes wrong by '
          'itself. The year is still not printed on the page.',
 precision='listing',
 why='Free, remote, three weeks to apply, and it says in its own words to apply even if you do not '
     'fit the profile. You are the person that sentence is written for.',
 view='Apply. It costs you a form and the worst case is no. Be straight in the application about '
      'being an eighteen-year-old medical student teaching himself the field &mdash; that is a more '
      'interesting applicant than a mediocre CS graduate, and they know it. <b>But do AGI Strategy '
      'first</b>: BlueDot&rsquo;s own page says this course builds on it, and expects you to already '
      'know how LLMs are trained and what gradient descent is. The certificate question is Not '
      'stated on this one, unlike AGI Strategy where the FAQ answers it yes.',
 conf='verified', checked='2026-09-07',
 tags=['free', 'online', 'cohort', 'ai safety', 'do agi strategy first'],
))

PASSES.append(dict(
 id='swayam-nptel', cat='course', domain='ai',
 name='SWAYAM and NPTEL',
 host='Ministry of Education, Government of India, with the IITs and IISc',
 platform='swayam.gov.in', url='https://swayam.gov.in/',
 blurb='India&rsquo;s national online course platform. Courses taught by IIT and IISc faculty, free '
       'to take, with an optional paid proctored exam at the end that carries actual university credit.',
 mark='A certificate from an IIT or IISc, and printed on the platform: credits you can '
      '&ldquo;get transferred to your degree&rdquo;.',
 fmt='hybrid', location='Learning is online; the certification exam is sat at a physical centre',
 travel='None to learn. The certification exam is held at test centres, so that part is in person.',
 fee='Learning is free &mdash; the site prints &ldquo;Free Course from Top Universities&rdquo;. The '
     'certification exam is charged separately; <b>the fee is Not stated on the homepage</b> and you '
     'should read it on the course page before registering.',
 commit='A semester per course, typically a few hours a week.',
 eligible='Open enrolment. No eligibility restriction is printed on the homepage.',
 apply='Enrol on the course page during the semester window; register separately for the exam.',
 starts='', starts_text='Runs in semesters. The site currently shows the approved course list for '
        'the July 2026 semester, and results for the January 2026 semester.',
 deadline='', deadline_text='Enrolment and exam registration windows are per-semester and per-course. '
          'The homepage does not print the exact dates &mdash; it says only that certain courses are '
          '&ldquo;open for exam registration now&rdquo;.',
 precision='none',
 why='You are already an IIT Madras BS student, which makes this the cheapest credibility on the '
     'entire page: the same institutions, real credit, and nothing to be selected for. It is the '
     'only item here where the certificate can count towards a degree rather than sitting beside one.',
 view='Go and read how the credit transfer actually works for your IITM BS programme specifically, '
      'because that is where this stops being a certificate and starts being a shortcut. The trap is '
      'the one everybody falls into: enrolling free, never registering for the exam, and ending the '
      'semester with nothing to show. If you enrol in one, register for the exam the same day.',
 conf='listing', checked='2026-09-04',
 tags=['free to learn', 'paid exam', 'online', 'credit', 'india', 'iit'],
))

PASSES.append(dict(
 id='openwho', cat='course', domain='med',
 name='OpenWHO', host='World Health Organization', platform='openwho.org',
 url='https://openwho.org/channels',
 blurb='The WHO&rsquo;s own online learning platform &mdash; short courses in outbreak response, '
       'clinical management, emergency care and infectious disease, in many languages.',
 mark='Courses badged by the World Health Organization. Whether a Record of Achievement is issued '
      'is Not stated on the pages I could read.',
 fmt='remote', location='Online, self-paced',
 travel='None.',
 fee='No fee is printed. The platform is a public health resource.',
 commit='Short courses, typically a few hours each.',
 eligible='Channel access varies. Most channels are marked <b>&ldquo;Public, Restricted&rdquo;</b>; '
          'the Community First Aid Response Course is marked <b>&ldquo;Public, Open&rdquo;</b>. What '
          '&ldquo;restricted&rdquo; requires is Not stated on the channels page.',
 apply='Create an account and enrol in an open channel.',
 starts='', starts_text='Self-paced, always available.',
 deadline='', deadline_text='No deadline.',
 precision='none',
 why='WHO material on outbreak response and clinical management, free, before you have started '
     'MBBS. The subject matter is the actual practice of the thing you are about to study.',
 view='Start with the one channel I could confirm is fully open &mdash; Community First Aid Response '
      '&mdash; and see what the platform is like before assuming the rest. I could not confirm the '
      'certificate policy from outside, and that matters here: if these do not issue a Record of '
      'Achievement, this is knowledge rather than credibility, and it belongs on a different list '
      'in your head.',
 conf='listing', checked='2026-09-04',
 tags=['free', 'online', 'who', 'public health', 'no deadline'],
))

# ============================ MEMBERSHIP ====================================

PASSES.append(dict(
 id='rsna-member-in-training', cat='member', domain='med',
 name='RSNA Members-in-Training',
 host='Radiological Society of North America', platform='rsna.org',
 url='https://www.rsna.org/membership/discounted-membership-rates',
 blurb='Free membership of the Radiological Society of North America for medical students, with the '
       'full standard member benefits package.',
 mark='Membership of a major international medical society, in your name, at no cost.',
 fmt='remote', location='Membership is remote; the annual meeting is in Chicago',
 travel='None required. Members-in-training get discounts on RSNA meetings if you ever go.',
 fee='Free. Printed literally on the rates page: <b>$0, complimentary</b>.',
 commit='Minutes to apply. No ongoing obligation.',
 eligible='Printed literally: medical students, residents, fellows in radiology or radiologic '
          'science programmes, and imaging sciences graduate students. <b>You are not eligible until '
          'you are enrolled in MBBS</b>, because of how you have to apply &mdash; see below.',
 apply='Upload a programme verification form <b>signed by your dean or programme director</b> to '
       'your RSNA account, or send the members-in-training application form to '
       'customerservice@rsna.org. That signature is the catch: it needs a dean, so it needs you to '
       'have started.',
 starts='', starts_text='Whenever you are enrolled.',
 deadline='', deadline_text='No deadline. Permanently open.',
 precision='none',
 why='Free membership of an international medical society is the cheapest real credential in '
     'existence, and radiology is the single most machine-learning-exposed specialty in medicine &mdash; '
     'which is precisely the intersection you are standing on.',
 view='<b>You cannot do this yet</b> and I want to be straight about that rather than let you find '
      'out at the form: it needs a signature from a dean you do not have until MBBS starts. Put it '
      'on a list for your first fortnight at medical college, when you will be surrounded by '
      'administrative people anyway. Then it costs one signature and nothing else, permanently.',
 conf='verified', checked='2026-09-04',
 tags=['free', 'medicine', 'radiology', 'no deadline', 'after mbbs starts'],
))

# ============================ COMMUNITIES ===================================

PASSES.append(dict(
 id='cohere-labs-community', cat='community', domain='ai',
 name='Cohere Labs Open Science Community',
 host='Cohere Labs', platform='cohere.com/research/open-science',
 url='https://cohere.com/research/open-science',
 blurb='An open research community of several thousand people doing machine learning research '
       'together, run by a frontier AI lab, free to join and open to people with no institutional '
       'affiliation.',
 mark='Collaborators, and access to the room where open ML research is done. Members do publish; '
      'co-authorship is not promised anywhere on the page and I am not going to imply it is.',
 fmt='remote', location='Online, worldwide',
 travel='None.',
 fee='Free.',
 commit='Yours to set. It is a community, not a course.',
 eligible='Open to &ldquo;researchers, engineers, linguists, social scientists, and lifelong '
          'learners&rdquo;. The page shows the application status as <b>Open</b> and states that '
          '&ldquo;Applications are reviewed on a weekly basis&rdquo;.',
 apply='An application form. Reviewed weekly, so there is no window to miss.',
 starts='', starts_text='Whenever you are accepted.',
 deadline='', deadline_text='No deadline. Rolling, reviewed weekly.',
 precision='none',
 why='It is a way into real ML research that does not require a university to vouch for you. The '
     'page says 5,000+ researchers and describes lifelong learners as welcome &mdash; that is an '
     'unusually open door for a frontier lab.',
 view='Apply, and then treat acceptance as the beginning rather than the achievement. Communities '
      'like this reward the people who turn up to things and do unglamorous work on somebody '
      'else&rsquo;s project for a few months. That is genuinely how people with no credentials end '
      'up on papers &mdash; but it is months, not weeks, and joining alone leaves no mark at all.',
 conf='verified', checked='2026-09-04',
 tags=['free', 'remote', 'ml research', 'no deadline', 'rolling'],
))

PASSES.append(dict(
 id='ml-collective', cat='community', domain='ai',
 name='ML Collective', host='ML Collective', platform='mlcollective.org',
 url='https://mlcollective.org/',
 blurb='A non-profit whose stated purpose is making machine learning research possible for people '
       'without a lab &mdash; a weekly reading group, open collaborations, office hours, and free '
       'compute.',
 mark='A research home when you do not have one, and a reading group that will teach you how papers '
      'are actually read.',
 fmt='remote', location='Online',
 travel='None.',
 fee='Free. The site prints the mission as making research opportunities &ldquo;accessible and free '
     'for all&rdquo;, and mentions &ldquo;free compute resources&rdquo;.',
 commit='Yours to set. The reading group is weekly.',
 eligible='Printed literally: &ldquo;MLC can be a &lsquo;research home&rsquo; for you regardless of '
          'your affiliation, employer, or background.&rdquo;',
 apply='Join the reading group or the Discord. No application is printed on the page.',
 starts='', starts_text='The reading group runs weekly.',
 deadline='', deadline_text='No deadline printed.',
 precision='none',
 why='That one sentence &mdash; regardless of your affiliation &mdash; is the whole reason this is '
     'on the wall. It is written for exactly your situation.',
 view='The reading group is the part to use. Turning up weekly to a paper discussion, for six '
      'months, will teach you more about machine learning than any certificate on this page, and it '
      'costs nothing but a recurring hour. It leaves no formal mark, which is why I have rated its '
      'prestige low and its learning high &mdash; do not confuse the two, and do not let it replace '
      'the things that do leave a mark.',
 conf='verified', checked='2026-09-04',
 tags=['free', 'remote', 'reading group', 'no deadline', 'no gatekeeper'],
))

# ============================ PEER REVIEW ===================================

PASSES.append(dict(
 id='prereview', cat='review', domain='research',
 name='PREreview', host='PREreview', platform='prereview.org', url='https://prereview.org/',
 blurb='A platform for reviewing preprints openly, built specifically to bring early-career '
       'researchers into peer review rather than leaving it to established academics.',
 mark='Published reviews with your name on them, permanently, citable. This is the only item on the '
      'wall where the credential is a thing you write rather than a thing you receive.',
 fmt='remote', location='Online',
 travel='None.',
 fee='Free.',
 commit='One preprint at a time. A review is an evening.',
 eligible='Printed literally: it exists to &ldquo;support and empower diverse and historically '
          'excluded communities of researchers (particularly those at early stages of their career) '
          'to find a voice, train, and engage in peer review&rdquo;. Open to all researchers &mdash; '
          'the site&rsquo;s own tagline is &ldquo;Open preprint reviews. For all researchers.&rdquo;',
 apply='No application. Create an account and review something.',
 starts='', starts_text='Whenever you want. The site was carrying reviews dated September 2026 when '
        'I opened it.',
 deadline='', deadline_text='No deadline. Permanently open.',
 precision='none',
 why='Peer review is the one part of academic life that normally requires a PhD to enter, and this '
     'is a legitimate door into it that is open to you today. It also runs training workshops and '
     'live review sessions, so you are not doing it blind.',
 view='This is the highest-leverage item on the page and almost nobody your age knows it exists. '
      'Reviewing three preprints properly in your first MBBS year would teach you more about how '
      'research actually works than a year of lectures, and it produces a public, citable trail with '
      'your name on it. Start by reading their existing reviews and joining a Live Review before '
      'writing your own &mdash; a bad public review is also permanent.',
 conf='verified', checked='2026-09-04',
 tags=['free', 'remote', 'peer review', 'no deadline', 'your name on it'],
))

# ============================ CITIZEN SCIENCE ===============================

PASSES.append(dict(
 id='zooniverse', cat='citizen', domain='research',
 name='Zooniverse', host='The Zooniverse', platform='zooniverse.org',
 url='https://www.zooniverse.org/projects',
 blurb='The largest platform for people-powered research &mdash; real research projects, including '
       'biomedical ones, where volunteers classify the data the researchers cannot get through alone.',
 mark='Contribution to real datasets. Whether volunteers are credited or acknowledged is Not stated '
      'on the projects page.',
 fmt='remote', location='Online',
 travel='None.',
 fee='Free.',
 commit='Minutes at a time. Genuinely.',
 eligible='Not restricted on the projects page. It describes itself as &ldquo;People-Powered '
          'Research&rdquo; and includes a K-12 section, so school-age participation is supported.',
 apply='None. Whether an account is required is Not stated on the listing page.',
 starts='', starts_text='Any time.',
 deadline='', deadline_text='No deadline. Individual projects have their own lifespans.',
 precision='none',
 why='Medicine is one of its listed disciplines. Two of its live projects are Monkey Health Explorer '
     '&mdash; identifying white blood cell types &mdash; and Etch A Cell. That is real histology and '
     'real cell imaging, for free, before you have seen a slide in a lecture.',
 view='Be clear-eyed about what this is: it is learning and it is contribution, but on its own it is '
      'not credibility, and I have rated it that way. Where it becomes valuable is as the cheap way '
      'to find out whether you actually enjoy looking at cells for hours &mdash; which is a genuinely '
      'useful thing to know about yourself before you choose a specialty. Do the white blood cell '
      'one for an evening.',
 conf='verified', checked='2026-09-04',
 tags=['free', 'remote', 'no deadline', 'histology', 'try it tonight'],
))

PASSES.append(dict(
 id='foldit', cat='citizen', domain='research',
 name='Foldit', host='University of Washington / Foldit team', platform='fold.it',
 url='https://fold.it/',
 blurb='A game where players fold proteins by hand, and the best human solutions have fed back into '
       'real structural biology.',
 mark='An intuition for protein structure that is very hard to get from a textbook. Whether players '
      'have been credited as authors is Not stated on the page I opened.',
 fmt='remote', location='Online, downloadable',
 travel='None.',
 fee='No cost is mentioned. The page offers a download and a sign-up.',
 commit='As little as you like. Individual puzzles have their own timeframes.',
 eligible='Not restricted on the page. It describes itself as &ldquo;a revolutionary crowdsourcing '
          'computer game enabling you to contribute to scientific research&rdquo;.',
 apply='Download it.',
 starts='', starts_text='Any time.',
 deadline='', deadline_text='No overall deadline. Individual puzzles open and close.',
 precision='none',
 why='Protein structure is coming for you twice over &mdash; once in biochemistry and once in AI, '
     'because structure prediction is the most famous thing machine learning has done to biology. '
     'Folding them by hand for a few evenings makes both halves make sense.',
 view='This is a toy that happens to be real, and I am putting it low on prestige for exactly that '
      'reason. But it is the single most enjoyable way to understand why protein folding is hard, '
      'and understanding that is what makes the AlphaFold story mean something instead of being a '
      'headline. Treat it as recreation with a side effect.',
 conf='verified', checked='2026-09-04',
 tags=['free', 'remote', 'no deadline', 'protein', 'fun'],
))

# ============================ GRANT =========================================

PASSES.append(dict(
 id='emergent-ventures-india', cat='grant', domain='open',
 name='Emergent Ventures India', host='Mercatus Center, George Mason University',
 platform='mercatus.org', url='https://www.mercatus.org/emergent-ventures',
 blurb='A rolling grant and fellowship programme for people with early, ambitious ideas, with a '
       'dedicated India track. Deliberately low-overhead: a short application, no institution needed.',
 mark='A grant and a funder&rsquo;s name behind your own project &mdash; and the cohort, which is '
      'the part people say matters most.',
 fmt='remote', location='Anywhere. The India track is for projects focused on India.',
 travel='None required.',
 fee='Free to apply.',
 commit='The application is short by design. What you do with a grant is yours.',
 eligible='Printed literally: applicants must be &ldquo;13 years of age or older&rdquo;. No '
          'nationality restriction is printed. Dedicated support is offered &ldquo;for projects with '
          'a focus on India, Africa and the Caribbean, or Ukraine&rdquo;, chosen from a dropdown in '
          'the application.',
 apply='One online application. Select India under &ldquo;My Project Will Affect&rdquo;.',
 starts='', starts_text='Whenever your application is accepted. Cohorts are announced periodically.',
 deadline='', deadline_text='No deadline. Applications are open year-round.',
 precision='none',
 why='It funds ideas, not credentials, from people as young as thirteen, on a rolling basis. There '
     'is no window to miss and no institution to go through &mdash; which makes it the one thing on '
     'this page you could act on the day you have an idea worth funding.',
 view='Do not apply yet. Apply when you have built something &mdash; and you build things: the '
      'competition wall, the diary system, the MCC simulator. The application rewards a specific '
      'idea and a person who has already started, not a promising student asking for support. Keep '
      'this on the wall as the thing you go to <i>after</i> a project exists, and note that because '
      'it is rolling, waiting costs you nothing at all.',
 conf='verified', checked='2026-09-04',
 tags=['free', 'rolling', 'no deadline', 'grant', 'india', 'when you are ready'],
))

# ============================ ROLES =========================================

PASSES.append(dict(
 id='sgb-mediators', cat='role', domain='open',
 name='Science Gallery Bengaluru &mdash; Mediators',
 host='Science Gallery Bengaluru', platform='bengaluru.sciencegallery.com',
 url='https://bengaluru.sciencegallery.com/quantum-mediators',
 blurb='Mediators are the people on the gallery floor who take visitors through the exhibits &mdash; '
       'trained each season by the artists and researchers behind the show.',
 mark='Printed literally: mediators take &ldquo;intensive training with a range of artists and '
      'scholars&rdquo; each season. A public-facing science communication role with a named '
      'institution behind it.',
 fmt='in-person', location='Science Gallery Bengaluru, Bellary Road',
 travel='You would need to be in Bengaluru for the season.',
 fee='Not stated. The page describes mediators as &ldquo;staff members&rdquo; but prints no pay '
     'information.',
 commit='A season. The exact hours are Not stated on the page.',
 eligible='<b>Not stated on the page.</b> It lists the current QUANTUM mediators with photographs '
          'and prints no eligibility, no age rule and no application route.',
 apply='Not stated on the mediators page, which is a showcase of the current cohort rather than a '
       'way in. Recruitment runs through their <b>Open Calls</b> page at '
       '/work-with-us-open-calls and their Jobs page. <b>Re-checked 7 September 2026, all three '
       'pages: still no live mediator call</b> &mdash; Open Calls carries only closed ones and '
       'the word &ldquo;mediator&rdquo; appears nowhere on Jobs except in the site menu. So these '
       'fields are blank because there is nothing to state, not because nobody looked. The '
       'general contact is info@bengaluru.sciencegallery.com.',
 starts='', starts_text='Recruited per exhibition season. The current season is QUANTUM.',
 deadline='', deadline_text='No open call today. Their Open Calls page carried only two closed ones '
          '&mdash; Entangled Ecosystems Grant II, closed 7 August 2026, and INTELLIGENCE, closed '
          '11 January 2026.',
 precision='none',
 why='<b>You asked for this one yourself.</b> In your diary on 3 September you wrote that on the '
     'Bangalore trip you would &ldquo;find mediators at the Science Gallery &mdash; people to '
     'actually talk to&rdquo;. They are a real programme with a real name, and the gallery is free '
     'to walk into.',
 view='There is no live call, so there is nothing to apply to today &mdash; and that is the honest '
      'answer rather than a form to fill. But you are going to Bengaluru, entry is free, and '
      'mediators are on the floor: the actual move is to go, talk to one, and ask how they got the '
      'role and when the next season recruits. That is a better source than any page I can open, and '
      'it is exactly the thing you already said you wanted to do.',
 conf='verified', checked='2026-09-04',
 tags=['bengaluru', 'free entry', 'no live call', 'go and ask', 'your own idea'],
))

PASSES.append(dict(
 id='sgb-externship', cat='role', domain='open',
 name='Science Gallery Bengaluru &mdash; Undergraduate Externship',
 host='Science Gallery Bengaluru', platform='bengaluru.sciencegallery.com',
 url='https://bengaluru.sciencegallery.com/externships',
 blurb='A one-month attachment shadowing across the gallery&rsquo;s departments &mdash; programmes, '
       'learning, production, design, research and communications.',
 mark='A month inside a working science-and-art institution, across six departments, and the people '
      'you meet doing it.',
 fmt='in-person', location='Science Gallery Bengaluru',
 travel='Bengaluru, for a month.',
 fee='Not stated on the page.',
 commit='Printed literally: &ldquo;20 hours of engagement per week&rdquo; for &ldquo;1 month&rdquo;.',
 eligible='The page names two tracks, &ldquo;High School Externships&rdquo; and '
          '&ldquo;Undergraduate Externships&rdquo;. You would be the second. Nothing further is printed.',
 apply='Not stated on the page. Contact info@bengaluru.sciencegallery.com.',
 starts='', starts_text='Printed literally: externships run &ldquo;in the months of May and June&rdquo;.',
 deadline='', deadline_text='Not stated. The page&rsquo;s most recent post is dated 11 May 2024, so '
          'treat its live status as unconfirmed.',
 precision='none',
 why='An explicitly undergraduate track, one month, in May or June &mdash; which is exactly when a '
     'medical college year gives you a gap. Shadowing six departments is an unusually broad look '
     'inside an institution.',
 view='The page is from 2024 and I could not confirm it is still running, which is worth knowing '
      'before you build a summer around it. Email them &mdash; one message settles it, and asking '
      'about the externship is also a natural way to ask about the mediator role in the same breath.',
 conf='listing', checked='2026-09-04',
 tags=['bengaluru', 'undergraduate', 'may-june', 'status unconfirmed'],
))

PASSES.append(dict(
 id='sgb-internship', cat='role', domain='open',
 name='Science Gallery Bengaluru &mdash; Internship',
 host='Science Gallery Bengaluru', platform='bengaluru.sciencegallery.com',
 url='https://bengaluru.sciencegallery.com/internships',
 blurb='A full-time internship of six months to a year at the gallery.',
 mark='Six to twelve months inside a science communication institution.',
 fmt='in-person', location='Science Gallery Bengaluru',
 travel='Bengaluru, and you would have to live there.',
 fee='Not stated on the page &mdash; it does not say whether interns are paid.',
 commit='Printed literally: &ldquo;Be available for a full-time internship for six months to a '
        'year&rdquo;. That is full time, and it does not fit alongside MBBS.',
 eligible='Printed literally: &ldquo;Be enrolled in a college/ university or be a recent '
          'graduate&rdquo;, and &ldquo;Have good verbal and written command of English&rdquo;. '
          'Kannada is described as desirable but optional.',
 apply='Email internships@bengaluru.sciencegallery.com.',
 starts='', starts_text='Not stated.',
 deadline='', deadline_text='No live opening. The page says it lists present opportunities and '
          'currently shows none.',
 precision='none',
 why='It is on the wall for completeness, because it is the third of the gallery&rsquo;s three '
     'routes in and you should see all three side by side to pick the right one.',
 view='<b>Not for you</b>, and I would rather say so than pad the wall. Full time for six to twelve '
      'months is incompatible with starting MBBS. The externship is the one that fits your life; '
      'this is here so you can see why.',
 conf='verified', checked='2026-09-04',
 tags=['bengaluru', 'full time', 'not for you', 'no live opening'],
))

# ============================ CONFERENCES ===================================

PASSES.append(dict(
 id='cgtcon-2026', cat='conf', domain='med',
 name='11th International Cell &amp; Gene Therapy Conference (CGTCON 2026)',
 host='Not stated on the IndiaBioscience listing', platform='indiabioscience.org/events',
 url='https://indiabioscience.org/events',
 blurb='An international conference on cell and gene therapy, in Tamil Nadu, in its eleventh year.',
 mark='Attendance at an international conference in one of the fastest-moving areas of medicine.',
 fmt='in-person', location='Tamil Nadu, India',
 travel='Tamil Nadu, two days.',
 fee='Not stated on the listing.',
 commit='Two days, 9&ndash;10 October 2026.',
 eligible='Not stated on the listing.',
 apply='Registration through the conference&rsquo;s own site, linked as &ldquo;Official Website&rdquo; '
       'from the IndiaBioscience listing.',
 starts='2026-10-09', starts_text='9&ndash;10 October 2026',
 deadline='2026-10-08', deadline_text='8 October 2026, printed on the IndiaBioscience listing as '
          '&ldquo;Registration deadline 08 October&rdquo;',
 precision='listing',
 why='Cell and gene therapy is where medicine is actually changing shape right now, and conferences '
     'are the one place you can sit in a room with a field before you are qualified to work in it.',
 view='Conferences are the most overrated thing on this wall for someone at your stage &mdash; you '
      'will understand perhaps a fifth of it &mdash; with one exception that makes them worth it: '
      'if it has a student abstract or poster track, presenting a poster is a real, citable line. '
      'The listing does not say whether it has one. That is the single question to ask their site '
      'before deciding.',
 conf='listing', checked='2026-09-04',
 tags=['tamil nadu', 'conference', 'gene therapy', 'ask about posters'],
))

PASSES.append(dict(
 id='ncbs-spatialomics', cat='conf', domain='research',
 name='2nd SpatialOmics Symposium', host='NCBS Bangalore', platform='ncbs.res.in/events',
 url='https://www.ncbs.res.in/events',
 blurb='A three-day symposium on spatial omics &mdash; measuring what genes and proteins are doing '
       'while keeping track of where in the tissue they are doing it.',
 mark='Attendance at a research symposium at NCBS.',
 fmt='in-person', location='NCBS, Bengaluru',
 travel='Bengaluru, three days.',
 fee='Not stated on the NCBS listing.',
 commit='Three days, 21&ndash;23 October 2026.',
 eligible='Not stated on the NCBS listing.',
 apply='Through the symposium page. Not linked from the events listing.',
 starts='2026-10-21', starts_text='21&ndash;23 October 2026',
 deadline='', deadline_text='No registration deadline is printed on the NCBS listing.',
 precision='none',
 why='Spatial omics sits precisely where your two subjects meet &mdash; it is histology answered '
     'with data science, and it is one of the hottest areas in biology right now.',
 view='Of all the NCBS events, this is the one whose subject is closest to the intersection you are '
      'actually building a life on. Three days in October in the city you are visiting anyway. Find '
      'the symposium page and see whether they admit non-presenting attendees &mdash; many symposia '
      'do, cheaply, for students.',
 conf='listing', checked='2026-09-04',
 tags=['bengaluru', 'ncbs', 'spatial omics', 'your intersection'],
))

PASSES.append(dict(
 id='ncbs-manotsava', cat='conf', domain='med',
 name='Manotsava 2026: Neuroscience Research Symposium',
 host='Centre for Brain and Mind, NCBS', platform='ncbs.res.in/events',
 url='https://www.ncbs.res.in/events',
 blurb='A two-day neuroscience research symposium run by the NCBS Centre for Brain and Mind.',
 mark='Attendance at a neuroscience symposium at NCBS.',
 fmt='in-person', location='NCBS, Bengaluru',
 travel='Bengaluru, two days.',
 fee='Not stated on the NCBS listing.',
 commit='Two days, 3&ndash;4 December 2026.',
 eligible='Not stated on the NCBS listing.',
 apply='Through the symposium page. Not linked from the events listing.',
 starts='2026-12-03', starts_text='3&ndash;4 December 2026',
 deadline='', deadline_text='No registration deadline is printed on the NCBS listing.',
 precision='none',
 why='Neuroscience is one of the few areas where an MBBS and a data science degree stop being two '
     'separate things, and this is the local one.',
 view='Three months out, two days long, in Bengaluru. The useful move is to find out now whether it '
      'takes student registrations and whether it has a poster session, because if it does, three '
      'months is enough time to actually have something to put on one.',
 conf='listing', checked='2026-09-04',
 tags=['bengaluru', 'ncbs', 'neuroscience'],
))

PASSES.append(dict(
 id='ncbs-annual-talks-2027', cat='lecture', domain='research',
 name='NCBS Annual Talks 2027: &ldquo;Dimensions of Life&rdquo;',
 host='NCBS Bangalore', platform='ncbs.res.in/events', url='https://www.ncbs.res.in/events',
 blurb='NCBS&rsquo;s flagship annual talks, three days at the start of January.',
 mark='Nothing but having been in the room &mdash; which is what a talk is, and why it is on a '
      'different kind of card from the rest.',
 fmt='in-person', location='NCBS, Bengaluru',
 travel='Bengaluru, three days.',
 fee='Not stated on the NCBS listing.',
 commit='Three days, 6&ndash;8 January 2027.',
 eligible='Not stated on the NCBS listing.',
 apply='Not stated on the NCBS listing.',
 starts='2027-01-06', starts_text='6&ndash;8 January 2027',
 deadline='', deadline_text='No deadline is printed. A talk is not applied for &mdash; you turn up, '
          'if they let you.',
 precision='none',
 why='It is NCBS&rsquo;s showcase, it is titled &ldquo;Dimensions of Life&rdquo;, and it is three '
     'days of the best talks they can assemble. If any single event would tell you whether research '
     'biology is your world, it is this one.',
 view='This is the cheapest possible test of whether you actually want the research life, and I '
      'would put it above several of the workshops for that reason alone. Check in December whether '
      'outside attendance is allowed. If it is, and you can be in Bengaluru in early January, go.',
 conf='listing', checked='2026-09-04',
 tags=['bengaluru', 'ncbs', 'talks', 'go and look'],
))

PASSES.append(dict(
 id='iisc-spicmacay', cat='lecture', domain='open',
 name='IISc SPICMACAY Hindustani Vocal Concert',
 host='Indian Institute of Science', platform='iisc.ac.in/news-events/events-upcoming',
 url='https://www.iisc.ac.in/news-events/events-upcoming/',
 blurb='A Hindustani vocal concert at the J N Tata Auditorium, part of the SPICMACAY series that '
       'brings classical performance onto campuses.',
 mark='Nothing at all, and that is fine. It is an evening on the IISc campus.',
 fmt='in-person', location='J N Tata Auditorium, IISc Bengaluru',
 travel='Bengaluru, one evening.',
 fee='Not stated on the IISc listing. SPICMACAY events are generally free, but the page does not '
     'say so and I am not going to state it as fact.',
 commit='One evening.',
 eligible='Not stated on the IISc listing.',
 apply='Not stated.',
 starts='2026-09-06', starts_text='6 September 2026',
 deadline='', deadline_text='No deadline. It happens on the 6th.',
 precision='none',
 why='It is on the wall as an honest example of the category: a thing that happens on one evening, '
     'costs nothing, leaves no credential, and gets you onto the IISc campus. You said you want to '
     'go to science fests in Bengaluru &mdash; this is what the calendar of that actually looks like.',
 view='Two days away and you are not in Bengaluru, so you will miss this one. It is here to show you '
      'the shape of the thing: IISc publishes a live events page, most of what is on it is open, and '
      'checking it once a fortnight while you are in the city costs nothing. <b>Bookmark the page, '
      'not the concert.</b>',
 conf='listing', checked='2026-09-04',
 tags=['bengaluru', 'iisc', 'one evening', 'example of the category'],
))

PASSES.append(dict(
 id='sgb-quantum', cat='lecture', domain='open',
 name='QUANTUM &mdash; Science Gallery Bengaluru',
 host='Science Gallery Bengaluru', platform='bengaluru.sciencegallery.com',
 url='https://quantum.scigalleryblr.org/exhibition',
 blurb='A year-long exhibition on quantum physics at the interface of science and art, with its own '
       'programme of events running alongside it.',
 mark='Nothing formal. A day inside a very good exhibition, and mediators on the floor to talk to.',
 fmt='in-person', location='Science Gallery Bengaluru, Bellary Road',
 travel='Bengaluru, a day.',
 fee='Free &mdash; printed literally: &ldquo;Science Gallery Bengaluru charges no admission fee. '
     'Every exhibition, every programme, every season.&rdquo;',
 commit='An afternoon.',
 eligible='Open to all. The gallery&rsquo;s stated audience is young adults.',
 apply='None. Walk in.',
 starts='', starts_text='Running now, year-long.',
 deadline='', deadline_text='No deadline while the season runs.',
 precision='none',
 why='Free, open now, in the city you are going to, with the mediators you already said you wanted '
     'to talk to standing in it. There is no application, no fee and no gatekeeper &mdash; the only '
     'cost is going.',
 view='Do this on the Bangalore trip. It is the one item on this entire page that requires nothing '
      'from you except turning up, and it doubles as the way into the mediator question. Ask a '
      'mediator how they got the job. That single conversation is worth more than the three '
      'gallery entries on this wall put together.',
 conf='verified', checked='2026-09-04',
 tags=['bengaluru', 'free', 'no deadline', 'walk in', 'do this'],
))

# ============================ AMBASSADOR ====================================

PASSES.append(dict(
 id='msft-student-ambassador', cat='badge', domain='build',
 name='Microsoft Learn Student Ambassadors', host='Microsoft', platform='mvp.microsoft.com',
 url='https://mvp.microsoft.com/en-US/studentambassadors',
 blurb='A global programme of students who run events and build community around Microsoft '
       'technology on their own campuses, with tiers you progress through.',
 mark='A title from Microsoft that you hold and can put on a profile, plus the community behind it.',
 fmt='hybrid', location='Based on your own campus, with a global online community',
 travel='Not stated on the pages I could read.',
 fee='Not stated on the pages I could read.',
 commit='Not stated on the pages I could read.',
 eligible='<b>Not stated on either page I opened.</b> The programme pages are marketing; the '
          'eligibility, the intake and the benefits are behind a sign-in. <b>I could not look</b>, '
          'which is different from finding nothing.',
 apply='A &ldquo;Get Started&rdquo; route on their site, behind a Microsoft sign-in.',
 starts='', starts_text='Not stated.',
 deadline='', deadline_text='Not stated. Whether intake is rolling or by cohort is unknown to me.',
 precision='none',
 why='It is on the wall because you asked what categories exist, and &ldquo;a title a company gives '
     'you for a year&rdquo; is a real category you would not otherwise have thought of. GitHub runs '
     'a near-identical one, Campus Experts, whose terms are also behind a login.',
 view='<b>I could not read the terms and I am not going to invent them.</b> That is the honest state '
      'of this card. Fifteen minutes signed in would settle whether it is open to an IITM BS student '
      'and what it actually asks of you. Worth those fifteen minutes, because ambassador programmes '
      'are unusually cheap credibility &mdash; but do not treat anything on this card as confirmed.',
 conf='listing', checked='2026-09-04',
 tags=['title', 'campus', 'terms unread', 'behind a login'],
))

PASSES.append(dict(
 id='github-campus-experts', cat='badge', domain='build',
 name='GitHub Campus Experts', host='GitHub Education', platform='githubcampus.expert',
 url='https://githubcampus.expert/',
 blurb='GitHub&rsquo;s programme for students who build technical communities on their campus, with '
       'training and a certification at the end of it.',
 mark='A GitHub-issued title and training. The exact credential is Not stated on the public page.',
 fmt='hybrid', location='Your own campus, plus an online community',
 travel='Not stated. The public page lists Campus Experts and the events they run at their '
        'own institutions.',
 fee='Not stated on the public page.',
 commit='Not stated on the public page.',
 eligible='<b>Not stated.</b> The public site shows current and alumni experts and their events, '
          'and nothing else. The Apply link redirects to a GitHub OAuth sign-in, so the eligibility '
          'rules are behind a login. <b>I could not look.</b>',
 apply='Through education.github.com, which requires a GitHub account.',
 starts='', starts_text='Not stated.',
 deadline='', deadline_text='Not stated.',
 precision='none',
 why='The rules note that you have an account somewhere you do not really use, and that it is most '
     'likely GitHub. If so, this costs you a sign-in to investigate &mdash; and it is the '
     'best-regarded of the campus ambassador programmes among people who write software.',
 view='Same honest position as the Microsoft one: <b>the terms are behind a login and I did not read '
      'them.</b> The difference is that you may already have the account. Sign in once and read the '
      'requirements properly &mdash; and note that these programmes usually want you to run actual '
      'events, which is a real time cost, not a badge you collect.',
 conf='listing', checked='2026-09-04',
 tags=['title', 'campus', 'terms unread', 'behind a login', 'github'],
))


# ============================ CERTIFICATION =================================
# A category that was empty on the first build, because CITI Program was blocked
# by the browser's domain permissions and 404'd to the fetcher. This one is
# reachable, free, and issues a credential with an expiry date on it.

PASSES.append(dict(
 id='nida-gcp', cat='cert', domain='med',
 name='Good Clinical Practice certification',
 host='National Institute on Drug Abuse Clinical Trials Network',
 platform='gcp.nidatraining.org', url='https://gcp.nidatraining.org/',
 blurb='The standard training in how clinical trials must legally and ethically be run &mdash; '
       'twelve modules built on the ICH Good Clinical Practice principles and the US Code of '
       'Federal Regulations.',
 mark='A named GCP certificate. <b>Every clinical trial in the world requires this of its staff</b>, '
      'so it is one of the few things an eighteen-year-old can hold that a research coordinator '
      'would recognise instantly.',
 fmt='remote', location='Online, self-paced',
 travel='None.',
 fee='Free. The page states the training &ldquo;has been funded in whole or in part with Federal '
     'funds from the National Institute on Drug Abuse&rdquo;, and no price is shown anywhere on it.',
 commit='Printed literally: it &ldquo;is self-paced and takes approximately six hours to '
        'complete&rdquo;. Twelve modules, each with a quiz you must pass at 80% &mdash; there is also a '
        '100% option for anyone whose ethics committee demands it. The twelve: introduction to clinical '
        'trials, institutional review boards, informed consent, confidentiality and privacy, participant '
        'safety and adverse events, quality assurance, the research protocol, documentation and '
        'record-keeping, research misconduct, roles and responsibilities, recruitment and retention, and '
        'investigational new drugs.',
 eligible='No restriction by profession or background is printed. The page says only '
          '&ldquo;If you do not have an account, click here to register&rdquo;.',
 apply='Register an account and start. There is no application and no cohort.',
 starts='', starts_text='Whenever you want. Self-paced.',
 deadline='', deadline_text='No deadline. <b>The certificate itself expires</b> &mdash; the page '
          'prints that &ldquo;Within the NIDA Clinical Trials Network, certification expires after '
          'three years.&rdquo;',
 precision='none',
 extra='This is the category the first build of this page could not fill. CITI Program, the other '
       'well-known route to research-ethics certification, was unreachable from this machine.',
 why='Six hours, free, no gatekeeper, and it ends in a credential that is genuinely required '
     'infrastructure in clinical research rather than a participation certificate. It is also the '
     'single most direct answer to the word you keep using &mdash; credibility &mdash; because it '
     'is the thing that lets you be listed on a trial at all.',
 view='<b>Do this one in your first month of MBBS, or before.</b> Six hours is one weekend. Nobody '
      'in your year will have it, and it converts &ldquo;I am interested in research&rdquo; into '
      'something a person running a study can act on. One honest caveat: it is written to US '
      'federal regulations, so it is not an Indian regulatory qualification &mdash; it is the '
      'international standard the Indian rules are modelled on, and it is recognised as training, '
      'not as a licence.',
 conf='verified', checked='2026-09-07',
 tags=['free', 'online', 'certificate', 'no deadline', 'clinical research', 'one weekend'],
))

# ============================ PUBLISHING ====================================
# The other empty category. It was empty because ijms.info refused the
# connection - twice, and in a browser too. It turned out the WWW subdomain is
# the broken one and the bare domain works. Checking the host, not just the URL,
# is what unblocked an entire category.

PASSES.append(dict(
 id='ijms', cat='publish', domain='med',
 name='International Journal of Medical Students',
 host='International Journal of Medical Students', platform='ijms.info',
 url='https://ijms.info/',
 blurb='A peer-reviewed journal, running since 2009, that exists specifically so that medical '
       'students can publish. Diamond open access: free to publish and free to read.',
 mark='<b>A byline in a peer-reviewed, indexed journal.</b> The single most durable thing on this '
      'entire wall &mdash; it is citable, permanent, and it is yours.',
 fmt='remote', location='Online, international',
 travel='None.',
 fee='Free, both ways. Printed literally: <b>no submission fees, no article processing charges and '
     'no publication fees.</b> It calls itself Diamond Open Access, which means neither the author '
     'nor the reader pays.',
 commit='As long as the work takes. A case report is weeks; original research is months.',
 eligible='Printed literally: every submission must include at least one author who is '
          '&ldquo;a current medical student enrolled in a recognized primary medical-degree '
          'program; or a physician within three years of medical-school graduation.&rdquo; '
          'Co-authors need not be. It also states that a student <b>cannot be added to a paper '
          'purely to satisfy this</b> &mdash; the qualifying author must have genuinely contributed.',
 apply='Through the journal&rsquo;s online submission system, with a separate title page and a '
       'masked manuscript.',
 starts='', starts_text='Whenever you have something. Submissions are accepted year-round.',
 deadline='', deadline_text='No deadline. Rolling submission, no issue cut-offs.',
 precision='none',
 extra='Accepted types include original research, case reports, narrative and systematic reviews, '
       'editorials, experience articles, letters and meeting abstracts. <b>A letter to the editor '
       'or an experience article is a realistic first publication</b> in a way that original '
       'research is not.',
 why='You are about to become exactly the person this journal was built for, it costs nothing at '
     'either end, and it takes submissions every day of the year. There is no cohort to be selected '
     'into and no window to miss &mdash; the only gate is having something to say.',
 view='Read three published articles here before you write anything, and start with the smallest '
      'form rather than the largest: a letter or an experience article, not a research paper you do '
      'not yet have the data for. The honest caveat is that a student journal carries less weight '
      'than a specialty journal, and I have rated its prestige accordingly &mdash; <b>but a real '
      'byline beats an imagined better one</b>, and the skill of getting through peer review once '
      'is what makes the second time possible.',
 conf='verified', checked='2026-09-04',
 tags=['free', 'online', 'no deadline', 'byline', 'medical students only', 'diamond open access'],
))

PASSES.append(dict(
 id='cureus', cat='publish', domain='med',
 name='Cureus Journal of Medical Science',
 host='Cureus, backed by Springer Nature', platform='cureus.com',
 url='https://www.cureus.com/',
 blurb='A peer-reviewed medical journal built around fast, low-cost publishing, with case reports '
       'as a first-class article type rather than an afterthought.',
 mark='A peer-reviewed publication with a DOI, in a journal backed by Springer Nature.',
 fmt='remote', location='Online, international',
 travel='None.',
 fee='<b>Not free, and the exact terms are unconfirmed.</b> The home page states &ldquo;the average '
     'cost to publish peer-reviewed research is only $400, rather than thousands of dollars. And '
     'nearly one-third of authors publish for free!&rdquo; <b>I could not open the pricing or '
     'author-guide pages</b> &mdash; both returned 403 to a fetcher and the domain is blocked to my '
     'browser &mdash; so what makes an article free is unknown to me. Read it yourself before '
     'submitting.',
 commit='Weeks, for a case report.',
 eligible='Not stated on the pages I could reach. Unlike IJMS it is not a student journal, so there '
          'is no student requirement and no student guarantee either.',
 apply='Through their online submission system.',
 starts='', starts_text='Whenever you have something.',
 deadline='', deadline_text='No deadline. Rolling submission.',
 precision='none',
 why='It is the other realistic route to a first publication, and it takes case reports seriously '
     '&mdash; which matters, because a case report is the one kind of paper a junior clinical '
     'student can genuinely contribute to.',
 view='<b>Second choice behind IJMS, and only because of the fee.</b> IJMS costs nothing and was '
      'built for you; this one has a price I could not pin down. Keep it for the case where IJMS '
      'declines something, or where a supervisor already publishes here. And note the criticism '
      'honestly, since you will hear it: Cureus is sometimes described as publishing too easily. '
      'It is peer-reviewed and Springer-backed, and it is still not the same as a specialty journal.',
 conf='listing', checked='2026-09-04',
 tags=['online', 'no deadline', 'byline', 'case reports', 'fee unconfirmed'],
))

# ============================ MENTORSHIP ====================================
# The third empty category. SPAR was doing half of this job from the fellowship
# shelf; this is the half where the product is simply a person who talks to you.

PASSES.append(dict(
 id='eighty-thousand-hours-advising', cat='mentor', domain='open',
 name='80,000 Hours one-to-one advising',
 host='80,000 Hours', platform='80000hours.org',
 url='https://80000hours.org/speak-with-us/',
 blurb='A free video call with an adviser whose whole job is helping people choose what to do with '
       'their working life, aimed at people trying to pick high-impact directions.',
 mark='An hour with somebody who has had this conversation a thousand times, plus the introductions '
      'that come out of it. No certificate &mdash; the output is a decision.',
 fmt='remote', location='Video call, anywhere in the world',
 travel='None.',
 fee='Free. Printed literally: &ldquo;Our donors cover the cost of this service because they see it '
     'as an opportunity for impact.&rdquo;',
 commit='An application form, then a call.',
 eligible='Students are named explicitly: &ldquo;We speak with people at a wide range of different '
          'points in their career, including students.&rdquo; No geographic restriction is printed. '
          'They add that they &ldquo;especially encourage people from underrepresented backgrounds '
          'to apply&rdquo;. <b>They do select</b> &mdash; not everyone who applies gets a call.',
 apply='An online application. Printed literally: &ldquo;We usually get back to people within about '
       'two weeks of applying.&rdquo;',
 starts='', starts_text='Whenever they get back to you.',
 deadline='', deadline_text='No deadline. Applications are reviewed on a rolling basis.',
 precision='none',
 why='You are eighteen, holding a medical degree and a data science degree at once, and trying to '
     'work out what that combination is for. That is precisely the question this service exists to '
     'be asked, it is free, and there is no window to miss.',
 view='Worth an application, with one caveat you should go in knowing: they are explicitly oriented '
      'towards a particular set of problems, artificial intelligence risk chief among them, so the '
      'advice comes with a worldview attached. <b>Take it as one strong opinion rather than as '
      'career guidance in general.</b> Apply when you can answer &ldquo;what are you actually '
      'trying to decide&rdquo; in two sentences &mdash; a vague application gets a vague call.',
 conf='verified', checked='2026-09-04',
 tags=['free', 'remote', 'no deadline', 'one to one', 'they select'],
))

# ============================ AND ONE MORE TALK =============================

PASSES.append(dict(
 id='iisc-open-day', cat='lecture', domain='research',
 name='IISc Open Day',
 host='Indian Institute of Science', platform='openday.iisc.ac.in',
 url='https://openday.iisc.ac.in/',
 blurb='One Saturday a year the whole of IISc opens its labs to the public &mdash; demonstrations, '
       'popular lectures, poster sessions and quizzes across every department.',
 mark='Nothing formal. A day inside India&rsquo;s best-known research institute, talking to the '
      'people who work in it.',
 fmt='in-person', location='IISc campus, Bengaluru',
 travel='Bengaluru, one Saturday.',
 fee='Free. Printed literally: &ldquo;Entry to the Open Day at IISc is free.&rdquo;',
 commit='One day, 9:00 am to 5:00 pm.',
 eligible='Open to everyone. The page describes it as being for &ldquo;students, science and '
          'technology enthusiasts, and the public&rdquo;.',
 apply='The site carries a registration link. Whether registration is compulsory is Not stated.',
 starts='', starts_text='The 2026 Open Day was <b>Saturday 7 March 2026</b>, 9am&ndash;5pm. That has '
        'passed; it is an annual fixture, so the next one should fall in early March 2027. <b>The '
        '2027 date is Not stated yet.</b>',
 deadline='', deadline_text='No deadline. You turn up.',
 precision='recurring', recurring=True,
 why='It is the single cheapest way to stand inside a research institute and ask people what they '
     'actually do all day &mdash; free, public, no application. You said you want to go to science '
     'fests in Bengaluru; this is the biggest one there is.',
 view='Nothing to do today &mdash; the 2026 one has gone. It is on the wall because it is annual '
      'and early March, and because a day of this is worth more to a decision about research than '
      'any amount of reading about it. If you are in Bengaluru in March, go. Check the site in '
      'January for the 2027 date.',
 conf='verified', checked='2026-09-04',
 tags=['bengaluru', 'free', 'annual', 'walk in', 'public'],
))


PASSES.append(dict(
 id='wcmsr', cat='conf', domain='med',
 name='World Conference of Medical Student Research (WCMSR)',
 host='International Journal of Medical Students', platform='ijms.info',
 url='https://ijms.info/IJMS/announcement',
 blurb='A two-day international research conference run by and for medical students, held entirely '
       'online and livestreamed, with an open call for abstracts.',
 mark='<b>A presented abstract</b> if you submit one &mdash; which is a citable line and the '
      'shortest real route from &ldquo;I did a small project&rdquo; to something on paper. If you '
      'only attend, nothing, and that is still worth two days.',
 fmt='remote', location='Fully virtual, livestreamed on the IJMS YouTube channel',
 travel='None whatsoever.',
 fee='Free. Printed literally: the conference is &ldquo;free for everyone&rdquo;, and '
     '&ldquo;Attendance is open to everyone, and no registration fee is required.&rdquo;',
 commit='Two days to attend. Months, if you are preparing an abstract.',
 eligible='<b>To attend: anyone.</b> To present, printed literally: &ldquo;At least one author must '
          'be a current medical student or a physician within three years of graduation&rdquo;, '
          'satisfying ICMJE authorship criteria and holding an ORCID.',
 apply='Nothing at all to attend &mdash; you watch the livestream. To present, you submit an '
       'abstract before the deadline. They take &ldquo;original research across a broad range of '
       'disciplines, including clinical medicine, surgery, public health, medical education, and '
       'basic sciences&rdquo;, and the accepted designs include observational and interventional '
       'studies, case reports and meta-analyses.',
 starts='', starts_text='The 2026 conference ran 11&ndash;12 July 2026 and has passed. It is annual; '
        'the 2027 dates are Not stated yet.',
 deadline='', deadline_text='Abstract submission for the 2026 edition closed on 10 May 2026 &mdash; '
          'about two months before the conference. Expect a similar gap in 2027, but <b>no 2027 '
          'date has been invented here.</b>',
 precision='recurring', recurring=True,
 extra='It is run by the same people as the International Journal of Medical Students, which is '
       'also on this wall. The two together are the most complete route from a small project to a '
       'byline that exists for someone at your stage, and both cost nothing.',
 why='A research conference where the entire premise is that the researchers are medical students, '
     'free, online, and it accepts case reports &mdash; the one study design a junior student can '
     'realistically contribute to. Attendance needs nothing but a link.',
 view='Two separate actions, and do not confuse them. <b>Attending costs you nothing and needs no '
      'permission</b> &mdash; find the 2026 recordings on their YouTube channel this month and '
      'watch an hour, because seeing what a medical student actually presents will calibrate you '
      'better than any advice I can give. <b>Presenting is the 2027 goal</b>, and it needs an '
      'abstract by roughly May, which means having a project by about February. That is a real, '
      'dated path, and it is the most concrete one on this page.',
 conf='verified', checked='2026-09-04',
 tags=['free', 'remote', 'annual', 'medical students', 'abstract', 'attend for nothing'],
))


PASSES.append(dict(
 id='khorana', cat='fellowship', domain='med',
 name='Khorana Program for Scholars',
 host='Indo-U.S. Science and Technology Forum (IUSSTF), with WINStep Forward',
 platform='iusstf.org', url='https://iusstf.org/khorana-program-for-scholars',
 blurb='Ten to twelve weeks of research at a leading American university, over the summer, with '
       'flights, a stipend and health insurance paid.',
 mark='A summer of research at a US university, funded, with a named supervisor there. <b>There is '
      'nothing else on this wall that carries this much weight.</b>',
 fmt='in-person', location='A leading university in the United States',
 travel='Round-trip airfare is paid. The page lists what is covered as &ldquo;Round-trip Airfare&rdquo;, '
        '&ldquo;Stipend&rdquo; and &ldquo;Health Insurance&rdquo;. Amounts are Not stated on the page.',
 fee='Free to apply.',
 commit='Printed literally: &ldquo;10-12 weeks&rdquo; over the summer.',
 eligible='<b>MBBS is named in the eligibility list</b>, and so is the year rule that excludes you '
          'today. Printed literally: &ldquo;Pre-final year students enrolled in B. Tech., M. Tech., '
          'B.Sc., M.Sc., B.E., M.E., M.S., Integrated B. S-M.S., B.V. Sc., M.V. Sc., B. Pharm., '
          'M. Pharm., <b>MBBS.</b>, and Master in Medical Science and Technology (MMST)&rdquo; in '
          'biotechnology and allied fields. And then: <b>&ldquo;First Year, Final year and PhD '
          'students are NOT eligible to apply.&rdquo;</b>',
 apply='Online, through the IUSSTF application portal for visitation programmes.',
 starts='', starts_text='The summer following the application, for ten to twelve weeks.',
 deadline='', deadline_text='The page currently describes the summer 2025 cycle, whose submission '
          'deadline it prints as <b>7 October 2024</b>. So the window is roughly late September to '
          'early October each year. <b>No date for your cycle has been invented here</b> - check the '
          'site each September.',
 precision='recurring', recurring=True,
 extra='Its sister programme, the <b>S.N. Bose Scholars Program</b>, is NOT for you and I checked so '
       'you do not have to: its disciplines are &ldquo;Atmospheric and Earth Sciences; Chemical '
       'Sciences; Engineering Sciences; Mathematical and Computational Sciences; and, Physical '
       'Sciences&rdquo;, it directs medical and biology students to Khorana instead, and its '
       'implementing partner&rsquo;s page says the programme is currently on hold.',
 why='It is the most prestigious thing an Indian medical undergraduate can realistically aim at, it '
     'pays for everything including the flight, and its own eligibility list contains the letters '
     'MBBS. It was the one real gap left on this wall.',
 view='<b>You cannot apply this year, and the page says so in as many words: first-year students are '
      'not eligible.</b> That is not a reason to leave it off - it is a reason to know about it now, '
      'because it wants a <i>pre-final year</i> student, which means the application you eventually '
      'send will be judged on research you started years earlier. The things that make this winnable '
      'are the ones already on this wall: the JNCASR fellowship, a byline in IJMS, the GCP '
      'certificate. Treat Khorana as the thing they add up to, and check iusstf.org every September.',
 conf='verified', checked='2026-09-04',
 tags=['annual', 'funded', 'usa', 'mbbs named', 'not first year', 'the long game'],
))


# ---- added 4 September 2026, by the sweep of the four "unreachable" sources.
# Both of these come from pages that had been marked unopened on a WRONG URL.

PASSES.append(dict(
 id='iscb-student-member', cat='member', domain='ai',
 name='ISCB Student Membership',
 host='International Society for Computational Biology',
 platform='iscb.org membership details',
 url='https://www.iscb.org/membership-details/individual-membership-details',
 blurb='Student membership of the international society for computational biology &mdash; the '
       'field where your data science degree and your medicine stop being two separate things.',
 mark='A named society membership, a travel-fellowship route to real conferences, and the member '
      'directory of the field. Small, cheap, and permanently open.',
 fmt='remote', location='Online. The society is international and membership is not tied to a place.',
 travel='None to join. Membership is what makes the travel fellowships available, not the reverse.',
 fee='15 USD a year. The page prices by country income band and prints the student tiers '
     'literally: &ldquo;Student - SH&rdquo; studying in a High Income Country is 50 USD, '
     '&ldquo;Student - SUM&rdquo; Upper-Middle is 25 USD, &ldquo;Student - SLM&rdquo; '
     '&ldquo;studying in a Lower-Middle Income Country based on ranking of economies&rdquo; is '
     '<b>15 USD</b>, and Low Income is 5 USD. <b>The page does not name India.</b> It asks you to '
     'use its own dues calculator; India is a World Bank lower-middle-income economy, so SLM is '
     'the band that should apply &mdash; confirm it on the calculator before paying.',
 commit='None. It is a subscription, not a programme. You join and you are a member.',
 eligible='Printed literally: &ldquo;Student memberships are available to all full-time students.&rdquo; '
          'No discipline, degree or country bar is printed, and nothing on the page requires you to '
          'already work in computational biology.',
 apply='Online through the membership pages. You pick your tier, pay the dues, and you are in.',
 starts='', starts_text='Whenever you join. Membership runs a year from that day.',
 deadline='', deadline_text='No deadline. Membership is open all year.',
 precision='none',
 why='It is the cheapest real credential-adjacent thing on this wall, and it sits exactly on the '
     'seam you are actually walking &mdash; medicine on one side, the IIT Madras data science '
     'degree on the other. Computational biology is the discipline that already joined them.',
 view='Fifteen dollars is about the price of two coffees, so the question is not the money, it is '
      'whether you would use it. The parts worth having are real: <b>travel fellowships to ISCB '
      'conferences, ECCB, PSB and RECOMB</b>, at least 10 per cent off affiliated conferences and '
      'up to 200 USD off the society&rsquo;s own, plus the member directory and ISCB TV. The '
      'discounts on publishing fees are for people already publishing and are not for you yet. '
      '<b>Join it the year you first want to go to a conference, not before</b> &mdash; a '
      'membership held for its own sake teaches nothing, and this one renews annually whether it '
      'is used or not. One honest caveat: the page&rsquo;s most recent visible year is 2022, so '
      'check the dues calculator rather than trusting these figures.',
 conf='verified', checked='2026-09-04',
 tags=['computational biology', 'membership', 'cheap', 'travel fellowships', 'global'],
))

PASSES.append(dict(
 id='iiser-pune-sspc', cat='fellowship', domain='research',
 name='IISER Pune Summer Student Programme',
 host='Indian Institute of Science Education and Research, Pune',
 platform='IISER Pune summer student programme portal',
 url='https://www.iiserpune.ac.in/SummerStudentProgrammes',
 blurb='Four to eight weeks of summer research at IISER Pune with a faculty member, for students '
       'who are not from IISER Pune. Runs every summer; applications open in the winter before it.',
 mark='A summer inside a working research group at a national institute, with a free hostel room '
      'and a supervisor who has watched you work.',
 fmt='in-person', location='IISER Pune campus, Pashan, Pune',
 travel='Pune, for four to eight weeks. The programme page prints '
        '&ldquo;IISER-Pune will support the selected summer students with a (free) room in the '
        'students&rsquo; hostel&rdquo;, and then, plainly, &ldquo;However, we are unable to provide '
        'any financial support to cover the cost of travel and boarding in the hostel mess (about '
        'Rs. 6000 per month)&rdquo;. <b>So the room is free and the food and the fare are not.</b>',
 fee='Free to apply &mdash; no application fee is printed anywhere on the programme page. '
     '<b>Attending is not free.</b> The room is given, and the page puts the mess bill at about '
     'Rs. 6000 a month, with your travel on top; both are yours to pay.',
 commit='Printed literally: &ldquo;4-8 weeks during the period May 15th &ndash; July 21st&rdquo;.',
 eligible='Printed literally: applicants must be in the &ldquo;2nd, 3rd, or 4th year of '
          'B.Sc/B.Tech/B.E or equivalent&rdquo; or the &ldquo;1st year of M.Sc/M.Tech or '
          'equivalent&rdquo;, with &ldquo;minimum 60% (or equivalent) in overall grades, or 80% in '
          'the particular stream(s) of interest&rdquo;. The form is '
          '&ldquo;strictly for non-IISER Pune students&rdquo;, and students already selected '
          'through IASc or JNCASR fellowships are not eligible by this route. '
          '<b>MBBS is not named, and the page never defines what &ldquo;or equivalent&rdquo; '
          'means.</b> That is the whole question for you and it is not answered on the page.',
 apply='Online, through the summer programme portal, in the application window that opens in the '
       'winter. You name the disciplines you want to work in.',
 starts='', starts_text='Four to eight weeks between 15 May and 21 July, dates set with your guide.',
 deadline='', deadline_text='<b>The 2026 round is over</b> &mdash; it took applications through '
          'February 2026 and its selection is complete. The next round, SSPC-2027, should open '
          'around <b>February 2027</b>; the exact date is Not stated yet.',
 precision='recurring', recurring=True,
 why='It is a third annual summer-research door, alongside the Science Academies fellowship and '
     'JNCASR, and the three do not open at the same moment &mdash; so knowing all three is how you '
     'stop a February from passing you by. This one asks for no letter of recommendation on the '
     'form and gives you a free room, which makes it the least gatekept of the three.',
 view='<b>Read the eligibility line before you get attached to this one.</b> It asks for the 2nd, '
      '3rd or 4th year of a B.Sc, B.Tech or B.E, and MBBS is not in that list. There are two '
      'honest readings and I am not going to pretend I know which is right: either &ldquo;or '
      'equivalent&rdquo; covers a medical degree, or it does not. <b>The IIT Madras BS in Data '
      'Science is the more interesting angle</b> &mdash; that is literally a B.S., and if you are '
      'in its second year by February 2027 you meet the letter of the rule through that degree '
      'rather than through medicine. <b>Write and ask them, in December, before the form opens.</b> '
      'One email settles it, and the answer is worth having whichever way it goes. Note also that '
      'holding an IASc or JNCASR fellowship disqualifies you here, so these are alternatives, not '
      'a portfolio to apply to all at once.',
 conf='verified', checked='2026-09-04',
 tags=['annual', 'pune', 'summer research', 'free accommodation', 'eligibility unclear'],
 stretch=True,
))
