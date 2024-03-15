import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up the screen
WIDTH, HEIGHT = 1662, 938
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Who Wants to Be a Millionaire")

# Load background image and "riktig A" image
background_image = pygame.image.load("Spørsmål.jpg")
riktig_A_image = pygame.image.load("Riktig A.jpg")
riktig_B_image = pygame.image.load("Riktig B.jpg")
riktig_C_image = pygame.image.load("Riktig C.jpg")
riktig_D_image = pygame.image.load("Riktig D.jpg")

feil_A_image = pygame.image.load("Feil A.jpg")
feil_B_image = pygame.image.load("Feil B.jpg")
feil_C_image = pygame.image.load("Feil C.jpg")
feil_D_image = pygame.image.load("Feil D.jpg")

You_lost_image = pygame.image.load("You Lost.jpg")

# Lifeline images
fifty_fifty_image = pygame.image.load("5050.png")
ask_the_audience_image = pygame.image.load("Ask the crowd.png")
call_a_friend_image = pygame.image.load("Call friend.png")

# Define fonts with bigger sizes
question_font = pygame.font.Font(None, 48)  # Increased font size for the question
answer_font = pygame.font.Font(None, 36)    # Increased font size for the answers
result_font = pygame.font.Font(None, 72)    # Adjust as needed

# Define questions and answers
questions = [
    "What is the capital of France?",
    "What is the largest planet in our solar system?",
    "Who painted the Mona Lisa?",
    "Who is the author of the Harry Potter book series?",
    "What is the chemical symbol for water?",
    "Which of these football clubs have not won the treble?", 
    "What is the capital of Australia?", 
    "What is the longest river in the world?",
    "Who developed the theory of relativity?",
    "In which year did the Titanic sink?",
    "Which country is known as the Land of the Rising Sun?",
    "In which year did the Chernobyl nuclear disaster occur?",
    "Who was the first person to step on the moon?", 
    "What is the smallest country in the world by land area?",
    "Who discovered penicillin?",
    "What is the largest mammal in the world?",

    # Add more questions here...
]

answers = [
    ["Rome", "London", "Berlin", "Paris"],
    ["Jupiter", "Saturn", "Mars", "Earth"],
    ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"],
    ["J.R.R. Tolkien", "J.K. Rowling", "Stephenie Meyer", "George R.R. Martin"],
    ["W", "O2", "H2O", " CO2"],
    ["FC Bayern Munchen", "FC Barcelona", "Inter Milan", "Real Madrid"],
    ["Sydney", "Canberra", "Melbourne", "Brisbane"],
    ["Mississippi", "Amazon", "Yangtze", " Nile"],
    ["Galileo Galilei", "Isaac Newton", "Albert Einstein", " Nikola Tesla"],
    ["1933", "1912", "1921", " 1905"],
    ["Japan", "China", "Australia", " South Korea"],
    ["1991", "2000", "1979", " 1986"],
    ["Alan Shepard", "Yuri Gagarin", "Buzz Aldrin", "Neil Armstrong"],
    ["Liechtenstein", "San Marino", "Vatican City", "Monaco"],
    ["Alexander Fleming", "Louis Pasteur", "Robert Koch", "Oppenheimer"],
    ["Hippopotamus", "African Elephant", "Blue Whale", "Giraffe"],

    # Add corresponding answers here...
]

correct_answers = [3, 0, 0, 1, 2, 3, 1, 3, 2, 1, 0, 3, 3, 2, 0, 2]  # Index of correct answers for each question
money_pool = 1000000  # Starting money pool
question_index = 0  # Index of current question

# Define anchor point for the question text
question_anchor = (831, 470)

# Define anchor points for answer options
answer_anchors = [(490, 640), (1160, 640), (490, 795), (1160, 795)]

# Lifelines usage
fifty_fifty_used = False
ask_the_audience_used = False
call_a_friend_used = False

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def draw_question_and_answers():
    # Render question text with the specified font size at the anchor point
    draw_text(questions[question_index], question_font, WHITE, *question_anchor)
        
    # Render answer options with the default font size
    for i, (answer, anchor) in enumerate(zip(answers[question_index], answer_anchors)):
        draw_text(f"{i+1}. {answer}", answer_font, WHITE, *anchor)

def draw_result(result):
    draw_text(result, result_font, RED if result.startswith("Wrong") else GREEN, WIDTH/2, 300)

def display_lifelines():
    # Display lifeline logos at the top right corner
    if not fifty_fifty_used:
        screen.blit(fifty_fifty_image, (WIDTH - fifty_fifty_image.get_width(), 0))
    if not ask_the_audience_used:
        screen.blit(ask_the_audience_image, (WIDTH - fifty_fifty_image.get_width(), fifty_fifty_image.get_height()))
    if not call_a_friend_used:
        screen.blit(call_a_friend_image, (WIDTH - fifty_fifty_image.get_width(), fifty_fifty_image.get_height() * 2))


# Lifeline images (resized)
fifty_fifty_image = pygame.transform.scale(pygame.image.load("5050.png"), (100, 75))
ask_the_audience_image = pygame.transform.scale(pygame.image.load("Ask the crowd.png"), (100, 75))
call_a_friend_image = pygame.transform.scale(pygame.image.load("Call friend.png"), (100, 100))

