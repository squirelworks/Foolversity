# Foolversity

Companion to Foolcourse. It makes the files. Foolcourse reads them.

For now it generates three things:

- student files, `.fcs` (Foolcourse Student)
- school files, `.school.json`
- curriculum files, the same JSON Foolcourse already reads

```bash
python3 foolversity.py student alex --name "Alex Kim" --school nida --cohort 2026-A
python3 foolversity.py school nida --name "Nida" --curriculum "Street sense" --student alex
python3 foolversity.py curriculum "Street sense" --official phone --extra reading_maps

# write into a Foolcourse tree
python3 foolversity.py student alex --out /path/to/Foolcourse
```

A later cut can enroll, roster, and lock the school file down. This cut
only generates.
