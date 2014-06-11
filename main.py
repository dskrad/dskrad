#!/usr/bin/env python
# A = a * e**(-lambda*time)
Tc99m = 0.11533248
F18   = 0.3788724682
from math import e
from sys import argv
from bottle import run, route, static_file, template

def dcy(isotope, activity, count=12):
  hours = xrange(count+1)
  activities = []
  ret_str = []
  for hour in hours:
    time = "{:02d} hour(s)".format(hour)
    act = activity * e**(-isotope*hour)
    activities.append((time, act))
  for activity in activities:
    ret_str.append("{} {:6.2f} mCi\n".format(*activity))
  return ret_str

@route("/<isotope>/<activity>")
def main(isotope, activity):
  if isotope == "Tc99m":
    return template("decay", content=dcy(Tc99m, float(activity)),
        header="Tc99m decay")
  elif isotope == "F18":
    return template("decay", content=dcy(F18, float(activity)),
        header="F18 decay")
  else:
    return template("decay",
        content=["Format url as", "/Tc99m/10.0 or", "/F18/12.2"],
        header="Error")

@route("/<isotope>/<activity>/<count>")
def main(isotope, activity, count):
  if isotope == "Tc99m":
    return template("decay", content=dcy(Tc99m, float(activity), int(count)),
        header="Tc99m decay")
  elif isotope == "F18":
    return template("decay", content=dcy(F18, float(activity), int(count)),
        header="F18 decay")
  else:
    return template("decay",
        content=["Format url as", "/Tc99m/10.0 or", "/F18/12.2"],
        header="Error")

@route("/<filename>")
def static(filename):
  return static_file(filename, root=".")

@route("/<anything:re:.*>")
def default(anything):
  return template("decay",
      content=["Format url as", "/Tc99m/10.0 or", "/F18/12.2"],
      header="Error")

run(server="gae")
