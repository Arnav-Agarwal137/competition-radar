# -*- coding: utf-8 -*-
"""data.py -> radar.html, THE BILL WALL, second pass.

WHAT CHANGED FROM THE FIRST PASS, and why:

1. EVERY COMPETITION HAS ITS OWN THEME. He said the first pass still grouped them
   by category. Each bill now carries its own paper, ink and rule colour set
   inline, plus one of ten poster treatments. Thirty-five distinct papers.

2. TRUST IS ON THE FACE OF THE CARD. He said no information should be stated in a
   way that makes him choose something and then discover he has wasted his time.
   So each bill shows how much of it was confirmed - VERIFIED means the
   competition's own page was opened, FROM A LISTING means only a listing was -
   and every unconfirmed field is red rather than quietly grey.

3. DIFFICULTY AND MY VIEW. Each bill carries a 1-5 difficulty judged for him
   specifically, and a paragraph on whether and how to proceed. Both are labelled
   as my opinion rather than the source's.

4. PERFORMANCE. He noticed a slight lag. Removed: `background-attachment:fixed`
   (repaints a full-viewport gradient every scroll frame), the repeating gradient
   over it, `backdrop-filter` on the sticky rail, the per-card `filter:
   saturate()` and `grayscale()` (filters on 35 large elements force compositing
   and are expensive), a `mix-blend-mode` overlay, and the per-card rotation.
   Debounced the search input. `content-visibility:auto` was tried and REMOVED:
   inside a CSS columns layout it left cards below the fold permanently blank,
   which looks broken. The real culprits were the fixed background and the
   filters; without those the page scrolls fine without it.
"""
import io, sys, os, re, html, datetime, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import data as D

OUT = os.path.join(HERE, 'radar.html')
TODAY = datetime.date.fromisoformat(D.TODAY)

# REFUSE TO BAKE A STALE COUNTDOWN BASELINE. Added 10 September 2026.
#
# D.TODAY had sat at 2026-09-03 for a week. Every baked data-days was seven
# days wrong, an entry on the sister wall that had closed two days earlier
# baked as "4 days" and sat in the closing-within-the-week banner, and NOTHING
# CAUGHT IT: the audit passed, and the re-weather parity check agreed with the
# page precisely because it measures against this same constant. A stale
# baseline is invisible to every checker that shares it.
#
# So the guard goes where the work cannot proceed without it, rather than in a
# note asking the next session to remember. A warning I can read past, a check
# I have to run and a step I have to recall are the same thing in different
# clothes; this one stops the build.
#
# The live page re-weathers itself from data-deadline, so the SYMPTOM is
# limited to the no-JS fallback and to every offline check - which is most of
# them, and is why this is worth a hard failure rather than a printed notice.
_real = datetime.date.today()
if TODAY != _real:
    sys.exit(
        'REFUSING TO BUILD: data.py TODAY is %s but today is %s (%+d days).\n'
        '  TODAY is the baseline the baked countdowns are measured from and it\n'
        '  must move on every build. Set data.py TODAY = %r and build again.\n'
        '  DO NOT touch READ_ON (%s) - that records when a human harvested the\n'
        '  sources and must not move for a rebuild.'
        % (TODAY, _real, (TODAY - _real).days, _real.isoformat(), D.READ_ON))


def esc(s):
    return html.escape(str(s), quote=False)


def attr(s):
    """Escape for use INSIDE a quoted HTML attribute.

    esc() deliberately leaves quotes alone, because bill values are authored HTML
    and escaping them would print the entity. That is right for element content
    and wrong for an attribute: one plain double quote in a prize or eligibility
    line would close the attribute early and break the card, with nothing
    erroring. No bill contains one today; this makes sure the first one that does
    cannot take a card down quietly.
    """
    return html.escape(str(s), quote=True)


def runway(b):
    if b.get('precision') == 'recurring':
        return None, 'returns'
    if not b.get('deadline'):
        return None, 'evergreen'
    d = (datetime.date.fromisoformat(b['deadline']) - TODAY).days
    if d < 0:
        return d, 'torn'
    if d <= 7:
        return d, 'lastcall'
    if d <= 30:
        return d, 'settling'
    return d, 'fresh'


def tilt(bill_id):
    """A deterministic lean, so the wall looks pasted up rather than laid out.
    Same id always gives the same angle, so cards do not jump between builds.
    A static transform is GPU-composited and costs nothing - it was never the
    cause of the lag he reported; the filters and the fixed background were."""
    h = int(hashlib.md5(bill_id.encode()).hexdigest()[:8], 16)
    return round(((h % 200) - 100) / 100 * 1.4, 2)


def pretty_iso(iso):
    """'2026-09-14' -> '14 Sep 2026'. Matches what reweather() renders in the
    browser, so the server-built banner and the re-weathered one read alike."""
    d = datetime.date.fromisoformat(iso)
    return '%d %s %d' % (d.day, MONTH[d.month - 1], d.year)


WEATHER = {
 'fresh': 'FRESHLY PASTED', 'settling': 'ON THE WALL', 'lastcall': 'LAST CALL',
 'torn': 'CLOSED', 'returns': 'RETURNS', 'evergreen': 'ALWAYS UP',
}

CONF = {
 'verified': ('VERIFIED AT SOURCE',
              'I opened this competition&rsquo;s own page and read these fields there.'),
 'listing':  ('FROM A LISTING',
              'Taken from a listing page, not the competition&rsquo;s own. Anything the listing '
              'did not print is marked in red inside.'),
 'stale':    ('NOT RE-CHECKED',
              'Carried from an earlier pass and not confirmed today. Check every field yourself.'),
}

UNCERTAIN = ('not stated', 'unconfirmed', 'unknown', 'check before', 'not confirmed',
             'estimate', 'not printed', 'no direct link')

bills = []
for b in D.BILLS:
    days, w = runway(b)
    bills.append(dict(b, _days=days, _w=w))

ORDER = {'fresh': 0, 'settling': 1, 'lastcall': 2, 'evergreen': 3, 'returns': 4, 'torn': 5}
bills.sort(key=lambda b: (ORDER[b['_w']], -(b['_days'] if b['_days'] is not None else 0)))


def field(label, value):
    """A field he cannot trust must LOOK untrustworthy rather than sit quietly
    among the real ones. This is the whole point of the second pass."""
    if value is None or value == '':
        return ('<div class="f uncertain"><dt>%s</dt><dd><span class="unk">not stated on the '
                'source</span></dd></div>' % esc(label))
    # Values are authored HTML and carry entities (&mdash;, &euro;, &#8377;).
    # Escaping them would print the entity instead of the character.
    v, cls = str(value), ''
    if any(t in str(value).lower() for t in UNCERTAIN):
        v, cls = '<span class="unk">%s</span>' % v, ' uncertain'
    return '<div class="f%s"><dt>%s</dt><dd>%s</dd></div>' % (cls, esc(label), v)


DIFWORD = {1: 'an afternoon', 2: 'a weekend', 3: 'a couple of weeks',
           4: 'weeks of real work', 5: 'an open research problem'}

MONTH = ('Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec').split()


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


def short(value, n=76):
    """Trim for the FACE. A trimmed value must never READ as complete, and
    it must never be BROKEN HTML - see _visible_trim for why that matters.
    The full text is carried in the title attribute and printed in the sheet."""
    return _visible_trim(str(value).strip(), n)


