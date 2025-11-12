library(shiny)
library(bslib)
library(dplyr)
library(ggplot2)
library(lubridate)

data <- readxl::read_excel("../data/cbb2ed28-310d-4389-a1ec-64bb538fc090.xlsx")

# Load your data here if not already loaded
# data <- read.csv("your_data.csv")

ui <- page_sidebar(
  title = "Peelut Mezahemet Analysis",
  sidebar = sidebar(
    selectInput(
      "peelut",
      "Select Peelut Mezahemet:",
      choices = NULL # Will be populated in server
    )
  ),
  card(
    card_header("Administrative Status Distribution"),
    plotOutput("status_plot")
  ),
  card(
    card_header("Treatment Dates Distribution"),
    plotOutput("dates_plot")
  ),
  card(
    card_header("Summary Statistics"),
    tableOutput("summary_table")
  )
)

server <- function(input, output, session) {
  # Update choices after data is available
  observe({
    req(exists("data"))

    choices <- sort(unique(data$`Peelut mezahemet`))
    choices <- choices[!is.na(choices)]

    updateSelectInput(
      session,
      "peelut",
      choices = choices,
      selected = choices[1]
    )
  })

  # Filter data based on selection
  filtered_data <- reactive({
    req(input$peelut)
    req(exists("data"))

    data %>%
      filter(`Peelut mezahemet` == input$peelut)
  })

  # Status distribution plot
  output$status_plot <- renderPlot({
    req(filtered_data())

    filtered_data() %>%
      count(`Matzav Minhali`) %>%
      ggplot(aes(
        x = reorder(`Matzav Minhali`, n),
        y = n,
        fill = `Matzav Minhali`
      )) +
      geom_col() +
      coord_flip() +
      labs(
        title = "Administrative Status Distribution",
        x = "Status",
        y = "Count"
      ) +
      theme_minimal() +
      theme(legend.position = "none")
  })

  # Treatment dates distribution plot
  output$dates_plot <- renderPlot({
    req(filtered_data())

    # Convert dates (handle Excel numeric dates and regular dates)
    df_dates <- filtered_data() %>%
      filter(!is.na(`Moed thilat tipul`), `Moed thilat tipul` != "") %>%
      mutate(
        date = case_when(
          grepl("^[0-9]{5}$", `Moed thilat tipul`) ~ as.Date(
            as.numeric(`Moed thilat tipul`),
            origin = "1899-12-30"
          ),
          TRUE ~ as.Date(`Moed thilat tipul`, format = "%Y")
        )
      ) %>%
      filter(!is.na(date))

    if (nrow(df_dates) > 0) {
      ggplot(df_dates, aes(x = date)) +
        geom_histogram(bins = 20, fill = "steelblue", color = "white") +
        labs(
          title = "Treatment Start Dates Distribution",
          x = "Date",
          y = "Count"
        ) +
        theme_minimal() +
        theme(
          plot.title = element_text(size = 20, face = "bold"),
          axis.title = element_text(size = 18),
          axis.text = element_text(size = 16)
        )
    } else {
      ggplot() +
        annotate(
          "text",
          x = 0.5,
          y = 0.5,
          label = "No date data available",
          size = 6
        ) +
        theme_void()
    }
  })

  # Summary table
  output$summary_table <- renderTable({
    req(filtered_data())

    data.frame(
      Metric = c(
        "Total Sites",
        "Unique Status Types",
        "Sites with Treatment Dates"
      ),
      Value = c(
        nrow(filtered_data()),
        n_distinct(filtered_data()$`Matzav Minhali`, na.rm = TRUE),
        sum(
          !is.na(filtered_data()$`Moed thilat tipul`) &
            filtered_data()$`Moed thilat tipul` != ""
        )
      )
    )
  })
}

shinyApp(ui, server)
