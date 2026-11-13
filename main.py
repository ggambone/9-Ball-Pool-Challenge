from drafter import *
from dataclasses import dataclass
from bakery import assert_equal

set_website_title("9-Ball Challenge")

set_site_information(
    author="Giuli Gambone",
    description="Learn about 9-ball pool through trivia questions and "
    "interactive pool scenarios.",
    sources="Thanks to drafter documentation and course materials.",
    planning=[],
    links=[]
)

hide_debug_information()
set_website_framed(False)

@dataclass
class Question:
    '''
    Stores information about an individual trivia question
    
    Attributes:
        question (str): the text of the trivia question
        answers (list[str]): the possible answers
        correct_answer (str): the correct answer to the question
        explanation (str): the explanation of the correct answer
        difficulty (str): the question's difficulty level
    '''
    question: str
    answers: list[str]
    correct_answer: str
    explanation: str
    difficulty: str
    
@dataclass
class Scenario:
    '''
    Stores the information about an individual pool scenario
    
    Attributes:
        situation (str): the description of the current pool situation
        choices (list[str]): the possible decisions the player can make
        ratings (list[str]): the strategic rating of each choice
        explanations (list[str]): the explanation of each possible choice
    '''
    situation: str
    choices: list[str]
    ratings: list[str]
    explanations: list[str]
    

@dataclass
class State:
    '''
    Stores the player's information and current progress
    
    Attributes:
        player_name (str): the name entered by the player
        difficulty (str): the selected difficulty for trivia
        score (int): the number of trivia questions answered correctly
        question_index (int): the index of the current trivia question
        questions (list[Question]): collection of trivia questions
        scenario_step (int): the current step in the pool scenario game
        scenarios (list[Scenario]): collection of pool scenarios
        scenario_history (list[str]): a record of the player's scenario choices
        feedback (str): feedback explaining the result of the player's most recent answer
        show_explanations (bool): whether explanations are displayed after trivia answers
    '''
    player_name: str
    difficulty: str
    score: int
    question_index: int
    questions: list[Question]
    scenario_step: int
    scenarios: list[Scenario]
    scenario_history: list[str]
    feedback: str
    show_explanations: bool
    
def make_test_state() -> State:
    '''
    Helper function that creates and returns a fresh State object for unit tests
    
    Returns:
        State: a new State object with information for testing the routes
    '''
    return State(
        "Tester",
        "Beginner",
        0,
        0,
        make_questions(10, "Beginner"),
        0,
        make_scenarios(),
        [],
        "",
        False
    )
    
