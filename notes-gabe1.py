# FoxDot Tutorial 1: Basics

p1 >> pluck(4) # plays a note on repeat

p1.stop() # stops p1 from playing


p1 >> pluck([0,1,2[3,5,7,9]]) # plays 0,1,2,3  0,1,2,5  0,1,2,7 (lacing)

p1 >> pluck([0,1,2,(3,5,7,9)]) # plays 3,5,7,9 together (chord)

print(SynthDefs) # print all available synths

print(Player.Attributes()) # prints player attributes

p2 >> blip(oct=4, dur=[1/2,1/2,1]) # default octave is 5. Dur is duration of each note
# changing dur while player is running, it updates real-time

Clock.clear() # stops all player objects (Ctrl + .)

print(Clock) # list of playing objects

Clock.bpm = 100 # changes tempo(default is 120)

print(Scale.names) # see all scales available

Scale.default = "major" # changes current scale

p3 >> play("x-o-") # plays sound samples. Each character is mapped to a folder of files
                   # first file is played by default

p3 >> play("x-o[--]") # string goes through a parser that allows pattern
                      # manipulation. Square brackets plays samples in one duration
                      
p3 >> play("x-o(-[--])") # plays x-o-  x-o--  x-o- (lacing) lacing here uses parentheses

p3 >> play("x-o{-[--][-o][----])}") # plays any within curly braces randomly 

p3 >> play("x-o{-[--][-o][----])}", sample=[2,3,4]) # plays other samples within folder



