# ARJ Multiplication Tables Trainer CLI

The purpose of this program is to train about multiplication tables from 2 to 10.

This is based on tests that have been done at "Le Petit Athénée de Jodoigne" which is part of "Athénée Royale de Jodoigne" school.

**Belt Colors**

1) ⚪️: 8 calculations on table 2 and 10
2) 🟡: 8 calculations on table 2, 5 and 10
3) 🟠: 8 calculations on table 2, 3, 5 and 10
4) 🩷: 10 calculations on table 2, 3, 4, 5 and 10
5) 🟢: 12 calculations on table 2, 3, 4, 5, 6 and 10
6) 🔵: 15 calculations on table 2, 3, 4, 5, 6, 7 and 10
7) 🟣: 18 calculations on table 2, 3, 4, 5, 6, 7, 8 and 10
8) 🟤: 20 calculations on table 2, 3, 4, 5, 6, 7, 8, 9 and 10

## How To Use It ?

This program is writen using Python so basically you only need Python installed on your workstation, nothing more as there is no library dependencies. 🎉

### Usage

```shell
# Show help
> python3 src/main.py --help
usage: main.py [-h] [--color {white,yellow,orange,pink,green,blue,purple,brown,all}] [--print-only]

ARJ Multiplication Tables Trainer CLI

options:
  -h, --help            show this help message and exit
  --color {white,yellow,orange,pink,green,blue,purple,brown,all}
  --print-only
```

### Run all in once (Marathon mode)

You can do all tables in one go by setting `--color` parameter to `all` value.

You can either do or only print (`--print-only`) all of them.

```shell
# Train all tables as small game (Marathon mode)
> python3 src/main.py --color all

# Only print calculations of all belt's colors
> python3 src/main.py --color all --print-only
```

### Train specific belt's color

```shell
# Only print calculations of yellow belt
> python3 src/main.py --color yellow --print-only
Belt Color: 🟡 (Yellow - 8 of [2, 5, 10])
 5 x  5 =
 2 x 10 =
 8 x 10 =
 0 x  5 =
 7 x  2 =
 8 x  2 =
 8 x  5 =
 5 x  2 =

# Train as a small game to gain green belt
> python3 src/main.py --color green              
Belt Color: 🟢 (Green - 12 of [2, 3, 4, 5, 6, 10])
 7 x  4 = 28
 8 x  4 = 32
 6 x  5 = 30
 9 x  4 = 36
 5 x  4 = 20
 7 x 10 = 70
 8 x 10 = 80
 1 x 10 = 10
10 x  3 = 30
 8 x  2 = 16
 7 x  5 = 35
 5 x  2 = 10
------------------------------
Result: 12/12 (100.00%)
Time: 20s of 60s (OK)
You win! 🏆🎉
```

## Docker

### Build

```shell
docker build -t arj-multiplication-tables-trainer-cli .
```

### Run

```shell
# Only print calculations of brown belt
> docker run --rm arj-multiplication-tables-trainer-cli --color brown --print-only
Belt Color: 🟤 (Brown - 20 of [2, 3, 4, 5, 6, 7, 8, 9, 10])
 3 x  7 =
 5 x  4 =
 4 x  6 =
10 x  6 =
 0 x  5 =
 2 x  2 =
 1 x  3 =
 3 x  9 =
 3 x  6 =
10 x  2 =
 6 x  4 =
 7 x  6 =
 8 x  7 =
10 x  4 =
 0 x  9 =
 1 x  4 =
 2 x  6 =
 1 x 10 =
 7 x  2 =
 7 x  5 =

# Train a small game to gain brown belt
> docker run --rm -ti arj-multiplication-tables-trainer-cli --color brown
Belt Color: 🟤 (Brown - 20 of [2, 3, 4, 5, 6, 7, 8, 9, 10])
 4 x  9 = 36
 3 x 10 = 30
 9 x  5 = 45
 8 x  3 = 24
 5 x 10 = 50
 1 x  3 = 3
 1 x  9 = 9
 7 x  7 = 49
 6 x  5 = 30
 5 x  6 = 30
 9 x  7 = 63
 8 x  8 = 64
 0 x  7 = 0
 1 x  8 = 8
 7 x  9 = 63
 3 x  5 = 15
 3 x  8 = 24
 5 x  5 = 25
10 x  4 = 40
 0 x  9 = 0
------------------------------
Result: 20/20 (100.00%)
Time: 35s of 60s (OK)
You win! 🏆🎉
```
