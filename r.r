# Load necessary libraries
library(tm)
library(SnowballC)

# Load dataset
data <- read.csv("sentiment_data.csv")

# Preprocessing
corpus <- Corpus(VectorSource(data$text))
corpus <- tm_map(corpus, content_transformer(tolower))
corpus <- tm_map(corpus, removePunctuation)
corpus <- tm_map(corpus, removeNumbers)
corpus <- tm_map(corpus, removeWords, stopwords("en"))
corpus <- tm_map(corpus, stemDocument)

# Convert to Document-Term Matrix
dtm <- DocumentTermMatrix(corpus)
dtm <- as.data.frame(as.matrix(dtm))

# Add the sentiment column back
dtm$sentiment <- data$sentiment

# Save the preprocessed data
write.csv(dtm, "preprocessed_data.csv", row.names = FALSE)