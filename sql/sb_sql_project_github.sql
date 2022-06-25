show databases

    => country_club
    => mysql
    => wordpress etc.


use country_club

show tables

    => Bookings
    => Facilities
    => Members



***************************************************************************************
/* Q1: Some of the facilities charge a fee to members, but some do not.
Please list the 'names' of the facilities that do. */
***************************************************************************************

select * from country_club.Facilities

=> columns like : 'membercost', 'guestcost', 'initialoutlay',
                  'monthlymaintenance'

select * from country_club.Facilities
    where membercost > 0

***********************************************************************************
/* Q2: How many facilities do not charge a fee to members? */
**********************************************************************************


select * from country_club.Facilities
    where membercost = 0


*************************************************************************************
/* Q3: How can you produce a list of facilities that charge a fee to members,
where the fee is less than 20% of the facility's monthly maintenance cost?
*************************************************************************************


Return the 'facid', 'facility name', 'member cost', and 'monthly maintenance' of the
facilities in question. */


    => columns are following such as

    => 'name', 'membercost', 'guestcost', 'initialoutlay', 'monthlymaintenance'

select facid,
       name,
       membercost,
       monthlymaintenance

       from country_club.Facilities
       where membercost < 0.2*monthlymaintenance


select * from country_club.Facilities
    where membercost < 0.2*monthlymaintenance


/* Q4: How can you retrieve the 'details of facilities with ID 1 and 5' ?
Write the query without using the OR operator. */


select * from country_club.Facilities
    where facid in (1,5)



/* Q5: How can you produce

a list of facilities, with each labelled as
    => 'cheap' or 'expensive',

depending on if their 'monthly maintenance cost' is

    => more than $100? Return the name and monthly maintenance of the facilities
in question. */


select name,
    case when(monthlymaintenance > 100)
        then 'EXPENSIVE'
    else
        'CHEAP' end as COST
    from country_club.Facilities


/* Q6: You'd like to get the 'first' and 'last' name of the 'last member(s)'
who signed up. Do not use the LIMIT clause for your solution. using
country_club.Members */


-- this question is from

--      => Members

-- has columns such as

        => memid
        => surname    **
        => firstname  **
        => address
        => zipcode
        => telephone
        => recommendedby
        => joindate


(select * from Members order by joindate desc limit 1)
union
(select * from Members order by joindate asc limit 1);


/* Q7: How can you produce a list of all members who have used a tennis court?
Include in your output the name of the court, and the name of the member
formatted as a single column. Ensure no duplicate data, and order by
the member name. */


=> Bookings
=> Facilities
=> Members


SELECT
        country_club.Bookings.memid,
        CONCAT(country_club.Members.firstname, ' ', country_club.Members.surname)
        AS fullname,
        country_club.Bookings.facid,
        country_club.Facilities.name

FROM
        country_club.Bookings

JOIN
        country_club.Facilities
ON
        country_club.Facilities.facid = country_club.Bookings.facid


JOIN
        country_club.Members
ON
        country_club.Members.memid = country_club.Bookings.memid

WHERE
        country_club.Facilities.name LIKE 'Tennis Court%'

GROUP BY fullname
ORDER BY fullname


/* Q8: How can you produce 'a list of bookings' on the day of '2012-09-14' which
will cost the member (or guest) more than $30?

Remember that guests have
different costs to members (the listed costs are per half-hour 'slot'), and
the guest user's ID is always 0. Include in your output the name of the
facility, the name of the member formatted as a single column, and the cost.
Order by descending cost, and do not use any subqueries. */
*/


SELECT

        country_club.Bookings.starttime,
        country_club.Bookings.memid,
        CONCAT(country_club.Members.firstname, ' ', country_club.Members.surname) AS fullname,
        country_club.Bookings.facid,
        country_club.Facilities.name,

CASE
WHEN
        country_club.Bookings.memid = '0'
THEN
        country_club.Bookings.slots*country_club.Facilities.guestcost
ELSE
        country_club.Bookings.slots*country_club.Facilities.membercost
END AS
        cost

FROM
        country_club.Bookings


JOIN
    country_club.Facilities
ON
        country_club.Facilities.facid = country_club.Bookings.facid
JOIN
        country_club.Members
ON
        country_club.Members.memid = country_club.Bookings.memid
Where
        country_club.Bookings.starttime LIKE '2012-09-14%'
AND
        (CASE WHEN country_club.Bookings.memid = '0' THEN country_club.Bookings.slots country_club.Facilities.guestcost
        ELSE country_club.Bookings.slots country_club.Facilities.membercost END) > 30.0

ORDER BY
        cost DESC




/* Q9: This time, produce the same result as in Q8, but using a subquery. */

