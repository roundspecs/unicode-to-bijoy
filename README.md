
# unicode-to-bijoy
A python script that takes Unicode string converts it into [Bijoy](https://en.wikipedia.org/wiki/Bengali_input_methods#Bijoy)
```py
>>> from unicode2bijoy import to_bijoy
>>> to_bijoy("একা বসে তুমি")
GKv e‡m Zywg
>>> to_bijoy("""একা বসে তুমি,
... দেখছো কি একই আকাশ?
... দিন শেষে তার তারাগুলো দিবে দেখা।""")
GKv e‡m Zywg,
‡`L‡Qv wK GKB AvKvk?
w`b ‡k‡l Zvi Zviv¸‡jv w`‡e ‡`Lv|
```
Its not entirely perfect. Let me know if you think it can be improved.

