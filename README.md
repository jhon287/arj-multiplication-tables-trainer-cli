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

```shell
> python3 src/main.py --help
usage: main.py [-h] [--color {white,yellow,orange,pink,green,blue,purple,brown}]

ARJ Multiplication Tables Trainer CLI

options:
  -h, --help            show this help message and exit
  --color {white,yellow,orange,pink,green,blue,purple,brown}

> python3 src/main.py --color yellow
 0 x 10 =
 2 x 10 =
 7 x  2 =
 6 x  5 =
 8 x 10 =
 9 x  2 =
 5 x  5 =
 2 x  5 =
```

## Docker

### Build

```shell
docker build -t arj-multiplication-tables-trainer-cli .
```

### Run

```shell
> docker run --rm arj-multiplication-tables-trainer-cli --color brown
 8 x  5 =
 4 x  4 =
 0 x  9 =
 4 x  8 =
 1 x  6 =
 5 x  7 =
 4 x  9 =
 6 x 10 =
 7 x  2 =
 2 x  8 =
 5 x  2 =
 9 x  7 =
 9 x  8 =
 9 x  5 =
 6 x  7 =
 0 x  5 =
 7 x  6 =
10 x  6 =
10 x  9 =
 5 x  4 =
```
