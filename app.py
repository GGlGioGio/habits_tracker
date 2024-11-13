from flask import Flask, jsonify, request

app = Flask(__name__)

# Мок-данные для привычек
habits = []

@app.route('/habits', methods=['GET'])
def get_habits():
    return jsonify(habits)

@app.route('/habits', methods=['POST'])
def add_habit():
    habit = request.json.get('habit')
    habits.append({'habit': habit, 'done': False})
    return jsonify({'message': 'Habit added successfully'}), 201

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
