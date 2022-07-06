
show columns from mytable; 

drop table if exists trend;
create table trend(Month varchar(20), vcount float);

show tables;

insert into trend(Month, vcount) 
  select "APR", pt1 from  (select b_p1, count(b_p1)/30000.0 as pt1 from 
    (select PAY_1, case when PAY_1<1 then 1 else 0 end as b_p1 from mytable) sub 
       group by b_p1) sub where b_p1>0;

insert into trend(Month, vcount) 
  select "MAY", pt2 from  (select b_p2, count(b_p2)/30000.0 as pt2 from 
    (select PAY_2, case when PAY_2<1 then 1 else 0 end as b_p2 from mytable) sub 
       group by b_p2) sub where b_p2>0;

insert into trend(Month, vcount) 
  select "JUN", pt3 from  (select b_p3, count(b_p3)/30000.0 as pt3 from 
    (select PAY_3, case when PAY_3<1 then 1 else 0 end as b_p3 from mytable) sub 
       group by b_p3) sub where b_p3>0;

insert into trend(Month, vcount) 
  select "JULY", pt4 from  (select b_p4, count(b_p4)/30000.0 as pt4 from 
    (select PAY_4, case when PAY_4<1 then 1 else 0 end as b_p4 from mytable) sub 
       group by b_p4) sub where b_p4>0;


insert into trend(Month, vcount) 
  select "AUG", pt5 from  (select b_p5, count(b_p5)/30000.0 as pt5 from 
    (select PAY_5, case when PAY_5<1 then 1 else 0 end as b_p5 from mytable) sub 
       group by b_p5) sub where b_p5>0;


insert into trend(Month, vcount) 
  select "SEP", pt6 from  (select b_p6, count(b_p6)/30000.0 as pt6 from 
    (select PAY_6, case when PAY_6<1 then 1 else 0 end as b_p6 from mytable) sub 
       group by b_p6) sub where b_p6>0;



select * from trend; 


