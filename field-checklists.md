# Field checklists

Reference lists for section 11 of `SKILL.md`. Choose the list or lists that fit the paper, then extend them with what a specialist reviewer in the exact subfield would expect. Each list describes what a reviewer looks for in the manuscript, not how to carry out the research.

Reporting guidelines for health, life-science and social-science studies are indexed by the EQUATOR Network (equator-network.org). Where one applies, go through it item by item against the paper. If no list here fits, build one with step 2 of section 11, and consider contributing it to the repository.

## Contents

1. Laboratory experiments in the physical sciences and engineering
2. Worked example: geotechnical laboratory and in-situ testing
3. Chemistry and materials science
4. Life-science laboratory research
5. Field and observational studies in the earth, environmental and ecological sciences
6. Computational modeling and simulation
7. Machine learning and data science
8. Engineering design, case histories and practice papers
9. Clinical and health research
10. Animal research
11. Quantitative social and behavioral science
12. Economics, finance and management
13. Education research
14. Qualitative research
15. Mixed-methods research
16. Systematic reviews and meta-analyses
17. Theoretical and mathematical work
18. Humanities and historical scholarship
19. Law and legal scholarship
20. Theses and thesis chapters

## 1. Laboratory experiments in the physical sciences and engineering

- **Standards:** every method cites its governing standard with the designation and year (ASTM, ISO, EN or BS, for example), and any departure from it is explained.
- **Materials and specimens:** origin, composition, preparation, initial state and the number of specimens.
- **Apparatus:** the equipment, its calibration, resolution and measurement uncertainty.
- **Test conditions:** loading or testing rates, temperature, humidity and boundary conditions.
- **Corrections:** each correction applied to the raw data, with its basis.
- **Repeatability:** replicate tests for each condition and the scatter among them.
- **Benchmarking:** results compared with reference materials and published data.
- **Scale:** conclusions limited to the conditions tested.

## 2. Worked example: geotechnical laboratory and in-situ testing

- **Standards:** each test follows and cites the correct standard (ASTM, ISO or BS) with its year; departures are explained.
- **Material:** USCS classification, grain-size distribution (D50, Cu, Cc), fines content, specific gravity, minimum and maximum void ratios with the standard used, and mineralogy.
- **Specimen and state:** how specimens were prepared; their initial void ratio or relative density, density and water content; saturation (B-value); consolidation and stress history (OCR, K0); the stress path; the strain or loading rate; and the drainage and boundary conditions.
- **Particle degradation:** measured before and after testing where it matters, through the change in gradation or a breakage index.
- **Corrections and conventions:** membrane, area, cone pore-pressure and comparable corrections declared and applied; one sign convention and one stress notation (σ′v, p′, q, εa) used throughout; effective and total stresses never confused.
- **Equipment:** the apparatus, how it was calibrated, and the uncertainty of each measurement.
- **Repeatability:** the number of tests per condition and their scatter; no trend inferred from single tests without saying so.
- **Benchmarking:** results compared with reference soils (quartz sand, for example) and with published data.
- **Practice:** implications for piles, pipelines, anchors and similar structures follow from the data and stay within the stress range, density and scale tested.
- **Field and in-situ data:** the site, depth and method given, together with permission to publish.

## 3. Chemistry and materials science

- **Synthesis and preparation:** procedures detailed enough to repeat, with quantities, conditions, yields and scale; hazards noted.
- **Characterization:** the identity and purity of each new compound or material shown with the evidence the field expects (NMR, mass spectrometry, elemental analysis, X-ray diffraction or microscopy, for example), with the spectra and data in the supporting information.
- **Crystal structures:** deposited in the appropriate database (the CCDC or ICSD, for example), with the deposition numbers given.
- **Measurements:** instrument, calibration, conditions and uncertainty; replicate samples or batches.
- **Performance claims:** benchmarked against the state of the art under the same, stated test conditions (catalysts, batteries and membranes are common cases).
- **Processing and testing of materials:** processing route, microstructure, specimen geometry and test standards.
- **Data:** raw data and analysis files shared where the venue asks for them.

## 4. Life-science laboratory research

- **Reporting framework:** the MDAR checklist (Materials, Design, Analysis and Reporting) where the venue uses it, and ARRIVE for work with animals.
- **Materials:** cell lines with their source and authentication; antibodies and other key resources with identifiers such as RRIDs; strains and reagents.
- **Design:** biological and technical replicates distinguished, with the number of each; randomization and blinding where relevant.
- **Statistics:** the test used, n and what n refers to, exact P values or confidence intervals, and effect sizes.
- **Images:** acquisition settings and processing stated; no manipulation that alters the meaning; original images and blots available.
- **Data and code:** sequences, structures and omics data deposited in the community repository (GenBank, PDB or GEO, for example), with accession numbers.
- **Approvals:** ethics, biosafety and permits.

## 5. Field and observational studies in the earth, environmental and ecological sciences

