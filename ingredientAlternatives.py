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
    "egg": "Used for binding or adding moisture. Alternatives like applesauce can provide moisture without the fat.",
    "flour": "Used for structure. Nut-based flours provide a gluten-free alternative with similar binding properties.",
    "sugar": "Used for sweetness. Natural sweeteners like honey or maple syrup can provide sweetness with added nutrients.",
    "butter": "Used for fat. Plant-based oils like coconut or olive oil can provide healthy fats.",
    "milk": "Used for moisture. Plant-based milks like almond or oat milk can provide moisture without the lactose.",
    "cheese": "Used for flavor. Nutritional yeast provides a cheesy flavor without the dairy.",
    "onion": "Used for flavor. Leeks, shallots, and scallions provide a similar flavor profile.",
    "garlic": "Used for flavor. Leeks, shallots, and scallions provide a similar flavor profile.",
    "chicken": "Used for protein. Plant-based proteins like tofu, tempeh, and seitan can provide a similar texture.",
    "beef": "Used for protein. Lentils, mushrooms, and jackfruit can provide a similar texture.",
    "pork": "Used for protein. Lentils, mushrooms, and jackfruit can provide a similar texture.",
    "fish": "Used for protein. Plant-based proteins like tofu, tempeh, and seitan can provide a similar texture.",
    "shrimp": "Used for protein. Plant-based proteins like tofu, tempeh, and seitan can provide a similar texture.",
    "carrot": "Used for color and flavor. Sweet potatoes, bell peppers, and zucchini provide similar color and texture.",
    "celery": "Used for flavor and texture. Bell peppers, fennel, and cucumber provide similar crunch and taste.",
    "bell pepper": "Used for color and flavor. Tomatoes, carrots, and celery provide similar color and texture.",
    "tomato": "Used for color and flavor. Bell peppers, carrots, and celery provide similar color and texture.",
    "potato": "Used for starch. Sweet potatoes, cauliflower, and parsnips provide similar texture and flavor.",
    "broccoli": "Used for texture and flavor. Cauliflower, asparagus, and green beans provide similar crunch and taste.",
    "spinach": "Used for nutrients. Kale, swiss chard, and collard greens provide similar vitamins and minerals.",
    "lettuce": "Used for texture. Spinach, arugula, and kale provide similar crunch and taste.",
    "cucumber": "Used for texture and flavor. Zucchini, bell peppers, and celery provide similar crunch and taste.",
    "celantro": "Used for flavor. Parsley, basil, and mint provide similar taste and aroma."
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
