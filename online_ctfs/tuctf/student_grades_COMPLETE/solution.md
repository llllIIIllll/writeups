Student Grades
=============

> We are trying to find out what our grade was, but we don't seem to be in the database...

> Can you help us out?

> http://104.199.151.39/index.html


I wrote a script to act as a fuzzer, to quickly see what SQL statements I could execute and what response I would get. Thankfully, the response displayed what kind of SQL query it was running. I could clearly see some injection points, so I tried some UNION SELECT tactics to find more parts of the database.

http://pentestmonkey.net/cheat-sheet/sql-injection/mysql-sql-injection-cheat-sheet

```
Z' UNION SELECT 1, table_name FROM information_schema.tables; #
```



I was able to find the `tuctf_info` table with that, and then I selected everything in that table. That had the flag!


```
<tr><td>flag</td><td>TUCTF{v4ccinate_y0ur_databa5e5}</td></tr>
```