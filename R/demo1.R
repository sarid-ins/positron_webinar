library(tidyverse)
data <- readxl::read_excel("data/cbb2ed28-310d-4389-a1ec-64bb538fc090.xlsx")
# Source: https://data.gov.il/dataset/contaminatedterrains/resource/cbb2ed28-310d-4389-a1ec-64bb538fc090

# Things to demonstrate:

# Initializations ----
# Background: ctrl+shift+p to enable positron assistant.

# Write a short code that shows the first few lines of the data:
glimpse(data)


data_clean <- data |>
  mutate(
    treatment_year = case_when(
      # If it's a 4-digit year (already in correct format)
      str_detect(`Moed thilat tipul`, "^\\d{4}$") ~ as.integer(
        `Moed thilat tipul`
      ),
      # If it's an Excel serial date (numeric > 10000, typically 5 digits)
      str_detect(`Moed thilat tipul`, "^\\d{5}$") ~ year(as.Date(
        as.numeric(`Moed thilat tipul`),
        origin = "1899-12-30"
      )),
      # If it's already a date format, extract year
      !is.na(`Moed thilat tipul`) ~ year(ymd(
        `Moed thilat tipul`,
        quiet = TRUE
      )),
      # Otherwise, NA
      TRUE ~ NA_integer_
    )
  )

# Show the distribution of variable `Moed thilat tipul` using a ggplot2
ggplot(data_clean, aes(x = treatment_year)) +
  geom_bar(fill = "steelblue") +
  labs(
    title = "Distribution of Treatment Start Dates by Year",
    x = "Year",
    y = "Count"
  ) +
  theme_minimal()


top_activities <- data_clean |>
  filter(!`Peelut mezahemet` %in% c("-", "אחר")) |>
  count(`Peelut mezahemet`, sort = TRUE) |>
  head(8)

ggplot(top_activities, aes(x = n, y = reorder(`Peelut mezahemet`, n))) +
  geom_col(fill = "#e74c3c", alpha = 0.8) +
  labs(
    title = "Gas Stations Lead Contaminated Sites in Israel",
    subtitle = "Top polluting activities by number of contaminated sites",
    x = "Number of Contaminated Sites",
    y = NULL,
    caption = "Source: data.gov.il"
  ) +
  theme_minimal(base_size = 13) +
  theme(
    plot.title = element_text(face = "bold", size = 16),
    panel.grid.major.y = element_blank()
  )

# save the plot to tmp_plots in a png:
ggsave("tmp_plots/top_activities.png", width = 8, height = 5)

# Show in-code comments by selection / ctrl+.
# Show chat
# Show completions

# Use assistant and console + glimpse to get context on the data

# Use assistant to decide how to analyze a specific topic, e.g. see the distribution of polluting sites

# See what kind of of activities are at which state

# Show how to use assistant for a commit message

# Explain about the different chat types and chat modes of assistant (Agent, Ask, Edit)

# Show what happens when we have an error (explain, fix via `/`)

# Extending the context with more files, e.g. a readme.md

# Show how to access the various assistant tools (the clip -> tools...)

# Show how to analyze a chart (using #getPlot tool)

# Show the shiny assistant

# Show how assistant writes a commit message for us
