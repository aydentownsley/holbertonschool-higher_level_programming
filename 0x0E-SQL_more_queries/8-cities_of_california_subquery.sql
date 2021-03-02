-- SQL SCRIPT
-- LIST AL CA CITIES IN DATABASE (using lowecase sql)
select * from hbtn_0d_usa.cities where state_id=(select id from hbtn_0d_usa.states where name="California") order by id asc;