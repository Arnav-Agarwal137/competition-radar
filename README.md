# Competition Radar

Two wall-shaped pages that exist because I found a competition **six days before
its deadline** and believed I could have won it with a month.

**Lead time is the product.** A page that surfaces something four days out has
failed at its only job.

### The Bill Wall — things you enter and might win
Competitions, hackathons, challenges, shared tasks. **141 entries.**

### The Pass Wall — things you walk into and come out marked by
Seminars, workshops, schools, fellowships, courses, memberships, peer review,
citizen science, grants and roles.

Both are live: see the **Pages** link on this repository.

---

## Why it looks like a wall of posters

The obvious design for "a list of competitions" is a leaderboard or a trophy
shelf, which is why most such pages look identical. But the thing this exists to
prevent is **a notice you did not see in time** — and the form built entirely
around notices appearing and expiring is a **fly-posted bill wall**.

Choosing the metaphor from the *wound* rather than the *subject* paid for itself
three times:

- Every item wants its own look — posters are *supposed* to differ.
- **Urgency lives in the material, not a badge.** A fresh bill is crisp; one
  running out of runway is sun-faded and curling; an expired one is torn. You
  feel it before you read it.
- A bill shouts its reward and whispers its terms, which is exactly the right
  hierarchy for a prize and its eligibility rules.

## How the walls handle

| | |
|---|---|
| **One-tap filter chips** | Bills: *Closing · Big name · Best to learn from · Beginner · Remote · Research · Medicine · Anyone*. Passes adds *Fellowship · Grant · Course · Conference · Certification · Membership · Ambassadorship · Community · Comes round · Bengaluru* |
| **Sort by "Most useful to you"** | Not by deadline or prize — by a judgement of what is actually worth your time. *Prestige* is the other axis |
| **Press `/` anywhere** | Jumps straight into search without touching the mouse |
| **Press `Escape`** | Clears the search and puts the whole wall back |
| **Filters as you type** | Debounced, so the wall re-flows while you think |
| **Sorting and filtering** | By deadline, by reward, by what you are eligible for |
| **Phone layouts** | Both walls are built for a phone, not shrunk onto one |
| **One file each** | **Bill Wall 779 KB, Pass Wall 355 KB** — every entry embedded, no server, works offline |

## What is actually hard about this

Not the page. **The data.** Almost every mistake this project has made was a
verification failure, and they are all written down in the source:

- **An index is not a source.** A listing said "accepting submissions" for three
  things that had closed a year earlier. One aggregator said "active" about a
  competition whose registration shut four months before.
- **A page that renders beautifully tells you nothing about whether it is alive.**
  One institute's events page returned thirty-nine perfectly formatted, fully
  dated events — every one of them from **2016**.
- **"Not stated" is a claim about how much of the source you opened**, not a fact
  about the source. One entry recorded a requirement as unstated while the site's
  own Tasks tab specified it exactly; seven sibling tabs had never been read.
- **A prize was published fifty-three times too large**, read off a page nobody
  opened properly. Every figure now carries how it was obtained.

So each entry records **when it was checked**, **how confident** that reading is
(`verified` / `listing`), and **how precise** the deadline is (`exact` /
`derived`). Where something could not be reached, the wall says which kind of
failure it was — refused, timed out, 404, a bad certificate chain, or a 403 that
is a fact about *the fetcher*, not the host.

## Layout

```
bills/index.html     The Bill Wall  - built page
passes/index.html    The Pass Wall  - built page
src/bills_*.py       Entry data, by domain
src/passes.py        Pass data
src/data.py          Assembles and validates the bills
src/judgement*.py    Per-entry ratings
src/build*.py        Renders the pages
```

Data and rendering are deliberately separate, and `data.py` **refuses to build**
when a derived flag disagrees with its own source text — six entries whose text
said "no fee" had been silently filed as paid, so that is now an assertion rather
than a habit.

---

## These are built for one person, on purpose

The commentary on each entry is written **to me** — my age, my subject, my
constraints, what I should do about that specific competition and why. That is
not a leak, it is the point: a generic list of competitions is worth very little,
and a judged one is worth a lot.

**If you want a wall built around your own situation, ask me.** It is the same
machinery pointed at a different person.

## Licence

Free noncommercial use and private improvements are permitted for newly licensed original work.
Share the official links freely. Redistributing copies, publishing modified versions, public mirrors,
rebranding, and commercial use require Arnav Agarwal's prior written permission.
Keep authorship and required notices. This is a source-available custom licence, not an open-source licence.
Earlier licence grants and third-party rights remain in force; see [LICENSE-HISTORY.md](LICENSE-HISTORY.md).
Previously published source, embedded app notices, tags and downloadable binaries retain their earlier grants;
this policy does not retroactively prohibit their previously permitted use or distribution.

Full terms: [LICENSE](LICENSE). Permission requests: [GitHub issues](https://github.com/Arnav-Agarwal137/competition-radar/issues).

Check every deadline at its official source before acting on it.

Built by [Arnav Agarwal](https://github.com/Arnav-Agarwal137).

