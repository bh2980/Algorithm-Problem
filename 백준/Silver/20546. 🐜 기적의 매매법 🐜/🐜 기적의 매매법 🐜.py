BNP_money, BNP_stock = int(input()), 0
TIMING_money, TIMING_stock = BNP_money, 0

prices = list(map(int, input().split()))

for index in range(14):
  today_price = prices[index]
  #BNP
  quo, left = divmod(BNP_money, today_price)
  if quo > 0:
    BNP_stock += quo
    BNP_money = left

  if index >= 3:
  #TIMING
    if prices[index - 3] > prices[index-2] > prices[index - 1] > today_price:
      quo, left = divmod(TIMING_money, today_price)
      
      if quo > 0:
        TIMING_stock += quo
        TIMING_money = left

    elif prices[index - 3] < prices[index-2] < prices[index - 1] < today_price:
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