def make_questions(number: int, difficulty: str) -> list[Question]:
    '''
    Creates and returns the collection of trivia questions
    
    Args:
        number(int): number of trivia questions to include
        difficulty (str): the difficulty level of the questions
    
    Returns:
        list[Question]: list of trivia questions
    '''
    all_questions = [
        Question(
            "How many numbered object balls are used in 9-ball?",
            ["7", "9", "15"],
            "9",
            "9-ball uses nine object balls numbered 1 through 9.",
            "Beginner"
        ),
        Question(
            "Which ball must you hit first during a normal shot?",
            ["The 9-ball", "The lowest numbered ball", "Any ball"],
            "The lowest numbered ball",
            "You must contact the lowest numbered ball on the table first.",
            "Beginner"
        ),
        Question(
            "Which ball must be legally pocketed to win a rack?",
            ["The 1-ball", "The 8-ball", "The 9-ball"],
            "The 9-ball",
            "The player who legally pockets the 9-ball wins the rack.",
            "Beginner"
        ),
        Question(
            "How are the nine balls arranged before a game?",
            ["In a triangle", "In a diamond", "In a straight line"],
            "In a diamond",
            "The nine balls are arranged tightly in a diamond shape.",
            "Beginner"
        ),
        Question(
            "Where is the 9-ball placed in the rack?",
            ["At the top", "In the center", "At the bottom"],
            "In the center",
            "The 9-ball is placed in the center of the diamond.",
            "Beginner"
        ),
        Question(
            "If you legally pocket a ball other than the 9-ball, what happens?",
            ["Your turn continues", "Your turn ends", "You lose the rack"],
            "Your turn continues",
            "If you make a legal shot and pocket a ball, you continue shooting.",
            "Beginner"
        ),
        Question(
            "If no ball is pocketed on a break, how many object balls must reach a "
            "rail for a legal break?",
                 ["At least 2", "At least 3", "At least 4"],
                 "At least 4",
                 "At least four object balls much reach a rail if no ball is pocketed on the break.",
                 "Intermediate"
            ),
        Question(
            "What does 'ball in hand' mean?",
            ["The player can place the cue ball anywhere on the table",
             "The player can move any object ball",
             "Nothing, this is not a pool rule"
             ],
            "The player can place the cue ball anywhere on the table",
            "After most fouls in standard 9-ball, the incoming player recieves "
            "ball in hand and can place the cue ball anywhere on the table.",
            "Intermediate"
        ),
        Question(
            "What happens if the 9-ball is pocketed on a foul?",
            ["The player who pocketed it wins", "The 9-ball is spotted back on the table",
             "The game automatically ends"],
            "The 9-ball is spotted back on the table",
            "If the 9-ball is pocketed on a foul, it is returned to the table rather "
            "than counting as a win.",
            "Intermediate"
        ),
        Question(
            "What happens if you hit the wrong object ball first?",
            ["You automatically win", "It is a foul", "Nothing happens"],
            "It is a foul",
            "Failing to contact the lowest numbered ball first is a foul.",
            "Intermediate"
        ),
        Question(
            "What is it called when the cue ball is pocketed?",
            ["A scratch", "A safety", "A break"],
            "A scratch",
            "A scratch occurs when the cue ball is pocketed. This is a foul.",
            "Intermediate"
        ),
        Question(
            "Where do you aim on the cue ball for a stop shot?",
            [
                "Hit the cue ball above center",
                "Hit the dead center of the cue ball",
                "Hit the cue ball slightly below center"
            ],
            "Hit the cue ball slightly below center",
            "For a stop shot, hit the cue ball slightly below center with firm speed. "
            "The moment the cue ball strikes the object ball, all energy is transferred into it "
            "and the cue ball will freeze dead in its tracks.",
            "Advanced"
        ),
        Question(
            "What is the main purpose of applying side English to the cue ball?",
            [
                "To change how the cue ball rebounds off a rail",
                "To make the object ball travel faster",
                "To prevent the cue ball from moving"
            ],
            "To change how the cue ball rebounds off a rail",
            "Side English applies left or right spin to the cue ball, which can "
            "change its rebound angle when it contacts a rail.",
            "Advanced"
        ),
        Question(
            "Can a player legally pocket the 9-ball using a combination shot?",
            [
                "Yes, if the lowest-numbered ball is contacted first",
                "No, the 9-ball must always be hit directly",
                "Only on the break"
            ],
            "Yes, if the lowest-numbered ball is contacted first",
            "A combination shot can legally pocket the 9-ball as long as the cue ball "
            "contacts the lowest-numbered ball first and the shot otherwise follows the rules.",
            "Advanced"
        ),
        Question(
            "Why might a player choose a defensive shot instead of attempting a difficult "
            "pocket?",
            [
                "To make the game end immediately",
                "To leave the opponent with a difficult next shot",
                "To give the opponent ball in hand"
            ],
            "To leave the opponent with a difficult next shot",
            "A defensive shot focuses on cue ball placement and making the "
            "opponent's next shot difficult rather than trying to pocket a ball.",
            "Advanced"
        ),
        Question(
            "Why is cue-ball position important after pocketing an object ball?",
            [
                "It determines who breaks next",
                "It helps set up the next shot",
                "It changes the order of the balls"
            ],
            "It helps set up the next shot",
            "Good cue ball control helps a player get into position to legally contact and pocket "
            "the next lowest numbered ball.",
            "Advanced"
        )
    ]
    
    questions = []
    
    for question in all_questions:
        if question.difficulty == difficulty:
            if len(questions) < number:
                questions.append(question)
    
    return questions

