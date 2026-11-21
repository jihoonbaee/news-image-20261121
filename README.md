# news-image-20261121

One image summing up the world news of **Saturday 21 November 2026**,
for the make.fun `news-image-20261121` competition.

![entry](entry.png)

## Status

**DRAFT** (built 21 Nov 2026 ~05:00 UTC). The day is not over yet: this
image covers the news verified by 05:00 UTC. It MUST be refreshed after
21 November ends everywhere, before submission (deadline 22 Nov 07:00 WIB).
See `DRAFT-BRIEF-21-nov.md` for the story list, sources, and refresh notes.

## Files

- `entry.png` — the entry image (1024×1024, ≤1 MiB).
- `main.ts` — the entry program (Node 22, stdlib only): copies `entry.png`
  to `$MAKEFUN_OUTPUT_DIR` (default `/output`).
- `render.py` — local build tool (Pillow) that draws `entry.png` from the
  `STORIES` list. Not run by the grader. Re-run after editing stories:
  `python3 render.py` (it fails loudly if any text exceeds its line budget).
- `DRAFT-BRIEF-21-nov.md` — story selection, verification, pre-registration,
  and refresh checklist.

## Verify

```sh
python3 render.py
mkdir -p out1 out2
MAKEFUN_OUTPUT_DIR=out1 node main.ts
MAKEFUN_OUTPUT_DIR=out2 node main.ts
sha256sum entry.png out1/entry.png out2/entry.png  # all three identical
```
