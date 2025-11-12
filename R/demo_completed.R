library(tidyverse)

data <- readxl::read_excel("data/cbb2ed28-310d-4389-a1ec-64bb538fc090.xlsx")

# Things to demonstrate:

# Initializations ----
# Background: ctrl+shift+p to enable positron assistant.
# Show in-code comments by selection / ctrl+.
# Show chat
# Show completions

# Use assistant and console + glimpse to get context on the data

# Use assistant to decide how to analyze a specific topic, e.g. see the distribution of polluting sites

# Count polluting activity types
activity_distribution <- data |>
    count(`Peelut mezahemet`, sort = TRUE, name = "count") |>
    mutate(percentage = round(count / sum(count) * 100, 1))

activity_distribution
# Visualize the distribution
ggplot(
    activity_distribution,
    aes(x = reorder(`Peelut mezahemet`, count), y = count)
) +
    geom_col(fill = "steelblue") +
    geom_text(aes(label = count), hjust = -0.2, size = 3) +
    coord_flip() +
    labs(
        title = "Distribution of Contaminating Activities",
        x = "Activity Type",
        y = "Number of Sites"
    ) +
    theme_minimal()

# Create tmp_plots directory if it doesn't exist
if (!dir.exists("tmp_plots")) {
    dir.create("tmp_plots")
}

# Visualize the distribution
p <- ggplot(
    activity_distribution,
    aes(x = reorder(`Peelut mezahemet`, count), y = count)
) +
    geom_col(fill = "steelblue") +
    geom_text(aes(label = count), hjust = -0.2, size = 3) +
    coord_flip() +
    labs(
        title = "Distribution of Contaminating Activities",
        x = "Activity Type",
        y = "Number of Sites"
    ) +
    theme_minimal()

# Save plot to temporary directory
ggsave(
    "tmp_plots/activity_distribution.png",
    plot = p,
    width = 10,
    height = 6,
    dpi = 300
)

p