#testing make_questions
assert_equal(len(make_questions(10, "Beginner")), 6)
assert_equal(len(make_questions(10, "Intermediate")), 5)
assert_equal(len(make_questions(10, "Advanced")), 5)

#testing that the requested number of questions is returned
assert_equal(len(make_questions(3, "Beginner")), 3)

#testing that questions match the selected difficulty
assert_equal(make_questions(10, "Beginner")[0].difficulty, "Beginner")
assert_equal(make_questions(10, "Intermediate")[0].difficulty, "Intermediate")
assert_equal(make_questions(10, "Advanced")[0].difficulty, "Advanced")


def make_scenarios() -> list[Scenario]:
    '''
    Creates and returns the collection of pool scenarios
    
    Returns:
        list[Scenario]: A list of the pool scenarios
    '''
    scenarios = [
        Scenario(
            "You're playing 9-ball. The 1-ball is near a pocket, "
            "and you have a fairly clear shot. What would you like to do?",
            [
                "Attempt to pocket the 1-ball",
                "Play a defensive shot",
                "Attempt to hit the 9-ball directly"
            ],
            ["Strong", "Reasonable", "Poor"],
            [
                "This is a strong choice. You have a good opportunity "
                "to pocket the lowest numbered ball and continue your turn.",
                "This is a reasonable strategic choice. You may give up your "
                "turn, but you could leave your opponent with a difficult shot.",
                "This is not a legal shot. You must contact the lowest numbered "
                "ball on the table first."
            ]
        ),
        Scenario(
            "You successfully pocketed the 1-ball. The 2-ball is "
            "near a pocket, but your current position makes the shot "
            "difficult. What would you like to do?",
            [
                "Attempt the difficult shot anyway",
                "Play a defensive shot to make your opponent's next shot difficult.",
                "Hit the 9-ball first to try to move it out of the way."
            ],
            ["Reasonable", "Strong", "Poor"],
            [
                "You might successfully pocket the 2-ball, but a difficult shot "
                "increases the chance of missing and leave your opponent with "
                "an opportunity.",
                "This is a strong strategic choice. A defensive shot can "
                "make your opponent's next turn more difficult when you do not "
                "have a good opportunity to pocket the ball.",
                "This is a foul because you must contact the lowest numbered "
                "ball on the table first. In this case, it is the 2-ball."
            ]
        ),
        Scenario(
            "You have pocketed several balls, and the 9-ball is now "
            "the lowest numbered ball remaining. What is your goal?",
            [
                "Pocket  the 9-ball legally.",
                "Hit the cue ball into the 9-ball without trying to pocket it.",
                "Try to pocket the cue ball."
            ],
            ["Strong", "Reasonable", "Poor"],
            [
                "Exactly! Legally pocketing the 9-ball wins the rack.",
                "You can legally contact the 9-ball without pocketing it, "
                "but this does not win the rack. You would need another turn "
                "to try again if your shot is otherwise legal.",
                "Pocketing the cue ball is a foul known as a 'scratch'. "
                "Your opponent would receive ball in hand for their shot."
            ]
        )
    ]
    
    return scenarios


assert_equal(len(make_scenarios()), 3)
assert_equal(make_scenarios()[0].ratings[0], "Strong")
assert_equal(make_scenarios()[2].ratings[0], "Strong")

def is_correct(question: Question, answer: str) -> bool:
    '''
    Determines whether the player's selected answer is correct
    
    Args:
        question (Question): the trivia question being answered
        answer (str): the answer the player selected
        
    Returns:
        bool: True if the answer is correct, False if the answer is incorrect
    '''
    return answer == question.correct_answer
#testing is_correct
assert_equal(is_correct(make_questions(10, "Beginner")[0], "9"), True)
assert_equal(is_correct(make_questions(10, "Beginner")[0], "7"), False)
    
@route
def index(state: State) -> Page:
    '''
    Displays the welcome page for the 9-Ball Challenge Game
    
    Args:
        state(State): The current state of the game
    
    Returns:
        Page: the welcome page with an input for the player's name
    '''
    return Page(state, [
        Header("9-Ball Pool Challenge"),
        "Welcome to the 9-Ball Pool Challenge!",
        "Learn the rules of 9-ball, test your knowledge, "
        "and challenge yourself with realistic pool scenarios.",
        "\n",
        "Enter your name to get started:",
        TextBox("player_name", placeholder= "Enter your name"),
        Button("Start Playing", "start_game")
    ])

