-- SQL SCRIPT
-- LIST AL CA CITIES IN DATABASE
SELECT id, name FROM hbtn_0d_usa.cities WHERE state_id=(SELECT id FROM hbtn_0d_usa.states WHERE name="California") ORDER BY id ASC;