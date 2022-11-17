
from flask import Flask, render_template
import random



app = Flask(__name__)

new_bilder=[]
bilder = []
shuffled_bilder = []
lista_bilder = []
@app.route('/')

def home():
    new_bilder = []
    bilder = []
    shuffled_bilder = []
    lista_bilder = []
    lista_bilder=["😹", "🐰", "🙋‍♂️", "🤠", "👩‍🔧", "🐶", "🐥", "💁🏻‍♀️"]
    #lista_bilder = ["A", "B", "C", "D", "E", "F", "G", "H"]
    print(lista_bilder[1])

    list_of_bilder = lista_bilder
    for item in list_of_bilder:

            bilder.append(item)
            bilder.append(item)
    print(bilder)

   # for item in bilder:
      # new_bilder.append(item)
      # new_bilder.splice(randInt, 1);
    shuffled_bilder = random.sample(bilder,16)
    #shuffled_bilder = random.sample(new_bilder, len(new_bilder))
    #list_random = list(set(new_bilder))
    #a = 16
   # shuffled_bilder = random.sample(bilder, a)


    print(shuffled_bilder)
    return render_template("index.html", shuffled_bilder=shuffled_bilder)






if __name__ == '__main__':
    app.run(debug=False)



