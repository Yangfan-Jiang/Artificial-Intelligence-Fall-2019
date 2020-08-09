  (define (problem prob)
 (:domain boxman)
 (:objects p11 p12 p13 p14 p15 p16 p17 p18 
           p21 p22 p23 p24 p25 p26 p27 p28 
           p31 p32 p33 p34 p35 p36 p37 p38
           p41 p42 p43 p44 p45 p46 p47 p48
           p51 p52 p53 p54 p55 p56 p57 p58
           p61 p62 p63 p64 p65 p66 p67 p68
           p71 p72 p73 p74 p75 p76 p77 p78
           p81 p82 p83 p84 p85 p86 p87 p88 - pos
           pearl1 pearl2 pearl3 pearl4 - pearl
           m - man
           )
 (:init (wall p21) (wall p31) (wall p41) (wall p51) (wall p61) (wall p22)
        (wall p62) (wall p23) (wall p43) (wall p63) (wall p73) (wall p83)
        (wall p14) (wall p24) (wall p84) (wall p15) (wall p85) (wall p16)
        (wall p46) (wall p56) (wall p66) (wall p76) (wall p86) (wall p17)
        (wall p47) (wall p18) (wall p28) (wall p38) (wall p48)

        (clear p32) (clear p42) (clear p52) (clear p33) (clear p44) (clear p54)
        (clear p64) (clear p74) (clear p25) (clear p35) (clear p55) (clear p65)
        (clear p75) (clear p26) (clear p36) (clear p27) (clear p37) 

        (manpos p52)

        (pearlpos p32) (pearlpos p35) (pearlpos p45) 
        (boxpos p53) (boxpos p34) (boxpos p45) 


        (near p11 p12) (near p11 p21) (near p12 p13) (near p12 p22) (near p13 p14) (near p13 p23) (near p14 p15) (near p14 p24)
        (near p15 p16) (near p15 p25) (near p16 p17) (near p16 p26) (near p17 p18) (near p17 p27) (near p18 p28)
        (near p21 p22) (near p21 p31) (near p22 p23) (near p22 p32) (near p23 p24) (near p23 p33) (near p24 p25) (near p24 p34)
        (near p25 p26) (near p25 p35) (near p26 p27) (near p26 p36) (near p27 p28) (near p27 p37) (near p28 p38)
        (near p31 p32) (near p31 p41) (near p32 p33) (near p32 p42) (near p33 p34) (near p33 p43) (near p34 p35) (near p34 p44)
        (near p35 p36) (near p35 p45) (near p36 p37) (near p36 p46) (near p37 p38) (near p37 p47) (near p38 p48)
        (near p41 p42) (near p41 p51) (near p42 p43) (near p42 p52) (near p43 p44) (near p43 p53) (near p44 p45) (near p44 p54)
        (near p45 p46) (near p45 p55) (near p46 p47) (near p46 p56) (near p47 p48) (near p47 p57) (near p48 p58)
        (near p51 p52) (near p51 p61) (near p52 p53) (near p52 p62) (near p53 p54) (near p53 p63) (near p54 p55) (near p54 p64)
        (near p55 p56) (near p55 p65) (near p56 p57) (near p56 p66) (near p57 p58) (near p57 p67) (near p58 p68) 
        (near p61 p62) (near p61 p71) (near p62 p63) (near p62 p72) (near p63 p64) (near p63 p73) (near p64 p65) (near p64 p74) 
        (near p65 p66) (near p65 p75) (near p66 p67) (near p66 p76) (near p67 p68) (near p67 p77) (near p68 p78)
        (near p71 p72) (near p71 p81) (near p72 p73) (near p72 p82) (near p73 p74) (near p73 p83) (near p74 p75) (near p74 p84)
        (near p75 p76) (near p75 p85) (near p76 p77) (near p76 p86) (near p77 p78) (near p77 p87) (near p78 p88)
        (near p81 p82) (near p82 p83) (near p83 p84) (near p84 p85) (near p85 p86) (near p86 p87) (near p87 p88)

        (atline p11 p12 p13) (atline p12 p13 p14) (atline p13 p14 p15) (atline p14 p15 p16) (atline p15 p16 p17) (atline p16 p17 p18)
        (atline p21 p22 p23) (atline p22 p23 p24) (atline p23 p24 p25) (atline p24 p25 p26) (atline p25 p26 p27) (atline p26 p27 p28)
        (atline p31 p32 p33) (atline p32 p33 p34) (atline p33 p34 p35) (atline p34 p35 p36) (atline p35 p36 p37) (atline p36 p37 p38)
        (atline p41 p42 p43) (atline p42 p43 p44) (atline p43 p44 p45) (atline p44 p45 p46) (atline p45 p46 p47) (atline p46 p47 p48)
        (atline p51 p52 p53) (atline p52 p53 p54) (atline p53 p54 p55) (atline p54 p55 p56) (atline p55 p56 p57) (atline p56 p57 p58)
        (atline p61 p62 p63) (atline p62 p63 p64) (atline p63 p64 p65) (atline p64 p65 p66) (atline p65 p66 p67) (atline p66 p67 p68)
        (atline p71 p72 p73) (atline p72 p73 p74) (atline p73 p74 p75) (atline p74 p75 p76) (atline p75 p76 p77) (atline p76 p77 p78)
        (atline p81 p82 p83) (atline p82 p83 p84) (atline p83 p84 p85) (atline p84 p85 p86) (atline p85 p86 p87) (atline p86 p87 p88)

        (atline p11 p21 p31) (atline p21 p31 p41) (atline p31 p41 p51) (atline p41 p51 p61) (atline p51 p61 p71) (atline p61 p71 p81)
        (atline p12 p22 p32) (atline p22 p32 p42) (atline p32 p42 p52) (atline p42 p52 p62) (atline p52 p62 p72) (atline p62 p72 p82)
        (atline p13 p23 p33) (atline p23 p33 p43) (atline p33 p43 p53) (atline p43 p53 p63) (atline p53 p63 p73) (atline p63 p73 p83)
        (atline p14 p24 p34) (atline p24 p34 p44) (atline p34 p44 p54) (atline p44 p54 p64) (atline p54 p64 p74) (atline p64 p74 p84)
        (atline p15 p25 p35) (atline p25 p35 p45) (atline p35 p45 p55) (atline p45 p55 p65) (atline p55 p65 p75) (atline p65 p75 p85)
        (atline p16 p26 p36) (atline p26 p36 p46) (atline p36 p46 p56) (atline p46 p56 p66) (atline p56 p66 p76) (atline p66 p76 p86)
        (atline p17 p27 p37) (atline p27 p37 p47) (atline p37 p47 p57) (atline p47 p57 p67) (atline p57 p67 p77) (atline p67 p77 p87)
        (atline p18 p28 p38) (atline p28 p38 p48) (atline p38 p48 p58) (atline p48 p58 p68) (atline p58 p68 p78) (atline p68 p78 p88)
)
 (:goal 
        (and (boxpos p32) (boxpos p35) (boxpos p45))
 )
)