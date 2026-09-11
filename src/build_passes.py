# -*- coding: utf-8 -*-
"""passdata.py -> passes.html, THE PASS WALL.

The bill wall's sibling, on his instruction of 4 September 2026: same design
world, its own page, its own URL.

WHY IT LOOKS LIKE THIS

The bill wall is a hoarding of fly-posted bills, because its wound is a notice
he did not see in time. This page is the SAME hoarding, but what is pinned to it
is not bills - it is the things people pin up next to bills: ticket stubs,
enrolment slips, admission cards, certificates, membership cards, staff passes,
a cheque stub, a handbill with no date on it at all.

That choice is not decoration. It is the answer to the one design constraint he
was given, in diary 0004:

    A bill that never expires is a bill that trains you to ignore bills.

Five of the thirteen categories have NO deadline. If they wore the same object as
the ones closing this week, the wall would teach him to stop reading it. So each
category is a different physical object, and the five undated ones never weather,
never fade and never carry a countdown.

TWO CLOCKS, NOT ONE
`deadline` is when you must APPLY. `starts` is when the thing HAPPENS. A talk has
the second and not the first; a fellowship has the first and its dates come much
later. The face of the card says which clock it is running on, in different words
for each, because collapsing them is how a wall states something false.

PERFORMANCE, inherited from the other wall's mistakes and not re-learned here:
no background-attachment:fixed, no backdrop-filter, no per-card CSS filter, no
mix-blend-mode, no content-visibility. The static per-card tilt stays - it was
measured at 0.03ms on the other wall and removing it on suspicion was a loss.
"""
import io, os, sys, re, html, datetime, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import passdata as D

OUT = os.path.join(HERE, 'passes.html')
TODAY = datetime.date.fromisoformat(D.TODAY)

# REFUSE TO BAKE A STALE COUNTDOWN BASELINE - see the long note in build.py.
# This is the wall the bug was actually FOUND on: passdata.TODAY sat at
# 2026-09-04 until 10 September, so the EMBO-IndiaBioscience course, which
# closed on the 8th, baked as "4 days" and was lifted into the
# closing-within-the-week banner as the one thing about to shut.
_real = datetime.date.today()
if TODAY != _real:
    sys.exit(
        'REFUSING TO BUILD: passdata.py TODAY is %s but today is %s (%+d days).\n'
        '  Set passdata.py TODAY = %r and build again. DO NOT touch READ_ON (%s).'
        % (TODAY, _real, (TODAY - _real).days, _real.isoformat(), D.READ_ON))


def esc(s):
    """Element content. Quotes are deliberately left alone: values are authored
    HTML carrying entities, and escaping them would print the entity."""
    return html.escape(str(s), quote=False)


def attr(s):
    """Inside a quoted attribute, quotes MUST be escaped or one stray double
    quote closes the attribute early and takes the card down silently.

    It also folds every non-ASCII character to a numeric reference. Attribute
    values here are built with html.unescape() - the search haystack and the
    title tooltips both decode the entities the data is written in - so without
    this fold, six literal curly quotes and dashes ended up inside attributes.
    They rendered correctly on the deployed artifact, because the host supplies
    a charset meta, and turned to mojibake the moment the same file was served
    from anywhere that did not. Entities make the page self-describing.
    """
    s = html.escape(str(s), quote=True)
    return ''.join(c if ord(c) < 128 else '&#%d;' % ord(c) for c in s)


def tilt(eid):
    h = int(hashlib.md5(eid.encode()).hexdigest()[:8], 16)
    return round(((h % 200) - 100) / 100 * 1.3, 2)


MONTH = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split()


def pretty(iso):
    y, m, d = iso.split('-')
    return '%d %s %s' % (int(d), MONTH[int(m) - 1], y)


def clock(e):
    """Which clock is this entry running on, and how much of it is left?

    Returns (days, state, kind). `kind` is the thing the three-objects rule is
    about: 'apply' means there is a form and a closing date, 'happens' means it
    simply occurs on a day, 'open' means neither and it never expires.
    """
    if e['precision'] == 'recurring':
        return None, 'returns', 'returns'
    if e['deadline']:
        d = (datetime.date.fromisoformat(e['deadline']) - TODAY).days
        kind = 'apply'
    elif e['starts']:
        d = (datetime.date.fromisoformat(e['starts']) - TODAY).days
        kind = 'happens'
    else:
        return None, 'open', 'open'
    if d < 0:
        return d, 'gone', kind
    if d <= 7:
        return d, 'lastcall', kind
    if d <= 30:
        return d, 'settling', kind
    return d, 'fresh', kind


# Two vocabularies, on purpose. "CLOSES IN" and "HAPPENS IN" are different
# statements and a wall that says the first about the second is lying.
STAMP = {
 ('apply', 'fresh'):    'OPEN &middot; APPLY',
 ('apply', 'settling'): 'CLOSING',
 ('apply', 'lastcall'): 'LAST CALL',
 ('apply', 'gone'):     'CLOSED',
 ('happens', 'fresh'):    'UPCOMING',
 ('happens', 'settling'): 'THIS MONTH',
 ('happens', 'lastcall'): 'THIS WEEK',
 ('happens', 'gone'):     'PASSED',
 ('open', 'open'):        'ALWAYS OPEN',
 ('returns', 'returns'):  'COMES ROUND',
}

CONF = {
 'verified': ('VERIFIED AT SOURCE',
              'I opened this thing&rsquo;s own page and read these fields off it.'),
 'listing':  ('FROM A LISTING',
              'Taken from a listing page, not the thing&rsquo;s own page. Anything the listing did '
              'not print is marked in red inside.'),
 'stale':    ('NOT RE-CHECKED',
              'Carried from an earlier pass and not confirmed today.'),
}

UNCERTAIN = ('not stated', 'unconfirmed', 'unknown', 'not printed', 'could not look',
             'could not read', 'could not confirm', 'not chased', 'status unconfirmed',
             'behind a login', 'behind a sign-in', 'not been done', 'my reading')

CASHY = re.compile(r'[$€£₹]|&euro;|&pound;|&#8377;')


def uncertain(v):
    return any(t in str(v).lower() for t in UNCERTAIN)


def _visible_trim(v, n):
    """Cut authored HTML to n VISIBLE characters without ever splitting a tag
    or an entity, and close anything still open.

    Values on these walls are authored HTML: they carry &mdash;, &#8377; and
    deliberate <b> emphasis. Counting raw characters cuts through all three.
    This walks the string, charging one unit per rendered character, passing
    tags and entities through whole, and appends the closing tags for any
    elements left open at the cut. Returns (html, was_trimmed).
    """
    out, stack, vis, i, L = [], [], 0, 0, len(v)
    while i < L and vis < n:
        c = v[i]
        if c == '<':
            j = v.find('>', i)
            if j == -1:
                break
            tag = v[i:j + 1]
            m = re.match(r'</\s*([A-Za-z0-9]+)', tag)
            if m:
                name = m.group(1).lower()
                if name in stack:
                    while stack and stack.pop() != name:
                        pass
            else:
                m2 = re.match(r'<\s*([A-Za-z0-9]+)', tag)
                if m2 and not tag.rstrip().endswith('/>'):
                    stack.append(m2.group(1).lower())
            out.append(tag)
            i = j + 1
            continue
        if c == '&':
            j = v.find(';', i)
            if j != -1 and 0 < j - i <= 9:
                out.append(v[i:j + 1])
                i = j + 1
                vis += 1
                continue
        out.append(c)
        i += 1
        vis += 1
    trimmed = i < L
    s = ''.join(out)
    if trimmed:
        # Back off to the last space in the trailing TEXT run, so the cut lands
        # between words rather than mid-word. Never touch anything before the
        # last '>' - that would reopen the very hole this function closes.
        tail_from = s.rfind('>') + 1
        sp = s.rfind(' ', tail_from)
        if sp > tail_from:
            s = s[:sp]
        s = s.rstrip(' ,;:-') + '&hellip;'
    for name in reversed(stack):
        s += '</%s>' % name
    return s, trimmed


def short(value, n=86):
    """Trim for the FACE. A trimmed value must never READ as complete, and
    it must never be BROKEN HTML - see _visible_trim for why that matters.
    The full text is carried in the title attribute and printed in the sheet."""
    return _visible_trim(str(value).strip(), n)


def field(label, value):
    if value is None or str(value).strip() == '':
        return ('<div class="f uncertain"><dt>%s</dt><dd><span class="unk">not stated on the '
                'source</span></dd></div>' % esc(label))
    v = str(value)
    cls = ''
    if uncertain(v):
        v, cls = '<span class="unk">%s</span>' % v, ' uncertain'
    return '<div class="f%s"><dt>%s</dt><dd>%s</dd></div>' % (cls, esc(label), v)