@route
def start_game(state: State, player_name: str) -> Page:
    '''
    Saves the player's name and takes them to the main menu
    
    Args:
        state(State): the current state of the game
        player_name (str): the name entered by the player
    
    Returns:
        Page: the main menu page
    '''
    if player_name == "":
        state.player_name = "Player"
    else:
        state.player_name = player_name
        
    return menu(state)

@route
def menu(state: State) -> Page:
    '''
    Displays the main menu and available game activities

    Args:
        state (State): the current state of the game

    Returns:
        Page: the main menu with options for trivia and pool scenarios
    '''
    return Page(state, [
        Header("Main Menu"),
        "Welcome, " + state.player_name + "!",
        "Choose an activity:",
        "\n",
        "Choose your trivia difficulty:",
        SelectBox("difficulty",
                  ["Beginner", "Intermediate", "Advanced"],
                  state.difficulty),
        CheckBox("show_explanations", state.show_explanations),
        " Show explanations after each question",
        "\n",
        Button("9-Ball Trivia", "start_trivia"),
        Button("Pool Scenarios", "scenario_intro")
    ])

@route
def start_trivia(state: State, difficulty: str = "",
                 show_explanations: bool | None = None) -> Page:
    """
    Starts a new trivia game and resets the player's score and progress

    Args:
        state (State): The current state of the game
        difficulty (str): The selected trivia difficulty
        show_explanations (bool): Whether explanations should be displayed

    Returns:
        Page: The first trivia question
    """
    if difficulty != "":
        state.difficulty = difficulty

    if show_explanations is not None:
        state.show_explanations = show_explanations
        
    state.score = 0
    state.question_index = 0
    state.feedback = ""
    state.questions = make_questions(5, state.difficulty)

    return trivia(state)

@route
def trivia(state: State) -> Page:
    '''
    Displays the current trivia question & possible answers
    
    Args:
        state(State): The current state of the game
        
    Returns:
        Page: The current trivia question or the results page
    '''
    if state.question_index >= len(state.questions):
        return results(state)
    
    current_question = state.questions[state.question_index]
    
    return Page(state, [
        Div(
            Header("9-Ball Trivia"),
            "Question " + str(state.question_index + 1)
            + " of " + str(len(state.questions)),
            "\n",
            "Current Score: " + str(state.score),
            "\n",
            current_question.question,
            SelectBox("selected_answer", current_question.answers),
            Button("Submit Answer", "check_trivia"),
            "\n",
            Button("Return to Menu", "menu"),
            style_background_color = "#DCEBFA",
            style_min_height = "100vh",
            style_padding = "20px"
        )
    ])

@route
def check_trivia(state: State, selected_answer: str) -> Page:
    '''
    Checks the player's answer and updates their score and feedback.
    It accesses the current Question instance from the questions list and then
    calls the is_correct helper to determine whether the player's
    answer matches the correct one. If the answer is correct, the
    player's score increases by 1. Otherwise the feedback identifies the correct answer.
    If the player enabled explanations, the question's explanation is added
    to the feedback.

    Args:
        state (State): The current state of the game
        selected_answer (str): the answer selected by the player

    Returns:
        Page: the trivia feedback page
    '''
    current_question = state.questions[state.question_index]

    if is_correct(current_question, selected_answer):
        state.score = state.score + 1
        state.feedback = "Correct!"
    else:
        state.feedback = (
            "Not quite! The correct answer is "
            + current_question.correct_answer + "."
        )

    if state.show_explanations:
        state.feedback = state.feedback + "\n" + current_question.explanation

    return trivia_feedback(state)

