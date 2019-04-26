>> > chessepizze = session.query(MenuItem).filter_by(name='chesse pizze')
>> > print cessepizze.name
Traceback(most recent call last):
    File "<stdin>", line 1, in < module >
NameError: name 'cessepizze' is not defined
>> > print chessepizze.name
Traceback(most recent call last):
    File "<stdin>", line 1, in < module >
AttributeError: 'Query' object has no attribute 'name'
>> > print chessepizze.id
Traceback(most recent call last):
    File "<stdin>", line 1, in < module >
AttributeError: 'Query' object has no attribute 'id'
>> > for name in chessepizze:
... print name.name
...
>> > for name in chessepizze:
... print name.id
...
>> >
>> > veggieBurgers = session.query(MenuItem).filter_by(name='Veggie Burger')
>> > for veggieBurger in beggierBurgers:
... print veggieBurger.id
... print veggieBurger.price
... print veggieBurger.restaurant.name
... print"\n"
...
Traceback(most recent call last):
    File "<stdin>", line 1, in < module >
NameError: name 'beggierBurgers' is not defined
>> > for veggieBurger in veggieBurgers: ... print veggieBurger.id
... print veggieBurger.price
... print veggieBurger.restaurant.name
... print"\n"
...
2
$7.50
Urban Burger


10
$5.99
Urban Burger


21
$9.50
Panda Garden


27
$6.80
Thyme for That Vegetarian Cuisine


37
$7.00
Andala's


43
$9.50
Auntie Ann's Diner'


>> > UrbanVeggieBurger = session.query(MenuItem).filter_by(id=8).one()
>> > print UrbanVeggieBurger.price
$.99
>> > UrbanVeggieBurger = session.query(MenuItem).filter_by(id=10).one()
>> > print UrbanVeggieBurger.price$5.99
>> > UrbanVeggieBurger.price = '$2.99'
>> > print UrbanVeggieBurger.price
$2.99
>> > session.add(UrbanVeggieBurger)
>> > session.commit()
>> > veggieBurgers = session.query(MenuItem).filter_by(name='Veggie Burger')
>> > for veggieBurger in veggieBurgers:
... print veggieBurger.id
... print veggieBurger.price
... print veggieBurger.restaurant.name
... print
...
2
$7.50
Urban Burger

10
$2.99
Urban Burger

21
$9.50
Panda Garden

27
$6.80
Thyme for That Vegetarian Cuisine

37
$7.00
Andala's

43
$9.50
Auntie Ann's Diner'

>> > for veggieBurger in veggieBurgers:
...     veggieBurger.price = '$2.99'
...     session.add(veggieBurger)
...     session.commit()
...
>> > for veggieBurger in veggieBurgers:
... print veggieBurger.price
... print veggieBurger.id
... print veggieBurger.restaurant.name
...
$2.99
2
Urban Burger
$2.99
10
Urban Burger
$2.99
21
Panda Garden
$2.99
27
Thyme for That Vegetarian Cuisine
$2.99
37
Andala's
$2.99
43
Auntie Ann's Diner'

# delete from database
>> > chessepizze = session.query(MenuItem).filter_by(name='Chesse Pizze').one()
>> > print chessepizze
<database_setup.MenuItem object at 0x7f891e28ae50 >
>> > print chessepizze.name
Chesse Pizze
>> > session.delete(chessepizze)
>> > session.commit()
