SELECT F.flavor
from ICECREAM_INFO as I, FIRST_HALF as F
where I.flavor = F.flavor
and total_order > 3000
and ingredient_type = 'fruit_based'
order by total_order desc