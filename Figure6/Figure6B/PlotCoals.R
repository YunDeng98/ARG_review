A = readLines("InferenceNew.pairwise.coal")
NAMES = c("CHB", "FIN", "GBR", "YRI"   )
scaling = .8
pdf(file = "Relate.pdf", width = 14*scaling*0.85, height = 8*scaling)  

vermilion = rgb(213/255,94/255,0) 
blue = rgb(86/255,180/255,233/255)  
orange = rgb(230/255,159/255,0)  
black =  rgb(0,0,0)  

colorsss = c( orange, black, blue, vermilion)

x = as.numeric(strsplit(A[2], " ")[[1]])
x = sort(c(x[-1] + 0.0000001 , x, 10**8))
CHB =  as.numeric(strsplit(A[3], " ")[[1]])[-c(1,2)]
CHB = rep(CHB ,each  = 2)
FIN =  as.numeric(strsplit(A[8], " ")[[1]])[-c(1,2)]
FIN = rep(FIN ,each  = 2)

GBR =  as.numeric(strsplit(A[13], " ")[[1]])[-c(1,2)]
GBR = rep(GBR  ,each  =2)

YRI =  as.numeric(strsplit(A[18], " ")[[1]])[-c(1,2)]
YRI = rep(YRI  ,each  =2)

x[1] = 1
 
plot(log10(x*28), log10(.5/CHB) , ylim = c(2,6.25), type = "l", xlab = "Years Ago",
      xlim = c(3,7), col = blue ,   axes=F,  lwd = 3, ylab = "Population Size (Ne)")
lines(log10(x*28),log10(.5/FIN ) , col =  black ,  type = "l", lwd=3 )
lines(log10(x*28),log10(.5/GBR ), col = orange , type = "l", lwd= 3)
lines(log10(x*28),log10(.5/YRI) ,col = vermilion,  type = "l", lwd= 3 )


RealXAxis2 = c(expression(10^2), expression(10^3 ), expression(10^4 ),  expression(10^5 ), expression(10^6 ) )

axis(2, at=c(2,3,4,5,6), labels=RealXAxis2)

 
RealXAxis2 = c(expression(10^2), expression(10^3 ), expression(10^4 ),  expression(10^5 ), expression(10^6 ), expression(10^7 ))

axis(1, at=c(2,3,4,5,6,7), labels=RealXAxis2)

box()


 legend("topright", lwd = 3, col = c( vermilion, blue, orange, black), legend  = c("Yoruba", "Han Chinese", "British", "Finnish"))
 
 
 dev.off()