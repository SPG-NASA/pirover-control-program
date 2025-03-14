# Pi Rover Control Program

A rudimentary program to drive the Raspberry Pi Rovers with

## Setup/Cables

### L298N -> GPIO pins:

IN1 -> 17

IN2 -> 22

ENA -> 5

IN3 -> 23

IN4 -> 24

ENB -> 6

### Powerbank configuration
// todo

## Usage

First run this on the Pi:

```python receiver.py```

Then this on the controlling computer:

```python controller.py [Rover IP]```

