import bpy

def delete_collection(collection_name):
    collection = bpy.data.collections.get(collection_name)

    if collection is None:
        print(f"Collection '{collection_name}' does not exist.")
        return

    for obj in collection.objects:

        collection.objects.unlink(obj)
        bpy.data.objects.remove(obj, do_unlink=True)

    print(f"All objects in the collection '{collection_name}' have been deleted.")