def faceline(label, value):
    if value is None or str(value).strip() == '':
        return '<b>%s</b><span class="unk">not stated</span>' % esc(label)
    full, trimmed = short(value, 64)
    cls = ' class="unk"' if uncertain(value) else ''
    title = ' title="%s"' % attr(html.unescape(str(value))) if trimmed else ''
    return '<b>%s</b><span%s%s>%s</span>' % (esc(label), cls, title, full)


# ---------------------------------------------------------------- order
#
# Default is MOST RUNWAY LEFT, exactly as on the bill wall, and for the same
# reason: a deadline-first default is the thing that caused this whole project.
# There is deliberately no "closing soonest" order. Instead the things closing
# within a week get their own banner at the top, which surfaces the urgency
# without making urgency the lens.

entries = []
for e in D.ENTRIES:
    days, state, kind = clock(e)
    entries.append(dict(e, _days=days, _state=state, _kind=kind))

RANK = {'fresh': 0, 'settling': 1, 'lastcall': 2, 'open': 3, 'returns': 4, 'gone': 5}
entries.sort(key=lambda e: (RANK[e['_state']], -(e['_days'] if e['_days'] is not None else 0)))

cards = []
for order_index, e in enumerate(entries):
    days, state, kind = e['_days'], e['_state'], e['_kind']

    if kind == 'open':
        rt = 'no deadline, ever'
    elif kind == 'returns':
        rt = 'annual &mdash; the window comes round'
    elif days < 0:
        rt = ('closed %d days ago' if kind == 'apply' else 'was %d days ago') % abs(days)
    elif days == 0:
        rt = 'closes today' if kind == 'apply' else 'today'
    else:
        unit = 'day' if days == 1 else 'days'
        rt = ('%d %s to apply' if kind == 'apply' else 'in %d %s') % (days, unit)

    cat = D.CATS[e['cat']]
    fmt_word = {'remote': 'Remote', 'in-person': 'In person', 'hybrid': 'Hybrid'}[e['fmt']]
    free = e['fee'].lower().startswith(('free', 'no fee', 'none', 'no cost'))

    if free:
        fee_chip = '<i class="c-free">Free</i>'
    elif uncertain(e['fee']):
        fee_chip = '<i class="c-nofee">Cost not stated</i>'
    else:
        fee_chip = '<i class="c-paid">Costs something</i>'
    chips = ['<i class="c-%s">%s</i>' % (e['fmt'], fmt_word), fee_chip]
    if e.get('stretch'):
        chips.append('<i class="c-stretch">Above you, for now</i>')
    if e.get('recurring'):
        chips.append('<i class="c-annual">Annual</i>')

    # The MARK band. On the bill wall this slot holds the prize, because the
    # question there is "what do I win". Here the question is "what does this
    # leave behind that somebody else can see", so it holds what you walk away
    # with - and when the honest answer is "nothing", it says nothing.
    mark_full, mark_trim = short(e['mark'], 104)
    mark = ('<p class="mark"><b>What you walk away with</b><span%s%s>%s</span></p>' % (
        ' class="unk"' if uncertain(e['mark']) else '',
        ' title="%s"' % attr(html.unescape(str(e['mark']))) if mark_trim else '',
        mark_full))

    # The facts strip. The FIRST line differs by clock, which is the whole
    # three-objects idea made visible on the face of the card.
    if kind == 'apply':
        first = faceline('Apply by', pretty(e['deadline']))
    elif kind == 'happens':
        first = faceline('Happens', e['starts_text'])
    elif kind == 'returns':
        first = faceline('Window', 'Shut &mdash; comes round each year')
    else:
        first = '<b>Deadline</b><span class="always">None. Open whenever you are.</span>'

    facts = '<div class="facts">%s%s%s</div>' % (
        first, faceline('Who', e['eligible']), faceline('Time', e['commit']))

    def pips(n):
        return ''.join('<i class="%s"></i>' % ('on' if i < n else '') for i in range(5))

    stand = ('<p class="stand"><b>My rating</b>'
             '<span>Prestige<span class="pips">%s</span></span>'
             '<span>Worth learning from<span class="pips">%s</span></span></p>'
             % (pips(e['prestige']), pips(e['learning'])))

    sheet = ''.join([
        field('What it actually is', '%s &mdash; %s' % (cat['label'], cat['note'])),
        field('Who runs it', e['host']),
        field('Where I found it', e['platform']),
        field('Remote or in person', '%s &mdash; %s' % (fmt_word, e['location'])),
        field('Travel', e['travel']),
        field('Cost', e['fee']),
        field('Time it takes', e['commit']),
        field('Who may take part', e['eligible']),
        field('How you get in', e['apply']),
        field('When it happens', e['starts_text']),
        field('Application deadline', e['deadline_text']),
        field('What you walk away with', e['mark']),
    ] + ([field('Also worth knowing', e['extra'])] if e.get('extra') else []))

    gaps = sum(1 for t in (e['fee'], e['eligible'], e['apply'], e['commit'], e['deadline_text'])
               if uncertain(t))

    prec = {
     'exact':     'This date was printed as a date on the thing&rsquo;s own page.',
     'listing':   'This date came from a listing page, not the thing&rsquo;s own page.',
     'recurring': 'This cycle has closed. The next window is described in the words the source '
                  'used, and no date has been invented for it.',
     'none':      'No application deadline is stated anywhere I could reach.',
    }[e['precision']]

    th, (cflag, ctip) = e['theme'], CONF[e['conf']]
    city = 'bengaluru' if 'bengaluru' in e['tags'] else ''

    cards.append("""
<article class="pass %(treat)s s-%(state)s k-%(kind)s" data-id="%(id)s" data-cat="%(cat)s"
  data-dom="%(dom)s" data-fmt="%(fmt)s" data-fee="%(feec)s" data-state="%(state)s"
  data-kind="%(kind)s" data-conf="%(conf)s" data-city="%(city)s"
  data-days="%(days)s" data-deadline="%(iso)s" data-starts="%(isos)s"
  data-pr="%(pr)s" data-le="%(le)s" data-ord="%(ord)s" data-text="%(hay)s" tabindex="0"
  style="--paper:%(paper)s;--pink:%(ink)s;--prule:%(rule)s;--tilt:%(tilt)sdeg">
  <div class="pin" aria-hidden="true"></div>
  <div class="objx" aria-hidden="true"></div>
  <header class="ph">
    <span class="kind">%(catlabel)s</span>
    <span class="state">%(stamp)s</span>
  </header>
  <p class="rw">%(rt)s</p>
  <h3 class="pt">%(name)s</h3>
  <p class="phost">%(host)s &middot; <span>%(platform)s</span></p>
  <p class="pblurb">%(blurb)s</p>
  %(mark)s
  <div class="chips">%(chips)s</div>
  %(facts)s
  %(stand)s
  <div class="mine">
    <p class="why"><b>Why it is on your wall</b>%(why)s</p>
    <p class="view"><b>My view on actually doing it</b>%(view)s</p>
  </div>
  <p class="conf conf-%(conf)s" title="%(ctip)s"><i></i>%(cflag)s%(gapnote)s</p>
  <button class="peel" aria-expanded="false">Read the whole pass</button>
  <div class="sheet" hidden>
    <dl>%(sheet)s</dl>
    <p class="prec">%(prec)s</p>
    <a class="go" href="%(url)s" target="_blank" rel="noopener">Go to the source &rarr;</a>
  </div>
  <div class="tags">%(tags)s</div>
</article>""" % dict(
        treat=th['treatment'], state=state, kind=kind, id=esc(e['id']), cat=e['cat'],
        dom=e['domain'], fmt=e['fmt'], feec='free' if free else 'paid', conf=e['conf'], city=city,
        days=(days if days is not None else 9999),
        iso=e['deadline'], isos=e['starts'],
        pr=e['prestige'], le=e['learning'], ord=order_index,
        paper=th['paper'], ink=th['ink'], rule=th['rule'], tilt=tilt(e['id']),
        # attr(), not esc(): this is an attribute value, and esc() deliberately
        # leaves quotes alone. Decoding the entities first is what makes a search
        # for "peoples" match and a search for "rsquo" not.
        hay=attr(html.unescape(' '.join([e['name'], e['host'], e['blurb'], e['mark'],
                                         e['eligible'], e['platform'], cat['label'],
                                         ' '.join(e['tags'])])).lower()),
        catlabel=esc(cat['label']).upper(), stamp=STAMP[(kind, state)], rt=rt,
        name=e['name'], host=e['host'], platform=e['platform'], blurb=e['blurb'],
        mark=mark, chips=''.join(chips), facts=facts, stand=stand,
        why=e['why'], view=e['view'], cflag=cflag, ctip=ctip,
        gapnote=('<em> &middot; %d field%s never stated</em>' % (gaps, '' if gaps == 1 else 's'))
                if gaps else '',
        sheet=sheet, prec=prec, url=esc(e['url']),
        tags=''.join('<span>%s</span>' % esc(t) for t in e['tags']),
    ))

