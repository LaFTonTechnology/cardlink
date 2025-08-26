# Usage Examples
Готовые примеры использования <b>cardlink</b> с асинхронным клиентом.

### Инициализация
```python
from cardlink import CardLink

cardlink = CardLink(token="YOUR_API_TOKEN", shop_id="YOUR_SHOP_ID")
```
<br><br>


### Создание счёта ```create_bill```
```python
async def main():
    bill = await cardlink.create_bill(
        amount=100,
        order_id="ORDER123",
        description="Оплата заказа",
        type="normal",  # или "multi"
        currency_in="RUB",
        custom="meta-data",
        payer_pays_commission=0,
        payer_email="user@example.com",
        name="Иван Иванов",
        ttl=3600,
        success_url="https://example.com/success",
        fail_url="https://example.com/fail",
        payment_method="BANK_CARD",  # или "SBP"
        request_fields_email=True,
        request_fields_phone=False,
        request_fields_name=False,
        request_fields_comment=False
    )
    print(bill)
```

### Получение баланса ```get_balance```
```python
async def main():
    balances = await cardlink.get_balance()
    print(balances)
```


### Получение счёта ```get_bill```
```python
async def main():
    bill = await cardlink.get_bill(id="qwerty12345")
    print(bill)
```


### Платежи по счёту ```bill_payments```
```python
async def main():
    payments = await cardlink.bill_payments(
        id="qwerty12345",
        per_page=50,
        cursor=None
    )
    print(payments)
```


### Возвраты: полный и частичный ```refund_full``` / ```refund_partial```
```python
# Полный возврат
async def main():
    refund = await cardlink.refund_full(payment_id="pay_123")
    print(refund)

# Частичный возврат
async def main():
    refund = await cardlink.refund_partial(
        payment_id="pay_123",
        amount=25.5
    )
    print(refund)
```


### Получение возврата ```get_refund```
```python
async def main():
    refund = await cardlink.get_refund(id="refund_12345")
    print(refund)
```


### Поиск возвратов ```search_refund```
```python
import datetime as dt

async def main():
    result = await cardlink.search_refund(
        payment_id="pay_123",
        start_date=dt.datetime(2025, 1, 1),
        finish_date=dt.datetime(2025, 2, 1),
        per_page=100,
        cursor=None
    )
    print(result)
```


### Персональная выплата ```personal_payout```
```python
async def main():
    payout = await cardlink.personal_payout(
        amount=150.0,
        payout_account_id="acc_42",
        account_currency="RUB",  # опционально: 'USD', 'EUR'
        recipient_pays_commission=False,
        order_id="ORDER-OUT-1"
    )
    print(payout)
```


### Выплаты: карта / СБП / крипто / Steam ```create_payout_*```
```python
# На банковскую карту
async def main():
    payout = await cardlink.create_payout_credit_card(
        amount=500,
        currency="RUB",
        account_identifier="4111111111111111",
        card_holder="IVAN IVANOV",
        account_currency="RUB",
        recipient_pays_commission=False,
        order_id="PO-1001"
    )
    print(payout)

# Через СБП
async def main():
    payout = await cardlink.create_payout_sbp(
        amount=500,
        currency="RUB",
        account_identifier="+79990000000",  # телефон/идентификатор
        account_bank="TCSBANK",
        account_currency="RUB",
        recipient_pays_commission=False,
        order_id="PO-1002"
    )
    print(payout)

# Криптовалюта
async def main():
    payout = await cardlink.create_payout_crypto(
        amount=100,
        currency="USD",
        account_identifier="TLX...TRXADDRESS",
        account_network="TRX",  # или "ETH"
        account_currency="USD",
        recipient_pays_commission=True,
        order_id="PO-1003"
    )
    print(payout)

# Steam
async def main():
    payout = await cardlink.create_payout_steam(
        amount=300,
        currency="RUB",
        account_identifier="steam_7656119...",
        account_currency="RUB",
        recipient_pays_commission=False,
        order_id="PO-1004"
    )
    print(payout)
```


### Получение выплаты ```get_payout```
```python
async def main():
    payout = await cardlink.get_payout(
        id="payout_12345",
        # или:
        # order_id="PO-1001",
    )
    print(payout)
```


### Поиск выплат ```search_payout```
```python
import datetime as dt

async def main():
    payouts = await cardlink.search_payout(
        start_date=dt.datetime(2025, 3, 1),
        finish_date=dt.datetime(2025, 3, 31),
        per_page=100,
        cursor=None
    )
    print(payouts)
```


### Справочник банков ```get_banks```
```python
async def main():
    banks = await cardlink.get_banks()
    print(banks)
```


### Поиск платежей ```search_payments```
```python

import datetime as dt

async def main():
    payments = await cardlink.search_payments(
        start_date=dt.datetime(2025, 1, 1),
        finish_date=dt.datetime(2025, 1, 31),
        shop_id=None,
        per_page=200,
        cursor=None
    )
    print(payments)
```


### Получение платежа ```get_payment```
```python
async def main():
    payment = await cardlink.get_payment(
        id="payment_12345",
        refunds=True,
        chargeback=False
    )
    print(payment)
```
