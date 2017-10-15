b1 >> bass([0,1,(0,2),(-1,1),[0,16,0,24]], dur=[4], amp=.5)


l1 >> piano(bpm = 120,dur = [1/4,1/4,1/2,1/4,1/4]).follow(b1) + [1,10,12,(11,15)]


b1 >> bass([0,-2,1], dur=8, verb=8, room=.2)

p1 >> piano(dur=P[.5,1,1,.5,1], amp=PRand([2,3,2.5,2.2,1.7]), lpf=800).follow(b1
            ) + [(2,4,8), (2,4,8), (2,4,8), (2,4,[11,12,[13,16],14,15,16])]
            
p2 >> pluck(dur=PDur(3,12), amp=linvar([.2,.8],[4])).follow(b1).every(1, 'stutter',8) + [7,8,(9,[11,12,15,(11,13)])]


.every(1, 'stutter',8) + [7,8,(9,[11,12,15,(11,13)])]

# bossa nova
b1 >> bass(PRand([0,1,4]) + [0,7,-3,-5], amp=0, dur=8,bpm=130)

p2 >> piano(bpm=130, dur=P[.5,1,1,.5,1], lpf=800, amp=PRand([2,3,2.5,2.2,1.7]), oct=4).follow(b1
            ).every(PRand([12,16,4,32]), 'stutter', PRand([5,6]), degree=( 
                    # because of an issue, can't do [7,8,9,[11,13,15]]
                    # so sprinkle these in by commenting/uncommenting
                    # b1.degree + [7,8,9,11]
                    # b1.degree + [7,8,9,13]
                    # b1.degree + [7,8,9,15]
                    # b1.degree + [7,15]
                    # b1.degree + [7,13]
                    b1.degree + [7,11]
                    # because of an issue, everys can't stack, put it on a separate line
                    )) + [([2,(-1,2)],4,8),0,(2,4,8),-3,(2,4,8)]
                    # don't forget ^ this (-1, 2) after
                    
p2.every(40, 'stutter', 8, degree=[11,9,7,3])
 
# can't find a way around the degree [[]] problem in stutter and no stacked every's               
a = P[P[1,3],[2],P[3,1]]

p3 >> piano([0,1], dur=2).every([8,16], 'stutter', PRand([8,4]), degree=a)

# not sure bout this one
v1 >> blip(bpm=130, dur=[2,.5,1,.5,4], amp=linvar([0,0,0,0,0,0,0,0,.2,1,.5,0],8), oct=5, room=2).follow(b1
          ).stop() + [[(6,8),8],5,[(4,6),7],[3,11],[5,(5,7,10)]]

print(SynthDefs)

print(Player.Attributes())