@route
def trivia_feedback(state: State) -> Page:
    '''
    Displays feedback explaining whether the player's answer was correct

    Args:
        state (State): The current state of the game

    Returns:
        Page: The feedback page with the player's updated score
    '''
    return Page(state, [
        Div(
            Header("Answer Feedback"),
            state.feedback,
            "\n",
            "Current Score: " + str(state.score),
            Button("Next Question", "next_question"),
            style_background_color = "#DCEBFA",
            style_min_height = "100vh",
            style_padding = "20px"
        )
    ])

@route
def next_question(state: State) -> Page:
    '''
    Advances to the next trivia question
    
    Args:
        state (State): The current state of the game
    
    Returns:
        Page: The next trivia question or the final results
    '''
    state.question_index = state.question_index + 1
    
    return trivia(state)

@route
def results(state: State) -> Page:
    '''
    Displays the player's final trivia score
    
    Args:
        state (State): The current state of the game
        
    Returns:
        Page: The completed trivia results page
    '''
    return Page(state, [
        Div(
            Header("Trivia Complete!"),
            "You finished all the questions!",
            "Your final score: " + str(state.score)
            + " out of " + str(len(state.questions)),
            Button("Play Again", "start_trivia"),
            Button("Return to Menu", "menu"),
            style_background_color = "#DCEBFA",
            style_min_height = "100vh",
            style_padding = "20px"
        )
    ])


@route
def scenario_intro(state: State, difficulty: str,
                   show_explanations: bool) -> Page:
    """
    Introduces the pool scenario activity

    Args:
        state (State): The current state of the game
        difficulty (str): The selected trivia difficulty
        show_explanations (bool): Whether explanations should be displayed

    Returns:
        Page: The introduction page for pool scenarios
    """
    state.difficulty = difficulty
    state.show_explanations = show_explanations

    return Page(state, [
        Header("Pool Scenarios"),
        "Welcome to the 9-ball game scenarios!",
        "You'll be presented with different situations "
        "and must decide how you would play.",
        "After each decision, you'll receive feedback "
        "explaining how your choice affects the game.",
        "\n",
        Button("Start Scenarios", "start_scenarios"),
        Button("Back to Menu", "menu")
    ])

@route
def start_scenarios(state: State) -> Page:
    '''
    Starts a new scenario game and resets the player's progress
    
    Args:
        state (State): The current state of the game
        
    Returns:
        Page: the first pool scenario
    '''
    state.scenario_step = 0
    state.scenario_history = []
    state.feedback = ""
    state.scenarios = make_scenarios()
    
    return scenario(state)

@route
def scenario(state: State) -> Page:
    '''
    Shows the current pool scenario and its possible choices
    
    Args:
        state (State): The current state of the game
        
    Returns:
        Page: The current scenario and its choices
    '''
    current_scenario = state.scenarios[state.scenario_step]
    
    return Page(state, [
        Div(
            Header("Pool Scenarios"),
            "Scenario " + str(state.scenario_step + 1)
            + " of " + str(len(state.scenarios)),
            "\n",
            current_scenario.situation,
            SelectBox("selected_choice", current_scenario.choices),
            Button("Submit Choice", "check_scenario"),
            "\n",
            Button("Return to Menu", "menu"),
            style_background_color="#DFF0DF",
            style_min_height="100vh",
            style_padding="20px"
        )
    ])

@route
def check_scenario(state: State, selected_choice: str) -> Page:
    '''
    Checks the player's scenario choice and provides feedback
    
    Args:
        state(State): The current state of the game
        selected_choice (str): The choice selected by the player
        
    Returns:
        Page: Feedback about the player's decision
    '''
    current_scenario = state.scenarios[state.scenario_step]
    
    choice_index = 0
    found_choice = False
    
    for choice in current_scenario.choices:
        if choice == selected_choice and not found_choice:
            found_choice = True
        elif not found_choice:
            choice_index += 1
        
    rating = current_scenario.ratings[choice_index]
    explanation = current_scenario.explanations[choice_index]
    
    state.feedback = rating + "! " + explanation
    state.scenario_history.append(selected_choice + " - " + rating)
    
    return scenario_feedback(state)

