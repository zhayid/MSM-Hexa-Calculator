from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def calculate_probability(target_main, target_sub, current_main, current_sub_1, current_sub_2):
    """
    Calculate the probability of reaching the target Hexa stats.

    The probability is the weighted average of how close each current stat
    is to its target, expressed as a percentage (0–100).

    Main stat is weighted at 50%, and the two sub stats split the remaining 50%.
    """
    main_progress = min(current_main / target_main, 1.0) if target_main > 0 else 0.0
    sub_progress = min((current_sub_1 + current_sub_2) / (target_sub * 2), 1.0) if target_sub > 0 else 0.0

    probability = (main_progress * 0.5 + sub_progress * 0.5) * 100
    return round(probability, 2)


@app.route('/api/calculate', methods=['POST'])
def handle_calculation():
    try:
        data = request.json

        target_main = int(data.get('target_main', 0))
        target_sub = int(data.get('target_sub', 0))
        current_main = int(data.get('current_main', 0))
        current_sub_1 = int(data.get('current_sub_1', 0))
        current_sub_2 = int(data.get('current_sub_2', 0))

        # Validate minimums
        if target_main < 7:
            return jsonify({'success': False, 'error': 'TARGET_MAIN must be at least 7.'}), 400
        if target_sub < 9:
            return jsonify({'success': False, 'error': 'TARGET_SUB must be at least 9.'}), 400
        if current_main < 3:
            return jsonify({'success': False, 'error': 'CURRENT_MAIN must be at least 3.'}), 400

        probability = calculate_probability(target_main, target_sub, current_main, current_sub_1, current_sub_2)

        return jsonify({'success': True, 'probability': probability})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400


@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
