
mkdir templates 
python3 scaffold.py user username email password fm country_id phone
python3 scaffold.py country name
python3 scaffold.py city name
python3 scaffold.py trip user_id country_id city_id
python3 scaffold.py sport name
python3 scaffold.py record record_broken sportsperson_name country_id city_id year sport_id
python3 scaffold.py user_broken_record broken_record user_id country_id city_id year sport_id
python3 scaffold.py trip_links user_broken_record_id trip_id
