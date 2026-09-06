# Bandit Write-up — Levels 0 to 10

## Overview

This write-up documents the commands and approach used to solve OverTheWire Bandit Levels 0–10.

## Passwords

| Level | Password |
|---|---|
| Level 0 → Level 1 | `6y2kwnwK6grgvwvpVLaaT2IcpFEKOhNR` |
| Level 1 → Level 2 | `PK8fYLZg2hnHSz83pBLliEPKdD3QToB` |
| Level 2 → Level 3 | `7ZZ2LFrykP2zEyvBl4m3clcL7tGYJPME` |
| Level 3 → Level 4 | `xzTXq1rDJQVVAzdv5cHq1TQytTWufAMq` |
| Level 4 → Level 5 | `6C7h9GD8M6ai5nr7wo1RonrzFjj9yIrG` |
| Level 5 → Level 6 | `pXa26xhMWaC2SvDotA4r9EgZkulOeSBW` |
| Level 6 → Level 7 | `Bmnnvf82KzQlfxgAI2d1zYbr1u9pr3E3` |
| Level 7 → Level 8 | `VR1IjMayciFxbnUokuQmJFw6QCVKtub` |
| Level 8 → Level 9 | `EjmOSvuAu7sGAHqHVcBDPirReT03kxl` |
| Level 9 → Level 10 | `B0s2khmbT9u0geKuOoVGW3JZKhndE3BG` |
| Level 10 → Level 11 | `pyfOY6HwUsDj5rL9UvyhU7MCmv8vN5Ro` |

## Level 0 → Level 1

### Objective

Log in to Bandit and read the file containing the password for the next level.

### Command

```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220
cat readme
```

### Password

`6y2kwnwK6grgvwvpVLaaT2IcpFEKOhNR`

### Technique

The level stores the password in a normal text file named readme. `cat` displays its contents.

## Level 1 → Level 2

### Objective

Read a file whose name is `-`.

### Command

```bash
cat ./-
```

### Password

`PK8fYLZg2hnHSz83pBLliEPKdD3QToB`

### Technique

A filename beginning with `-` can be interpreted as a command-line option. Prefixing it with `./` tells the shell that it is a file path.

## Level 2 → Level 3

### Objective

Read a file containing spaces in its filename.

### Command

```bash
cat "./--spaces in this filename--"
```

### Password

`7ZZ2LFrykP2zEyvBl4m3clcL7tGYJPME`

### Technique

The filename contains spaces, so it must be quoted (or the spaces can be escaped).

## Level 3 → Level 4

### Objective

Find and read the hidden file in the `inhere` directory.

### Command

```bash
cd inhere
find . -maxdepth 1 -type f -exec cat {} \;
```

### Password

`xzTXq1rDJQVVAzdv5cHq1TQytTWufAMq`

### Technique

Hidden files normally begin with `.`. The search locates the file in `inhere` and prints its contents.

## Level 4 → Level 5

### Objective

Find the human-readable file among several files.

### Command

```bash
cd inhere
file ./*
```

### Password

`6C7h9GD8M6ai5nr7wo1RonrzFjj9yIrG`

### Technique

The `file` command identifies the type of each file. This avoids manually opening every file.

## Level 5 → Level 6

### Objective

Find the only file with the required size and properties.

### Command

```bash
find . -type f -size 1033c ! -executable
cat ./<identified-file>
```

### Password

`pXa26xhMWaC2SvDotA4r9EgZkulOeSBW`

### Technique

`find` filters regular files by exact size and excludes executable files.

## Level 6 → Level 7

### Objective

Find a file somewhere on the server with the specified owner, group, and size.

### Command

```bash
find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null
cat <path>
```

### Password

`Bmnnvf82KzQlfxgAI2d1zYbr1u9pr3E3`

### Technique

The search starts at `/`; `2>/dev/null` suppresses permission errors. The filters match the required owner, group, and size.

## Level 7 → Level 8

### Objective

Find the password on the line associated with the word `millionth` in `data.txt`.

### Command

```bash
grep millionth data.txt
```

### Password

`VR1IjMayciFxbnUokuQmJFw6QCVKtub`

### Technique

`grep` searches text for a matching pattern and returns the relevant line.

## Level 8 → Level 9

### Objective

Find the line in `data.txt` that occurs only once.

### Command

```bash
sort data.txt | uniq -u
```

### Password

`EjmOSvuAu7sGAHqHVcBDPirReT03kxl`

### Technique

`uniq -u` identifies unique lines after sorting makes equal lines adjacent.

## Level 9 → Level 10

### Objective

Find the human-readable string in a binary-looking file.

### Command

```bash
strings data.txt | grep "="
```

### Password

`B0s2khmbT9u0geKuOoVGW3JZKhndE3BG`

### Technique

`strings` extracts printable sequences and `grep` filters for strings containing `=`.

## Level 10 → Level 11

### Objective

Decode the Base64-encoded contents of `data.txt`.

### Command

```bash
base64 -d data.txt
```

### Password

`pyfOY6HwUsDj5rL9UvyhU7MCmv8vN5Ro`

### Technique

The file contains Base64-encoded data; `-d` tells `base64` to decode it.

## Commands / Techniques Learned

| Level | Main technique |
|---|---|
| 0 | `cat` |
| 1 | Handling filenames beginning with `-` |
| 2 | Quoting filenames containing spaces |
| 3 | Hidden files and directory search |
| 4 | File identification with `file` |
| 5 | Searching with `find` |
| 6 | Advanced `find` filters |
| 7 | Text search with `grep` |
| 8 | `sort` + `uniq` |
| 9 | `strings` + `grep` |
| 10 | Base64 decoding |

## Conclusion

Levels 0–10 introduced practical Linux command-line and basic data-analysis techniques.
