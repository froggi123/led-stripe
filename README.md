# Led-Stripe
Controll a WS2812 LED-stripe with a raspberry pi

these examples requires rpi_ws281x

Primary target is to get used to github und lern a bit python.

## Functions

* LED Position
* KnightRider Style Light (not implemented)
* Comets (not implemented)
* SnowFall (not implemented)

### LED Position

Instead turning on and off single LED's, this function shall turn on the LEDs according a position, while distributing intermediate positions between two LED's.
Example: On Position 2, LED Nr. 2 will light with the desired strength. On Position 1.5, LED on Position 1 and 2 will light with each 50% of desired strength.
