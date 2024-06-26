from jsonpath_ng import parse
import json

# Exemple d'objet JSON (à remplacer par vos données réelles)
json_object = {
    "documents": [
        {"geometry": {"geom": {"type": "Point", "coordinates": [662986.330288, 5334629.563859]}}},
        # Ajoutez d'autres documents ici si nécessaire
    ]
}

# Index à extraire
i = 0  # Remplacez par l'index correct si nécessaire

# Construire l'expression JSONPath
jsonpath_expr = parse(f"$.documents[{i}].geometry.geom")

# Trouver le résultat
result_geom = jsonpath_expr.find(json_object)

# Vérifier que le résultat n'est pas vide et extraire les coordonnées
if result_geom:
    result_geom_json = result_geom[0].value  # Prendre la première correspondance
    coordinates = result_geom_json['coordinates']
    x, y = coordinates
    print(f"x: {x}, y: {y}")
else:
    print("Aucune correspondance trouvée pour le chemin JSONPath.")
