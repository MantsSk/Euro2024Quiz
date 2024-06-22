from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management

def get_question(question_id):
    connection = sqlite3.connect('euro2024_quiz.db')
    cursor = connection.cursor()
    
    cursor.execute('SELECT id, question, option1, option2, option3, option4 FROM Euro2024Quiz WHERE id = ?', (question_id,))
    question = cursor.fetchone()
    
    connection.close()
    return question

def get_correct_answer(question_id):
    connection = sqlite3.connect('euro2024_quiz.db')
    cursor = connection.cursor()
    
    cursor.execute('SELECT correct_answer FROM Euro2024Quiz WHERE id = ?', (question_id,))
    correct_answer = cursor.fetchone()[0]
    
    connection.close()
    return correct_answer

@app.route('/')
def index():
    session['current_question'] = 1
    session['score'] = 0
    session['answers'] = {}
    return redirect(url_for('quiz'))

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        question_id = session['current_question']
        selected_option = request.form.get(str(question_id))
        session['answers'][str(question_id)] = selected_option
        
        correct_answer = get_correct_answer(question_id)
        if selected_option == correct_answer:
            session['score'] += 1
        
        session['current_question'] += 1

    question_id = session['current_question']
    question = get_question(question_id)

    if question is None:
        return redirect(url_for('result'))
    
    return render_template('quiz.html', question=question)

@app.route('/result')
def result():
    score = session.get('score', 0)
    return render_template('result.html', score=score)

if __name__ == '__main__':
    app.run(debug=True)
