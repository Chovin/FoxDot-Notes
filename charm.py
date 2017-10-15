# add room later
p1 >> pads([0,1,[2,2,2,3],[(3,5,7,9),(2,4,6,8),(1,3,5,7),([0,-2],2,[(4,6),5])]], room=linvar([0,2],2), dur=[.5,1,PDur(3,13)])

# then add this
c >> charm(lpf=300).follow(p1)

