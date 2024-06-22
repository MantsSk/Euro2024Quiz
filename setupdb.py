import sqlite3

def setup_database():
    connection = sqlite3.connect('euro2024_quiz.db')
    cursor = connection.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Euro2024Quiz (
        id INTEGER PRIMARY KEY,
        question TEXT NOT NULL,
        option1 TEXT NOT NULL,
        option2 TEXT NOT NULL,
        option3 TEXT NOT NULL,
        option4 TEXT NOT NULL,
        correct_answer TEXT NOT NULL
    )
    ''')
    
    questions = [
        ("Which country is hosting Euro 2024?", "France", "Germany", "Spain", "Italy", "Germany"),
        ("How many teams are participating in Euro 2024?", "16", "20", "24", "32", "24"),
        ("Which stadium will host the final match of Euro 2024?", "Wembley Stadium", "Allianz Arena", "Olympiastadion", "Stade de France", "Olympiastadion"),
        ("Who won the Euro 2020 tournament?", "Italy", "England", "France", "Portugal", "Italy"),
        ("Which team has won the most Euro titles?", "Germany", "Spain", "Italy", "France", "Germany"),
        ("Who is the all-time top scorer in Euro history?", "Cristiano Ronaldo", "Michel Platini", "Thierry Henry", "Alan Shearer", "Cristiano Ronaldo"),
        ("Which country won the first Euro championship in 1960?", "Soviet Union", "Germany", "Spain", "Italy", "Soviet Union"),
        ("How often is the Euro tournament held?", "Every 2 years", "Every 3 years", "Every 4 years", "Every 5 years", "Every 4 years"),
        ("Which team won Euro 2016?", "France", "Portugal", "Germany", "Spain", "Portugal"),
        ("Who was the top scorer in Euro 2016?", "Antoine Griezmann", "Cristiano Ronaldo", "Olivier Giroud", "Eden Hazard", "Antoine Griezmann"),
        ("Which country has hosted the Euro tournament the most times?", "Germany", "France", "England", "Italy", "France"),
        ("What is the name of the official match ball for Euro 2024?", "Telstar", "Tango", "Uniforia", "Al Rihla", "Uniforia"),
        ("Which team has appeared in the most Euro finals?", "Germany", "Spain", "Italy", "France", "Germany"),
        ("Which player holds the record for most appearances in Euro tournaments?", "Gianluigi Buffon", "Iker Casillas", "Cristiano Ronaldo", "Lothar Matthäus", "Cristiano Ronaldo"),
        ("Which country won Euro 2004 in a surprising victory?", "Portugal", "Greece", "France", "Netherlands", "Greece"),
        ("How many times has Italy won the Euro championship?", "1", "2", "3", "4", "2"),
        ("Who was named the Best Player of Euro 2020?", "Harry Kane", "Gianluigi Donnarumma", "Luka Modrić", "Kevin De Bruyne", "Gianluigi Donnarumma"),
        ("Which country won Euro 1992?", "Germany", "Denmark", "Netherlands", "France", "Denmark"),
        ("Who scored the winning goal in the Euro 2000 final?", "David Trezeguet", "Zinedine Zidane", "Thierry Henry", "Patrick Vieira", "David Trezeguet"),
        ("Which city will host the opening match of Euro 2024?", "Berlin", "Munich", "Rome", "Paris", "Munich"),
        ("Which team is known as 'La Roja'?", "Italy", "France", "Spain", "Portugal", "Spain"),
        ("Who was the coach of Germany during their Euro 1996 victory?", "Berti Vogts", "Franz Beckenbauer", "Joachim Löw", "Jürgen Klinsmann", "Berti Vogts"),
        ("Which country did Spain defeat in the Euro 2012 final?", "Italy", "Germany", "Portugal", "France", "Italy"),
        ("Which team did France beat in the Euro 2000 final?", "Italy", "Germany", "Netherlands", "Portugal", "Italy"),
        ("How many goals did Michel Platini score in Euro 1984?", "5", "7", "9", "11", "9"),
        ("Who was the youngest player to score in a Euro tournament?", "Wayne Rooney", "Cristiano Ronaldo", "Kylian Mbappé", "Johan Vonlanthen", "Johan Vonlanthen"),
        ("Which country did Portugal defeat in the Euro 2016 final?", "France", "Germany", "Spain", "Italy", "France"),
        ("Who was the top scorer in Euro 2008?", "David Villa", "Fernando Torres", "Luka Modrić", "Andriy Shevchenko", "David Villa"),
        ("Which country has appeared in the most Euro tournaments without winning?", "Netherlands", "Portugal", "England", "Russia", "England"),
        ("Which player scored the fastest goal in Euro history?", "Dmitri Kirichenko", "Robbie Keane", "Alan Shearer", "Emil Forsberg", "Dmitri Kirichenko")
    ]
    
    cursor.executemany('''
    INSERT INTO Euro2024Quiz (question, option1, option2, option3, option4, correct_answer)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', questions)
    
    connection.commit()
    connection.close()

if __name__ == "__main__":
    setup_database()