def faceline(label, value):
    """One row of the facts strip, keeping the red-for-unconfirmed contract."""
    if value is None or str(value).strip() == '':
        return ('<b>%s</b><span class="unk">not stated</span>' % esc(label))
    full, trimmed = short(value)
    cls = ' class="unk"' if any(t in str(value).lower() for t in UNCERTAIN) else ''
    title = ' title="%s"' % attr(html.unescape(str(value))) if trimmed else ''
    return '<b>%s</b><span%s%s>%s</span>' % (esc(label), cls, title, full)


def closes(b):
    """A short, exact closing date for the face.

    Deliberately NOT the countdown: the countdown is what the weekly scout
    rewrites, and a date does not rot between refreshes the way "12 days" does.
    """
    if b.get('precision') == 'recurring':
        return 'Shut &mdash; comes round again'
    if not b.get('deadline'):
        return 'No deadline stated'
    y, m, d = b['deadline'].split('-')
    return '%d %s %s' % (int(d), MONTH[int(m) - 1], y)

CASH = re.compile(r'[$€£₹]|&euro;|&pound;|&#8377;')

# A currency symbol in the prize field does NOT mean the entrant receives money.
# Found 7 September 2026: the DREAM x CACHE prize text was expanded to explain
# that the prospective phase costs the entrant money and that a CA$20,000 assay
# fee is waived. Both are sums the entrant PAYS or does not pay - and the single
# "$" flipped data-cash from "no" to "yes", putting a bill whose own headline
# reads "NOT CASH - CO-AUTHORSHIP" under the "Cash prize" filter.
#
# The general shape, and it is why this is a regex and not an edit to one entry:
# the flag asks "does he get money", the pattern only asks "does a currency
# symbol appear", and any prize text that mentions a fee, a cost, a waiver or a
# sponsor's spend breaks that equivalence.
#
# THE DENIAL MUST COME FIRST. The first version of this fix matched "non-cash"
# anywhere, and immediately broke a prize that genuinely pays: Prom Virgo's
# "$1,500 in cash prizes, plus 2 non-cash prizes" flipped to no, because a
# phrase describing ONE COMPONENT of a prize was read as a denial of all of it.
# So position decides. A prize that opens by denying cash ("NOT CASH -
# CO-AUTHORSHIP...") is denying the whole thing; a currency figure that appears
# before any denial is real money the entrant receives, whatever qualifications
# follow it. _audit.py check 15 fails the build if flag and text disagree.
NOCASH = re.compile(r'(?i)\bnot\s+cash\b|\bno\s+cash\s+prize\b')


def _pays_cash(prize):
    """True when the prize text says the entrant receives money."""
    m_cash = CASH.search(prize)
    if not m_cash:
        return False
    m_deny = NOCASH.search(prize)
    return not (m_deny and m_deny.start() < m_cash.start())

