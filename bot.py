from telegram.ext import ApplicationBuilder, CommandHandler
from selenium import webdriver
import pandas as pd

BOT_TOKEN = "8268102521:AAGwnyuDOUhNCc9R3ulhC9eCFoFPmc7Nmc0"

async def scrape(update, context):
    query = " ".join(context.args)

    driver = webdriver.Chrome()
    driver.get(f"https://www.google.com/maps/search/{query}")

    names = []
    places = driver.find_elements("class name","hfpxzc")

    for p in places[:20]:
        names.append(p.text)

    df = pd.DataFrame(names, columns=["Business Name"])
    df.to_csv("leads.csv")

    await update.message.reply_document(open("leads.csv","rb"))

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("scrape", scrape))

app.run_polling()
