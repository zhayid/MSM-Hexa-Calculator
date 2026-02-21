from flask import Flask, request, jsonify
from flask_cors import CORS
import math
import numpy as np
app = Flask(__name__)
CORS(app, origins="*")


def calculate_probability(target_main, target_sub, current_main, current_sub_1, current_sub_2):
    """
    Calculate the probability of reaching the target Hexa stats.

    The probability is the weighted average of how close each current stat
    is to its target, expressed as a percentage (0–100).

    Main stat is weighted at 50%, and the two sub stats split the remaining 50%.
    """
    prob = 0
    adjust_8 = 0.15/0.2
    adjust_9 = adjust_8 * 0.1 / 0.2
    adjust_10 = adjust_9 * 0.05 / 0.2
    prob_adjust = {7: 1, 8: adjust_8, 9: adjust_9, 10: adjust_10}

    combo = [current_main, current_sub_1, current_sub_2]
    left = 20 - np.sum(combo)

    for i in range(target_main,11):
        steps = i - combo[0]

        prob_to_add = pow(0.2, steps) * pow(.8, left-steps) * math.comb(left,steps)
        prob_mul = 1
        if i == 9:
            prob_mul = ((0.85 / 0.8) ** int((left - steps) / steps))
        if i == 10:
            prob_mul = ((0.9 / 0.8) ** int((left - steps) / steps))
        prob += prob_to_add * prob_adjust[i]*prob_mul

    if target_sub <=10:
        for j in range(target_sub, max(20-combo[0]-combo[2]+1, 11)):
            steps = j - combo[1]
            prob_to_add = pow(0.4, steps) * pow(.6, left-steps) * math.comb(left, steps)
            prob += prob_to_add

        for j in range(target_sub, max(20-combo[0]-combo[1]+1, 11)):
            steps = j - combo[2]
            prob_to_add = pow(0.4, steps) * pow(.6, left-steps) * math.comb(left, steps)
            prob += prob_to_add

    return round(prob * 100, 2)


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