cards = []
for order_index, b in enumerate(bills):
    days, w = b['_days'], b['_w']
    if days is None:
        rt = {'returns': 'shut &mdash; comes round again', 'evergreen': 'no deadline'}[w]
    elif days < 0:
        # SINGULAR AT ONE, and this line was 'closed %d days ago' until
        # 10 September 2026. The runway branch below had always got it right,
        # so the two halves of one sentence disagreed - and reweather() in the
        # browser gets it right too, which made this a genuine divergence
        # between the baked page and the page a reader actually sees.
        #
        # It could only ever show on the single day a bill is exactly one day
        # past its deadline, and the countdown baseline had been frozen for a
        # week, so no bill had passed through that state since the code was
        # written. Moving the baseline to the real date put two bills there at
        # once and the parity checker caught both immediately.
        rt = 'closed %d %s ago' % (abs(days), 'day' if abs(days) == 1 else 'days')
    elif days == 0:
        rt = 'closes today'
    else:
        rt = '%d day%s of runway' % (days, '' if days == 1 else 's')

    fmt_word = {'remote': 'Remote', 'in-person': 'In person', 'hybrid': 'Hybrid'}[b['fmt']]
    free = b['fee'].lower().startswith(('free', 'no fee', 'none'))

    fee_unknown = any(t in b['fee'].lower() for t in UNCERTAIN)
    if free:
        fee_chip = '<i class="c-free">Free</i>'
    elif fee_unknown:
        fee_chip = '<i class="c-nofee">Fee not stated</i>'
    else:
        fee_chip = '<i class="c-paid">%s</i>' % b['fee']
    chips = ['<i class="c-%s">%s</i>' % (b['fmt'], fmt_word), fee_chip]
    if b.get('stretch'):
        chips.append('<i class="c-stretch">Above you, for now</i>')
    if b.get('recurring'):
        chips.append('<i class="c-annual">Annual</i>')

    d = b['difficulty']
    if d == 0:
        diff = ('<p class="dif"><b>Difficulty for you</b>'
                '<span class="unk">not enough is known to judge</span></p>')
    else:
        pips = ''.join('<i class="%s"></i>' % ('on' if i < d else '') for i in range(5))
        diff = ('<p class="dif"><b>Difficulty for you</b><span class="pips">%s</span>'
                '<span class="dw">%s</span></p>' % (pips, DIFWORD[d]))

    # The face of the bill. Prize first, because that is the gain and the
    # question he is actually asking when he looks at a wall of these.
    prize_full, prize_trimmed = short(b['prize'], 92)
    # "Unknown" must mean NO PRIZE FIGURE IS KNOWN - not "some detail about the
    # prize is uncertain". Found 7 September 2026 by the new cash-flag check:
    # matching an UNCERTAIN token anywhere in the text caught three bills whose
    # headline figure is perfectly well known and where only a detail was not -
    # XPRIZE Quantum's "$5,000,000 total purse. The split across phases is not
    # stated", Learn2Design's "EUR 25,000 total pool ... The split is not stated",
    # and CrunchDAO's "$100,000, as listed by ML Contests. The figure is NOT
    # confirmed on CrunchDAO's own page". All three rendered their whole reward
    # in the red not-stated styling AND were flagged data-cash="no", so a
    # five-million-dollar competition was hidden from the "Cash prize" filter.
    #
    # So a currency figure that appears BEFORE the first uncertainty token wins:
    # the amount is known, the caveat still prints in full beside it, and the
    # reader judges the sourcing from the confidence dot as they do everywhere
    # else. Same ordering principle as _pays_cash above.
    _pl = str(b['prize']).lower()
    _unc = [_pl.find(t) for t in UNCERTAIN if t in _pl]
    _fig = CASH.search(str(b['prize']))
    prize_unknown = bool(_unc) and not (_fig and _fig.start() < min(_unc))
    gain = ('<p class="gain"><b>Reward</b><span%s%s>%s</span></p>' % (
        ' class="unk"' if prize_unknown else '',
        ' title="%s"' % attr(html.unescape(str(b['prize']))) if prize_trimmed else '',
        prize_full))

    facts = '<div class="facts">%s%s%s</div>' % (
        faceline('Closes', closes(b)),
        faceline('Team', b['team']),
        faceline('Who', b['eligible']))

    # Does a real currency figure appear in the prize? A text property of what
    # the source printed, not a judgement about the competition - "500 Zindi
    # points", "Swag only" and "NONE." all correctly come out as no.
    has_cash = (not prize_unknown) and _pays_cash(str(b['prize']))

    # My two ratings, on the face and labelled as mine. Kept in one line so the
    # card does not turn into a scorecard.
    def _pips(n):
        return ''.join('<i class="%s"></i>' % ('on' if i < n else '') for i in range(5))
    stand = ('<p class="stand"><b>My rating</b>'
             '<span>Prestige<span class="pips">%s</span></span>'
             '<span>Worth learning from<span class="pips">%s</span></span></p>'
             % (_pips(b['prestige']), _pips(b['learning'])))

    sheet = ''.join([
        field('What it actually is', b['kind']),
        field('What you submit', b['submit']),
        field('Remote or in person', '%s &mdash; %s' % (fmt_word, b['location'])),
        field('Travel', b['travel']),
        field('Entry fee', b['fee']),
        field('Prize', b['prize']),
        field('Team size', b['team']),
        field('Who may enter', b['eligible']),
        field('Effort', b['effort']),
        field('Deadline', b['deadline_text']),
        field('Host', b['host']),
        field('Found on', b['platform']),
        field('Also worth knowing', b.get('extra')),
    ] + ([field('Finding it', b['find'])] if b.get('find') else []))

    gaps = sum(1 for t in (b['prize'], b['travel'], b['eligible'], b['fee'], b['team'])
               if any(x in str(t).lower() for x in UNCERTAIN))
    prec = {
      'exact':     'The source printed this deadline as a date.',
      'derived':   'The source printed only &ldquo;N days left&rdquo;. This date is computed from '
                   '3 Sep 2026 and could be a day out.',
      'listing':   'This deadline came from a listing page, not the competition&rsquo;s own page.',
      'recurring': 'This cycle has closed. The next window is an estimate from the last one.',
      'none':      'No deadline is stated anywhere I could reach.',
    }[b.get('precision', 'none')]

    th = b['theme']
    cflag, ctip = CONF[b['conf']]

    cards.append("""
<article class="bill %(treat)s w-%(w)s" data-id="%(id)s" data-dom="%(dom)s"
  data-fmt="%(fmt)s" data-fee="%(feec)s" data-w="%(w)s" data-conf="%(conf)s"
  data-days="%(days)s" data-deadline="%(iso)s" data-text="%(hay)s"
  data-pr="%(pr)s" data-le="%(le)s" data-diff="%(diffn)s" data-cash="%(cash)s" data-ord="%(ord)s"
  tabindex="0"
  style="--paper:%(paper)s;--pink:%(ink)s;--prule:%(rule)s;--tilt:%(tilt)sdeg">
  <div class="tape" aria-hidden="true"></div>
  <header class="bh"><span class="stamp">%(stamp)s</span><span class="rw">%(rt)s</span></header>
  <h3 class="bt">%(name)s</h3>
  <p class="bhost">%(host)s &middot; <span>%(platform)s</span></p>
  <p class="bblurb">%(blurb)s</p>
  %(gain)s
  <div class="chips">%(chips)s</div>
  %(facts)s
  %(diff)s
  %(stand)s
  <div class="mine">
    <p class="why"><b>Why it is on your wall</b>%(why)s</p>
    <p class="view"><b>My view on actually doing it</b>%(view)s</p>
  </div>
  <p class="conf conf-%(conf)s" title="%(ctip)s"><i></i>%(cflag)s%(gapnote)s</p>
  <button class="peel" aria-expanded="false">Read the whole bill</button>
  <div class="sheet" hidden>
    <dl>%(sheet)s</dl>
    <p class="prec">%(prec)s</p>
    <a class="go" href="%(url)s" target="_blank" rel="noopener">Go to the source &rarr;</a>
  </div>
  <div class="tags">%(tags)s</div>
</article>""" % dict(
        gain=gain, facts=facts, stand=stand,
        pr=b['prestige'], le=b['learning'], diffn=b['difficulty'],
        cash=('yes' if has_cash else 'no'), ord=order_index,
        treat=th['treatment'], w=w, id=esc(b['id']), dom=b['domain'], fmt=b['fmt'],
        feec='free' if free else 'paid', conf=b['conf'],
        days=(days if days is not None else 9999),
        # A machine-readable deadline lets the weekly scout recompute every
        # countdown by arithmetic alone, with no network and no new facts.
        iso=(b.get('deadline') or ''),
        paper=th['paper'], ink=th['ink'], rule=th['rule'], tilt=tilt(b['id']),
        # Decode entities before building the search haystack, so a search for
        # "pokemon" matches and a search for "mdash" does not.
        hay=esc(html.unescape(' '.join([b['name'], b['host'], b['blurb'], b['kind'],
                                        b['eligible'], b['platform'],
                                        ' '.join(b.get('tags', []))])).lower()),
        stamp=WEATHER[w], rt=rt, name=b['name'], host=b['host'],
        platform=b['platform'], blurb=b['blurb'], chips=''.join(chips), diff=diff,
        why=b['why'], view=b['view'], cflag=cflag, ctip=ctip,
        gapnote=('<em> &middot; %d field%s never stated</em>'
                 % (gaps, '' if gaps == 1 else 's')) if gaps else '',
        sheet=sheet, prec=prec, url=esc(b['url']),
        tags=''.join('<span>%s</span>' % esc(t) for t in b.get('tags', [])),
    ))

src_rows = []
for s in sorted(D.SOURCES, key=lambda x: (not x['checked'], x['name'])):
    src_rows.append('<li class="%s"><a href="%s" target="_blank" rel="noopener">%s</a>'
                    '<i>%s &middot; %s</i><p>%s</p></li>'
                    % ('read' if s['checked'] else 'unread', esc(s['url']), esc(s['name']),
                       esc(s['kind']), esc(s['region']), s['note']))

counts = {}
for b in bills:
    counts[b['_w']] = counts.get(b['_w'], 0) + 1
live = sum(counts.get(k, 0) for k in ('fresh', 'settling', 'lastcall', 'evergreen'))
verified = sum(1 for b in bills if b['conf'] == 'verified')

