import asyncio
from typing import Dict

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from cardlink import CardLink
from cardlink.types import Bill, BillStatus


BOT_TOKEN = "BOT TOKEN"
SHOP_TOKEN = "TOKEN"
SHOP_ID = "SHOP ID"


bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()
cl: CardLink = CardLink(token=SHOP_TOKEN, shop_id=SHOP_ID)


bills: Dict[str, Message] = {}


async def check_payment() -> None:
    for bill_id in bills.copy().keys():
        times: int = bills[bill_id]['times']
        message: Message = bills[bill_id]['message']
        bill: Bill = await cl.get_bill_status(id=bill_id)

        bills[bill_id]['times'] -= 1

        if bill.status == BillStatus.success:
            await message.answer(
                f"✅ Bill #{bill.id} for {bill.amount} {bill.currency_in} has been paid."
            )
            bills.pop(bill_id)

        if times == 1:
            bills.pop(bill_id)


@dp.message(Command("bill"))
async def command_bill(message: Message) -> None:
    bill: Bill = await cl.create_bill(amount=10, currency_in="RUB")
    await message.answer(text=f"Bill #{bill.id}:\n{bill.amount} {bill.currency_in}\n\n💸 <a href='{bill.link_page_url}'>Pay</a>", parse_mode="HTML")
    bills[bill.id] = {"message": message, "times": 20}


async def main() -> None:
    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
    scheduler.add_job(check_payment, trigger="interval", seconds=3)
    scheduler.start()

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
