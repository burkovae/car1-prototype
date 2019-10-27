
# 2019-10-27 Moving stuff around

In the little time I had over past months, 
I now have gathered all the prototype code and will
slowly but steadily move functionality into a repository.

So basically I have now a semi-working servo motor and
a semi working distance sensor. At least the parts
work separately - the big goal is to bring them all together
into working hardware. With that in mind it is time to give 
the project some structure.

First short term goal: combine Standard Firmata protocol
with the VL53L0X so that I can read sensor data as well
as control the motor in parallel.