@route
def scenario_feedback(state: State) -> Page:
    '''
    Displays feedback about the player's scenario decision.
    
    Args:
        state(State): The current state of the game
        
    Returns:
        Page: Feedback page for the player's decision
    '''
    if state.scenario_step == len(state.scenarios) - 1:
        next_button = Button("View Results", "scenario_results")
    else:
        next_button = Button("Next Scenario", "next_scenario")
        
    return Page(state, [
        Div(
            Header("Scenario Feedback"),
            state.feedback,
            "\n",
            next_button,
            Button("Return to Menu", "menu"),
            style_background_color="#DFF0DF",
            style_min_height="100vh",
            style_padding="20px"
        )
    ])

@route
def next_scenario(state: State) -> Page:
    '''
    Advances to the next pool scenario based on the player's decision.
    Conditional statements determine which scenario is presented next. It accesses the
    scenario history to evaluate previous choices, then modifies the Scenario instances
    in the scenarios list to create different situations based on what the player
    chooses to do.

    Args:
        state (State): The current state of the game

    Returns:
        Page: The next scenario or the final results page
    '''
    state.scenario_step = state.scenario_step + 1

    if state.scenario_step == 1:
        first_choice = state.scenario_history[0]

        if "Reasonable" in first_choice:
            state.scenarios[1] = Scenario(
                "Your defensive shot made your opponent's turn difficult. "
                "They hit the 1-ball legally but did not pocket it. "
                "It is now your turn, but you have a difficult position. "
                "What would you do?",
                [
                    "Attempt the difficult shot.",
                    "Play another defensive shot.",
                    "Hit the 9-ball first."
                ],
                ["Reasonable", "Strong", "Poor"],
                [
                    "You could pocket the ball, but the difficult position "
                    "makes missing a possibility.",
                    "A second defensive shot could keep your opponent "
                    "under pressure.",
                    "This is a foul because you must contact the "
                    "lowest numbered ball first."
                ]
            )

        elif "Poor" in first_choice:
            state.scenarios[1] = Scenario(
                "Your foul gave your opponent ball in hand. They took "
                "their turn but did not pocket the 1-ball. It is now "
                "your turn, and you have a clear opportunity. "
                "What would you do?",
                [
                    "Attempt to pocket the 1-ball.",
                    "Play a defensive shot.",
                    "Hit the 9-ball first."
                ],
                ["Strong", "Reasonable", "Poor"],
                [
                    "This is a good opportunity to pocket the lowest "
                    "numbered ball and continue your turn.",
                    "A defensive shot is a reasonable alternative "
                    "if you prefer to make your opponent's next shot difficult.",
                    "This is a foul because you must contact the "
                    "lowest numbered ball first."
                ]
            )
            
    if state.scenario_step == 2:
        second_choice = state.scenario_history[1]

        if "Strong" in second_choice:
            if "Poor" in state.scenario_history[0]:
                situation = (
                    "You took advantage of the opportunity and pocketed "
                    "the 1-ball. After making progress through the rack, "
                    "only the 9-ball remains. You have a clear opportunity "
                    "to win. What do you do?"
                )
            else:
                situation = (
                    "Your defense worked, and you got another opportunity "
                    "to shoot. After you pocket the 2-ball and make progress "
                    "through the rack, only the 9-ball remains. "
                    "You have a clear opportunity to win. What do you do?"
                )

            state.scenarios[2] = Scenario(
                situation,
                [
                    "Pocket the 9-ball legally.",
                    "Play a defensive shot.",
                    "Hit the cue ball into the 9-ball without pocketing it."
                ],
                ["Strong", "Reasonable", "Reasonable"],
                [
                    "Exactly! Legally pocketing the 9-ball wins the rack.",
                    "This is legal, but you are giving up a good opportunity "
                    "to win the rack.",
                    "This can be a legal shot, but you still need to "
                    "pocket the 9-ball to win."
                ]
            )

        elif "Reasonable" in second_choice:
            state.scenarios[2] = Scenario(
                "After a difficult exchange with your opponent, "
                "you have another opportunity. Only the 9-ball remains, "
                "but your position is not ideal. What do you do?",
                [
                    "Attempt to pocket the 9-ball.",
                    "Play a defensive shot.",
                    "Hit the cue ball into the 9-ball without contacting it legally."
                ],
                ["Reasonable", "Strong", "Poor"],
                [
                    "You could win, but the difficult position increases "
                    "the chance of missing.",
                    "A defensive shot could make your opponent's next "
                    "opportunity more difficult.",
                    "Failing to make legal contact with the required "
                    "object ball is a foul."
                ]
            )

        elif "Poor" in second_choice:
            state.scenarios[2] = Scenario(
                "After your foul, your opponent received ball in hand "
                "but failed to finish the rack. Only the 9-ball remains, "
                "and it is now your turn. What do you do?",
                [
                    "Attempt to pocket the 9-ball legally.",
                    "Play a defensive shot.",
                    "Intentionally commit another foul."
                ],
                ["Strong", "Reasonable", "Poor"],
                [
                    "This is your opportunity to win. Legally pocket "
                    "the 9-ball to finish the rack.",
                    "A defensive shot is legal, but you are passing "
                    "up an opportunity to win.",
                    "Committing another foul gives your opponent "
                    "another opportunity."
                ]
            )
    
    if state.scenario_step >= len(state.scenarios):
        return scenario_results(state)

    return scenario(state)