# ---------------------------------------------------------------- last call
#
# The default order is most-runway-first, which is right and is the point of the
# project. But two things on this wall close within the week, and burying them
# under thirty entries would be the Gujarat failure with better manners. So they
# get a banner instead of a sort order.

soon = [e for e in entries if e['_state'] == 'lastcall' and e['_kind'] == 'apply']
soon.sort(key=lambda e: e['_days'])
rows = ''.join(
    '<li><b>%s day%s</b> <a href="#%s">%s</a> <i>%s</i></li>'
    % (e['_days'], '' if e['_days'] == 1 else 's', esc(e['id']), e['name'],
       pretty(e['deadline']))
    for e in soon)
# ALWAYS emit the section, hidden when empty. The script rebuilds this list from
# the cards on every load, and it can only do that if there is something to
# rebuild into - an omitted section means the banner silently stops working the
# first time the wall is opened on a day when nothing happens to be closing.
lastcall = ('<section class="alarm" id="alarm"%s><h2>Closing within the week</h2>'
            '<p>The wall is ordered by how much runway is left, not by what shuts first '
            '&mdash; that ordering is the whole point of it. These are the exceptions, '
            'lifted out so they cannot sink.</p><ol>%s</ol></section>'
            % ('' if soon else ' hidden', rows))

# ---------------------------------------------------------------- categories
#
# The category map is itself a deliverable: he said he does not know what
# categories exist. So it is printed on the page as a table, not just implied by
# the chips.

catrows = []
for slug, c in sorted(D.CATS.items(), key=lambda kv: kv[1]['label']):
    n = sum(1 for e in entries if e['cat'] == slug)
    catrows.append(
        '<li class="c-%s"><b>%s</b><i>%s</i><span>%s</span><em>%s</em></li>'
        % (slug, esc(c['label']), 'has a clock' if c['dated'] else 'never expires',
           c['note'], '%d here' % n))

catchips = ''.join(
    '<button class="chip cat" data-k="cat" data-v="%s" aria-pressed="false">%s</button>'
    % (slug, esc(c['label']))
    for slug, c in sorted(D.CATS.items(), key=lambda kv: kv[1]['label']))

# Counts written into the prose are DERIVED, never typed. The first build hard-
# coded "thirteen" in four places; the second sweep added three categories and
# every one of those sentences silently became false. A number a human types
# into copy is a number that goes stale the next time the data moves.
NUMWORD = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
           8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
           14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
           19: 'nineteen', 20: 'twenty'}


def numword(n):
    return NUMWORD.get(n, str(n))


N_CATS = len(D.CATS)
N_UNDATED_CATS = sum(1 for c in D.CATS.values() if not c['dated'])
CATWORD = numword(N_CATS)
UNDATEDWORD = numword(N_UNDATED_CATS)
# Deriving a word instead of typing one removes a stale-number bug and
# introduces a grammar one: the mast sentence STARTS with this word, and
# 'eight' shipped lower-case mid-paragraph. Caught by looking at the deployed
# page - a count can be perfectly correct and still read as a typo.
UNDATEDWORD_CAP = UNDATEDWORD[:1].upper() + UNDATEDWORD[1:]

# The lime rail on the category map marks the ones with no clock. Generated from
# the data for the same reason - it was a hand-written selector list and would
# have missed all three new undated categories.
UNDATED_CSS = ',\n'.join('.catmap li.c-%s' % slug
                         for slug, c in sorted(D.CATS.items()) if not c['dated'])
UNDATED_CSS += '{border-left-color:var(--lime)}'

src_rows = []
for s in sorted(D.SOURCES, key=lambda x: (not x['checked'], x['name'])):
    src_rows.append('<li class="%s"><a href="%s" target="_blank" rel="noopener">%s</a>'
                    '<i>%s &middot; %s</i><p>%s</p></li>'
                    % ('read' if s['checked'] else 'unread', esc(s['url']), s['name'],
                       s['kind'], s['region'], s['note']))

n_open = sum(1 for e in entries if e['_state'] == 'open')
n_live = sum(1 for e in entries if e['_state'] in ('fresh', 'settling', 'lastcall', 'open'))
n_ver = sum(1 for e in entries if e['conf'] == 'verified')
n_free = sum(1 for e in entries
             if e['fee'].lower().startswith(('free', 'no fee', 'none', 'no cost')))
n_src_open = sum(1 for s in D.SOURCES if s['checked'])

