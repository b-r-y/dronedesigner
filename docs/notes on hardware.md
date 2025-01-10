# Notes on drone hardware selection

To ger started with FPV drones a goo controller is essential. 
I've chosen to start iwth Radiomaster Boxer after several recommendation coming form online sources.
The key decision was the ELRS open source radio it comes with.
With the main TX slected the next main thing is the Receiver.

## Total cost estimate base on [Elefun](https://www.elefun.dk/rc/hobby.aspx)

The table below is a summary of the expected cost as of July 2024.

| Item  | Unit Cost  | Units | Total Cost |
|-------| -----------|-------|------------|
| Receiver| 260      | 1     |  260 |
| Flight controller stack | 850 | 1 | 850 |
| Frame | 310 | 1 | 360|

|-------|------------|-------|------------|
|  Extras| | | | |
| Small receiver | N/A | 1 | 0 |

## Frame

For this project I'll build a 5 inch drone.

When a drone size is denoted in inches, it means the propellor size (diameter) - the general power & size class the quad falls into.

When the size is denoted in millimeters, it usually means the frame size - the largest distance between two propellor/motor centers.

5" and 4" are too big for indoor flying, 3" can be used in big halls, but for flying at home one needs a 2.5" or smaller. 
Tiny whoops can have props as small as 1.2", but there is quite a bit of variation.

For this project I will use the open source [TBS Source One V5 5inch](https://www.team-blacksheep.com/products/prod:sourceone_v5) from [Elefun](https://www.elefun.dk/p/prod.aspx?v=56809).

## Receiver selection
The receiver has to be of course ELRS one but on the Flight Computer side there is some choice on what to do.
Following this [overview](https://oscarliang.com/rc-protocols/) i've chosen to go with CRSF protocol.
The features important for a receiver are:

* TCXO for stability
* PA for telemetry
* LNA for range
* Antenna diversity
* size is also important depending on the size of drone.

The main points above a present on most good receivers.
It seems mostly the diversity type is significant.
So i have selected to get two types:

1. True diversity receiver for best range (one of the two below depending on price at the time of purchase):

    * [RP4TD ExpressLRS 2.4GHz True Diversity Receiver](https://www.radiomasterrc.com/products/rp4td-expresslrs-2-4ghz-diversity-receiver) - about 260 DKK at [Elefun.dk](https://www.elefun.dk/p/prod.aspx?v=62256)
    * [BetaFPV SuperD](https://betafpv.com/products/superd-elrs-2-4g-diversity-receiver)
2. Something with integrated antenna for minimum size:

    * [RP2 V2 ExpressLRS 2.4ghz Nano Receiver](https://www.radiomasterrc.com/products/rp2-expresslrs-2-4ghz-nano-receiver?variant=46464165380327)

## Flight controller / Stack
 The flight controller can be combined with an ESC (Electronic Speed Control) and it is then called stack.
 The controller runs a bunch of sensor and input loops and prepares the motor signal, while the ESC is effectively a motor driver/modulator.

I have currently selected this stack: [SpeedyBee F405 V4 BLS 60A 30x30 FC&ESC Stack](https://www.speedybee.com/speedybee-f405-v4-bls-60a-30x30-fc-esc-stack/)

The size is 30x30 and it will probably fit on whatever 5 inch or bigger frame i get.

Current price is around 850 DKK from [Elefun](https://www.elefun.dk/p/prod.aspx?v=63420).

## Motors

As with many other fields I'll use brushless motors.


# References

[Elefun](https://www.elefun.dk/rc/hobby.aspx) - nice norwegian shop.

[Oscar Liang](https://oscarliang.com/) - great guides on everything FPV.



