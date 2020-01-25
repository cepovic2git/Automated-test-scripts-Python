class SearchHotelLocators:

    search_hotel_span_xpath = "//span[text()='Search by Hotel or City Name']"
    search_hotel_input_xpath = "//div[@id='select2-drop']//input"
    location_match_xpath = "//span[text()='Dubai']"
    check_in_input_xpath = "//div[@id='dpd1']//input"
    check_out_input_xpath = "//div[@id='dpd2']//input"
    travellers_input_id = "travellersInput"
    adult_input_id = "adultInput"
    child_input_id = "childInput"
    search_button_xpath = "//button[@type='submit']"

class SearchResultLocators:

    hotel_names_xpath = "//h4[contains(@class,'list_title')]//b"
    hotel_prices_xpath = "//div[contains(@class,'fs26 text-center')]//b"