CSS = r"""
:root{--wall:#26221e;--wall2:#1b1815;--ui:#f4efe6;--ui2:#b6aa99;--ui3:#8a7f72;
  --hot:#e8442f;--lime:#c8f04a;--line:#413a34}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;font-family:"Archivo",system-ui,sans-serif;font-size:16px;line-height:1.5;
  color:var(--ui);background:var(--wall)}
.sky{position:fixed;inset:0;z-index:-1;pointer-events:none;
  background:radial-gradient(120% 70% at 50% 0%,#37312b 0%,var(--wall) 45%,var(--wall2) 100%)}
a{color:inherit}
.mast{padding:34px 20px 18px;text-align:center}
.mast h1{font-family:"Archivo Black",sans-serif;font-size:clamp(34px,8.5vw,76px);line-height:.92;
  margin:0;letter-spacing:-.02em;text-transform:uppercase;color:#efe9dd;text-shadow:3px 3px 0 var(--hot)}
.mast .sub{font-family:"Azeret Mono",monospace;font-size:10px;letter-spacing:.2em;
  text-transform:uppercase;color:var(--ui3);margin:13px 0 0}
.mast .say{max-width:660px;margin:15px auto 0;color:#d6cdbf;font-size:16.5px;
  font-family:"Rokkitt",Georgia,serif}
.mast .say b{color:var(--lime)}
.mast .pol{max-width:680px;margin:11px auto 0;font-size:12.5px;color:var(--ui3);
  font-family:"Azeret Mono",monospace;line-height:1.9}
.rail{position:sticky;top:0;z-index:60;padding:9px 14px;background:#171411;
  border-bottom:1px solid var(--line);display:flex;gap:7px;align-items:center;
  flex-wrap:wrap;justify-content:center}
.rail input{font-family:"Archivo",sans-serif;font-size:14px;background:#221e1a;color:var(--ui);
  border:1px solid #423b34;border-radius:3px;height:34px;padding:0 11px;width:170px}
.rail input:focus{outline:2px solid var(--lime);outline-offset:1px}
.chip{font-family:"Azeret Mono",monospace;font-size:9px;letter-spacing:.1em;text-transform:uppercase;
  background:none;color:var(--ui2);border:1px solid #45403a;border-radius:3px;height:34px;
  padding:0 10px;cursor:pointer;white-space:nowrap}
.chip:hover{color:var(--ui);border-color:#736a60}
.chip:focus-visible{outline:2px solid var(--lime);outline-offset:1px}
.chip[aria-pressed="true"]{background:var(--lime);color:#1a1a10;border-color:var(--lime);font-weight:600}
.count{font-family:"Azeret Mono",monospace;font-size:9px;color:var(--ui3);letter-spacing:.1em}
.sorter{display:inline-flex;align-items:center;gap:6px;height:34px}
.sorter span{font-family:"Azeret Mono",monospace;font-size:9px;letter-spacing:.1em;
  text-transform:uppercase;color:var(--ui3)}
.sorter select{font-family:"Azeret Mono",monospace;font-size:9px;letter-spacing:.08em;
  text-transform:uppercase;background:#221e1a;color:var(--ui);border:1px solid #45403a;
  border-radius:3px;height:34px;padding:0 8px;cursor:pointer}
.sorter select:focus-visible{outline:2px solid var(--lime);outline-offset:1px}
/* CSS multi-column balances COLUMN-MAJOR: with 118 cards over four columns,
   the top of the screen shows items 1, 31, 61 and 91. That is fine when the
   order is runway, and wrong the moment he asks for "the most useful on top",
   because only the left column would obey him.

   So the wall is flex columns filled by script, shortest-column-first in the
   current order: the top ROW holds the top four. `columns` is kept as the
   fallback below - if the script fails for any reason the wall still lays out,
   just column-major, rather than collapsing into one long strip. */
.wall{max-width:1520px;margin:0 auto;padding:24px 16px 70px;
  display:flex;align-items:flex-start;gap:20px}
.wall.nojs{display:block;columns:4;column-gap:20px}
.col{flex:1 1 0;min-width:0}
@media (max-width:1400px){.wall.nojs{columns:3}}
@media (max-width:1020px){.wall.nojs{columns:2}}
@media (max-width:700px){.wall{gap:0;padding:16px 12px 60px}.wall.nojs{columns:1}}
.bill{break-inside:avoid;position:relative;margin:0 0 20px;padding:19px 18px 15px;
  background:var(--paper);color:#1a1713;display:inline-block;width:100%;
  box-shadow:0 1px 0 rgba(0,0,0,.3),0 8px 20px rgba(0,0,0,.34);
  transform:rotate(var(--tilt));will-change:transform;
  transition:transform .16s ease-out,box-shadow .16s ease-out}
.bill:hover,.bill:focus-within{transform:rotate(0deg) translateY(-4px);
  box-shadow:0 2px 0 rgba(0,0,0,.34),0 16px 34px rgba(0,0,0,.5);z-index:5}
.bill:focus-visible{outline:3px solid var(--lime);outline-offset:2px}
.tape{position:absolute;top:-8px;left:50%;margin-left:-35px;width:70px;height:17px;
  transform:rotate(-1.4deg);
  background:rgba(228,216,192,.5);box-shadow:0 1px 2px rgba(0,0,0,.28)}
.bh{display:flex;justify-content:space-between;align-items:baseline;gap:10px;
  font-family:"Azeret Mono",monospace;font-size:8.5px;letter-spacing:.15em;
  text-transform:uppercase;margin-bottom:9px}
.stamp{font-weight:600;color:var(--prule)}
.rw{color:#6d645a}
.bt{font-size:22px;line-height:1.08;margin:0 0 5px;color:var(--pink);
  font-family:"Archivo Black",sans-serif;letter-spacing:-.012em;text-wrap:balance}
.bhost{font-family:"Azeret Mono",monospace;font-size:9.5px;color:#7c7268;margin:0 0 10px;
  letter-spacing:.04em}
.bhost span{color:#5c544c}
.bblurb{margin:0 0 11px;font-family:"Rokkitt",Georgia,serif;font-size:17px;line-height:1.42;color:#26211b}
.chips{display:flex;flex-wrap:wrap;gap:5px;margin-bottom:10px}
.chips i{font-family:"Azeret Mono",monospace;font-style:normal;font-size:8.5px;letter-spacing:.1em;
  text-transform:uppercase;padding:3px 7px;border-radius:2px;border:1px solid rgba(0,0,0,.2);
  background:rgba(255,255,255,.45)}
.c-in-person{background:#ffdccb}.c-paid{background:#ffe9b8}
.c-nofee{background:#ffe0d8;color:#a8321e;border-color:#e0a89c}
.c-stretch{background:#1c1a17;color:#efe9dd;border-color:#1c1a17}
.c-annual{background:#d3e6ff}
.dif{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin:0 0 11px;
  font-family:"Azeret Mono",monospace;font-size:8px;letter-spacing:.15em;text-transform:uppercase;
  color:#8a8076}
.dif b{font-weight:500}
.pips{display:inline-flex;gap:3px}
.pips i{width:9px;height:9px;border:1px solid var(--prule);border-radius:50%;display:block}
.pips i.on{background:var(--prule)}
.dw{color:#3d362f;text-transform:none;letter-spacing:0;font-size:11.5px}
/* My two ratings, on one line so the card does not become a scorecard. Kept
   visually identical to the difficulty pips because it is the same KIND of
   thing: my opinion, not the source's. */
.stand{display:flex;align-items:center;gap:6px 13px;flex-wrap:wrap;margin:0 0 11px;
  font-family:"Azeret Mono",monospace;font-size:8px;letter-spacing:.15em;
  text-transform:uppercase;color:#8a8076}
.stand b{font-weight:500}
.stand>span{display:inline-flex;align-items:center;gap:5px}
.stand .pips i{width:7px;height:7px}
.t-night .stand{color:#8a90a8}
/* THE REWARD BAND. He asked for the important facts to be on the face of the
   sticky note rather than behind the fold: "when I open the page on the
   stuckynote itself it should have the imp info, like prize, and just gains".
   On a real fly-posted bill the reward is the largest thing after the headline,
   so the metaphor pays for the change rather than fighting it. */
.gain{display:flex;align-items:baseline;gap:10px;margin:0 0 10px;padding:8px 0;
  border-top:1px solid rgba(0,0,0,.15);border-bottom:1px solid rgba(0,0,0,.15)}
.gain b{font-family:"Azeret Mono",monospace;font-size:8px;letter-spacing:.18em;
  text-transform:uppercase;color:#8a8076;font-weight:500;flex:0 0 auto;padding-top:4px}
.gain span{font-family:"Archivo Black",sans-serif;font-size:17.5px;line-height:1.16;
  color:var(--pink);letter-spacing:-.012em}
.gain span.unk{font-family:"Azeret Mono",monospace;font-size:11px;font-weight:500;
  letter-spacing:.04em;line-height:1.5}
.facts{display:grid;grid-template-columns:auto 1fr;gap:3px 11px;margin:0 0 11px;font-size:12.5px}
.facts b{font-family:"Azeret Mono",monospace;font-size:8px;letter-spacing:.13em;
  text-transform:uppercase;color:#8a8076;font-weight:500;padding-top:3px;white-space:nowrap}
.facts span{color:#3d362f;line-height:1.4}
.t-night .gain{border-color:rgba(255,255,255,.2)}
.t-night .facts span{color:#c6ccdd}
.t-night .gain b,.t-night .facts b{color:#8a90a8}
.mine{border-left:2px solid var(--prule);padding-left:11px;margin-bottom:11px}
.mine p{margin:0 0 9px;font-size:14.5px;line-height:1.5;color:#3d362f}
.mine p:last-child{margin-bottom:0}
/* DIRECT FIRST CHILD ONLY. This was `.mine b` until 7 September 2026, and it
   matched every <b> inside the why/view PROSE as well as the label that opens
   each paragraph - so an emphasised phrase mid-sentence rendered as an 8px grey
   uppercase label on its own line, silently inverting the hierarchy.
   It had never shown because no bill used inline <b> in why or view; the moment
   five did, the DREAM-Q card read "...when the timeline was actually read:" then
   "EIGHTEEN REGISTERED PARTICIPANTS" as a caption. Nothing errored, every check
   passed, and the audit cannot see it - it was found by opening the LIVE page and
   looking at it. Same bug, same fix, as the pass wall's `.mark > b`. */
.mine p > b:first-child{display:block;font-family:"Azeret Mono",monospace;font-size:8px;
  letter-spacing:.18em;text-transform:uppercase;color:#8a8076;margin-bottom:3px}
.mine p b{font-weight:600}
.view{padding-top:8px;border-top:1px dotted rgba(0,0,0,.16)}
.conf{display:flex;align-items:center;gap:6px;margin:0 0 10px;font-family:"Azeret Mono",monospace;
  font-size:8.5px;letter-spacing:.13em;text-transform:uppercase}
.conf i{width:7px;height:7px;border-radius:50%;display:block;flex:0 0 auto}
.conf em{font-style:normal;opacity:.85;letter-spacing:.06em}
.conf-verified{color:#1d6b3f}.conf-verified i{background:#1d6b3f}
.conf-listing{color:#9a6210}.conf-listing i{background:#9a6210}
.conf-stale{color:#a8321e}.conf-stale i{background:#a8321e}
.peel{width:100%;font-family:"Azeret Mono",monospace;font-size:9.5px;letter-spacing:.15em;
  text-transform:uppercase;background:rgba(0,0,0,.055);color:#2a251f;
  border:1px dashed rgba(0,0,0,.28);border-radius:2px;height:33px;cursor:pointer}
.peel:hover{background:rgba(0,0,0,.11)}
.peel:focus-visible{outline:2px solid var(--prule);outline-offset:1px}
.sheet{margin-top:12px;border-top:1px solid rgba(0,0,0,.16);padding-top:11px}
.sheet dl{margin:0}
.f{display:grid;grid-template-columns:112px 1fr;gap:3px 12px;padding:5px 0;
  border-bottom:1px dotted rgba(0,0,0,.13);font-size:13.5px}
.f:last-child{border-bottom:none}
.f dt{font-family:"Azeret Mono",monospace;font-size:8px;letter-spacing:.13em;text-transform:uppercase;
  color:#8a8076;padding-top:3px;margin:0}
.f dd{margin:0;color:#26211b}
.f.uncertain dt{color:#a8321e}
.unk{color:#a8321e;font-style:italic;font-weight:500}
.prec{font-family:"Azeret Mono",monospace;font-size:8.5px;line-height:1.65;color:#8a8076;margin:9px 0 0}
.go{display:block;margin-top:10px;text-align:center;font-family:"Archivo Black",sans-serif;
  font-size:12.5px;letter-spacing:.04em;text-transform:uppercase;text-decoration:none;
  background:var(--pink);color:var(--paper);padding:11px;border-radius:2px}
.go:hover{background:#1a1713}
.tags{display:flex;flex-wrap:wrap;gap:4px;margin-top:10px;padding-top:8px;
  border-top:1px solid rgba(0,0,0,.09)}
.tags span{font-family:"Azeret Mono",monospace;font-size:8px;letter-spacing:.08em;color:#8a8076}
.tags span::before{content:"#"}

.t-clinic{border-top:6px solid var(--prule)}
.t-clinic .bt{font-family:"Archivo",sans-serif;font-weight:600;font-size:20px;text-transform:uppercase}
.t-bulletin{box-shadow:inset 0 4px 0 var(--prule),0 1px 0 rgba(0,0,0,.3),0 8px 20px rgba(0,0,0,.34)}
.t-bulletin .bt{font-family:"Rokkitt",Georgia,serif;font-weight:700;font-size:25px}
.t-gazette{border-top:4px double var(--prule);border-bottom:4px double var(--prule)}
.t-gazette .bt{font-family:"Rokkitt",Georgia,serif;font-weight:700;font-size:23px;
  text-transform:uppercase;letter-spacing:.03em}
.t-letter{border-top:1px solid var(--prule);border-bottom:1px solid var(--prule)}
.t-letter .bt{font-family:"Rokkitt",Georgia,serif;font-weight:700;font-size:26px;text-align:center;
  padding-bottom:7px;border-bottom:1px solid rgba(0,0,0,.14)}
.t-riso{border-top:6px solid var(--prule)}
.t-riso .bt{text-shadow:1.6px 1.6px 0 rgba(79,184,255,.45)}
.t-hoard{border-top:7px solid var(--prule)}
.t-hoard .bt{text-transform:uppercase;font-size:20px}
.t-night{border-top:5px solid var(--prule)}
.t-night,.t-night .bblurb,.t-night .f dd{color:#dfe4f2}
.t-night .bhost,.t-night .rw,.t-night .f dt,.t-night .tags span,.t-night .prec,
.t-night .dif,.t-night .mine p > b:first-child,.t-night .bhost span{color:#8a90a8}
.t-night .mine p,.t-night .dw{color:#c6ccdd}
.t-night .peel{color:#dfe4f2;border-color:rgba(255,255,255,.28);background:rgba(255,255,255,.07)}
.t-night .chips i{background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.18);color:#dfe4f2}
.t-night .tape{background:rgba(255,255,255,.14)}
.t-night .unk{color:#ff9c8c}
.t-night .sheet,.t-night .view,.t-night .tags{border-color:rgba(255,255,255,.16)}
.t-night .f{border-bottom-color:rgba(255,255,255,.12)}
.t-ticket{border:2px dashed var(--prule);border-radius:5px}
.t-ticket .bt{font-family:"Archivo",sans-serif;font-weight:600;font-size:21px}
.t-stencil{border-top:5px solid var(--prule)}
.t-stencil .bt{text-transform:uppercase;letter-spacing:.05em;font-size:19px}
.t-chart{border-top:2px solid var(--prule);
  background-image:linear-gradient(rgba(0,0,0,.045) 1px,transparent 1px);background-size:100% 22px}
.t-chart .bt{font-family:"Azeret Mono",monospace;font-weight:600;font-size:17px}

.w-lastcall .stamp{background:var(--hot);color:#fff;padding:2px 6px;border-radius:2px}
/* Closing-within-the-week banner. The wall is ordered by most runway left and
   that ordering is the whole point of it, so the few things about to shut get
   lifted OUT rather than sorted to the front. Rebuilt by reweather() on every
   load, so it can never name something that closed a month ago. */
.alarm{max-width:760px;margin:18px auto 0;padding:16px 18px;border:2px solid var(--hot);
  background:#2c211d;border-radius:3px}
.alarm h2{font-family:"Archivo Black",sans-serif;font-size:15px;letter-spacing:.06em;
  text-transform:uppercase;color:var(--hot);margin:0 0 8px}
.alarm p{margin:0 0 10px;font-size:13px;color:var(--ui2)}
.alarm ol{margin:0;padding-left:20px}
.alarm li{margin:5px 0;font-size:14.5px;color:var(--ui)}
.alarm li b{font-family:"Azeret Mono",monospace;color:var(--hot);font-size:12px}
.alarm li a{font-weight:600;color:var(--ui)}
.alarm li i{color:var(--ui3);font-size:12.5px;font-style:normal}
.w-returns .stamp{background:#1f4f86;color:#fff;padding:2px 6px;border-radius:2px}
.w-evergreen .stamp{background:#2f6b3a;color:#fff;padding:2px 6px;border-radius:2px}
.w-torn{opacity:.62}
.w-torn .bt{text-decoration:line-through;text-decoration-thickness:2px}
.w-torn .stamp{background:#6d645a;color:#fff;padding:2px 6px;border-radius:2px}

.src{max-width:1120px;margin:0 auto;padding:0 18px 90px}
.src h2{font-family:"Archivo Black",sans-serif;font-size:clamp(21px,4vw,32px);text-transform:uppercase;
  color:#efe9dd;margin:0 0 6px}
.src .lede{color:#c0b5a5;margin:0 0 16px;font-family:"Rokkitt",serif;font-size:17px;max-width:62ch}
.src .key{font-family:"Azeret Mono",monospace;font-size:9.5px;color:var(--ui3);margin:0 0 18px;
  letter-spacing:.05em;line-height:1.9}
.src .key b{color:#55b06a}
.src ol{list-style:none;margin:0;padding:0;columns:2;column-gap:26px}
@media (max-width:760px){.src ol{columns:1}}
.src li{break-inside:avoid;margin-bottom:14px;padding:11px 13px;border-radius:3px;
  background:rgba(255,255,255,.04);border-left:3px solid #55b06a}
.src li.unread{border-left-color:#6d645a}
.src li a{font-family:"Archivo Black",sans-serif;font-size:14.5px;color:#efe9dd;text-decoration:none}
.src li a:hover{color:var(--lime)}
.src li i{display:block;font-family:"Azeret Mono",monospace;font-style:normal;font-size:8.5px;
  letter-spacing:.13em;text-transform:uppercase;color:var(--ui3);margin:3px 0 5px}
.src li p{margin:0;font-size:14px;color:#c0b5a5;line-height:1.45}
.nores{text-align:center;color:var(--ui2);font-family:"Azeret Mono",monospace;font-size:13px;padding:56px 20px}
.foot{max-width:1120px;margin:0 auto;padding:0 18px 80px;font-family:"Azeret Mono",monospace;
  font-size:10px;line-height:2;color:var(--ui3);border-top:1px solid var(--line);padding-top:20px}
.foot b{color:var(--ui2)}
.hide{display:none!important}
@media (max-width:700px){
  .bill{transform:none}
  .bill:hover,.bill:focus-within{transform:translateY(-2px)}
  .f{grid-template-columns:1fr;gap:1px}
  .f dt{padding-top:6px}
  .rail{gap:5px;padding:8px 10px}
  .rail input{width:118px}
  .chip{padding:0 8px;font-size:8.5px}
}
@media (hover:none){.bill:hover{transform:rotate(var(--tilt))}}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}
  .bill,.bill:hover{transform:none}}
"""

