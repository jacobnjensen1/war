myData <- read.csv("warTrends.csv")

jpeg(filename = 'warTrends.jpg')
plot(myData$one, ylim = c(.3, .7), type = "l", col = "blue", 
     ylab = "proportion of wins", xlab = "Matches", main = "Win Trend")
lines(myData$two, type = "l", col = "green")
legend("topright", legend = c("One", "Two"), col = c("blue", "green"), lty = 1, lwd = 2)
dev.off()