- **Site and period:** the location, given by coordinates or a map, the dates, and the conditions while sampling took place.
- **Sampling design:** the way sites, samples or plots were selected, the degree of replication, and the steps taken against bias.
- **Instruments:** make and model, calibration, detection limits, and quality control of the data (gaps, outliers, drift).
- **Scale:** claims matched to the spatial and temporal scale of the data; autocorrelation handled.
- **Uncertainty:** errors propagated to the reported quantities.
- **Permits:** permits for access and collection, and permission to publish data from the site.
- **Data:** placed in a repository with a persistent identifier wherever possible, in line with the FAIR principles.

## 6. Computational modeling and simulation

- **Model:** governing equations, constitutive models, assumptions and the limits of each.
- **Inputs:** every parameter with its source; the data used for calibration kept apart from the data used for validation.
- **Numerics:** the discretization, convergence with respect to mesh or time step, and the solver settings and tolerances.
- **Verification and validation:** evidence that the code solves the equations correctly (verification) and that the model reproduces independent experiments or field data (validation).
- **Sensitivity:** how uncertain parameters affect the main results.
- **Reproducibility:** the software and its version, access to the code, the input files and the random seeds.

## 7. Machine learning and data science

- **Data:** origin, size, license, collection period, preprocessing and known biases, ideally documented in a datasheet.
- **Splits:** training, validation and test sets kept apart, with no leakage through preprocessing, duplicates, or temporal or group structure.
- **Baselines:** strong baselines tuned with the same budget as the proposed method.
- **Evaluation:** metrics that suit the task and the class balance; results averaged over several seeds with their variance or confidence intervals; statistical tests whenever differences are small.
- **Ablations:** the contribution of each component demonstrated.
- **Compute:** the hardware, the training time and the extent of the hyperparameter search.
- **Claims:** generalization claims limited to the data actually tested; limitations and failure cases shown.
- **Checklists:** the venue's own checklist (the NeurIPS paper checklist, for example) and, for science that relies on machine learning, the REFORMS recommendations.

## 8. Engineering design, case histories and practice papers

- **Problem and constraints:** the need, the requirements and design criteria, the codes and standards applied, and the constraints of cost, safety, schedule and environment.
- **Alternatives:** the options considered and why the chosen one prevailed.
- **Design basis:** calculations or models, assumptions, and the safety or resistance factors used.
- **Performance evidence:** behavior measured or monitored after construction or deployment, compared with the predictions.
- **Case description:** the site or system, the timeline, the data sources and their quality; what failed as well as what worked.
- **Transferable lessons:** stated together with the conditions under which they hold, not as universal rules.
- **Permissions:** consent to publish project data, and confidentiality for clients and sites.

## 9. Clinical and health research

- **Guideline:** CONSORT 2025 for randomized trials, SPIRIT 2025 for trial protocols, STROBE for observational studies, STARD for diagnostic accuracy, TRIPOD+AI for prediction models, CARE for case reports, CHEERS 2022 for health economic evaluations, SQUIRE 2.0 for quality-improvement studies, and PRISMA 2020 for systematic reviews.
- **Registration:** trial or protocol registration number, and any departure from the registered plan.
- **Ethics:** the approving committee and its reference number, informed consent, and protection of personal data.
- **Participants:** eligibility criteria, recruitment, progress through the study (shown in a flow diagram) and losses to follow-up.
- **Outcomes:** primary and secondary outcomes specified in advance of the analysis.
- **Statistics:** justification of the sample size; handling of missing data, confounding and multiple comparisons; effect sizes with confidence intervals.
- **Harms:** adverse events reported.

## 10. Animal research

- **Guideline:** ARRIVE 2.0, at minimum the Essential 10.
- **Ethics:** the approving committee and its reference number, and the measures taken for animal welfare.
- **Design:** randomization, blinding, sample-size justification and the experimental unit.
- **Animals:** species, strain, sex, age, supplier and housing conditions.
- **Exclusions:** each animal or data point left out of the analysis, with the reason.

## 11. Quantitative social and behavioral science

- **Guideline:** APA Style JARS–Quant (apastyle.apa.org/jars) or the venue's own reporting standards.
- **Pre-registration:** whether the hypotheses and analyses were pre-registered, and any departure from the plan.
- **Sample:** the target population, sampling frame, recruitment, response rate and statistical power.
- **Measures:** validity and reliability of each scale, and the full wording of key items (in an appendix, for example).
- **Surveys:** mode of administration, question wording and order, how the response rate was calculated, and any weighting.
- **Analysis:** model assumptions tested, missing data dealt with, multiple comparisons controlled, and effect sizes given.
- **Causality:** causal wording used only where the design justifies it.
- **Ethics:** ethical approval, consent and anonymization of the data.
- **Open science:** data, code and materials shared, or the reason they cannot be.

## 12. Economics, finance and management