JS = r"""
(function(){
var bills=[].slice.call(document.querySelectorAll('.bill'));
var q=document.getElementById('q'), nores=document.getElementById('nores'),
    live=document.getElementById('live');
var F={dom:null,fmt:null,fee:null,run:null,conf:null,pr:null,le:null,diff:null,cash:null};
var wall=document.querySelector('.wall'), sortSel=document.getElementById('sort');

/* Ordering. The DEFAULT stays "most runway left" and that is deliberate: the
   whole project exists because a deadline-first view showed him something four
   days out. The other orders are his to choose, never the page's to assume.
   Ordering only touches the live DOM - the published source order is unchanged,
   so the weekly scout still reads the wall in runway order. */
/* ---------------------------------------------------------------- reweather
   The wall recomputes its own clocks on every load, from the deadlines baked
   into each card, before anything else runs.

   Why here rather than in the weekly cloud routine, which is how this wall used
   to do it: that routine edited the built HTML by hand, and on 5 September 2026
   it stopped being able to at all - the page passed 582 KB, so the artifact read
   began saving it to a protected path the routine was forbidden to touch, and
   two runs stalled on a permission prompt nobody was there to answer. Doing it
   in the browser means the wall is correct every time it is OPENED, needs
   nothing from any schedule, and cannot be corrupted by a bad edit. It is pure
   arithmetic over deadlines that were verified by hand - it invents nothing.

   It MUST update data-w and data-ord as well as the visible text: the runway
   filter reads data-w, and the default sort reads data-ord. Updating only what
   the eye can see would leave the filters quietly answering about last week.

   If this throws, the server-rendered values stand and the footer says which day
   they were built for. */
var WSTAMP={fresh:'FRESHLY PASTED',settling:'ON THE WALL',
            lastcall:'LAST CALL',torn:'CLOSED'};
var WORDER={fresh:0,settling:1,lastcall:2,evergreen:3,returns:4,torn:5};
var MON='Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split(' ');
function pretty(d){return d.getUTCDate()+' '+MON[d.getUTCMonth()]+' '+d.getUTCFullYear();}

function reweather(){
  var now=new Date();
  var today=Date.UTC(now.getFullYear(),now.getMonth(),now.getDate());
  var soon=[];
  bills.forEach(function(b){
    var d=b.dataset;
    /* evergreen and returns have no clock and must never acquire one */
    if(d.w==='returns'||d.w==='evergreen') return;
    if(!d.deadline) return;
    var p=d.deadline.split('-');
    var when=Date.UTC(+p[0],+p[1]-1,+p[2]);
    var days=Math.round((when-today)/86400000);
    var w=days<0?'torn':days<=7?'lastcall':days<=30?'settling':'fresh';
    d.days=days; d.w=w;
    b.classList.remove('w-fresh','w-settling','w-lastcall','w-torn');
    b.classList.add('w-'+w);
    var st=b.querySelector('.stamp'); if(st) st.textContent=WSTAMP[w];
    var rw=b.querySelector('.rw');
    if(rw){
      var u=(Math.abs(days)===1)?'day':'days';
      rw.textContent = days<0 ? ('closed '+Math.abs(days)+' '+u+' ago')
                     : days===0 ? 'closes today'
                     : (days+' '+u+' of runway');
    }
    if(days>=0&&days<=7)
      soon.push({id:d.id,days:days,
                 name:(b.querySelector('.bt')||{}).textContent||d.id,
                 when:pretty(new Date(when))});
  });

  /* Keep "most runway left" true after re-weathering, or the default order
     would still be yesterday's. Same rule the builder uses: weather bucket
     first, then most days remaining. */
  bills.forEach(function(b){
    var d=b.dataset, dd=(d.days===''||d.days==null)?0:+d.days;
    if(dd>9999) dd=9999; if(dd<-9999) dd=-9999;
    d.ord=(WORDER[d.w]||0)*100000+(10000-dd);
  });

  /* The banner is derived too, or it would name things that shut a month ago
     while the cards beside it read correctly. */
  var al=document.getElementById('alarm');
  if(al){
    var ol=al.querySelector('ol');
    if(!soon.length){ al.hidden=true; }
    else{
      al.hidden=false;
      soon.sort(function(a,b){return a.days-b.days;});
      ol.textContent='';
      soon.forEach(function(x){
        var li=document.createElement('li');
        var bb=document.createElement('b');
        bb.textContent=x.days+(x.days===1?' day':' days');
        var a=document.createElement('a'); a.href='#'+x.id; a.textContent=x.name;
        var i=document.createElement('i'); i.textContent=x.when;
        li.appendChild(bb); li.appendChild(document.createTextNode(' '));
        li.appendChild(a);  li.appendChild(document.createTextNode(' '));
        li.appendChild(i);  ol.appendChild(li);
      });
    }
  }
  var stamp=document.getElementById('asof');
  if(stamp) stamp.textContent=pretty(new Date(today));
}
try{ reweather(); }catch(e){ /* keep the values the page was built with */ }

var seq=bills.slice();
function order(mode){
  seq=bills.slice();
  seq.sort(function(a,b){
    var A=a.dataset, B=b.dataset;
    if(mode==='pr')  { if(+B.pr!==+A.pr) return +B.pr-+A.pr;
                       if(+B.le!==+A.le) return +B.le-+A.le; }
    if(mode==='le')  { if(+B.le!==+A.le) return +B.le-+A.le;
                       if(+B.pr!==+A.pr) return +B.pr-+A.pr; }
    if(mode==='use') { var sa=+A.pr + +A.le, sb=+B.pr + +B.le;
                       if(sb!==sa) return sb-sa;
                       if(+B.pr!==+A.pr) return +B.pr-+A.pr; }
    return +A.ord - +B.ord;   /* runway order, and every tie-break falls back to it */
  });
  layout();
}

/* Fill the columns shortest-first, in the current order, so the top ROW is the
   top of the order rather than the top of column one. */
function colCount(){
  var w=innerWidth;
  return w<=700?1:w<=1020?2:w<=1400?3:4;
}
var cols=[], colsFor=0;
function buildCols(n){
  cols=[]; wall.textContent='';
  for(var i=0;i<n;i++){ var c=document.createElement('div'); c.className='col';
                        cols.push(c); wall.appendChild(c); }
  colsFor=n;
}
function layout(){
  try{
    var n=colCount();
    if(n!==colsFor) buildCols(n);
    for(var i=0;i<cols.length;i++) cols[i].textContent='';
    var heights=new Array(cols.length); for(var j=0;j<heights.length;j++) heights[j]=0;
    for(var k=0;k<seq.length;k++){
      var el=seq[k];
      if(el.classList.contains('hide')) continue;
      var s=0; for(var m=1;m<heights.length;m++) if(heights[m]<heights[s]) s=m;
      cols[s].appendChild(el);
      heights[s]+=el.offsetHeight+20;
    }
  }catch(e){
    /* Never let a layout failure hide the wall. Put every card back and let the
       CSS `columns` fallback take over. */
    wall.className='wall nojs'; wall.textContent='';
    for(var z=0;z<bills.length;z++) wall.appendChild(bills[z]);
  }
}

document.querySelectorAll('.peel').forEach(function(btn){
  btn.addEventListener('click',function(){
    var s=btn.nextElementSibling, open=s.hasAttribute('hidden');
    if(open){s.removeAttribute('hidden');}else{s.setAttribute('hidden','');}
    btn.setAttribute('aria-expanded',open?'true':'false');
    btn.textContent=open?'Fold the bill back':'Read the whole bill';
  });
});

function apply(){
  var v=(q.value||'').trim().toLowerCase(), shown=0;
  for(var i=0;i<bills.length;i++){
    var b=bills[i], d=b.dataset, ok=true;
    if(F.dom && d.dom!==F.dom) ok=false;
    if(ok && F.fmt && d.fmt!==F.fmt) ok=false;
    if(ok && F.fee && d.fee!==F.fee) ok=false;
    if(ok && F.conf && d.conf!==F.conf) ok=false;
    if(ok && F.pr   && +d.pr   < +F.pr)   ok=false;
    if(ok && F.le   && +d.le   < +F.le)   ok=false;
    if(ok && F.diff && +d.diff > +F.diff) ok=false;
    if(ok && F.cash && d.cash!==F.cash) ok=false;
    if(ok && F.run){
      var w=d.w;
      if(F.run==='plenty' && !(w==='fresh'||w==='evergreen')) ok=false;
      if(F.run==='soon'   && !(w==='settling'||w==='lastcall')) ok=false;
      if(F.run==='shut'   && !(w==='torn'||w==='returns')) ok=false;
    }
    if(ok && v && d.text.indexOf(v)<0) ok=false;
    b.classList.toggle('hide',!ok);
    if(ok) shown++;
  }
  nores.classList.toggle('hide',shown>0);
  live.textContent=shown+' of '+bills.length+' bills';
  layout();
}

document.querySelectorAll('.chip[data-k]').forEach(function(c){
  c.addEventListener('click',function(){
    var k=c.dataset.k, was=F[k]===c.dataset.v;
    F[k]=was?null:c.dataset.v;
    document.querySelectorAll('.chip[data-k="'+k+'"]').forEach(function(o){
      o.setAttribute('aria-pressed',(!was && o===c)?'true':'false');
    });
    apply();
  });
});

sortSel.addEventListener('change',function(){order(sortSel.value);});

var rz;
addEventListener('resize',function(){clearTimeout(rz);rz=setTimeout(layout,120);});
/* Heights are wrong until the webfonts land, so lay out once more when they do. */
if(document.fonts && document.fonts.ready) document.fonts.ready.then(layout).catch(function(){});

var t;
q.addEventListener('input',function(){clearTimeout(t);t=setTimeout(apply,90);});
addEventListener('keydown',function(e){
  if(e.key==='/' && document.activeElement!==q){e.preventDefault();q.focus();}
  if(e.key==='Escape'){q.value='';apply();q.blur();}
});
apply();
})();
"""

