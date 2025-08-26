import asyncio
from cardlink import CardLink

cl = CardLink(token="ВАШ_ТОКЕН", shop_id="12345")


async def main():
    refund = await cl.create_full_refund(payment_id="PAYMENT ID")
    print(refund.id)

    refund = await cl.create_partial_refund(
        payment_id="PAYMENT ID",
        amount=100
    )
    print(refund.id)


if __name__ == "__main__":
    asyncio.run(main())
