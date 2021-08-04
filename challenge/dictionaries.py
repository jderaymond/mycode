#!/usr/bin/env python3
char_name =input("What character do you want to know about? (Starlord, Mystique, or She-Hulk) ").title()
char_stat =input("What statistic do you want to know about? (real name, powers, or archenemy) ").lower()

marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"She-Hulk":
  {"real name": "jennifer walters",
  "powers": "super strength & intelligence",
  "archenemy": "Titania"}
             }


print("{char_name.title()}'s {char_stat} is: {marvelchars[char_name][char_stat]}")
