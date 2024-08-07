import random
from colored import fore, back, style

# Definiciones de colores
COLORS = ['red', 'blue', 'green', 'yellow']
FEEDBACK_COLORS = {'correct': 'green', 'misplaced': 'yellow', 'none': 'white'}
NUM_COLORS = len(COLORS)
CODE_LENGTH = 4
MAX_ATTEMPTS = 12

def print_board(board):
    """ Imprime el tablero de juego en la terminal """
    for attempt in board:
        print(" ".join(attempt[0]) + " | " + " ".join(attempt[1]))
    print("-" * 40)

def generate_code():
    """ Genera un código secreto aleatorio """
    return [random.choice(COLORS) for _ in range(CODE_LENGTH)]

def get_feedback(code, guess):
    """ Devuelve la retroalimentación de la adivinanza """
    feedback = []
    code_copy = code[:]
    guess_copy = guess[:]
    
    # Círculos verdes
    for i in range(CODE_LENGTH):
        if guess[i] == code[i]:
            feedback.append('correct')
            code_copy[i] = None
    
    # Círculos naranjas
    for i in range(CODE_LENGTH):
        if guess_copy[i] in code_copy:
            feedback.append("misplaced")
            code_copy.remove(guess_copy[i])
    
    # Círculos blancos
    

    random.shuffle(feedback) 
    return feedback

def print_feedback(feedback):
    """ Imprime la retroalimentación en colores """
    feedback_colors = {
        'correct': fore('green') + '●' + style('reset'),
        'misplaced': fore('yellow') + '●' + style('reset'),
        'none': fore('white') + '●' + style('reset')
    }
    print(" ".join(feedback_colors[color] for color in feedback))

def player_guess():
    """ Permite al jugador hacer una adivinanza """
    while True:
        guess = input("Ingrese su adivinanza (4 colores de 'red', 'blue', 'green', 'yellow'): ").strip().split()
        if len(guess) == CODE_LENGTH and all(color in COLORS for color in guess):
            return guess
        print("Entrada inválida. Asegúrate de ingresar 4 colores válidos.")

def computer_guess(code):
    """ Algoritmo simple para que la computadora adivine (estrategia aleatoria) """
    return [random.choice(COLORS) for _ in range(CODE_LENGTH)]

def main():
    print("Bienvenido a Mastermind!")
    
    role = input("Quieres ser el creador del código (C) o el adivinador (A)? ").strip().upper()
    
    if role == 'C':
        secret_code = input("Ingrese el código secreto (4 colores de 'red', 'blue', 'green', 'yellow'): ").strip().split()
        if len(secret_code) != CODE_LENGTH or not all(color in COLORS for color in secret_code):
            print("Código inválido. Asegúrate de ingresar 4 colores válidos.")
            return
        is_creator = True
    elif role == 'A':
        secret_code = generate_code()
        is_creator = False
    else:
        print("Opción inválida.")
        return
    
    attempts = []
    for attempt in range(MAX_ATTEMPTS):
        if is_creator:
            guess = player_guess()
            feedback = get_feedback(secret_code, guess)
            attempts.append((guess, feedback))
            print_board(attempts)
            if guess == secret_code:
                print("¡Felicidades! Adivinaste el código secreto.")
                break
        else:
            guess = computer_guess(secret_code)
            feedback = get_feedback(secret_code, guess)
            attempts.append((guess, feedback))
            print("Intento de la computadora: " + " ".join(guess))
            print_feedback(feedback)
            if guess == secret_code:
                print("¡La computadora adivinó el código secreto!")
                break
    else:
        print("Se acabaron los intentos. El código secreto era: " + " ".join(secret_code))

if __name__ == "__main__":
    main()
''