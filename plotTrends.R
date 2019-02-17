myData <- read.csv("warTrends.csv")

jpeg(filename = 'warTrends.jpg')
totalMatches <- tail(myData$one, n=1) + tail(myData$two, n=1)
plot(myData$one / (myData$one + myData$two), x=(myData$one + myData$two), xlim = c(2, totalMatches), 
     ylim = c(.3, .7), type = "l", col = "blue", 
     ylab = "proportion of wins", xlab = "Matches", main = "Win Trend")
lines(myData$two / (myData$one + myData$two), x=(myData$one + myData$two), type = "l", col = "green")
legend("topright", legend = c("One", "Two"), col = c("blue", "green"), lty = 1, lwd = 2)
dev.off()