@route
def scenario_results(state: State) -> Page:
    '''
    Displays the player's completed scenario decisions

    Args:
        state (State): The current state of the game

    Returns:
        Page: The final scenario results and decision history
    '''
    content = [
        Header("Scenarios Complete!"),
        "You finished all the pool scenarios!",
        "Here is a review of your decisions:",
        "\n"
    ]

    scenario_number = 0

    for current_scenario in state.scenarios:
        content.append(
            Header("Scenario " + str(scenario_number + 1))
        )

        content.append(current_scenario.situation)

        if scenario_number < len(state.scenario_history):
            content.append(
                "Your choice: "
                + state.scenario_history[scenario_number]
            )

        content.append("\n")

        scenario_number = scenario_number + 1

    content.append(Button("Play Again", "start_scenarios"))
    content.append(Button("Return to Menu", "menu"))

    return Page(state, content)

def test_display_route(route_function):
    """
    Tests that a display-only route runs without errors

    Args:
        route_function: The display-only route to test
    """
    state = make_test_state()
    page = route_function(state)
    assert_equal(isinstance(page, Page), True)
    
    
#Unit Tests for Routes
#testing start_game
state = make_test_state()
start_game(state, "Giuli")
assert_equal(state.player_name, "Giuli")
state = make_test_state()
start_game(state, "")
assert_equal(state.player_name, "Player")

#testing start_trivia
state = make_test_state()
state.score = 5
state.question_index = 4

start_trivia(state, "Beginner", False)

assert_equal(state.score, 0)
assert_equal(state.question_index, 0)
assert_equal(state.difficulty, "Beginner")
assert_equal(state.show_explanations, False)

#testing start_trivia - Intermediate
test_state = make_test_state()
start_trivia(test_state, "Intermediate", False)

assert_equal(test_state.questions[0].difficulty, "Intermediate")
assert_equal(len(test_state.questions), 5)

#testing start_trivia - Advanced
test_state = make_test_state()
start_trivia(test_state, "Advanced", False)

assert_equal(test_state.questions[0].difficulty, "Advanced")
assert_equal(len(test_state.questions), 5)

#testing start_trivia with explanations enabled
test_state = make_test_state()
start_trivia(test_state, "Beginner", True)

assert_equal(test_state.show_explanations, True)

correct_answer = test_state.questions[0].correct_answer
check_trivia(test_state, correct_answer)

assert_equal(
    test_state.questions[0].explanation in test_state.feedback,
    True
)

#testing check_trivia for correct answer
state = make_test_state()
correct_answer = state.questions[0].correct_answer
check_trivia(state, correct_answer)
assert_equal(state.score, 1)
assert_equal("Correct!" in state.feedback, True)
#testing check_trivia for incorrect answer
state = make_test_state()
check_trivia(state, "Incorrect answer")
assert_equal(state.score, 0)
assert_equal("Not quite!" in state.feedback, True)