PAGE = u"""<title>The Bill Wall</title>
<meta name="color-scheme" content="dark">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600&family=Archivo+Black&family=Rokkitt:wght@400;500;700&family=Azeret+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>%(css)s</style>

<div class="sky"></div>

<header class="mast">
  <h1>The Bill Wall</h1>
  <p class="sub">%(total)d bills &middot; %(verified)d verified at source &middot; %(nsrc)d sources, %(nread)d harvested &middot; %(freshness)s</p>
  <p class="say">You found Gujarat six days out. This wall exists so that never happens twice
    &mdash; so it is sorted by <b>how much runway is left</b>, never by which deadline is nearest,
    and it keeps carrying the ones that have <b>shut but come round again</b>.</p>
  <p class="pol">Every field is what a source literally printed, or the words &ldquo;not stated&rdquo; in red. Nothing is inferred.<br>
    A green dot means I opened that competition&rsquo;s own page. An amber dot means I only saw a listing.<br>
    Borderline things are kept and flagged for you to judge. Only the plainly irrelevant is left off.<br>
    <b style="color:#c8f04a">3 September 2026 &mdash; every source has now been opened</b>, including the eighteen that had only ever been named.</p>
</header>

%(lastcall)s

<div class="rail">
  <input id="q" type="search" placeholder="Search  /" aria-label="Search the wall">
  <button class="chip" data-k="dom" data-v="med"      aria-pressed="false">Medicine</button>
  <button class="chip" data-k="dom" data-v="research" aria-pressed="false">Research</button>
  <button class="chip" data-k="dom" data-v="ai"       aria-pressed="false">AI &amp; ML</button>
  <button class="chip" data-k="dom" data-v="build"    aria-pressed="false">Build</button>
  <button class="chip" data-k="dom" data-v="open"     aria-pressed="false">Anyone</button>
  <button class="chip" data-k="fmt" data-v="remote"    aria-pressed="false">Remote</button>
  <button class="chip" data-k="fmt" data-v="in-person" aria-pressed="false">In person</button>
  <button class="chip" data-k="fee" data-v="free"      aria-pressed="false">Free</button>
  <button class="chip" data-k="run" data-v="plenty"    aria-pressed="false">Plenty of runway</button>
  <button class="chip" data-k="run" data-v="soon"      aria-pressed="false">Closing</button>
  <button class="chip" data-k="run" data-v="shut"      aria-pressed="false">Shut / returns</button>
  <button class="chip" data-k="conf" data-v="verified" aria-pressed="false">Verified only</button>
  <button class="chip" data-k="pr"   data-v="4" aria-pressed="false">Big name</button>
  <button class="chip" data-k="le"   data-v="5" aria-pressed="false">Best to learn from</button>
  <button class="chip" data-k="diff" data-v="2" aria-pressed="false">Beginner</button>
  <button class="chip" data-k="cash" data-v="yes" aria-pressed="false">Cash prize</button>
  <label class="sorter"><span>Order</span>
    <select id="sort" aria-label="Order the wall">
      <option value="run" selected>Most runway left</option>
      <option value="use">Most useful to you</option>
      <option value="pr">Prestige</option>
      <option value="le">What you would learn</option>
    </select>
  </label>
  <span class="count" id="live"></span>
</div>

<main class="wall">
%(cards)s
</main>
<p class="nores hide" id="nores">No bill on the wall matches that.</p>

<section class="src">
  <h2>Where the bills come from</h2>
  <p class="lede">Your brother said there are hundreds of these. There are &mdash; but only some
     carry things you could actually enter. This is every source considered, foreign ones included,
     in the order I would check them. On <b>3 September 2026</b> all eighteen that had only ever
     been <i>named</i> were opened, and the nine already harvested were swept again for what they
     had been carrying all along. Eight platforms nobody here had heard of turned up in the
     process, and they are on this list too.</p>
  <p class="key"><b>Every source on this list has now been opened.</b> There are no unharvested ones left.<br>
     Where a source turned out to be empty, stale or behind a sign-in, the note says exactly that
     &mdash; <b style="color:#b6aa99">&ldquo;checked and empty&rdquo; is an answer</b>, and it is
     written down rather than left looking like something nobody got round to.</p>
  <ol>%(sources)s</ol>
</section>

<footer class="foot">
  <b>The Bill Wall</b> &mdash; %(total)d bills, %(live)d live, %(verified)d verified at source.<br>
  <b>Nothing here is inferred.</b> A field the source did not print says so, in red. A deadline printed as a date is marked exact; one computed from &ldquo;N days left&rdquo; is marked derived and may be a day out.<br>
  <b>&ldquo;Why it is on your wall&rdquo;, &ldquo;My view&rdquo;, the difficulty and the two ratings are my judgement</b>, not the source&rsquo;s. Argue with all of them.<br>
  <b>Prestige</b> is whether the name means anything to a medical school, a lab or a panel. <b>Worth learning from</b> is how much it would teach you for the path you are on. They are separate on purpose: the SBI scholarship is high prestige and low learning &mdash; it is money, not education &mdash; and DALPHIN is the reverse.<br>
  <b>The wall defaults to most runway left</b>, and that is deliberate: this page exists because a deadline-first view showed you something four days out. The other orders are yours to pick.<br>
  <b>The countdowns recompute themselves every time you open this page</b>, in your browser, from deadlines that were verified by hand &mdash; so they are right today whatever today is, and the &ldquo;closing within the week&rdquo; banner is rebuilt with them. Facts were read on <b>3 September 2026</b>; clocks as of <b id="asof">3 Sep 2026</b>. A countdown never goes stale, but a <i>fact</i> can &mdash; refresh the wall weekly.<br>
  Keys: <b>/</b> to search, <b>Esc</b> to clear. Filters stack.
</footer>

<script>%(js)s</script>
"""

