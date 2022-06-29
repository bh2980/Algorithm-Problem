BNP_money = int(input())
BNP_stock = 0
TIMING_money = BNP_money
TIMING_stock = 0

prices = list(map(int, input().split()))

TIMING_pre_price = prices[0]
TIMING_pre_condition = '-'
TIMING_count = 0
TIMING_buy = False
TIMING_sell = False

for today_price in prices:
  #BNP
  quo, left = divmod(BNP_money, today_price)
  if quo > 0:
    BNP_stock += quo
    BNP_money = left

  #TIMING
  if TIMING_pre_price == today_price:
    TIMING_pre_condition = '-'
    TIMING_count = 0
  else:
    if TIMING_pre_price < today_price:
      if TIMING_pre_condition == '<':
        TIMING_count += 1
      else:
        TIMING_count = 1
        
      TIMING_pre_price = today_price
      TIMING_pre_condition = '<'
    else:
      if TIMING_pre_condition == '>':
        TIMING_count += 1
      else:
        TIMING_count = 1
        
      TIMING_pre_price = today_price
      TIMING_pre_condition = '>'

  if TIMING_count >= 3:
    if TIMING_pre_condition == '>':
      TIMING_buy = True
    elif TIMING_pre_condition == '<':
      TIMING_sell = True

  if TIMING_buy:
    TIMING_buy = False
    
    quo, left = divmod(TIMING_money, today_price)
    if quo > 0:
      TIMING_stock += quo
      TIMING_money = left

  if TIMING_sell:
    TIMING_sell = False
    TIMING_money += today_price * TIMING_stock
    TIMING_stock = 0

BNP_money += prices[-1] * BNP_stock
TIMING_money += prices[-1] * TIMING_stock

if BNP_money > TIMING_money:
  print("BNP")
elif BNP_money < TIMING_money:
  print("TIMING")
else:
  print("SAMESAME")
