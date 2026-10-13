# Foolversity

Version 1.0.0. Depends on Foolcourse 1.0.0.

Companion to Foolcourse. Separate repository, own code.
They do not import each other. They meet at files. See STANDARD.md.

For now it generates three things:

- student files, `.fcs` (Foolcourse Student)
- school files, `.school.json`
- curriculum files, the same JSON Foolcourse already reads

```bash
python3 foolversity
python3 foolversity student alex --name "Alex Kim" --school adin --cohort 2026-A
python3 foolversity school adin --name "Adin" --curriculum "Filing taxes" --student alex
python3 foolversity curriculum "Filing taxes" --official do_i_file --extra phone

# write into a Foolcourse tree
python3 foolversity student alex --out /path/to/Foolcourse
```

A later cut can enroll, roster, and lock the school file down. This cut
only generates.