CSS = r"""
:root{--wall:#26221e;--wall2:#1b1815;--ui:#f4efe6;--ui2:#b6aa99;--ui3:#8a7f72;
  --hot:#e8442f;--lime:#c8f04a;--sky:#6fd3e8;--line:#413a34}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;font-family:"Archivo",system-ui,sans-serif;font-size:16px;line-height:1.5;
  color:var(--ui);background:var(--wall)}
.sky{position:fixed;inset:0;z-index:-1;pointer-events:none;
  background:radial-gradient(120% 70% at 50% 0%,#332e28 0%,var(--wall) 45%,var(--wall2) 100%)}
a{color:inherit}
img{max-width:100%}

/* ---------------------------------------------------------------- masthead */
.mast{padding:34px 20px 16px;text-align:center}
.mast h1{font-family:"Archivo Black",sans-serif;font-size:clamp(32px,8vw,72px);line-height:.92;
  margin:0;letter-spacing:-.02em;text-transform:uppercase;color:#efe9dd;
  text-shadow:3px 3px 0 var(--sky)}
.mast .sub{font-family:"Azeret Mono",monospace;font-size:10px;letter-spacing:.2em;
  text-transform:uppercase;color:var(--ui3);margin:13px 0 0}
.mast .say{max-width:70ch;margin:16px auto 0;color:var(--ui2);font-size:15px}
.mast .say b{color:var(--ui)}
.mast .pol{max-width:78ch;margin:14px auto 0;color:var(--ui3);font-size:12.5px;line-height:1.75}
.sib{display:inline-block;margin-top:14px;font-family:"Azeret Mono",monospace;font-size:11px;
  letter-spacing:.12em;text-transform:uppercase;color:var(--wall);background:var(--lime);
  padding:7px 13px;border-radius:2px;text-decoration:none;font-weight:600}

/* ---------------------------------------------------------------- alarm */
.alarm{max-width:760px;margin:18px auto 0;padding:16px 18px;border:2px solid var(--hot);
  border-radius:3px;background:#2f1f1b}
.alarm h2{font-family:"Archivo Black",sans-serif;font-size:15px;letter-spacing:.06em;
  text-transform:uppercase;margin:0 0 6px;color:#ffb2a4}
.alarm p{margin:0 0 10px;font-size:13px;color:var(--ui2)}
.alarm ol{margin:0;padding-left:20px}
.alarm li{margin:5px 0;font-size:14.5px}
.alarm li b{font-family:"Azeret Mono",monospace;color:var(--hot);font-size:12px}
.alarm li a{font-weight:600}
.alarm li i{color:var(--ui3);font-size:12.5px;font-style:normal}

/* ---------------------------------------------------------------- rail */
/* NOT sticky. Two stacked rails both pinned at top:0 would sit on top of each
   other, and 27 chips is far too much screen to freeze on a phone anyway. */
.rail{display:flex;flex-wrap:wrap;gap:6px;align-items:center;justify-content:center;
  padding:11px 14px;margin:20px 0 4px;background:#221e1a;
  border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.rail.two{margin:0 0 16px;padding-top:0;border-top:0}
.chip:focus-visible,.peel:focus-visible,#q:focus-visible,.sorter select:focus-visible,
.go:focus-visible,.alarm a:focus-visible{outline:3px solid var(--lime);outline-offset:2px}
#q{font:500 13px "Archivo",sans-serif;color:var(--ui);background:#332e29;
  border:1px solid #4b433b;border-radius:2px;padding:7px 11px;min-width:190px}
#q::placeholder{color:var(--ui3)}
.chip{font:600 11.5px "Azeret Mono",monospace;letter-spacing:.06em;text-transform:uppercase;
  color:var(--ui2);background:#332e29;border:1px solid #4b433b;border-radius:2px;
  padding:6px 9px;cursor:pointer}
.chip:hover{color:var(--ui);border-color:#6b6058}
.chip[aria-pressed=true]{background:var(--lime);border-color:var(--lime);color:#1b1815}
.chip.cat[aria-pressed=true]{background:var(--sky);border-color:var(--sky)}
.sorter{display:flex;align-items:center;gap:6px;font:600 11.5px "Azeret Mono",monospace;
  letter-spacing:.06em;text-transform:uppercase;color:var(--ui3)}
.sorter select{font:600 11.5px "Azeret Mono",monospace;color:var(--ui);background:#332e29;
  border:1px solid #4b433b;border-radius:2px;padding:6px 8px}
.count{font:600 11.5px "Azeret Mono",monospace;color:var(--ui3);letter-spacing:.06em}

/* ---------------------------------------------------------------- wall */
/* The BASE state is CSS columns, which renders correctly with no script at all.
   The script switches it to flex columns it fills itself, because CSS columns
   balance column-major - items 1, 11, 21, 31 across the top - which would make
   every sort control look like it worked while mostly not working. Getting this
   the wrong way round would leave 39 cards in a single flex row for anyone whose
   script never ran, and the page's first still frame is what most people see. */
.wall{columns:4 320px;column-gap:20px;padding:6px 20px 40px;max-width:1560px;margin:0 auto}
.wall.flexed{display:flex;columns:auto;align-items:flex-start;gap:20px}
.wall:not(.flexed) .pass{margin-bottom:20px}
.col{flex:1 1 0;min-width:0;display:flex;flex-direction:column;gap:20px}
.nores{text-align:center;color:var(--ui3);padding:30px}
.hide{display:none!important}

/* --------------------------------------------------------- the pass itself */
.pass{position:relative;background:var(--paper);color:var(--pink);border-radius:2px;
  padding:26px 20px 16px;break-inside:avoid;transform:rotate(var(--tilt));
  overflow-wrap:anywhere;will-change:transform;
  transition:transform .16s ease-out,box-shadow .16s ease-out;
  box-shadow:0 2px 0 rgba(0,0,0,.35),0 14px 26px -14px rgba(0,0,0,.7)}
/* Under the cursor the lean straightens and the pass lifts - the same gesture,
   the same .16s ease-out and the same 4px lift as the bill wall, because he
   asked for the two pages to feel alike. It fires on :focus-within too, so it
   is not a mouse-only flourish.
   On the bill wall this was once removed as a suspected cause of lag, measured
   afterwards at 0.03ms, and put back when he noticed its absence within a day.
   Do not remove it again without measuring first. */
.pass:hover,.pass:focus-within{transform:rotate(0deg) translateY(-4px);
  box-shadow:0 2px 0 rgba(0,0,0,.34),0 18px 36px -12px rgba(0,0,0,.75);z-index:5}
.pass:focus-visible{outline:3px solid var(--lime);outline-offset:3px}

/* A pin, not tape. Bills are pasted; passes are pinned up. */
.pin{position:absolute;top:7px;left:50%;width:11px;height:11px;margin-left:-5px;border-radius:50%;
  background:radial-gradient(circle at 34% 30%,#fff 0 14%,var(--hot) 16% 70%,#8d2214 72% 100%);
  box-shadow:0 2px 3px rgba(0,0,0,.4)}

.ph{display:flex;justify-content:space-between;align-items:center;gap:8px;
  font-family:"Azeret Mono",monospace;font-size:9.5px;letter-spacing:.14em;text-transform:uppercase}
.kind{font-weight:600;padding:3px 6px;border:1px solid var(--prule);border-radius:2px;opacity:.8}
.state{font-weight:600;opacity:.9}
.rw{font-family:"Azeret Mono",monospace;font-size:11px;letter-spacing:.05em;margin:8px 0 0;
  opacity:.62}
.pt{font-family:"Archivo Black",sans-serif;font-size:21px;line-height:1.1;margin:6px 0 0;
  letter-spacing:-.01em}
.phost{font-family:"Rokkitt",Georgia,serif;font-size:14px;margin:6px 0 0;opacity:.78}
.phost span{opacity:.7}
.pblurb{font-size:14px;margin:10px 0 0;opacity:.9}

/* The MARK band - this page's answer to the bill wall's REWARD band. */
.mark{margin:14px 0 0;padding:9px 0;border-top:2px solid var(--prule);
  border-bottom:2px solid var(--prule)}
/* DIRECT child only. These label rules used to be `.mark b`, `.mine b`, `.facts b`,
   which also matched every <b> inside a VALUE - and the values are authored HTML
   full of them. The result was the worst kind of bug: it did not break anything,
   it silently swapped the hierarchy. On the IJMS card the real headline ("A byline
   in a peer-reviewed, indexed journal") rendered as an 8px uppercase label and the
   sentence after it rendered as the headline. Found by looking at the page, not by
   any check - no assertion here could have seen it. */
.mark > b{display:block;font-family:"Azeret Mono",monospace;font-size:8.5px;letter-spacing:.18em;
  text-transform:uppercase;opacity:.65;margin-bottom:4px}
.mark span{font-family:"Archivo Black",sans-serif;font-size:15px;line-height:1.25;display:block}
.mark .unk{color:#b3200f;font-style:italic;font-family:"Archivo",sans-serif;font-weight:500;
  font-size:14px}

.chips{display:flex;flex-wrap:wrap;gap:5px;margin:11px 0 0}
.chips i{font:600 9.5px "Azeret Mono",monospace;letter-spacing:.09em;text-transform:uppercase;
  font-style:normal;padding:3px 6px;border-radius:2px;border:1px solid currentColor;opacity:.85}
.c-free{color:#12643f}.c-paid{color:#8a4b06}.c-nofee{color:#b3200f}
.c-remote{color:#1c4f79}.c-in-person{color:#7a2a5e}.c-hybrid{color:#4a4a1e}
.c-stretch{color:#8a4b06}.c-annual{color:#3f3a86}

.facts{margin:12px 0 0;display:grid;grid-template-columns:auto 1fr;gap:3px 9px;font-size:12.5px}
.facts > b{font-family:"Azeret Mono",monospace;font-size:8.5px;letter-spacing:.13em;
  text-transform:uppercase;opacity:.6;padding-top:3px}
.facts span b{font-weight:600}
.facts span{opacity:.9}
.facts .unk{color:#b3200f;font-style:italic}
.facts .always{color:#12643f;font-weight:600}

.stand{margin:12px 0 0;display:flex;flex-wrap:wrap;gap:4px 14px;align-items:center;
  font-family:"Azeret Mono",monospace;font-size:8.5px;letter-spacing:.11em;text-transform:uppercase;
  opacity:.72}
.stand>b{opacity:.8}
.stand span{display:inline-flex;align-items:center;gap:5px}
.pips{display:inline-flex;gap:2px}
.pips i{width:6px;height:6px;border-radius:50%;border:1px solid var(--prule);opacity:.5}
.pips i.on{background:var(--prule);opacity:1}

.mine{margin:13px 0 0;font-size:13.5px}
.mine p{margin:0 0 8px}
.mine p > b:first-child{display:block;font-family:"Azeret Mono",monospace;font-size:8.5px;
  letter-spacing:.16em;text-transform:uppercase;opacity:.6;margin-bottom:3px}
.mine p b{font-weight:600}
.view{opacity:.92}

.conf{display:flex;align-items:center;gap:6px;margin:11px 0 0;
  font-family:"Azeret Mono",monospace;font-size:9px;letter-spacing:.12em;text-transform:uppercase;
  opacity:.8}
.conf i{width:8px;height:8px;border-radius:50%;flex:none}
.conf-verified i{background:#12643f}
.conf-listing i{background:#c07a00}
.conf-stale i{background:#b3200f}
.conf em{font-style:italic;color:#b3200f;text-transform:none;letter-spacing:0}

.peel{margin:12px 0 0;width:100%;font:600 10.5px "Azeret Mono",monospace;letter-spacing:.14em;
  text-transform:uppercase;color:var(--paper);background:var(--pink);border:0;border-radius:2px;
  padding:9px;cursor:pointer}
.peel:hover{opacity:.88}
.sheet{margin:12px 0 0;border-top:1px dashed var(--prule);padding-top:11px}
.sheet dl{margin:0;display:grid;gap:8px}
.f dt{font-family:"Azeret Mono",monospace;font-size:8.5px;letter-spacing:.13em;
  text-transform:uppercase;opacity:.6}
.f dd{margin:2px 0 0;font-size:13.5px}
.f .unk{color:#b3200f;font-style:italic}
.prec{margin:11px 0 0;font-size:11.5px;font-style:italic;opacity:.66}
.go{display:inline-block;margin:11px 0 0;font:600 10.5px "Azeret Mono",monospace;
  letter-spacing:.12em;text-transform:uppercase;text-decoration:none;
  border-bottom:2px solid var(--prule);padding-bottom:2px}
.tags{display:flex;flex-wrap:wrap;gap:4px;margin:13px 0 0;padding-top:9px;
  border-top:1px solid var(--prule)}
.tags span{font-family:"Azeret Mono",monospace;font-size:8.5px;letter-spacing:.08em;
  text-transform:uppercase;opacity:.5}

/* ------------------------------------------------- weathering: DATED ONLY.
   The five undated categories never fade. A pass that can never expire must not
   look like one that is expiring, or the wall trains him to ignore the ones
   that are. */
.s-settling{box-shadow:0 2px 0 rgba(0,0,0,.35),0 12px 22px -14px rgba(0,0,0,.7)}
.s-lastcall{box-shadow:0 0 0 2px var(--hot),0 2px 0 rgba(0,0,0,.35),0 14px 26px -14px rgba(0,0,0,.7)}
.s-lastcall .state{color:#b3200f}
.s-gone{opacity:.5}
.s-gone .pt{text-decoration:line-through;text-decoration-thickness:2px}
.s-returns .state{color:#3f3a86}
.s-open .state{color:#12643f}

/* ------------------------------------------------------ THE THIRTEEN OBJECTS
   Each category is a different physical thing pinned to the same hoarding.
   `.objx` is the per-category ornament; it never affects layout. */
.objx{position:absolute;pointer-events:none}

/* TALK - a torn ticket stub: notched sides and a perforated tear line. */
.t-lecture{padding-left:30px}
.t-lecture .objx{left:0;top:0;bottom:0;width:20px;
  border-right:2px dashed var(--prule);opacity:.5;
  background:radial-gradient(circle at 0 0,transparent 0 5px,var(--prule) 5px 6px,transparent 6px)
             0 0/100% 14px repeat-y}
.t-lecture:before,.t-lecture:after{content:"";position:absolute;width:14px;height:14px;
  border-radius:50%;background:var(--wall);left:13px}
.t-lecture:before{top:-7px}.t-lecture:after{bottom:-7px}

/* WORKSHOP - a ruled enrolment slip. */
.t-workshop{background-image:repeating-linear-gradient(var(--paper) 0 25px,
  color-mix(in srgb,var(--prule) 12%,transparent) 25px 26px)}
.t-workshop .objx{top:9px;right:10px;width:44px;height:16px;border:1px solid var(--prule);
  opacity:.35}

/* SCHOOL - an admission card: heavy double rule and a punched corner. */
.t-school{border:2px solid var(--prule);box-shadow:inset 0 0 0 5px var(--paper),
  inset 0 0 0 6px color-mix(in srgb,var(--prule) 45%,transparent),
  0 14px 26px -14px rgba(0,0,0,.7)}
.t-school .objx{top:12px;right:12px;width:15px;height:15px;border-radius:50%;
  border:2px solid var(--prule);opacity:.45}

/* FELLOWSHIP - a sealed letter: a wax seal and a folded corner. */
.t-fellowship{background-image:linear-gradient(135deg,
  color-mix(in srgb,var(--prule) 10%,transparent) 0 26px,transparent 26px)}
.t-fellowship .objx{bottom:14px;right:14px;width:38px;height:38px;border-radius:50%;
  background:radial-gradient(circle at 35% 32%,
    color-mix(in srgb,var(--prule) 70%,#fff) 0 30%,var(--prule) 32% 100%);opacity:.5}

/* COURSE - a certificate: a fine double border. */
.t-course{box-shadow:inset 0 0 0 4px var(--paper),
  inset 0 0 0 5px color-mix(in srgb,var(--prule) 55%,transparent),
  inset 0 0 0 9px var(--paper),
  inset 0 0 0 10px color-mix(in srgb,var(--prule) 25%,transparent),
  0 14px 26px -14px rgba(0,0,0,.7);padding:30px 24px 18px}
.t-course .pt{text-align:center}
.t-course .ph{justify-content:center;gap:14px}

/* CONFERENCE - a delegate badge: a lanyard slot and a colour band. */
.t-conf{padding-top:34px}
.t-conf .objx{top:11px;left:50%;margin-left:-19px;width:38px;height:7px;border-radius:4px;
  border:2px solid var(--prule);opacity:.55;background:var(--wall)}
.t-conf .pin{display:none}
.t-conf:before{content:"";position:absolute;left:0;right:0;top:0;height:5px;
  background:var(--prule);opacity:.75}

/* MEMBERSHIP - a card: rounded, with a signature strip. */
.t-member{border-radius:11px}
.t-member .objx{left:0;right:0;bottom:52px;height:15px;
  background:color-mix(in srgb,var(--prule) 22%,transparent)}

/* AMBASSADORSHIP - an enamel badge: rounded with a gloss. */
.t-badge{border-radius:14px;
  background-image:linear-gradient(160deg,rgba(255,255,255,.55) 0 34%,transparent 34%)}
.t-badge .objx{top:16px;right:14px;width:26px;height:26px;border-radius:50%;
  border:3px double var(--prule);opacity:.4}

/* COMMUNITY - an open handbill: torn bottom edge, no date, no clock. */
.t-community .objx{left:0;right:0;bottom:-1px;height:9px;
  background:radial-gradient(circle at 5px -2px,transparent 0 6px,var(--wall) 6px) 0 0/12px 9px repeat-x}
.t-community .pt{font-size:23px}

/* PEER REVIEW - a rubber stamp struck across the corner. */
.t-review .objx{top:14px;right:-6px;width:86px;height:26px;border:2px solid var(--prule);
  border-radius:3px;transform:rotate(-11deg);opacity:.32}

/* CITIZEN SCIENCE - a tally sheet on graph paper. */
.t-citizen{background-image:
  linear-gradient(color-mix(in srgb,var(--prule) 10%,transparent) 1px,transparent 1px),
  linear-gradient(90deg,color-mix(in srgb,var(--prule) 10%,transparent) 1px,transparent 1px);
  background-size:16px 16px,16px 16px}
.t-citizen .objx{top:10px;right:12px;width:34px;height:14px;opacity:.4;
  background:repeating-linear-gradient(90deg,var(--prule) 0 2px,transparent 2px 7px)}

/* GRANT - a cheque stub: scalloped left edge and a micro-print rule. */
.t-grant{padding-left:28px}
.t-grant .objx{left:0;top:0;bottom:0;width:14px;opacity:.4;
  background:radial-gradient(circle at 0 7px,var(--wall) 0 7px,transparent 7px) 0 0/14px 14px repeat-y}
.t-grant .mark{border-top-width:4px;border-bottom-style:double;border-bottom-width:5px}

/* CERTIFICATION - a stamped credential: an embossed roundel and a validity rule.
   Deliberately unlike the course certificate: that one is a decorated border, this
   one is a stamp with an expiry, because the credential itself runs out. */
.t-cert{padding-top:30px}
.t-cert:before{content:"";position:absolute;left:16px;right:16px;top:14px;height:3px;
  background:var(--prule);opacity:.6}
.t-cert .objx{top:22px;right:14px;width:44px;height:44px;border-radius:50%;
  border:2px solid var(--prule);opacity:.35;
  background:repeating-conic-gradient(from 0deg,transparent 0 8deg,
    color-mix(in srgb,var(--prule) 40%,transparent) 8deg 16deg)}
.t-cert .mark{border-top-style:double;border-top-width:5px}

/* PUBLISHING - a galley proof: a narrow column of set type with a masthead rule
   and a hanging byline slot down the left edge. */
.t-publish{padding-left:26px}
.t-publish:before{content:"";position:absolute;left:0;right:0;top:0;height:6px;
  border-top:2px solid var(--prule);border-bottom:1px solid var(--prule);opacity:.65}
.t-publish .objx{left:11px;top:34px;bottom:16px;width:1px;
  background:repeating-linear-gradient(var(--prule) 0 5px,transparent 5px 9px);opacity:.4}
.t-publish .pt{font-family:"Rokkitt",Georgia,serif;font-weight:700;font-size:24px}

/* MENTORSHIP - a calling card: small, centred, one rule under the name, and
   nothing else on it. The whole point is that there is no apparatus. */
.t-mentor{padding:30px 26px 18px;border:1px solid var(--prule)}
.t-mentor .ph{justify-content:center;gap:14px}
.t-mentor .pt{text-align:center;font-family:"Rokkitt",Georgia,serif;font-weight:700;
  letter-spacing:.01em}
.t-mentor .phost{text-align:center}
.t-mentor .rw{text-align:center}
.t-mentor .objx{left:50%;margin-left:-30px;top:calc(100% - 100%);width:60px;height:1px;
  background:var(--prule);opacity:0}

/* ROLE - a staff pass: a header bar and a photo box. */
.t-role{padding-top:38px}
.t-role:before{content:"STAFF PASS";position:absolute;left:0;right:0;top:0;height:22px;
  background:var(--prule);color:var(--paper);font:600 9px "Azeret Mono",monospace;
  letter-spacing:.24em;display:flex;align-items:center;justify-content:center}
.t-role .pin{top:28px}
.t-role .objx{top:30px;right:16px;width:34px;height:42px;border:2px solid var(--prule);
  opacity:.35}

/* ---------------------------------------------------------------- catmap */
.catmap{max-width:1000px;margin:26px auto 0;padding:0 20px}
.catmap h2{font-family:"Archivo Black",sans-serif;font-size:19px;text-transform:uppercase;
  letter-spacing:.03em;margin:0 0 6px}
.catmap .lede{color:var(--ui2);font-size:14px;margin:0 0 16px;max-width:74ch}
.catmap ol{list-style:none;margin:0;padding:0;display:grid;gap:8px;
  grid-template-columns:repeat(auto-fill,minmax(300px,1fr))}
.catmap li{border:1px solid var(--line);border-left:4px solid var(--sky);border-radius:2px;
  padding:11px 13px;background:#2c2723}
/* Direct children of the map list only - the gap box below it is also inside
   .catmap and its <b> tags are inline emphasis, not headings. Same bug as .mark b. */
.catmap > ol > li > b{font-family:"Archivo Black",sans-serif;font-size:14px;display:block}
.catmap li i{font-family:"Azeret Mono",monospace;font-size:8.5px;letter-spacing:.13em;
  text-transform:uppercase;color:var(--ui3);font-style:normal}
.catmap li span{display:block;font-size:13px;color:var(--ui2);margin-top:5px}
.catmap li em{display:block;margin-top:6px;font-family:"Azeret Mono",monospace;font-size:9px;
  letter-spacing:.1em;text-transform:uppercase;color:var(--lime);font-style:normal}
/*@UNDATED_CSS@*/
/* The categories that exist and have nothing in them. Dashed, because an empty
   shelf is a different object from a stocked one - and leaving them off the map
   entirely would have made the map look finished when it is not. */
.gapbox{margin:16px 0 0;padding:14px 16px;border:1px dashed #6b6058;border-radius:2px;
  background:#2a2521}
.gapbox h3{font-family:"Archivo Black",sans-serif;font-size:13.5px;margin:0 0 6px;
  text-transform:uppercase;letter-spacing:.04em;color:#e8b04a}
.gapbox p{margin:0 0 9px;font-size:13px;color:var(--ui2);max-width:74ch}
.gapbox ul{margin:0;padding-left:18px;display:grid;gap:7px}
.gapbox li{font-size:13px;color:var(--ui2)}
.gapbox li b{color:var(--ui)}
.gapbox li i{color:var(--ui3)}

/* ---------------------------------------------------------------- sources */
.src{max-width:1000px;margin:36px auto 0;padding:0 20px}
.src h2{font-family:"Archivo Black",sans-serif;font-size:19px;text-transform:uppercase;
  letter-spacing:.03em;margin:0 0 6px}
.src .lede,.src .key{color:var(--ui2);font-size:14px;margin:0 0 12px;max-width:78ch}
.src ol{margin:0;padding-left:22px}
.src li{margin:0 0 13px}
.src li a{font-weight:600}
.src li i{display:block;font-family:"Azeret Mono",monospace;font-size:9px;letter-spacing:.11em;
  text-transform:uppercase;color:var(--ui3);font-style:normal;margin-top:2px}
.src li p{margin:4px 0 0;font-size:13px;color:var(--ui2)}
.src li.unread{opacity:.72}
.src li.unread a{color:#e8b04a}

.foot{max-width:900px;margin:34px auto 0;padding:20px;border-top:1px solid var(--line);
  color:var(--ui3);font-size:12.5px;line-height:1.85}
.foot b{color:var(--ui2)}

@media (max-width:700px){
  .pass{padding:24px 16px 14px}
  .pt{font-size:19px}
  .facts{grid-template-columns:1fr}
  .facts > b{padding-top:6px}
  /* No lean on a phone: there is no cursor to chase it, and a rotated card
     wastes horizontal space on the one screen that has none. */
  .pass{transform:none}
  .pass:hover,.pass:focus-within{transform:translateY(-2px)}
}
/* On touch, :hover sticks after a tap and the card would stay straightened
   until you touched something else. Pin it back to its lean. */
@media (hover:none){.pass:hover{transform:rotate(var(--tilt))}}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}
  .pass,.pass:hover,.pass:focus-within{transform:none}}
"""