# ------------------------------------------------------------------ last call
#
# ALWAYS emit this section, hidden when empty. reweather() rebuilds the list
# from the cards on every load and it can only do that if there is something to
# rebuild INTO - an omitted section would mean the banner silently stops working
# the first time the wall is opened on a day when nothing is closing.
soon = [b for b in bills if b['_w'] == 'lastcall']
soon.sort(key=lambda b: b['_days'])
alarm_rows = ''.join(
    '<li><b>%s day%s</b> <a href="#%s">%s</a> <i>%s</i></li>'
    % (b['_days'], '' if b['_days'] == 1 else 's', esc(b['id']), b['name'],
       pretty_iso(b['deadline']))
    for b in soon)
lastcall = ('<section class="alarm" id="alarm"%s><h2>Closing within the week</h2>'
            '<p>The wall is ordered by how much runway is left, not by what shuts '
            'first &mdash; that ordering is the whole point of it. These are the '
            'exceptions, lifted out so they cannot sink.</p><ol>%s</ol></section>'
            % ('' if soon else ' hidden', alarm_rows))

# THE MASTHEAD DATE IS DERIVED, NOT TYPED. It read "read 3 September 2026" as a
# literal in the template until 7 September 2026, while nine bills had been
# re-verified on the 7th - so the page understated its own freshness and would
# have gone on doing so for ever, because nothing recomputes a sentence.
# Global rule 7a: any date typed into copy is a duplicate of the data and drifts
# away from it, silently, with no test able to fail.
#
# TWO DATES, NOT ONE, because they are facts about different things and merging
# them would be the other half of that same rule. READ_ON is when the source
# sweep happened and must not move when a single card is re-checked; the latest
# `checked` is how fresh the freshest card is. Printing only the first makes the
# wall look stale; printing only the second implies the whole wall was re-read.
_latest = max(b['checked'] for b in bills)
_freshest = sum(1 for b in bills if b['checked'] == _latest)
freshness = 'sources read %s' % pretty_iso(D.READ_ON)
if _latest > D.READ_ON:
    freshness += ' &middot; %d re-checked %s' % (_freshest, pretty_iso(_latest))

out = PAGE % dict(css=CSS, js=JS, cards='\n'.join(cards), sources='\n'.join(src_rows),
                  lastcall=lastcall, freshness=freshness,
                  total=len(bills), live=live, verified=verified,
                  nsrc=len(D.SOURCES), nread=sum(1 for s in D.SOURCES if s['checked']))

io.open(OUT, 'w', encoding='utf-8', newline='\n').write(out)

print('written  : %s' % OUT)
print('bytes    : %d' % len(out.encode('utf-8')))
print('bills    : %d  (live %d, verified at source %d)' % (len(bills), live, verified))
print('sources  : %d  (%d harvested)' % (len(D.SOURCES), sum(1 for s in D.SOURCES if s['checked'])))
for k in ('fresh', 'settling', 'lastcall', 'evergreen', 'returns', 'torn'):
    if counts.get(k):
        print('   %-10s %d' % (k, counts[k]))
