import os
buenas = ["image3.jpg","image9.jpg","image13.jpg","image15.jpg",
          "metaData3.jpg","metaData9.jpg","metaData13.jpg","metaData15.jpg"]
ls = os.listdir("images")
ls1 = os.listdir("metadata")
for ig in ls:
    if ig is not buenas:
        os.remove(f"images/{ig}")
for txt in ls1:
    if txt is not buenas:
        os.remove(f"metadata/{txt}")