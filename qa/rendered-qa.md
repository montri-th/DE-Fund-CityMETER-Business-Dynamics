# CityMETER grant explainer — rendered QA

Date: 2026-08-01  
Artifact: `index.html`  
Profile: `data.explainer`

## Pre-release checks

- Landometer v0.8.8 structural authoring preflight: pass, 0 errors, 0 warnings.
- HTML parse: pass, 0 errors.
- IDs and fragments: 39 IDs, 0 duplicates, 0 broken internal links.
- Embedded JSON: 4 scripts parsed.
- Inline JavaScript: 2 scripts parsed.
- CSS structure: 391 opening and 391 closing braces.
- Locked facts: pass; no obsolete budget total detected.
- Team links: 11 public CV links present.
- Thai copy: independent full-page review passed.
- Fact and scope review: passed after removing nationwide-sample, causality, rights, coverage, and official/internal overclaims.
- Static responsive audit: pass at 320, 360, 390, and 768 px; source ledger wraps, mobile gate fields stack, and root clipping is removed.
- Long filename and SHA row: moved behind a short disclosure; all identifier tokens use targeted `overflow-wrap:anywhere`.

## Public rendered checks

- Released URL: `https://montri-th.github.io/DE-Fund-CityMETER-Business-Dynamics/`
- Released commit: `4a3e720e23b3617720f1e57440c11be4f311771e` (squash merge of PR #2).
- Desktop viewport: 1348 × 936 px; `documentElement.clientWidth` and `scrollWidth` were both 1348 px, so root horizontal overflow was 0 px.
- Released title and H1 matched the revised decision-first copy.
- Hero and decision gradient scenes were visually inspected in light mode; white foreground copy remained legible over the deterministic scrim and both scenes retained a useful entry/closure role.
- The long project-brief filename and SHA values are closed by default behind `ดูชื่อไฟล์และรหัสตรวจสอบ`; identifier tokens resolve to `overflow-wrap:anywhere`, and the source-ledger table uses fixed layout. Static responsive inspection passed with the disclosure content present at 320, 360, 390, and 768 px.
- Decision copy toggle: passed for open and closed states, including `aria-expanded`, hidden state, and button-label change.
- Resource search: `ISO` returned 1 of 17 records.
- Resource filter: `ทีมและ CV` returned 12 of 17 records; reset to `ทั้งหมด` returned 17 of 17 records.
- Theme control: passed through light, dark, and system states with the stored preference and accessible label updating correctly.
- Evidence links: 11 public web-safe CV PDF links remained present.
- Console: no warning or error originated from the released page. Logged errors came only from the cloud-browser extension URL, not the site origin.
- Constraint: the cloud-browser viewport could not be resized for a second mobile screenshot. Mobile readiness is therefore supported by the supplied real-device screenshot diagnosis plus static responsive checks, not claimed as a cloud-rendered mobile visual test.
