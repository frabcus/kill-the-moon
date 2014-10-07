#!/usr/bin/env python3

# Doctor Who, "Kill the Moon" electricity use

import pandas
import datetime
import numpy
import sys
import dateutil.parser

from ggplot import *
import pandas as pd

def do_date(x):
    d = dateutil.parser.parse(x)
    d = d.replace(year = 1900, month = 1, day = 1)
    return numpy.datetime64(d)

def read_file(name):
    df = pandas.io.parsers.read_csv(name, parse_dates = [2], skipinitialspace = True, date_parser = do_date)
    return df

#dfs = []
#df = read_file("2014-10-04.csv")
#df.append(read_file("2014-09-27.csv"))
#df.append(read_file("2014-09-20.csv"))
#df.append(read_file("2014-09-13.csv"))
#df.append(read_file("2014-09-06.csv"))
#df.append(read_file("2014-08-30.csv"))
#df.append(read_file("2014-08-23.csv"))

df = read_file("all.csv")

print(df.head())
print(df.describe())
print(df.dtypes)

p = ggplot(aes(x='timestamp', y='demand', color='datestamp'), df) + geom_line() #+ scale_x_date(labels = date_format("%Y-%m-%d %H:%M"), breaks='1 hour')

#for df in dfs[1:]:
#    p = p + geom_line(aes(x='timestamp', y='demand'), df, color='blue')

p = p + xlab("Time")
p = p + ylab("UK electricity demand (MW)")
p = p + ggtitle('''Electricity demand during Doctor Who episodes, comparing with "Kill the Moon"\n''')

p = p + geom_vline(xintercept=dateutil.parser.parse("1900-01-01 21:04:10"), color='black', size=1.7, linetype='--')

p = p + scale_x_date(labels = date_format("%H:%M"), breaks='1 hour')

fig = p.draw()
#ax = fig.axes[0]
#box = ax.get_position()
#ax.set_position([box.x0, box.y0, box.width, box.height])

fig.savefig("out.png")

#offbox = ax.artists[0]
#offbox.set_bbox_to_anchor((1, 0.5), ax.transAxes)
#print(fig)
#ggsave(p, "out.png")