JS = r"""
(function(){
/* ---------------------------------------------------------------- reweather
   The page recomputes its own clocks on every load, from the dates baked into
   each card, before anything else runs.

   Why here and not in the weekly cloud routine, which is how the bill wall does
   it: that routine edits the built HTML by hand, which means an LLM rewriting
   four attributes and two strings per card without slipping. It works, but it is
   the riskiest thing that job does, and between two runs the page is stale
   anyway. Doing it in the browser means the wall is correct every time it is
   OPENED, needs nothing from any schedule, and cannot be corrupted by a bad
   edit. It is pure arithmetic over dates that were verified by hand - it invents
   nothing, exactly like the bill wall's version.

   If this throws, the server-rendered values stay, and the footer says which day
   they were built for. */
/* NOT a literal middle dot: the build refuses any non-ASCII byte in the
   page, so that it never depends on the host supplying a charset. textContent
   takes a real character, not an HTML entity, so it is escaped here instead. */
var STAMP={
  'apply.fresh':'OPEN \u00b7 APPLY','apply.settling':'CLOSING',
  'apply.lastcall':'LAST CALL','apply.gone':'CLOSED',
  'happens.fresh':'UPCOMING','happens.settling':'THIS MONTH',
  'happens.lastcall':'THIS WEEK','happens.gone':'PASSED'};
var MON='Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split(' ');
function pretty(d){return d.getUTCDate()+' '+MON[d.getUTCMonth()]+' '+d.getUTCFullYear();}

function reweather(){
  var now=new Date();
  var today=Date.UTC(now.getFullYear(),now.getMonth(),now.getDate());
  var soon=[];
  document.querySelectorAll('.pass').forEach(function(p){
    var kind=p.dataset.kind;
    if(kind!=='apply'&&kind!=='happens') return;   /* open / returns never move */
    var iso=(kind==='apply')?p.dataset.deadline:p.dataset.starts;
    if(!iso) return;
    var parts=iso.split('-');
    var when=Date.UTC(+parts[0],+parts[1]-1,+parts[2]);
    var days=Math.round((when-today)/86400000);
    var state=days<0?'gone':days<=7?'lastcall':days<=30?'settling':'fresh';
    p.dataset.days=days; p.dataset.state=state;
    p.classList.remove('s-fresh','s-settling','s-lastcall','s-gone');
    p.classList.add('s-'+state);
    var st=p.querySelector('.state'); if(st) st.textContent=STAMP[kind+'.'+state];
    var rw=p.querySelector('.rw');
    if(rw){
      var u=(Math.abs(days)===1)?'day':'days', t;
      if(days<0)      t=(kind==='apply'?'closed ':'was ')+Math.abs(days)+' '+u+' ago';
      else if(days===0) t=(kind==='apply')?'closes today':'today';
      else            t=(kind==='apply')?(days+' '+u+' to apply'):('in '+days+' '+u);
      rw.textContent=t;
    }
    if(kind==='apply'&&days>=0&&days<=7)
      soon.push({id:p.dataset.id,days:days,
                 name:(p.querySelector('.pt')||{}).textContent||p.dataset.id,
                 when:pretty(new Date(when))});
  });

  /* The closing-this-week banner is derived too, or it would name things that
     shut a month ago while the cards beside it read correctly. */
  var al=document.getElementById('alarm');
  if(al){
    var ol=al.querySelector('ol');
    if(!soon.length){ al.hidden=true; }
    else{
      al.hidden=false;
      soon.sort(function(a,b){return a.days-b.days;});
      ol.textContent='';
      soon.forEach(function(s){
        var li=document.createElement('li');
        var b=document.createElement('b');
        b.textContent=s.days+(s.days===1?' day':' days');
        var a=document.createElement('a'); a.href='#'+s.id; a.textContent=s.name;
        var i=document.createElement('i'); i.textContent=s.when;
        li.appendChild(b); li.appendChild(document.createTextNode(' '));
        li.appendChild(a); li.appendChild(document.createTextNode(' '));
        li.appendChild(i); ol.appendChild(li);
      });
    }
  }
  var stamp=document.getElementById('asof');
  if(stamp) stamp.textContent=pretty(new Date(today));
}
try{ reweather(); }catch(e){ /* keep the values the page was built with */ }

var wall=document.querySelector('.wall'),
    passes=[].slice.call(document.querySelectorAll('.pass')),
    q=document.getElementById('q'),
    sortSel=document.getElementById('sort'),
    live=document.getElementById('live'),
    nores=document.getElementById('nores'),
    F={};
var seq=passes.slice();

function order(mode){
  var f={
    run:function(a,b){return (+a.dataset.ord)-(+b.dataset.ord);},
    use:function(a,b){return ((+b.dataset.pr)+(+b.dataset.le))-((+a.dataset.pr)+(+a.dataset.le))
                          || (+a.dataset.ord)-(+b.dataset.ord);},
    pr:function(a,b){return (+b.dataset.pr)-(+a.dataset.pr)||(+a.dataset.ord)-(+b.dataset.ord);},
    le:function(a,b){return (+b.dataset.le)-(+a.dataset.le)||(+a.dataset.ord)-(+b.dataset.ord);},
    cat:function(a,b){return a.dataset.cat<b.dataset.cat?-1:a.dataset.cat>b.dataset.cat?1:
                          (+a.dataset.ord)-(+b.dataset.ord);}
  }[mode]||null;
  if(f) seq.sort(f);
  layout();
}

function colCount(){var w=innerWidth;return w<=700?1:w<=1020?2:w<=1400?3:4;}
var cols=[],colsFor=0;
function buildCols(n){
  cols=[];wall.textContent='';
  wall.classList.add('flexed');
  for(var i=0;i<n;i++){var c=document.createElement('div');c.className='col';
                       cols.push(c);wall.appendChild(c);}
  colsFor=n;
}
/* Shortest-column-first fill, so the TOP ROW is the top of the order. CSS
   multi-column balances column-major, which would put items 1, 11, 21 and 31
   across the top and make every sort control look broken while appearing to
   work. */
function layout(){
  try{
    var n=colCount();
    if(n!==colsFor) buildCols(n);
    for(var i=0;i<cols.length;i++) cols[i].textContent='';
    var h=new Array(cols.length);for(var j=0;j<h.length;j++)h[j]=0;
    for(var k=0;k<seq.length;k++){
      var el=seq[k];
      if(el.classList.contains('hide')) continue;
      var s=0;for(var m=1;m<h.length;m++) if(h[m]<h[s]) s=m;
      cols[s].appendChild(el);
      h[s]+=el.offsetHeight+20;
    }
  }catch(e){
    /* Never let a layout failure hide the wall: drop back to the CSS-columns
       base state and put every card back, rather than leaving a blank page. */
    wall.className='wall';wall.textContent='';colsFor=0;cols=[];
    for(var z=0;z<passes.length;z++) wall.appendChild(passes[z]);
  }
}

document.querySelectorAll('.peel').forEach(function(btn){
  btn.addEventListener('click',function(){
    var s=btn.nextElementSibling,open=s.hasAttribute('hidden');
    if(open){s.removeAttribute('hidden');}else{s.setAttribute('hidden','');}
    btn.setAttribute('aria-expanded',open?'true':'false');
    btn.textContent=open?'Fold the pass back':'Read the whole pass';
    layout();
  });
});

function apply(){
  var v=(q.value||'').trim().toLowerCase(),shown=0;
  for(var i=0;i<passes.length;i++){
    var b=passes[i],d=b.dataset,ok=true;
    if(F.cat && d.cat!==F.cat) ok=false;
    if(ok && F.dom && d.dom!==F.dom) ok=false;
    if(ok && F.fmt && d.fmt!==F.fmt) ok=false;
    if(ok && F.fee && d.fee!==F.fee) ok=false;
    if(ok && F.conf && d.conf!==F.conf) ok=false;
    if(ok && F.city && d.city!==F.city) ok=false;
    if(ok && F.pr && +d.pr < +F.pr) ok=false;
    if(ok && F.le && +d.le < +F.le) ok=false;
    if(ok && F.st){
      var s=d.state;
      if(F.st==='open'  && s!=='open') ok=false;
      if(F.st==='soon'  && !(s==='lastcall'||s==='settling')) ok=false;
      if(F.st==='live'  && !(s==='fresh'||s==='settling'||s==='lastcall'||s==='open')) ok=false;
      if(F.st==='returns' && s!=='returns') ok=false;
    }
    if(ok && v && d.text.indexOf(v)<0) ok=false;
    b.classList.toggle('hide',!ok);
    if(ok) shown++;
  }
  nores.classList.toggle('hide',shown>0);
  live.textContent=shown+' of '+passes.length+' passes';
  layout();
}

document.querySelectorAll('.chip[data-k]').forEach(function(c){
  c.addEventListener('click',function(){
    var k=c.dataset.k,was=F[k]===c.dataset.v;
    F[k]=was?null:c.dataset.v;
    document.querySelectorAll('.chip[data-k="'+k+'"]').forEach(function(o){
      o.setAttribute('aria-pressed',(!was&&o===c)?'true':'false');
    });
    apply();
  });
});

sortSel.addEventListener('change',function(){order(sortSel.value);});

/* Jumping from the closing-this-week banner: clear filters so the target
   cannot be hidden, then scroll to it. */
document.querySelectorAll('.alarm a[href^="#"]').forEach(function(a){
  a.addEventListener('click',function(ev){
    ev.preventDefault();
    F={};
    document.querySelectorAll('.chip[data-k]').forEach(function(o){
      o.setAttribute('aria-pressed','false');});
    q.value='';apply();
    var t=document.getElementById(a.getAttribute('href').slice(1))
       || document.querySelector('[data-id="'+a.getAttribute('href').slice(1)+'"]');
    if(t){t.scrollIntoView({block:'center'});t.focus({preventScroll:true});}
  });
});

var rz;addEventListener('resize',function(){clearTimeout(rz);rz=setTimeout(layout,120);});
if(document.fonts&&document.fonts.ready) document.fonts.ready.then(layout).catch(function(){});
var t;q.addEventListener('input',function(){clearTimeout(t);t=setTimeout(apply,90);});
addEventListener('keydown',function(e){
  if(e.key==='/'&&document.activeElement!==q){e.preventDefault();q.focus();}
  if(e.key==='Escape'){q.value='';apply();q.blur();}
});
apply();
})();
"""

