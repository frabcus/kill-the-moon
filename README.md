"Kill the Moon" electricity use
===============================

Introduction
------------

On 4th October 2014, the Doctor Who episode "Kill the Moon" featured a gimmick
which may or may not have caused large numbers of people to turn their lights
on or off at the same time.

This repository contains code, data and notes for an initial pass at
seeing if there was any such effect by looking at UK electricity demand.


Graph and notes
---------------

![Kill the Moon electricity graph](https://raw.githubusercontent.com/frabcus/kill-the-moon/master/out.png)

Purple is the "Kill the Moon" broadcast. Other colours are previous episodes in
the same season. Note that programmes started at varying times (see later in
this README).

The dotted line is the time at which Courtney said "night night" as the last
lights on earth visible to Clara went out - that is to say at the very end of
the voting when we might expect peak electricity.

Comparisons with previous episodes are to see if irregular jumps in electricity
are common at that time on a Saturday.


Broadcast times
---------------

Broadcast time: 20:29:10 ([source](http://twidw.doctorwhonews.net/listing.php?bdid=52388))

35:00 minutes in "night night" all the lights go out (source: iPlayer)

Which is to say at: 21:04:10

Previous Doctor Who episode start times:

* 2014-10-04 20:29:10
* 2014-09-27 20:30:00
* 2014-09-20 19:30:00
* 2014-09-13 19:30:00
* 2014-09-06 19:30:00
* 2014-08-30 19:30:00
* 2014-08-23 19:50:00



Electricity data source
-----------------------

Downloaded from the [GridWatch database](http://www.gridwatch.templar.co.uk/download.php).



