import pymysql
import sys
import simplejson as json



# Returns MySQL database connection
def con_db(host, port, user, passwd, db):
    try:
        con = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db)

    except pymysql.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)

    return con

def query_db(con, dict):
    data_array = []

    # Request args
    home = dict["home"]
    year_built = dict["year_built"]
    zip_code = dict["zip_code"]
    list_price = dict["list_price"]
    min_list_price = dict["min_list_price"]
    max_list_price = dict["max_list_price"]
    beds = dict["beds"]
    baths = dict["baths"]
    sqft = dict["sqft"]
    dom = dict["dom"]
    parking = dict["parking"]
    prediction = dict["prediction"]
    bike_score = dict["bike_score"]
    transit_score = dict["transit_score"]
    walk_score = dict["walk_score"]
    order_by = dict["order_by"]
    sort = dict["sort"]

    # Query database
    cur = con.cursor()
    cur.execute(
        """
        SELECT DISTINCT home_index.home, list_price, 
			prediction*sqft, prediction*sqft-list_price AS difference,url, neighborhood,
			beds, baths, sqft, 
			ROUND((transit_score-58)/(100-58)*100), year_built, 
			ROUND((walk_score-45)/(100-45)*100), 
			ROUND(((1-(xouts/views))-.84)/(1-.84)*100), latitude, longitude
        FROM home_index
        JOIN home_url ON home_index.home = home_url.home
		WHERE sqft > 0 AND beds >= {2} AND list_price >= {0} AND list_price <= {1}
        ORDER BY {3} {4}
        """.format(min_list_price, max_list_price, beds, order_by, sort)
    )

    data = cur.fetchall()
    for home in data:
        index = {}

        index["home"] = home[0]
        index["list_price"] = home[1]
        index["prediction"] = home[2]
        index["difference"] = home[3]
        index["home_url"] = home[4]
        index["neighborhood"] = home[5]
        index["beds"] = home[6]
        index["baths"] = home[7]
        index["sqft"] = home[8]
        index["transit_score"] = home[9]
        index["year_built"] = home[10]
        index["walk_score"] = home[11]
        index["xouts"] = home[12]
        index["latitude"] = home[13]
        index["longitude"] = home[14]

        data_array.append(index)

    cur.close()
    con.close()
    return data_array