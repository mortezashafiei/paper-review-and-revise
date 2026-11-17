# Venue profiles

A venue profile is a short text file that tells the skill where a journal, conference or university keeps its official requirements and templates. When you name your venue, the skill finds its profile, opens those pages, and reads the current rules: article length, abstract, structure, reference style, figures, required statements, AI policy, type of peer review and deadlines. It records each rule with its link in `venue_guidelines.md`, checks your paper against all of them, and points you to the official template.

The rules are read afresh every time, so a profile never holds limits, fees or dates that could go out of date. If your venue has no profile, simply name it: the skill finds the official pages on its own and offers to write a profile for you.

## Profiles included

| Venue | Type | Field | File |
|---|---|---|---|
| Acta Geotechnica | journal | Geotechnical engineering | [acta-geotechnica.yaml](profiles/acta-geotechnica.yaml) |
| Géotechnique | journal | Soil and rock mechanics | [geotechnique.yaml](profiles/geotechnique.yaml) |
| Canadian Geotechnical Journal | journal | Geotechnical engineering | [canadian-geotechnical-journal.yaml](profiles/canadian-geotechnical-journal.yaml) |
| Geotechnical Testing Journal | journal | Soil and rock testing | [geotechnical-testing-journal.yaml](profiles/geotechnical-testing-journal.yaml) |
| Geo-Congress | conference | Geotechnical engineering | [geo-congress.yaml](profiles/geo-congress.yaml) |
| PLOS ONE | journal | Multidisciplinary | [plos-one.yaml](profiles/plos-one.yaml) |
| BMJ Open | journal | Medicine and public health | [bmj-open.yaml](profiles/bmj-open.yaml) |
| Psychological Science | journal | Psychology | [psychological-science.yaml](profiles/psychological-science.yaml) |
| IEEE Transactions, Journals and Letters | journal family | Electrical engineering and computing | [ieee-transactions-and-journals.yaml](profiles/ieee-transactions-and-journals.yaml) |
| NeurIPS | conference | Machine learning | [neurips.yaml](profiles/neurips.yaml) |
| Physical Review journals | journal family | Physics | [physical-review-journals.yaml](profiles/physical-review-journals.yaml) |
| Journal of the American Chemical Society | journal | Chemistry | [journal-of-the-american-chemical-society.yaml](profiles/journal-of-the-american-chemical-society.yaml) |
| American Economic Review | journal | Economics | [american-economic-review.yaml](profiles/american-economic-review.yaml) |
| Digital Scholarship in the Humanities | journal | Digital humanities | [digital-scholarship-in-the-humanities.yaml](profiles/digital-scholarship-in-the-humanities.yaml) |
| Journal of Linguistics | journal | Linguistics | [journal-of-linguistics.yaml](profiles/journal-of-linguistics.yaml) |

For journals from large publishers without a profile, [`publishers.md`](publishers.md) gives the official sites, where the guidelines are kept and which templates exist.

## Adding your own journal, conference or university

### Option 1: name it in the chat

Say, for example, "review my paper for the *Journal of Example Studies*". The skill locates the official pages, records the requirements with their links, and offers you a profile file. Keep the file and attach it in later chats so the skill starts from the right pages.

### Option 2: add a profile to your copy of the skill

1. Copy [`_template.yaml`](_template.yaml) to `profiles/<short-name>.yaml`, using lowercase letters, digits and hyphens (for example `journal-of-example-studies.yaml`).
2. Fill in the official name, the other names people use for the venue, and the links to its own pages. Leave out anything you are unsure of.
3. Put the file where the skill can read it:
   - **Claude app:** add the file to the `venues/profiles/` folder of the skill, zip the skill folder again, and upload the new zip in **Customize > Skills**.
   - **Claude Code:** save it in `~/.claude/skills/paper-review-and-revise/venues/profiles/`.
4. Optionally, check the file: from the repository folder, run `python3 scripts/check_skill.py` (it needs PyYAML).

### Option 3: share it with everyone

Open a pull request that adds your file to `venues/profiles/`. An automatic check confirms that the file is valid before it is merged. If you prefer, open an issue with the venue's name and its official links instead.

## What makes a good profile

- **Official links only:** the venue's own page on its publisher's or society's site, or the conference's own site. No third-party summaries, template mirrors or copies of old guidelines.
- **No limits, fees or dates.** They change, and the skill reads them live.
- **Notes you can trace.** Each note states a stable fact that appears on one of the linked pages.
- **`last_checked`** is the date you last opened the links.
- **One venue per file.** A family of journals that share their rules, such as the IEEE Transactions, may share one file with `type: journal-family`.
- **Theses:** use `type: thesis`, name the university as the publisher, and link the graduate school's formatting guidelines and template.

## The fields of a profile

| Field | Required | What it holds |
|---|---|---|
| `name` | yes | The full official name |
| `also_known_as` | no | Abbreviations and other names used to match the venue |
| `type` | yes | journal, journal-family, conference, book-series, thesis, preprint-server or other |
| `publisher` | no | Publisher, society, organizer or university |
| `fields` | no | Subject areas |
| `issn` | no | Print and electronic ISSN, as NNNN-NNNN |
| `links` | yes | Official pages; at least one of `homepage`, `author_guidelines` or `call_for_papers`, and any other named links |
| `templates` | no | Official template links, such as `latex`, `word` or `overleaf` |
| `notes` | no | Stable, venue-specific facts |
| `last_checked` | yes | The date the links were last opened, YYYY-MM-DD |

Every link must start with `https://`.

## Field lists

The `lists/` folder holds starting lists of venues by field, used when the skill suggests where to submit. [`lists/geotechnical-offshore.md`](lists/geotechnical-offshore.md) covers geotechnical and offshore engineering. To add a list for your field, copy its layout into `lists/<field>.md`.
