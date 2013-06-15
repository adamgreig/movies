import sqlite3
db = sqlite3.connect("/home/adam/.griffith/griffith.db")
cur = db.cursor()
print "Rate _all_ seen movies, or just the _unrated_ ones?"
torate = raw_input("[unrated] > ")
rows = list(cur.execute("SELECT movie_id, title, rating, notes"
                        " FROM movies WHERE seen ORDER BY title"))
for movie_id, title, rating, notes in rows:
    if torate != "all" and "Rated." in notes:
        continue
    print
    print "Rate `{0}'".format(title)
    print "Currently rated {0}. Just press enter to leave unchanged.".format(
        rating/2)
    print "0: Awful\t1: Didn't Like\t2: OK"\
          "\t3: Liked\t4: Really Liked\t5: Amazing"
    rating = -1
    while rating not in [str(i) for i in range(6)] + ['']:
        rating = raw_input("> ")
    if rating != "":
        rating = int(rating) * 2
        cur.execute("UPDATE movies SET rating = ? WHERE movie_id = ?",
                    (rating, movie_id))
        cur.execute("UPDATE movies SET notes = ? WHERE movie_id = ?",
                    (notes + "\nRated.", movie_id))
        db.commit()
