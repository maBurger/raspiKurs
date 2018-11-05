rrdtool graph tempweek.png -s 'now - 24 hour' -e 'now' DEF:temp0=temperature.rrd:temp0:AVERAGE LINE2:temp0#0000FF:Schreibtisch
exit 1