PAGE = u"""<title>The Pass Wall</title>
<meta name="color-scheme" content="dark">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600&family=Archivo+Black&family=Rokkitt:wght@400;500;700&family=Azeret+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>%(css)s</style>

<div class="sky"></div>

<header class="mast">
  <h1>The Pass Wall</h1>
  <p class="sub">%(total)d passes &middot; %(cats)d kinds of thing &middot; %(verified)d verified at source &middot; %(free)d free &middot; %(nsrc)d sources, %(nread)d opened &middot; %(freshness)s</p>
  <p class="say">The bill wall carries things you <b>enter and might win</b>. This one carries
     things you <b>walk into and come out marked by</b> &mdash; a seat for one evening, a
     certificate, a cohort, a membership, a title, a byline, a mentor.
     Same wall, different objects pinned to it.</p>
  <p class="pol">You said you did not know what categories were out there. <b style="color:#6fd3e8">So the map is the point, and it is printed below the wall</b> &mdash; %(catword)s genuinely different kinds of thing, not three.<br>
     Every field is what a source literally printed, or the words &ldquo;not stated&rdquo; in red. Nothing is inferred.<br>
     A green dot means I opened that thing&rsquo;s own page. An amber dot means I only saw a listing.<br>
     <b>Two clocks, never mixed:</b> &ldquo;apply by&rdquo; is a form with a closing date; &ldquo;happens&rdquo; is a day it simply occurs on. %(undatedwordcap)s of the %(catword)s categories have no clock at all, and those never fade &mdash; because a pass that can never expire must not look like one that is expiring.</p>
  <a class="sib" href="https://claude.ai/code/artifact/512537bc-1994-424f-8e42-a8bbfe57947f">&larr; The Bill Wall &mdash; competitions</a>
</header>

%(lastcall)s

<div class="rail">
  <input id="q" type="search" placeholder="Search  /" aria-label="Search the wall">
  %(catchips)s
</div>
<div class="rail two">
  <button class="chip" data-k="fee"  data-v="free"      aria-pressed="false">Free</button>
  <button class="chip" data-k="fmt"  data-v="remote"    aria-pressed="false">Remote</button>
  <button class="chip" data-k="fmt"  data-v="in-person" aria-pressed="false">In person</button>
  <button class="chip" data-k="city" data-v="bengaluru" aria-pressed="false">Bengaluru</button>
  <button class="chip" data-k="st"   data-v="open"      aria-pressed="false">No deadline</button>
  <button class="chip" data-k="st"   data-v="soon"      aria-pressed="false">Closing</button>
  <button class="chip" data-k="st"   data-v="returns"   aria-pressed="false">Comes round</button>
  <button class="chip" data-k="st"   data-v="live"      aria-pressed="false">Still open</button>
  <button class="chip" data-k="dom"  data-v="med"       aria-pressed="false">Medicine</button>
  <button class="chip" data-k="dom"  data-v="research"  aria-pressed="false">Research</button>
  <button class="chip" data-k="dom"  data-v="ai"        aria-pressed="false">AI &amp; ML</button>
  <button class="chip" data-k="conf" data-v="verified"  aria-pressed="false">Verified only</button>
  <button class="chip" data-k="pr"   data-v="4"         aria-pressed="false">Big name</button>
  <button class="chip" data-k="le"   data-v="5"         aria-pressed="false">Best to learn from</button>
  <label class="sorter"><span>Order</span>
    <select id="sort" aria-label="Order the wall">
      <option value="run" selected>Most runway left</option>
      <option value="use">Most useful to you</option>
      <option value="pr">Prestige</option>
      <option value="le">What you would learn</option>
      <option value="cat">By kind of thing</option>
    </select>
  </label>
  <span class="count" id="live"></span>
</div>

<main class="wall">
%(cards)s
</main>
<p class="nores hide" id="nores">Nothing on the wall matches that.</p>

<section class="catmap">
  <h2>The %(catword)s kinds of thing</h2>
  <p class="lede">You said: <i>&ldquo;i just dont know what other categories are there check em
     all&rdquo;</i>. This is the sweep. They are not variations on one idea &mdash; they differ in
     what they cost you, what they leave behind, and whether they have a clock on them at all.
     The %(undatedword)s marked <b style="color:#c8f04a">never expires</b> are the reason this page
     has more than one shape of card on it.</p>
  <ol>%(catrows)s</ol>
  <div class="gapbox">
    <h3>All sixteen are filled now. Here is what is still thin, and why.</h3>
    <p>The first build of this page shipped thirteen categories and named three it had found and
       could not fill. All three are filled. What unblocked them is worth writing down, because two
       of the three were my failure and not the internet&rsquo;s:</p>
    <ul>
      <li><b>Publishing</b> was empty because <code>www.ijms.info</code> refused the connection,
        twice, in a fetcher and in a browser. <b>The bare domain <code>ijms.info</code> works
        perfectly.</b> An entire category was missing because of four characters in a hostname.</li>
      <li><b>Certification</b> was empty because I tried one source, CITI Program, and it was blocked
        both ways. There was a free, reachable alternative &mdash; NIDA&rsquo;s Good Clinical
        Practice course &mdash; that I simply had not looked for. <i>&ldquo;I could not look&rdquo;
        was true of the source and not true of the category.</i></li>
      <li><b>Mentorship</b> was genuinely unswept. It now has one entry and deserves more.</li>
    </ul>
    <p><b>Still thin, stated plainly:</b> mentorship has one entry; certification has one, and the
       Indian regulatory equivalents are unexplored; publishing has two, and neither is a specialty
       journal. Three sources that could fill them out &mdash; CITI Program, ISCB and IUSSTF (the
       Khorana and S.N. Bose scholarships) &mdash; were unreachable from this machine on
       4 September 2026, and IUSSTF reset the connection in a real browser too, so that one is not
       a tooling problem.</p>
  </div>
</section>

<section class="src">
  <h2>Where these come from</h2>
  <p class="lede">Every source below was either opened on <b>4 September 2026</b> or is named as
     unopened. Nothing was written from a search snippet.</p>
  <p class="key"><b>&ldquo;I could not look&rdquo; is a different answer from &ldquo;I found
     nothing&rdquo;</b>, and the notes keep them apart. Two ambassador programmes are on this wall
     with their terms unread because they sit behind a login; that is said on the cards rather than
     guessed at. Eight sources were named and not opened, and they are listed at the bottom in amber
     rather than quietly left out.</p>
  <ol>%(sources)s</ol>
</section>

<footer class="foot">
  <b>The Pass Wall</b> &mdash; %(total)d passes, %(live)d of them still open to you, %(verified)d verified at source, %(nopen)d with no deadline at all.<br>
  <b>Nothing here is inferred.</b> A field the source did not print says so, in red. Where I could not read a page at all, the card says that too.<br>
  <b>&ldquo;Why it is on your wall&rdquo;, &ldquo;My view&rdquo; and the two ratings are my judgement</b>, not the source&rsquo;s. Argue with all of them.<br>
  <b>Prestige</b> is whether the name means anything to a medical school, a lab or a panel. <b>Worth learning from</b> is how much it would teach you. They are separate on purpose: RSNA membership is prestige 4 and learning 2 &mdash; it is a line on a CV, not an education &mdash; and ML Collective is exactly the reverse.<br>
  <b>Ordered by most runway left</b>, never by what shuts first. That default is the whole reason this project exists. The things closing within a week are lifted into the banner at the top instead.<br>
  <b>The countdowns recompute themselves every time you open this page</b>, in your browser, from dates that were verified by hand &mdash; so they are right today whatever today is, and the &ldquo;closing within the week&rdquo; banner is rebuilt with them. Facts were read on <b>4 September 2026</b>; clocks as of <b id="asof">4 Sep 2026</b>. A countdown never goes stale, but a <i>fact</i> can &mdash; refresh the wall weekly.<br>
  Keys: <b>/</b> to search, <b>Esc</b> to clear. Filters stack.
</footer>

<script>%(js)s</script>
"""

