import asyncio
from cardlink import CardLink

cl = CardLink(token="ВАШ_ТОКЕН", shop_id="12345")


async def main():
    bill = await cl.create_bill(amount=100)
    print(bill.link_page_url)


if __name__ == "__main__":
    asyncio.run(main())
