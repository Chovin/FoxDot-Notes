#### Jam sesh 10/16/2017 ####

# variable Vocab
# p => percussion,m => melody,b => bass

# global tempo
Clock.bpm = 160

# instruments
print(SynthDefs)

# tone shapers
print(Player.Attributes())

print(Clock)

############################################# percussion ###############################################

p1 >> play(['xxoxxxoo'], dur=[0.25,0.25,0.5,1,1,0.5,1,1], amp=2.5, lpf=2000) 

p2 >> play(P['((V-) )--'], dur=[1,1,.5,.5,1], sus=16) # why this no work  # wtf

p3 >> arpy(sus=linvar([.3,2],32), pan=(linvar([1,-1],32),linvar([-1,1],32)) )  # no. lol

#############################################  bass ##################################################

dd >> dub([0], slide=10, slidefrom=11, dur=[.5], amp= 1 if p6.degree=='V' else 0) # this is an unprecedented tone # mario baby :P # what #interesting



b1 >> bass([0,-2,1], dur=8, verb=8, room=.6, amp=2)

########################################## melody and leads ############################################

# brb, imma floss through this soothing music :P SAVE
# i think im gonna call it a night. Want me to put this up on the repo? yesh please, I have a folder up for jam seshs. Will do sir!

m1 >> arpy(dur=P[20,18,15,10], amp=10, lpf=300, sus=60).every(
           94.5, 'stutter', 32, degree=[5,6,7,9], amp=linvar([10,.5],[16, 78.5])
           ).follow(b1) + [(2,4,8), 11, (4,6,10,(-7,-7)), (11,13)] # woops

k1 >> scatter([-2], amp=linvar([.5,1.5], 4)) # im gonna title this "lofi sesh" -u-

# good sesh. good night. lofi richness. night!

m3 >> ripple([-2,-2,0,2,-2], amp=linvar([0,4,4,4,0],[94.5,16,16,32,30.5]), dur=[94.5,16,16,32,30.5], oct=4)   # will this work without a degree? # should # try ripple

s2 >> piano(dur=P[.5,1.5,1.5,.5,1,.5,.5,.5], lpf=600, amp=var([2,2,0,2],[20,18,15,10])).follow(b1).stop() + [7,6,9,8,7,6,[4,5],6,7] # meh naw dude it sounds sweet through the dark rhythm
   
m2 >> soprano(sus=1,amp=linvar([.3,.8], [36,12]), vib=linvar([1,2],.75), pan=linvar([-1,1],16)
              ).follow(h4) + var([0,(0,3)],32) # nice oh shet damn niiiiiiice

# lol dangit it deleted more than I selected
# damn haha
# let me rename the variables to reasonable names
