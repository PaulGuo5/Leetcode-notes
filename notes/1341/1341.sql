# Write your MySQL query statement below
(
    select u.name as results
    from Users as u, Movie_Rating as r
    where u.user_id = r.user_id
    group by r.user_id
    order by count(r.movie_id) DESC, u.name
    limit 1
)
union
(
    select m.title as results
    from Movies as m, Movie_Rating as r
    where m.movie_id = r.movie_id and created_at like '2020-02%'
    group by r.movie_id
    order by avg(r.rating) DESC, m.title
    limit 1
)
