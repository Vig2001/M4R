library(ggplot2)

# Simulate some data
set.seed(123)
height <- rnorm(1000, mean=170, sd=10)
wrist_width <- rnorm(1000, mean=6, sd=0.5)
data <- data.frame(wrist_width, height)

# Center the data
data_centered <- data
data_centered$wrist_width <- data_centered$wrist_width - mean(data_centered$wrist_width)
data_centered$height <- data_centered$height - mean(data_centered$height)

data_std <- data
data_std$wrist_width <- 
  (data_std$wrist_width - mean(data_std$wrist_width)) / sd(data_std$wrist_width)
data_std$height <- 
  (data_std$height - mean(data_std$height)) / sd(data_std$height)

# PCA on raw centered data
pca_raw <- prcomp(data, scale = FALSE, center = TRUE)

# PCA on standardized data (also centered)
pca_std <- prcomp(data, scale = TRUE, center = TRUE)

# Plotting for raw PCA
p1 <- ggplot(data_centered, aes(x=wrist_width, y=height)) +
  geom_point(alpha=0.5) +
  geom_segment(aes(x = - 20 * pca_raw$rotation[1,1],
                   y = - 20 * pca_raw$rotation[2,1],
                   xend = 20 * pca_raw$rotation[1,1],
                   yend = 20 * pca_raw$rotation[2,1]),
               arrow = arrow(length = unit(0.5, "cm")), color = "red") +
  geom_segment(aes(x = - 1 * pca_raw$rotation[1,2],
                   y = - 1 * pca_raw$rotation[2,2],
                   xend = 1 * pca_raw$rotation[1,2],
                   yend = 1 * pca_raw$rotation[2,2]),
               arrow = arrow(length = unit(0.5, "cm")), color = "blue") +
  xlim(-10, 10) +
  ylim(-50, 50) +
  labs(title = "Raw Centered Data",
       x = "Human Wrist Width (cm)", y = "Human Height (cm)") +
  theme_classic()

# Plotting for standardized PCA
p2 <- ggplot(data_std, aes(x=wrist_width, y=height)) +
  geom_point(alpha=0.5) +
  geom_segment(aes(x = - 2 * pca_std$rotation[1,1],
                   y = - 2 * pca_std$rotation[2,1],
                   xend = 2 * pca_std$rotation[1,1],
                   yend = 2 * pca_std$rotation[2,1]),
               arrow = arrow(length = unit(0.5, "cm")), color = "red") +
  geom_segment(aes(x = - 1 * pca_std$rotation[1,2],
                   y = - 1 * pca_std$rotation[2,2],
                   xend = 1 * pca_std$rotation[1,2],
                   yend = 1 * pca_std$rotation[2,2]),
               arrow = arrow(length = unit(0.5, "cm")), color = "blue") +
  xlim(-10, 10) +
  ylim(-10, 10) +
  labs(title = "Standardized Data",
       x = "Human Wrist Width", y = "Human Height") +
  theme_classic()

print(p1)
print(p2)