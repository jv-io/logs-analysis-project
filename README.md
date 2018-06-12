Jasper's News Log Analysis Project
===================================

**Introduction**

This program uses the standard udacity-database for the 'Logs Analysis Project'
that is part of the 'Intro to Programming Nanodegree'. It answers the three
questions automatically by running the code in the command line interface.

It runs on Python 2.7.12 and uses the psycopg2 and bleach libraries.

---

**Use**
1. Open the command line interface.
2. Cd into the right directory.
3. Run python newsdbqueries.py.

---

**Views created in database**

- slugpath: shows table with slugs and their counts that match articles.slug
```psql
create view slugpath as
select substring(path,'[^/]*$') as slugpath, count(*) as views
from log
group by slugpath
order by views desc;
```

- popnews: shows the 3 most popular articles of all time with their view count
```psql
create view popnews as
select articles.title, slugpath.views
from articles, slugpath
where articles.slug = slugpath.slugpath
order by slugpath.views desc
limit 3;
```

- authorviews: shows a list of author-id's of all the articles, and the view-count
```psql
create view authorviews as
select articles.author, slugpath.views
from articles, slugpath
where articles.slug = slugpath.slugpath
order by slugpath.views desc;
```

- popauthor: shows the most popular authors of all time with their total view count
```psql
create view popauthor as
select authors.name, sum(authorviews.views) as totalviews
from authors, authorviews
where authors.id = authorviews.author
group by authors.name
order by totalviews desc;
```

- statusday: shows a list of date, status, count sorted by day
```psql
create view statusday as
select to_char(time,'YYYY-MM-DD') as date, status, count(distinct(id))
from log
group by date,status
order by date;
```

- percentday: shows a list of date, status and percent sorted by day
```psql
create view percentday as
select date, status, 100 * count / sum(count) over (partition by date) as percent
from statusday;
```

- errorcheck: lists all days where more than 1% of the requests led to an 404 error
```psql
create view errorcheck as
select * from percentday
where status = '404 NOT FOUND'
and percent > 1
order by percent desc;
```