#testing next_question
state = make_test_state()
next_question(state)
assert_equal(state.question_index, 1)

#testing start_scenarios
state = make_test_state()
state.scenario_step = 2
state.scenario_history = ["Attempt to pocket the 1-ball"]
state.feedback = "Previous feedback"

state.scenarios[1] = Scenario(
    "Modified Scenario 2",
    ["Choice A", "Choice B"],
    ["Strong", "Poor"],
    ["Explanation A", "Explanation B"]
)

start_scenarios(state)
assert_equal(state.scenario_step, 0)
assert_equal(state.scenario_history, [])
assert_equal(state.feedback, "")
assert_equal(state.scenarios[1].situation,
             make_scenarios()[1].situation)
assert_equal(state.scenarios[1].choices,
             make_scenarios()[1].choices)
assert_equal(len(state.scenarios), 3)

#testing check_scenario
state = make_test_state()
selected_choice = state.scenarios[0].choices[0]
check_scenario(state, selected_choice)

assert_equal("Strong" in state.feedback, True)
assert_equal(len(state.scenario_history), 1)
assert_equal(state.scenario_history[0],
             selected_choice + " - Strong")

#testing next_scenario - reasonable 1st choice
state = make_test_state()
state.scenario_history = ["Play a defensive shot - Reasonable"]
next_scenario(state)

assert_equal(state.scenario_step, 1)
assert_equal("defensive shot" in
             state.scenarios[1].situation, True)


#testing next_scenario - poor 1st choice
state = make_test_state()
state.scenario_history = ["Hit the 9-ball first - Poor"]
next_scenario(state)

assert_equal(state.scenario_step, 1)
assert_equal("foul" in state.scenarios[1].situation, True)


#testing next_scenario - strong 2nd choice
state = make_test_state()
state.scenario_step = 1
state.scenario_history = [
    "Attempt to pocket the 1-ball - Strong",
    "Play a defensive shot - Strong"
]
next_scenario(state)

assert_equal(state.scenario_step, 2)
assert_equal("After you pocket the 2-ball" in
             state.scenarios[2].situation, True)


#testing next_scenario - reasonable 2nd choice
state = make_test_state()
state.scenario_step = 1
state.scenario_history = [
    "Attempt to pocket the 1-ball - Strong",
    "Attempt the difficult shot - Reasonable"
]
next_scenario(state)

assert_equal(state.scenario_step, 2)
assert_equal("difficult exchange" in
             state.scenarios[2].situation, True)


#testing next_scenario - poor 2nd choice
state = make_test_state()
state.scenario_step = 1
state.scenario_history = [
    "Attempt to pocket the 1-ball - Strong",
    "Hit the 9-ball first - Poor"
]
next_scenario(state)

assert_equal(state.scenario_step, 2)
assert_equal("After your foul" in
             state.scenarios[2].situation, True)

#testing next_scenario after final scenario
state = make_test_state()
state.scenario_step = 2
state.scenario_history = [
    "Attempt to pocket the 1-ball - Strong",
    "Play a defensive shot - Strong"
]

next_scenario(state)

assert_equal(state.scenario_step, 3)

#testing scenario_intro
state = make_test_state()
page = scenario_intro(state, "Advanced", True)

assert_equal(state.difficulty, "Advanced")
assert_equal(state.show_explanations, True)
assert_equal(isinstance(page, Page), True)

#testing display-only routes
test_display_route(index)
test_display_route(menu)
test_display_route(trivia)
test_display_route(trivia_feedback)
test_display_route(results)
test_display_route(scenario)
test_display_route(scenario_feedback)
test_display_route(scenario_results)

#testing triva after all questions are done
state = make_test_state()
state.question_index = len(state.questions)
page = trivia(state)
assert_equal(isinstance(page, Page), True)

#testing scenario_feedback on final scenario
state = make_test_state()
state.scenario_step = 2
page = scenario_feedback(state)
assert_equal(isinstance(page, Page), True)




start_server(State("", "Beginner", 0, 0, make_questions(5, "Beginner"),
                   0, make_scenarios(), [], "", False))
