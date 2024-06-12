scaling = .8
pdf(file = "TMRCA.pdf", width = 14*scaling*0.85, height = 8*scaling)  

vermilion = rgb(213/255,94/255,0)
blue = rgb(86/255,180/255,233/255)
orange = rgb(230/255,159/255,0)
green =  rgb(0,158/255,115/255)

colorsss = c( vermilion, blue, orange, green)

YRI = scan( "YRI.csv")
YRI = log10(YRI[YRI >= 0])
 
GBR = scan("GBR.csv")
GBR = log10(GBR[GBR >= 0])

CHB = scan("CHB.csv")
CHB = log10(CHB[CHB >= 0])

Quechua = scan("Quechua.csv")
Quechua = log10(Quechua[Quechua > 0])

BREAKPOINTS = seq(-0.000001 + min(c(CHB,YRI, Quechua, GBR)), 0.000001 + max(c(CHB,YRI, Quechua, GBR)), length.out = 70)
breakbounds = c(BREAKPOINTS, BREAKPOINTS + 0.000001)
breakbounds = sort(breakbounds)
breakbounds = breakbounds[-2]
breakbounds = breakbounds[-length(breakbounds)]

YRIdens <- hist(YRI, breaks = BREAKPOINTS, plot = FALSE)$density 
plot(breakbounds, rep(YRIdens, each = 2)* (BREAKPOINTS[2]-BREAKPOINTS[1])*length(YRI) , ylab = "Frequency", xlab = "Time to Most Recent Common Ancestor (generations)",
     lwd = 3, type = "l", ylim = c(0,10001), xlim= c(2.385, 4.82),   axes=F,
     col = colorsss[1])

YRIdens <- hist(CHB, breaks = BREAKPOINTS, plot = FALSE)$density 
lines(breakbounds, rep(YRIdens, each = 2)* (BREAKPOINTS[2]-BREAKPOINTS[1])*length(CHB) , lwd = 3,type = "l", col = colorsss[2])

YRIdens <- hist(GBR, breaks = BREAKPOINTS, plot = FALSE)$density 
lines(breakbounds, rep(YRIdens, each = 2)* (BREAKPOINTS[2]-BREAKPOINTS[1])*length(GBR) , lwd = 3,type = "l", col = colorsss[3])

YRIdens <- hist(Quechua, breaks = BREAKPOINTS, plot = FALSE)$density 
lines(breakbounds, rep(YRIdens, each = 2)* (BREAKPOINTS[2]-BREAKPOINTS[1])*length(Quechua) , lwd = 3, type = "l", col = colorsss[4])
axis(2)

RealXAxis = unique(c(seq(100,1000, length.out = 10) ,
seq(1000,10000, length.out = 10) ,
seq(10000,100000, length.out = 10) ))

RealXAxis2 = unique(c(100, 200, 500, 1000, 2000, 5000,  
                      10000, 20000, 50000, 100000))

axis(1, at=log10(RealXAxis), labels = F)
axis(1, at=log10(RealXAxis2), labels=RealXAxis2)

box()

legend("topleft", legend=c("Yoruba", "Han Chinese", "British", "Quechua"), col=colorsss, lwd = 3)

dev.off()