def fifty_fifty():
    global fifty_fifty_used, answer_anchors
    if not fifty_fifty_used:
        # Get the index of the correct answer
        correct_answer_index = correct_answers[question_index]
        # Create a list of indices of incorrect answers
        incorrect_answer_indices = [i for i in range(len(answers[question_index])) if i != correct_answer_index]
        # Randomly choose two incorrect answer indices to remove
        indices_to_remove = random.sample(incorrect_answer_indices, 2)
        # Reset answer anchor points for the current question
        answer_anchors = [(490, 640), (1160, 640), (490, 795), (1160, 795)]
        # Hide the removed answer options by moving their anchor points off-screen
        """ for index in indices_to_remove:
            answer_anchors[index] = (-100, -100) """
        fifty_fifty_used = True


def ask_the_audience():
    global ask_the_audience_used
    if not ask_the_audience_used:
        # Simulate audience voting
        votes = [random.randint(1, 100) for _ in range(len(answers[question_index]))]
        # Create a graph to display audience votes
        # For simplicity, let's just print the vote counts for each option
        for i, vote in enumerate(votes):
            print(f"Option {i+1}: {vote} votes")
        ask_the_audience_used = True

def call_a_friend():
    global call_a_friend_used
    if not call_a_friend_used:
        # Simulate a friend's answer
        friend_answer_index = random.choice(range(len(answers[question_index])))
        return friend_answer_index + 1  # Return the friend's answer (index + 1)
        call_a_friend_used = True

def game_loop():
    global money_pool, question_index

    running = True
    while running:
        screen.blit(background_image, (0, 0))  # Draw the background image
        
        # Draw the question and answers with a specified font size
        draw_question_and_answers()
        
        # Display lifelines
        display_lifelines()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if correct_answers[question_index] == 0:
                        draw_result("Correct!")
                        pygame.time.delay(2000)  # Delay for 5 seconds
                        screen.blit(riktig_A_image, (0, 0))  # Display "riktig A" image
                        pygame.display.flip()
                        pygame.time.delay(2000)  # Delay for another 5 seconds
                        question_index += 1  # Go to the next question
                    else:
                        draw_result("Wrong!")
                        pygame.time.delay(3000)
                        screen.blit(feil_A_image, (0,0))
                        pygame.display.flip()
                        pygame.time.delay(3000)
                        screen.blit(You_lost_image, (0,0))
                        pygame.display.flip()
                        pygame.time.delay(3000)
                        running = False

                elif event.key == pygame.K_2:
                    if correct_answers[question_index] == 1:
                        draw_result("Correct!")
                        pygame.time.delay(2000)  # Delay for 2 seconds
                        screen.blit(riktig_B_image, (0, 0))  # Display "riktig A" image
                        pygame.display.flip()
                        pygame.time.delay(2000)  # Delay for another 2 seconds
                        question_index += 1  # Go to the next question
                    else:
                        draw_result("Wrong!")
                        pygame.time.delay(3000)
                        screen.blit(feil_B_image, (0,0))
                        pygame.display.flip()
                        pygame.time.delay(3000)
                        screen.blit(You_lost_image, (0,0))
                        pygame.display.flip()
                        pygame.time.delay(3000)
                        running = False

                elif event.key == pygame.K_3:
                    if correct_answers[question_index] == 2:
                        draw_result("Correct!")
                        pygame.time.delay(2000)  # Delay for 2 seconds
                        screen.blit(riktig_C_image, (0, 0))  # Display "riktig A" image
                        pygame.display.flip()
                        pygame.time.delay(2000)  # Delay for another 2 seconds
                        question_index += 1  # Go to the next question
                    else:
                        draw_result("Wrong!")
                        pygame.time.delay(3000)
                        screen.blit(feil_C_image, (0,0))
                        pygame.display.flip()
                        pygame.time.delay(3000)
                        screen.blit(You_lost_image, (0,0))
                        pygame.display.flip()
                        pygame.time.delay(3000)
                        running = False

                elif event.key == pygame.K_4:
                    if correct_answers[question_index] == 3:
                        draw_result("Correct!")
                        pygame.time.delay(2000)  # Delay for 2 seconds
                        screen.blit(riktig_D_image, (0, 0))  # Display "riktig A" image
                        pygame.display.flip()
                        pygame.time.delay(2000)  # Delay for another 2 seconds
                        question_index += 1  # Go to the next question
                    else:
                        draw_result("Wrong!")
                        pygame.time.delay(3000)
                        screen.blit(feil_D_image, (0,0))
                        pygame.display.flip()
                        pygame.time.delay(3000)
                        screen.blit(You_lost_image, (0,0))
                        pygame.display.flip()
                        pygame.time.delay(3000)
                        running = False

                # Lifeline usage
                elif event.key == pygame.K_x:
                    fifty_fifty()
                elif event.key == pygame.K_z:
                    ask_the_audience()
                elif event.key == pygame.K_c:
                    call_a_friend()

        pygame.display.flip()

game_loop()
