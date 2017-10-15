# 6 
p2 >> play('mn')

# 2 w/out Vn
# 5 add Vn
p1 >> play('--  (-(-[Vn])) --   --- ', bits=4, crush=4)

# 1 [[3,3],[7,5]] first then add
g1 >> gong([[3,3,[2,1,[1,0]]],[7,5]])  # this had more

# 3 just dur and follow
# 4 [1,0]
# 7 add stutter
u1 >> pluck(dur=PDur(3,8), room=4, verb=.5).follow(g1).every(
            [8,16], 'stutter', 4, degree=[(9,11),12,18]) + [1,0]
