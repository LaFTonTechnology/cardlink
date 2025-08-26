# API

LaFTon Technology предоставляет удобный Python SDK для работы с CardLink API.

---

## Methods

Методы API:

- [`CardLink().create_bill()`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/methods/createBill.py)
- [`CardLink().get_bill()`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/methods/billStatus.py)
- [`CardLink().toggle_activity()`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/methods/toggleActivity.py)
- [`CardLink().search_bill()`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/methods/searchBill.py)
- [`CardLink().bill_payments()`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/methods/billPayments.py)
- [`CardLink().refund_full()`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/methods/createFullRefund.py)
- [`CardLink().refund_partial()`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/methods/createPartialRefund.py)
- [`CardLink().get_refund()`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/methods/refundStatus.py)
- [`CardLink().search_refund()`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/methods/searchRefund.py)
- [`CardLink().personal_payout()`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/methods/createPersonalPayout.py)
- [`CardLink().create_payout_credit_card()`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/methods/createRegularPayout.py)
- [`CardLink().create_payout_sbp()`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/methods/createRegularPayout.py)
- [`CardLink().create_payout_crypto()`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/methods/createRegularPayout.py)
- [`CardLink().create_payout_steam()`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/methods/createRegularPayout.py)
- [`CardLink().get_payout()`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/methods/payoutStatus.py)
- [`CardLink().search_payout()`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/methods/searchPayout.py)
- [`CardLink().get_balance()`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/methods/getBalance.py)
- [`CardLink().get_banks()`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/methods/getBanks.py)
- [`CardLink().get_payment()`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/methods/paymentStatus.py)
- [`CardLink().search_payments()`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/methods/searchPayments.py)

---

## Types

Основные типы, используемые в SDK:

- [`Balance`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/types/Balance.py)
- [`Balances`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/types/Balances.py)
- [`Bank`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/types/Bank.py)
- [`Banks`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/types/Banks.py)
- [`Bill`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/types/Bill.py)
- [`BillStatus`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/types/BillStatus.py)
- [`BillTypes`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/types/BillTypes.py)
- [`CreatedBill`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/types/CreatedBill.py)
- [`Crypto`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/types/Crypto.py)
- [`Currency`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/types/Currency.py)
- [`Item`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/types/Item.py)
- [`Links`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/types/Links.py)
- [`Meta`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/types/Meta.py)
- [`Payment`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/types/Payment.py)
- [`PaymentMethod`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/types/PaymentMethod.py)
- [`PaymentStatus`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/types/PaymentStatus.py)
- [`Payout`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/types/Payout.py)
- [`Payouts`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/types/Payouts.py)
- [`PayoutStatus`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/types/PayoutStatus.py)
- [`Refund`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/types/Refund.py)
- [`RefundStatus`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/types/RefundStatus.py)
- [`RefundType`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/types/RefundType.py)
- [`SearchedBill`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/types/SearchedBill.py)
- [`SearchedPayments`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/types/SearchedPayments.py)
- [`SearchedPayout`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/types/SearchedPayout.py)
- [`SearchedRefund`](https://github.com/LaFTonTechnology/cardlink/blob/main/cardlink/types/SearchedRefund.py)

---

## Errors

Ошибки, которые могут возникнуть при работе с API:

- `APIError` — ошибка, возвращаемая API.
- `CardLinkError` — базовое исключение SDK.
- `DeserializationError` — ошибка десериализации ответа.
- `MethodValuesError` — неверные значения параметров метода.
- `WrongNetworkError` — ошибка сети.

---

## Usage Example

```python
from cardlink import CardLink

cardlink = CardLink(token="your_api_token", shop_id="your_shop_id")

async def main():
    # Создание счета
    bill = await cardlink.create_bill(
        amount=100,
        order_id="ORDER123",
        description="Оплата заказа",
        currency_in="RUB",
        payer_email="user@example.com",
        payment_method="BANK_CARD"
    )
    print(bill)
```

```python
from cardlink import CardLink

cardlink = CardLink(token="your_api_token", shop_id="your_shop_id")

async def main():
    # Проверка баланса
    balances = await cardlink.get_balance()
    print(balances)
```


```python
from cardlink import CardLink

cardlink = CardLink(token="your_api_token", shop_id="your_shop_id")

async def main():
    # Создание выплаты на карту
    payout = await cardlink.create_payout_credit_card(
        amount=500,
        currency="RUB",
        account_identifier="4111111111111111",
        card_holder="IVAN IVANOV"
    )
    print(payout)
```