# The CSS is a value, not a template, so its one generated block is spliced in by
# token rather than by %-formatting - CSS is full of literal percent signs and
# %-formatting it would blow up on the first `100%`.
assert '/*@UNDATED_CSS@*/' in CSS, 'the undated-category CSS token has gone missing'
CSS = CSS.replace('/*@UNDATED_CSS@*/', UNDATED_CSS)
assert '/*@UNDATED_CSS@*/' not in CSS
assert '.catmap li.c-publish' in CSS, 'the generated undated-category CSS looks wrong'

# Derived, never typed - see the same block in build.py. This masthead said
# "read 4 September 2026" while four passes had been re-verified on the 7th.
_latest = max((e.get("checked") or "") for e in entries)
_freshest = sum(1 for e in entries if e.get("checked") == _latest)
freshness = "sources read %s" % pretty(D.READ_ON)
if _latest > D.READ_ON:
    freshness += " &middot; %d re-checked %s" % (_freshest, pretty(_latest))

out = PAGE % dict(
    freshness=freshness,
    css=CSS, js=JS, cards='\n'.join(cards), sources='\n'.join(src_rows),
    catrows='\n'.join(catrows), catchips=catchips, lastcall=lastcall,
    total=len(entries), cats=N_CATS, catword=CATWORD, undatedword=UNDATEDWORD,
    undatedwordcap=UNDATEDWORD_CAP,
    verified=n_ver, free=n_free,
    live=n_live, nopen=n_open, nsrc=len(D.SOURCES), nread=n_src_open)

