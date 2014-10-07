"Kill the Moon" electricity use
===============================

WARNING: Contains spoilers for this Doctor Who episode.


Introduction
------------

On 4th October 2014, the Doctor Who episode "Kill the Moon" featured a gimmick
which may or may not have caused large numbers of people to turn their lights
on or off at the same time.

This repository contains code, data and notes for an initial pass at
seeing if there was any such effect by looking at UK electricity demand.

[My comment](http://feelinglistless.blogspot.co.uk/2014/10/kill-moon.html#comment-1621665672)
on Stuart Burns' review of the episode kicked me off investigating this:

> Ha! So I was on the Doctors side with Clara's anger. We as humanity do and are
> having to take decisions as big as not killing the moon whether we like it or
> not. Clara represented our current global non-strategic take on this for me -
> whining wish that there was a God or similar to help us do hard things. (Rather
> than allowing global poverty, no space exploration and yes climate change.)
> 
> I hated the Base under siege part, dull and unformed. And the gravity thing was
> so nonsense I couldn't suspend disbelief.
> 
> I absolutely *loved* the lights on and off bit. Genius. We were watching in the
> dark on the sofa. I wanted to save the creature, my partner didn't. That and it
> being comfy on the sofa, meant we chose not to get up and turn the light on.
> 
> So in a way, I personally failed nearly as much as Clara nearly failed.
> 
> I don't know if on Saturday night you could see the viewing public deciding
> from the international space station. And my vote was spread out a day later by
> iPlayer. But whatever the flaws, is was so interactive in such a clever way.
> Fun and simple for kids and adults - did families have an argument and fight
> over the light switch? Yet with a real hard moral and practical choice behind
> it.
> 
> Cheesey yes, and for me completely novel and fun. The more I think about it,
> the more I respect the Doctor for making me choose.  


Graph and notes
---------------

In this graph, the purpley pink at the top is the "Kill the Moon" broadcast.
Other colours are previous episodes in the same season. Note that programmes
started at varying times (see later in this README).

Comparisons with previous episodes are to see if irregular jumps in electricity
are common at that time on a Saturday.

The dotted line is the time at which Courtney said "night night" as the last
lights on earth visible to Clara went out - that is to say at the very end of
the voting when we might expect highest/lowest electricity.

![Kill the Moon electricity graph](https://raw.githubusercontent.com/frabcus/kill-the-moon/master/out.png)


Analysis
--------

There was an increase of 560 MW between the two data points at 20:51:24 and
20:57:52. This is a little bit too early - Clara first says "turn your lights
off" at 33:15 minutes in, which is to say at 21:02:25. That said, clocks and
timings could easily be off - I don't have an error bar!

After the spike, there is then a dropoff back to trend with a similar rate to
previous weeks.

Also, note there is a shorter spike, of similar magnitude, slightly earlier at
20:41:06. That's far too early to be due to Clara. It isn't clear if this is
all some other distortion on the day.

Considering the first spike again... Suppose everyone is turning off a 40W bulb
(that's Fermi estimate near enough - living room lights probably have more
lumens on average than a conventional bulb of that wattage, but lots of people
will be using efficient lights now), 560 MW would be 14000 households.


Conclusion
----------

All told - visually, the graph is very compelling that electricity use during
"Kill the Moon" was different from previous weeks. 

There's no real way to be sure it was because of Doctor Who - correlation
doesn't indicate causation, and there are a few reasons to be suspicious.

Nevertheless, I like to think that by 14000 households, somewhere in space and
time, a small island of humans saved a space creature.


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

Thanks to [Owen Boswarva](https://twitter.com/owenboswarva/status/519403407434866688) for
telling me about this source, and plotting the first graph.


Technology
----------

I used this as an excuse to play with ggplot in Python. It's very good, but not
as mature as say Pandas and Matplotlib (which it depends upon). In particular,
not enough documentation. And a bug that means it isn't showing the legend
at all.




