# Paper Review and Revise

A free skill for Claude, with a copy-paste prompt for any other AI assistant, that reads your research paper the way a demanding but fair reviewer would, checks it against the current rules of the journal, conference or university you are aiming for, and helps you revise it. It is built for researchers and students in every discipline: the natural and physical sciences, engineering, medicine and health, the social sciences, economics and business, education, law and the humanities.

Created by Morteza Shafiei ([mortezashafiei](https://github.com/mortezashafiei)).

## What it does

- **Tests your numbers.** Recomputes the key values from your data files and confirms that the abstract, text, tables, figures and conclusions agree.
- **Reviews the whole paper.** The contribution, every section, the figures and tables (with ideas for new plots), and each reference: does the source exist, and does it support the claim it sits beside?
- **Catches contradictions.** Numbers, terms, symbols, units and abbreviations that do not match from one part of the paper to another.
- **Reads your venue's rules.** Name a journal, conference or university, and the skill opens its official author guidelines, records each requirement with its link, checks your paper against every one, and points you to the official LaTeX or Word template.
- **Edits the English.** Grammar, clarity and flow, one consistent voice, and none of the generic phrasing that makes text sound machine-written.
- **Delivers real files.** Word documents with genuine tracked changes (or a LaTeX diff), a point-by-point response to reviewers, a pre-submission checklist and a draft cover letter.
- **Never invents anything.** No made-up data, results or references. Whatever it could not verify is marked `VERIFY`.

## How to ask

| You say | You get |
|---|---|
| "Review my paper" | Three review rounds: substance and data; sections, figures and references; language. Type `next` between rounds. |
| "Review my paper for *Journal X*" | The same review, plus the journal's current requirements with their links, checked against your paper. |
| "Plan the revision" | A review and a written plan for the revision; the manuscript is not edited. |
| "Review and improve my paper" | The plan, then the revision as tracked changes, rescored by an independent reader. |
| "Format it for *Conference Y*" | The conference's current requirements, and your paper moved into its official template. |
| "Reply to the reviewers" (with their comments attached) | A revision that answers each comment, and a point-by-point response letter. |
| "Fix the English" | Language and style only. |
| "Is it ready to submit?" | A pre-submission checklist and a draft cover letter. |
| "Where should I submit this?" | Three suggested venues, each checked against its current aims and scope. |

It works on a full paper, a single section, an abstract or a thesis chapter. Request a **deep review** for three independent reviewers, or **teaching feedback** to learn why each major issue matters to reviewers.

## Your journal, conference or university

The skill reads each venue's requirements from the venue's own website every time, so the rules it applies are current. Fifteen venues come with ready-made profiles, and a publisher guide covers journals from 25 major publishers. For any other venue, you have three options:

1. **Name it in the chat.** The skill finds the official pages itself and offers to write a profile you can keep and attach next time.
2. **Add a profile to your copy of the skill.** Copy [`venues/_template.yaml`](venues/_template.yaml), fill in the official links, and save it in `venues/profiles/`.
3. **Share it with everyone.** Open a pull request with your profile; an automatic check confirms that it is valid.

The details are in [`venues/README.md`](venues/README.md).

## Install

### Claude (web and desktop app)

1. Download [`paper-review-and-revise.zip`](https://github.com/mortezashafiei/paper-review-and-revise/releases/latest/download/paper-review-and-revise.zip) from the latest release.
2. In Claude, open **Customize > Skills** ([claude.ai/customize/skills](https://claude.ai/customize/skills)).
3. Click **+**, choose **Create skill**, then **Upload a skill**, and select the zip.
4. Make sure code execution is on: **Settings > Capabilities** ("Create and edit files").

After that, open a new chat, attach your manuscript and data, and type "review my paper".

### Claude Code

```bash
git clone https://github.com/mortezashafiei/paper-review-and-revise ~/.claude/skills/paper-review-and-revise
```

Open Claude Code in the folder that holds your manuscript and say "review my paper".

### Any other AI assistant (ChatGPT, Gemini, Copilot and others)

Open [`PROMPT.md`](PROMPT.md), copy the prompt, complete the brackets, and paste it into a new chat with your files attached.

## Tips

- **Attach your data.** The data check finds the errors reviewers forgive least.
- **Name your venue early.** The format check and the template both depend on it.
- **Turn on web search**, or connect a literature tool such as Scite, so that references and venue rules are checked against real sources.
- **Protect confidential data.** Consult your sponsor's, ethics board's and data-protection rules before uploading anything.
- **Disclose AI use** if your venue requires it. The skill prompts you and inserts a placeholder for the statement.
- **Review edits individually.** You are the author, so keep whatever sounds like you.
- **Check before you submit.** AI reviewers make mistakes too, and the paper remains your responsibility.

## Adapting it to your field

- [`field-checklists.md`](field-checklists.md): what reviewers expect to see in 20 kinds of research, from laboratory and field studies, simulations and machine learning to clinical trials, economics, education, qualitative and mixed-methods work, law, the humanities and theses.
- [`venues/`](venues/): the venue profiles, the publisher guide and field lists of journals and conferences.

Fork the repository to build your own version, or open a pull request to add a checklist, a venue profile or a field list.

## What's new in version 2.0

- **Venue profiles** for 15 journals and conferences across engineering, medicine, psychology, computing, physics, chemistry, economics, linguistics and the humanities, with a template for adding your own.
- **A publisher guide** listing the official sites, guideline pages and templates of 25 publishers, and how to tell a genuine journal from a hijacked copy.
- **Live venue checks.** Every requirement is read from the venue's official site and recorded with its link and date.
- **Seven new field checklists:** chemistry and materials, life-science laboratory research, engineering design and case histories, economics and management, education, mixed methods, and law. The clinical list now follows CONSORT 2025 and SPIRIT 2025.
- **Automatic checks** that validate the skill and every venue profile whenever something changes.

## Files

| File | What it is |
|---|---|
| `SKILL.md` | The skill |
| `field-checklists.md` | Reviewer checklists by kind of research |
| `venues/README.md` | How venue profiles work and how to add one |
| `venues/_template.yaml` | A blank venue profile |
| `venues/profiles/` | Ready-made venue profiles |
| `venues/publishers.md` | Official sites, guidelines and templates of major publishers |
| `venues/lists/` | Starting lists of venues by field |
| `PROMPT.md` | The same review as a copy-paste prompt for any AI assistant |
| `scripts/check_skill.py` | Validates `SKILL.md` and the venue profiles |
| `.github/workflows/package-skill.yml` | Runs the checks and builds the upload-ready zip for each release |
| `LICENSE` | MIT License |
| `CITATION.cff` | How to cite this work |

## Cite

If the skill helps your work, please cite it. The **Cite this repository** button on this page gives the citation in APA and BibTeX formats.

## Acknowledgments

The review-and-rescore cycle is adapted from PaperOrchestra: Song, Y., Song, Y., Pfister, T., & Yoon, J. (2026). *PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing*. [arXiv:2604.05018](https://arxiv.org/abs/2604.05018).

## License

[MIT](LICENSE) © 2026 Morteza Shafiei. You may use, modify and share this skill, including in your own work, provided the copyright and license notice are kept.
