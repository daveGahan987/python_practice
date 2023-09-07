from restaurant import Restaurant, IceCreamStand

# *********** Restaurant *************

praga_restaurant = Restaurant('Praga', 'europenian')
gaga_restaurant = Restaurant('Gaga', 'georgian')
prima_vera_restaurant = Restaurant('Prima Vera', 'italian')

praga_restaurant.describe_restaurant()
gaga_restaurant.describe_restaurant()
prima_vera_restaurant.describe_restaurant()

ice_cream_restaurant = IceCreamStand('Super Ice Cream', 'morozivo')
ice_cream_restaurant.get_flavors()

praga_restaurant.set_number_served(45)
praga_restaurant.increment_number_served(32)
praga_restaurant.describe_restaurant()


