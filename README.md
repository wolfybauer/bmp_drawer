# BMP DRAWER

## WHY

needed a tool to draw monochromatic sprites as arrays of bits. like for embedded displays, etc.

## DEPENDENCIES

should only need pygame and pysimplegui:
`pip3 install pygame pysimplegui`

## COMMANDS

- left mouse: black (1)
- right mouse: white (0)
- H: flip horizontal
- V: flip vertical
- S: save

## OUTPUT

you can specify a name for your array/list at start of program, if so desired. else will use file name as array/list name.

- raw unformatted: .txt , just commas and spaces. one big line
- raw formatted: .txt , same but with newlines for prettiness
- c header: .h , pragma once + formatted array
- python list: .py , just a list in a py file

## IMMEDIATE TODO LIST

- implement R: rotate 90
- implement H: help screen
- refactor some stuff
- add ability to open and edit/append files
- add more colors
- tools: fill, line, square, circle
- maaaybe layers, onion skinning etc