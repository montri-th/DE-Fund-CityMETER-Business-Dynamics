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

Pending deployment of the release branch. Record the final URL, viewport, overflow metrics, theme, disclosure, search/filter, and decision-toggle tests here before merging to production.
