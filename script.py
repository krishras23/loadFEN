from tkinter.tix import FileEntry
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


PATH = "/Users/Soccerboy_Krish/Documents/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://lichess.org/analysis")


def calc(FEN):
    fen_box = driver.find_element_by_xpath("/html/body/div[1]/main/div[4]/div/div[1]/input")
    for i in range(57):
        fen_box.send_keys(Keys.BACK_SPACE)

    fen_box.send_keys(FEN)
    fen_box.send_keys(Keys.RETURN)


calc("rnbq1bnr/ppppp1pp/4kp2/8/8/4KP2/PPPPP1PP/RNBQ1BNR w - - 4 4")
