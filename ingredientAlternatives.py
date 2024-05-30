from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dummy data for demonstration
alternatives = {
    "egg": ["applesauce", "mashed banana", "yogurt"],
    "flour": ["almond flour", "coconut flour", "oat flour"],
    "sugar": ["honey", "maple syrup", "stevia"],
    "butter": ["coconut oil", "olive oil", "avocado"],
    "milk": ["almond milk", "soy milk", "oat milk"],
    "cheese": ["nutritional yeast", "cashew cheese", "tofu"],
    "onion": ["leek", "shallot", "scallion"],
    "garlic": ["leek", "shallot", "scallion"],
    "chicken": ["tofu", "tempeh", "seitan"],
    "beef": ["lentils", "mushrooms", "jackfruit"],
    "pork": ["lentils", "mushrooms", "jackfruit"],
    "fish": ["tofu", "tempeh", "seitan"],
    "shrimp": ["tofu", "tempeh", "seitan"],
    "carrot": ["sweet potato", "bell pepper", "zucchini"],
    "celery": ["bell pepper", "fennel", "cucumber"],
    "bell pepper": ["tomato", "carrot", "celery"],
    "tomato": ["bell pepper", "carrot", "celery"],
    "potato": ["sweet potato", "cauliflower", "parsnip"],
    "broccoli": ["cauliflower", "asparagus", "green beans"],
    "spinach": ["kale", "swiss chard", "collard greens"],
    "lettuce": ["spinach", "arugula", "kale"],
    "cucumber": ["zucchini", "bell pepper", "celery"],
    "celantro": ["parsley", "basil", "mint"],
}

substitution_reasons = {
    "applesauce": "Used for moisture. Mashed banana, yogurt, and pumpkin puree provide similar moisture.",
    "mashed banana": "Used for moisture. Applesauce, yogurt, and pumpkin puree provide similar moisture.",
    "yogurt": "Used for moisture. Applesauce, mashed banana, and pumpkin puree provide similar moisture.",
    "almond flour": "Used for texture. Coconut flour and oat flour provide similar texture.",
    "coconut flour": "Used for texture. Almond flour and oat flour provide similar texture.",
    "oat flour": "Used for texture. Almond flour and coconut flour provide similar texture.",
    "honey": "Used for sweetness. Maple syrup and stevia provide similar sweetness.",
    "maple syrup": "Used for sweetness. Honey and stevia provide similar sweetness.",
    "stevia": "Used for sweetness. Honey and maple syrup provide similar sweetness.",
    "coconut oil": "Used for fat. Olive oil and avocado provide healthy fats.",
    "olive oil": "Used for fat. Coconut oil and avocado provide healthy fats.",
    "avocado": "Used for fat. Coconut oil and olive oil provide healthy fats.",
    "almond milk": "Used for liquid. Soy milk and oat milk provide similar liquid.",
    "soy milk": "Used for liquid. Almond milk and oat milk provide similar liquid.",
    "oat milk": "Used for liquid. Almond milk and soy milk provide similar liquid.",
    "nutritional yeast": "Used for flavor. Cashew cheese and tofu provide similar taste and aroma.",
    "cashew cheese": "Used for flavor. Nutritional yeast and tofu provide similar taste and aroma.",
    "tofu": "Used for flavor. Nutritional yeast and cashew cheese provide similar taste and aroma.",
    "leek": "Used for flavor. Shallot and scallion provide similar taste and aroma.",
    "shallot": "Used for flavor. Leek and scallion provide similar taste and aroma.",
    "scallion": "Used for flavor. Leek and shallot provide similar taste and aroma.",
    "tofu": "Used for protein. Tempeh and seitan provide similar protein.",
    "tempeh": "Used for protein. Tofu and seitan provide similar protein.",
    "seitan": "Used for protein. Tofu and tempeh provide similar protein.", 
    "sweet potato": "Used for texture. Bell pepper, zucchini, and carrot provide similar texture.",
    "bell pepper": "Used for texture. Sweet potato, zucchini, and carrot provide similar texture.",
    "zucchini": "Used for texture. Sweet potato, bell pepper, and carrot provide similar texture.",
    "carrot": "Used for texture. Sweet potato, bell pepper, and zucchini provide similar texture.",
    "bell pepper": "Used for flavor. Tomato, carrot, and celery provide similar taste and aroma.",
    "tomato": "Used for flavor. Bell pepper, carrot, and celery provide similar taste and aroma.",
    "carrot": "Used for flavor. Bell pepper, tomato, and celery provide similar taste and aroma.",
    "celery": "Used for flavor. Bell pepper, tomato, and carrot provide similar taste and aroma.",  
    "sweet potato": "Used for flavor. Bell pepper, zucchini, and carrot provide similar taste and aroma.",
    "cauliflower": "Used for flavor. Parsnip, sweet potato, and potato provide similar taste and aroma.",
    "parsnip": "Used for flavor. Cauliflower, sweet potato, and potato provide similar taste and aroma.",
    "cauliflower": "Used for flavor. Parsnip, sweet potato, and potato provide similar taste and aroma.",
    "asparagus": "Used for flavor. Broccoli, green beans, and green peas provide similar taste and aroma.",
    "green beans": "Used for flavor. Broccoli, asparagus, and green peas provide similar taste and aroma.",
    "green peas": "Used for flavor. Broccoli, asparagus, and green beans provide similar taste and aroma.",
    "kale": "Used for flavor. Spinach, swiss chard, and collard greens provide similar taste and aroma.",
    "swiss chard": "Used for flavor. Spinach, kale, and collard greens provide similar taste and aroma.",
    "collard greens": "Used for flavor. Spinach, kale, and swiss chard provide similar taste and aroma.",
    "spinach": "Used for flavor. Kale, swiss chard, and collard greens provide similar taste and aroma.",
    "arugula": "Used for flavor. Lettuce, spinach, and kale provide similar taste and aroma.",
    "kale": "Used for flavor. Lettuce, spinach, and arugula provide similar taste and aroma.",
    "zucchini": "Used for flavor. Bell pepper, carrot, and celery provide similar taste and aroma.",
    "celery": "Used for flavor. Bell pepper, carrot, and zucchini provide similar taste and aroma.",
    "parsley": "Used for flavor. Celantro, basil, and mint provide similar taste and aroma.",
    "basil": "Used for flavor. Celantro, parsley, and mint provide similar taste and aroma.",
    "mint": "Used for flavor. Celantro, parsley, and basil provide similar taste and aroma."
}

@app.route('/find_alternatives', methods=['GET'])
def find_alternatives():
    ingredient = request.args.get('ingredient')
    if ingredient in alternatives:
        return jsonify({ingredient: alternatives[ingredient]})
    else:
        return jsonify({"error": "No alternatives found"}), 404

@app.route('/substitution_reasons', methods=['GET'])
def get_substitution_reasons():
    ingredient = request.args.get('ingredient')
    if ingredient in substitution_reasons:
        return jsonify({ingredient: substitution_reasons[ingredient]})
    else:
        return jsonify({"error": "No substitution reasons found"}), 404

if __name__ == '__main__':
    app.run(port=1500, debug=True)