# The page must be pure ASCII, with every non-ASCII character written as an HTML
# entity. Not fussiness: the Artifact host supplies the charset meta, so a raw
# UTF-8 curly quote renders correctly THERE and turns into mojibake anywhere the
# page is served without one. A literal U+2019 in a category note shipped exactly
# that - "other people<mojibake>s work" - and it was invisible on the deployed
# page and obvious the moment the same file was served from anywhere else.
# Fixing the one character would have left the next one to happen quietly.
_bad = sorted({c for c in out if ord(c) > 127})
if _bad:
    where = []
    for c in _bad:
        i = out.index(c)
        where.append('U+%04X %r near: %s' % (ord(c), c, out[max(0, i - 60):i + 20].replace('\n', ' ')))
    raise AssertionError(
        'the page contains %d literal non-ASCII character(s); write them as HTML entities '
        '(&rsquo; &mdash; &euro; &#8377;) so the page does not depend on the host supplying a '
        'charset:\n  %s' % (len(_bad), '\n  '.join(where)))

io.open(OUT, 'w', encoding='utf-8', newline='\n').write(out)

print('written  : %s' % OUT)
print('bytes    : %d' % len(out.encode('utf-8')))
print('passes   : %d  (live %d, verified %d, free %d, no-deadline %d)'
      % (len(entries), n_live, n_ver, n_free, n_open))
print('sources  : %d  (%d opened)' % (len(D.SOURCES), n_src_open))
print('closing within the week: %d' % len(soon))
for e in soon:
    print('   %2d days  %s' % (e['_days'], html.unescape(e['name'])))
from collections import Counter
for k, v in sorted(Counter(e['_state'] for e in entries).items()):
    print('   %-9s %d' % (k, v))
