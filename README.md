# Arcesium in Private Credit: Where to Push Next

An outside-in strategy project by **Andres Farrulla** (Economics, Accounting concentration, Stony Brook University), built in November 2026 alongside an application for Arcesium's Corporate Strategy Intern role.

**Recommendation:** Arcesium should make asset-based finance (ABF) the lead of its private credit strategy and position itself as the neutral system of record for loan-level data. In the base case, that push adds about **$19.5M in new annual recurring revenue within five years** (illustrative, see assumptions).

## What's in this repo

| Path | What it is |
| --- | --- |
| [`memo/Andres_Farrulla_Arcesium_Private_Credit_Memo.pdf`](memo/) | Two-page strategy memo with the recommendation, evidence, sizing and risks. Every figure links to its source. |
| [`model/Arcesium_Private_Credit_ABF_Model.xlsx`](model/) | Revenue scenario model. Switch Low / Base / High in `Assumptions!C4`. Tabs: README, Assumptions, Model, Scenarios, Sensitivity. |
| [`model/build_model.py`](model/build_model.py) | Python (openpyxl) script that generates the workbook, so every formula and source is reproducible. |
| [`research/research_report.md`](research/research_report.md) | Full research report: Arcesium profile, market sizing, competitor landscape, gaps and opportunities, with a 24-row assumptions table. |
| [`research/notes/`](research/notes/) | Raw notes from each research agent (company, market, incumbents, specialists). These came before fact-checking; the report and memo are the verified versions. |
| [`ESSAY.md`](ESSAY.md) | Why I built this project and what I learned. |

## How it was built

1. **Research agents.** Four AI agents ran in parallel, each assigned one area: Arcesium, market size, large incumbents (SS&C, Clearwater, State Street, BNY, FIS, Broadridge), and specialists and fund administrators (Allvue, Hypercore, Chronograph, 73 Strings and others).
2. **Verification.** Every figure used in the memo was checked against its original source page. That pass corrected several errors in the agents' output, including a mislabeled competitor, BNY's private credit offering and the State Street Alpha launch wording.
3. **Model.** Managers by AUM tier × Arcesium win rate × annual contract value, summed across tiers. A five-year build adds a client ramp and net revenue retention, and a sensitivity grid flexes win rate against contract value.
4. **Memo.** The findings were boiled down into one recommendation on two pages.

## Key findings

- Private credit reached **$4.1T in 2025** (AIMA/ACC). BlackRock and Preqin both project about **$4.5T by 2030**.
- ABF was **16% of 2024 deployment**, and PwC's 2026 survey ranks it among the most attractive strategies.
- Arcesium already runs a full consumer ABF lifecycle for **Neuberger Berman Specialty Finance**, launched **Arcesium Intelligence** (100+ agents) in May 2026, and integrated with **Hypercore** for loan servicing data in June 2026.
- Its main threat is **Clearwater**, which bought Beacon and Bistro and was taken private for **$8.4B** in June 2026.
- **Win rate and deal size drive the outcome far more than market growth.** Even the high case is under 3% of estimated private credit software spend.

## Caveats

This is an outside view built only from public sources. Manager counts by AUM tier, Arcesium win rates and contract values are **my estimates**, because none are public, and they're labeled that way throughout. Arcesium does not disclose revenue or client counts. Nothing here is affiliated with or endorsed by Arcesium.

## Contact

Andres Farrulla · Stony Brook University, Class of December 2026
