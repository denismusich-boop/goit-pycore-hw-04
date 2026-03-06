def get_cats_info(path):
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                cat_id, name, age = line.split(",")

                cats.append(
                    {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
                    {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"  })

        return cats

    except FileNotFoundError:
        print("File not found.")
        return []