SELECT *
FROM (
      SELECT
      Facilities.name as court_name,
      CONCAT(Members.firstname, ' ', Members.surname) AS member_name,
      CASE WHEN Bookings.memid = '0' THEN slots * Facilities.guestcost
      ELSE slots * Facilities.membercost END AS cost
      
      FROM Bookings
      LEFT JOIN Members
      ON Bookings.memid = Members.memid
      LEFT JOIN Facilities
      ON Bookings.facid = Facilities.facid
      AND (Bookings.starttime BETWEEN '2012-09-14 00:00:00' AND '2012-09-14 23:59:59')
      ) sub

WHERE sub.cost > 30
ORDER BY sub.cost DESC

-------------------------------------------------


SELECT
        bkfc.starttime,
        bkfc.memid,
        CONCAT(Members.firstname, ' ', Members.surname) AS fullname,
        bkfc.facid,
        bkfc.name,
        bkfc.cost

FROM    -- here we start the subquerry

        (SELECT Bookings.starttime,
        Bookings.memid,
        Bookings.facid,
        Facilities.name,

CASE
    WHEN

        Bookings.memid = '0'
        THEN Bookings.slots Facilities.guestcost
        ELSE Bookings.slots Facilities.membercost
        END AS cost

FROM Bookings


JOIN Facilities
ON
        Facilities.facid = Bookings.facid) bkfc    -- here we named the sub query
JOIN Members

ON
        Members.memid = bkfc.memid
Where bkfc.starttime LIKE '2012-09-14%'

AND bkfc.cost >30

ORDER BY bkfc.cost DESC



/* Q10: Produce a list of facilities with a total revenue less than 1000.
The output of facility name and total revenue, sorted by revenue. Remember
that there's a different cost for guests and members! */



USE country_club;
SELECT
Bookings.facid,
Facilities.name,
SUM(CASE WHEN Bookings.memid = '0'
    
    THEN
    Bookings.slots*Facilities.guestcost
    ELSE
    Bookings.slots*Facilities.membercost END) AS revenue
FROM Bookings

JOIN Facilities
ON
Facilities.facid = Bookings.facid
GROUP BY name
HAVING revenue < 1000
ORDER BY revenue

---------------------------------------------------------------

WORKS:


SELECT
        country_club.Bookings.memid,
        country_club.Bookings.facid,
        country_club.Facilities.name


FROM
        country_club.Bookings

JOIN
        country_club.Facilities
ON
        country_club.Facilities.facid = country_club.Bookings.facid

LIMIT 0 , 30


-----------------------------------------------------------------

SELECT
country_club.Bookings.memid,
country_club.Bookings.facid,
country_club.Facilities.name,
country_club.Members.surname
FROM
country_club.Bookings

JOIN
country_club.Facilities
ON
country_club.Facilities.facid = country_club.Bookings.facid

JOIN
country_club.Members
ON
country_club.Members.memid = country_club.Bookings.memid
GROUP BY surname

-----------------------------------------------------------------------

SELECT
    country_club.Facilities.starttime,
    country_club.Facilities.memid,
    CONCAT(country_club.Members.firstname, ' ', country_club.Members.surname)
    AS fullname,
    country_club.Facilities.facid,
    country_club.Facilities.name,
    country_club.Facilities.cost

FROM
    (SELECT country_club.Bookings.starttime,
    country_club.Bookings.memid,
    country_club.Bookings.facid,
    country_club.Facilities.name,

    CASE
        WHEN
            country_club.Bookings.memid = '0'
        THEN country_club.Bookings.slots*country_club.Facilities.guestcost
        ELSE country_club.Bookings.slots*country_club.Facilities.membercost
        END AS cost

    FROM country_club.Bookings

    JOIN
        country_club.Facilities
        ON
        country_club.Facilities.facid = country_club.Bookings.facid)
        country_club.Facilities

    JOIN
        country_club.Members

    ON
        country_club.Members.memid = country_club.Facilities.memid
        Where country_club.Facilities.starttime LIKE '2012-09-14%'

    AND
        country_club.Facilities.cost >30

    ORDER BY
        country_club.Facilities.cost DESC




**********************

SELECT bkfc.starttime, bkfc.memid, CONCAT(Members.firstname, ' ', Members.surname) AS fullname, bkfc.facid, bkfc.name, bkfc.cost
FROM
(SELECT Bookings.starttime, Bookings.memid, Bookings.facid, Facilities.name, CASE WHEN Bookings.memid = '0' THEN Bookings.slots Facilities.guestcost ELSE Bookings.slots Facilities.membercost END AS cost
 
 FROM Bookings
 JOIN Facilities
 ON Facilities.facid = Bookings.facid) bkfc
JOIN Members
ON Members.memid = bkfc.memid
Where bkfc.starttime LIKE '2012-09-14%'
AND bkfc.cost >30
ORDER BY bkfc.cost DESC


















