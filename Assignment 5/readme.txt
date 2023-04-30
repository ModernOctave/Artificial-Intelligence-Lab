Compiling:
    First compile the Desdemona framework; to do this navigate to the folder Desdemona/ then run the following command,

    make

    Then compile all the bots present by running the following command from the same folder,

    make bots

Running:
    To run a match between two bots run the following command from the Desdemona/ folder,

    ./bin/Desdemona <bot1 executable path> <bot2 executable path>

    For example to run Minimax bot against AlphaBeta bot run the following command,

    ./bin/Desdemona ./bots/MinimaxBot/bot.so  ./bots/AlphaBetaBot/bot.so

    Note that bot1 is Black and the bot2 is Red