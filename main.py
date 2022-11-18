
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
   
    lista_bilder=["😹", "🐰", "🙋‍♂️", "🤠", "👩‍🔧", "🐶", "🐥", "💁🏻‍♀️"]
    
    list_of_bilder = lista_bilder
    for item in list_of_bilder:

            bilder.append(item)
            bilder.append(item)
   

   
    shuffled_bilder = random.sample(bilder,16)
    
    return render_template("index.html", shuffled_bilder=shuffled_bilder)






if __name__ == '__main__':
    app.run(debug=False)



