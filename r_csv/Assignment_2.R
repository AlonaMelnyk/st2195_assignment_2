csv_page<-read_html("https://en.wikipedia.org/wiki/Comma-separated_values")

csv_table<- csv_page %>% 
  html_element(".wikitable") %>% 
  html_table()

write.csv(csv_table,file="table.csv")


new_table<- csv_page %>%
   html_nodes(csv_page, xpath = "//*[contains(text(), 'MUST SELL!')]