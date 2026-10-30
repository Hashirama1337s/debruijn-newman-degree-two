# Explicit de Bruijn–Newman bounds below 1/2 in degree 2, and a product lemma for Dedekind zeta functions

**Moki & Julio (AI-assisted) · 2026** · DOI [10.5281/zenodo.23794434](https://doi.org/10.5281/zenodo.23794434) (v1.0)

The note is [NOTE.md](NOTE.md). The code, sealed predictions, reports and checks behind it are in [bundle/](bundle/) (start with
[bundle/README.md](bundle/README.md); public status table: [bundle/STATUS.md](bundle/STATUS.md)).

## In plain words

Every L-function carries a "heat dial" t. Turning the dial up smooths the function and pushes its zeros onto one line. The smallest
setting at which every zero already sits on the line is the de Bruijn–Newman constant Λ. The generalised Riemann hypothesis for that
L-function says Λ ≤ 0; it is known that Λ ≥ 0, and classical theory gives Λ ≤ 1/2 for free. Bounds below 1/2 were known only in "degree 1"
(the Riemann zeta function, and since October 2026 real Dirichlet characters of small conductor, in a preprint).

- We prove Λ ≤ 0.449938 for the degree-2 L-function of the modular form η(z)η(23z), and Λ ≤ 0.489938 for that of η(2z)η(22z). We found no
  earlier bound below 1/2 in degree 2.
- A short product lemma (an application of Lieb–Sokal 1981 and Borcea–Brändén; nothing new claimed for it) turns known bounds into the
  first bounds below 1/2 for Dedekind zeta functions of number fields: Λ ≤ 0.2978 for every quadratic field with discriminant between 3 and
  400 in absolute value (resting on an unrefereed 2026 preprint), and Λ ≤ 0.449938 for the cubic field of discriminant −23 and its degree-6
  Galois closure.

The gains over 1/2 are modest and nothing here bears on the Riemann hypothesis itself. Proofs were checked by independent AI reviewers,
**not yet by a human expert**. Novelty statements are a search floor (arXiv and Zenodo, 30 October 2026), not a clearance.

## Reproduce

See [bundle/README.md](bundle/README.md) for commands and software versions, [bundle/CLEANROOM.md](bundle/CLEANROOM.md) for the clean-room
record (15/15 checks; the 13-hour certified region walks were not re-run), and [bundle/REDACTIONS.md](bundle/REDACTIONS.md) for the files
whose copies were redacted (names and machine paths only) with hashes before and after.

## Licence and citation

Text and data: CC BY 4.0 ([LICENSE](LICENSE)). Code (all .gp, .py and .sh files): MIT ([LICENSE-CODE](LICENSE-CODE)).
Please cite via [CITATION.cff](CITATION.cff).