- **Question and contribution:** the economic or management question, and what is new relative to the closest papers.
- **Identification:** the variation that identifies the effect, the assumptions it rests on, and tests of those assumptions (pre-trends, placebo tests or instrument strength, for example).
- **Data:** sources, sample construction, variable definitions, and any data that cannot be shared, with the reason.
- **Robustness:** alternative specifications, samples, measures and standard-error choices such as clustering.
- **Magnitude:** economic significance, not only statistical significance.
- **Theory:** assumptions stated and proofs complete, in an appendix when they are long.
- **Replication:** a replication package with data and code where the venue requires one (under the AEA Data and Code Availability Policy, for example), and registration of experiments (in the AEA RCT Registry, for example).
- **Management research:** constructs defined and measured validly, and common-method bias addressed for survey data.

## 13. Education research

- **Context:** setting, level, curriculum and participants, described well enough for readers to judge transferability.
- **Intervention:** what was done, by whom, for how long, and how faithfully it was delivered (fidelity).
- **Design:** a comparison group, or the reason there is none; how groups were formed; the clustering of students within classes and schools reflected in the analysis.
- **Measures:** validity and reliability of tests, surveys and rubrics; who scored them, and whether the scorers were blind to condition.
- **Outcomes:** effect sizes with confidence intervals, and attrition reported.
- **Ethics:** approval and consent, with particular care for minors.
- **Implications for practice:** limited to the setting studied.

## 14. Qualitative research

- **Guideline:** COREQ for interviews and focus groups, SRQR, or APA Style JARS–Qual.
- **Approach:** the methodology and why it was chosen.
- **Reflexivity:** where the researchers stand and how they relate to the participants.
- **Sampling:** strategy, size and the basis for stopping (saturation, for example).
- **Data collection:** the setting, the interview guide, and how sessions were recorded and transcribed.
- **Analysis:** the coding process, who coded, how the themes were developed, and how disagreements were resolved.
- **Trustworthiness:** triangulation, member checking or an audit trail, as appropriate.
- **Evidence:** quotations that support each theme, attributed to anonymized participants.

## 15. Mixed-methods research

- **Guideline:** GRAMMS (Good Reporting of A Mixed Methods Study) or APA Style JARS–Mixed.
- **Rationale:** why the question needs both kinds of data.
- **Design:** the type (convergent, explanatory sequential or exploratory sequential, for example), with the priority and sequence of each strand.
- **Each strand:** reported to the standard of its own kind (lists 11 and 14).
- **Integration:** where and how the strands were brought together (a joint display, for example) and what the integration added.
- **Divergence:** how disagreements between the strands were handled.

## 16. Systematic reviews and meta-analyses

- **Guideline:** PRISMA 2020, including its flow diagram and checklist.
- **Protocol:** registered (in PROSPERO, for example), with any departures explained.
- **Search:** the databases and dates searched, the complete search strings, and gray literature.
- **Selection:** eligibility criteria, screening by two independent reviewers, and their level of agreement.
- **Risk of bias:** judged for every study with a named tool.
- **Synthesis:** the effect measures, heterogeneity, sensitivity analyses and publication bias.
- **Certainty:** the certainty of the evidence for each outcome (with GRADE, for example).

## 17. Theoretical and mathematical work

- **Statements:** definitions, assumptions and results formulated precisely, with the new elements identified explicitly.
- **Proofs:** complete, or sketched clearly in the text with the full proof in an appendix; no step described as obvious unless it truly is.
- **Notation:** uniform throughout, each symbol defined a single time.
- **Checks:** special and limiting cases reproduce known results, and the units are consistent.
- **Prior work:** the advance over the closest known results.
- **Illustration:** at least one worked example or numerical illustration where it helps the reader.

## 18. Humanities and historical scholarship

- **Sources:** primary sources identified exactly (archive, collection, item), with their reliability examined.
- **Translations:** the original wording supplied wherever the argument rests on it, and the translator named.
- **Argument:** a clear thesis, evidence behind each claim, and counter-arguments addressed.
- **Scholarship:** the debate the paper enters and how it moves that debate forward.
- **Citation:** the venue's style (Chicago notes and bibliography, for example), applied consistently.
- **Permissions:** rights to reproduce images and texts.

## 19. Law and legal scholarship

- **Question and jurisdiction:** the legal question, and the jurisdictions and period covered.
- **Authorities:** primary sources (constitutions, statutes, regulations, cases, treaties) cited precisely and checked against the current law.
- **Method:** doctrinal, comparative, empirical or theoretical, stated explicitly; empirical legal studies also meet the relevant empirical lists.
- **Argument:** counter-arguments and contrary authority addressed.
- **Citation:** the venue's citation system (the Bluebook or OSCOLA, for example), applied consistently.
- **Contribution:** what the paper adds to scholarship, practice or reform.

## 20. Theses and thesis chapters

- **Role:** what the chapter contributes to the thesis as a whole and how it connects to the other chapters.
- **Consistency:** terminology, symbols and notation shared across chapters.
- **Literature:** current, and not repeated in full in every chapter.
- **Contribution:** the student's own contribution stated clearly, especially for chapters based on co-authored papers.
- **Rules:** the university's formatting and submission rules, including those for chapters that are published papers.
- **Examiners:** the questions examiners are likely to ask, with the answers already in the text.
