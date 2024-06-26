import requests
import json
import jsonpath_ng as jp

url = 'https://api.camptocamp.org/outings?act=snow_ice_mixed&grat=ED6,ED7'
nb_sorties = 30
response = requests.get(url)

if response.status_code == 200:
    json_object = response.json()

    for i in range(nb_sorties):
        try:
            # Extract title
            title_expr = f"$['documents'][{i}]['locales'][0]['title']"
            title = jp.parse(title_expr).find(json_object)
            title_value = title[0].value if title else "N/A"
            
            # Extract document ID
            document_ID_expr = f"$['documents'][{i}]['document_id']"
            document_ID = jp.parse(document_ID_expr).find(json_object)
            document_ID_value = document_ID[0].value if document_ID else "N/A"
            
            # Extract date
            date_expr = f"$['documents'][{i}]['date_end']"
            date = jp.parse(date_expr).find(json_object)
            date_value = date[0].value if date else "N/A"
            
            # Extract activity
            activity_expr = f"$['documents'][{i}]['activities']"
            activity = jp.parse(activity_expr).find(json_object)
            activity_value = activity[0].value if activity else "N/A"
            
            # Extract global rating
            rating_expr = f"$['documents'][{i}]['global_rating']"
            rating = jp.parse(rating_expr).find(json_object)
            rating_value = rating[0].value if rating else "N/A"
            
            # Extract additional ratings
            additional_ratings = {}
            for rating_key in [
                'rock_free_rating', 'labande_global_rating', 'hiking_rating',
                'ice_rating', 'ski_rating', 'snowshoe_rating', 'via_ferrata_rating',
                'mtb_up_rating', 'mtb_down_rating'
            ]:
                rating_expr = f"$['documents'][{i}]['{rating_key}']"
                rating = jp.parse(rating_expr).find(json_object)
                additional_ratings[rating_key] = rating[0].value if rating else "N/A"
            
            # Extract geometry
            geom_expr = f"$['documents'][{i}]['geometry']['geom']"
            geom = jp.parse(geom_expr).find(json_object)
            geom_value = geom[0].value if geom else "N/A"
            
            # Extract coordinates
            coordo_expr = "$['coordinates']"
            coordo = jp.parse(coordo_expr).find(geom_value)
            coordinates = coordo[0].value if coordo else "N/A"
            
            print(f"Title: {title_value}")
            print(f"Document ID: {document_ID_value}")
            print(f"Date: {date_value}")
            print(f"Activity: {activity_value}")
            print(f"Global Rating: {rating_value}")
            print(f"Additional Ratings: {additional_ratings}")
            print(f"Geometry: {geom_value}")
            print(f"Coordinates: {coordinates}")
            print("\n")

        except IndexError as e:
            print(f"Error processing entry {i}: {e}")

else:
    print(f"Failed to retrieve data: {response.status_code}")
