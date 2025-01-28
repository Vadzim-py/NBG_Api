import requests
from notion_client import Client
import os
from dotenv import load_dotenv

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")


NBG_API_URL = "https://nbg.gov.ge/gw/api/ct/monetarypolicy/currencies/en/json/"


notion = Client(auth=NOTION_TOKEN)


def get_usd_to_gel_rate(date):
    response = requests.get(f"{NBG_API_URL}?date={date}")
    if response.status_code == 200:
        data = response.json()
        for currency in data[0]["currencies"]:
            if currency["code"] == "USD":
                return float(currency["rateFormated"])
    return None

def get_new_rows():
    response = notion.databases.query(
        database_id=NOTION_DATABASE_ID,
        filter={
            "property": "Курс USD к GEL",
            "number": {"is_empty": True},
        },
    )
    return response.get("results", [])

def update_notion_row(row_id, usd_to_gel_rate):
    notion.pages.update(
        page_id=row_id,
        properties={
            "Курс USD к GEL": {"number": usd_to_gel_rate},
        },
    )

def main():
    new_rows = get_new_rows()
    if not new_rows:
        print("Нет новых строк для обновления.")
        return

    for row in new_rows:
        row_id = row["id"]
        date = row["properties"]["Дата прихода"]["date"]["start"]

        usd_to_gel_rate = get_usd_to_gel_rate(date)
        if not usd_to_gel_rate:
            print(f"Не удалось получить курс USD к GEL для даты {date}.")
            continue

        update_notion_row(row_id, usd_to_gel_rate)
        print(f"Строка {row_id} обновлена. Курс USD к GEL: {usd_to_gel_rate}.")

if __name__ == "__main__":
    main()