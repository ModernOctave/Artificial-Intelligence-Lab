/*
* @file botTemplate.cpp
* @author Arun Tejasvi Chaganty <arunchaganty@gmail.com>
* @date 2010-02-04
* Template for users to create their own bots
*/

#include "Othello.h"
#include "OthelloBoard.h"
#include "OthelloPlayer.h"
#include <cstdlib>
using namespace std;
using namespace Desdemona;



class MyBot: public OthelloPlayer
{
    public:
        /**
         * Initialisation routines here
         * This could do anything from open up a cache of "best moves" to
         * spawning a background processing thread. 
         */

        

        MyBot( Turn turn );

        /**
         * Play something 
         */
        virtual Move play( const OthelloBoard& board );
        virtual int minimax( const OthelloBoard& board, int depth, bool maximizingPlayer);
    private:
};


MyBot::MyBot( Turn turn )
    : OthelloPlayer( turn )
{
}

int MyBot::minimax( const OthelloBoard& board, int depth, bool maximizingPlayer )
{
        if ( depth == 0 )
        {
                switch( turn )
                {
                    case BLACK:
                        return board.getBlackCount() - board.getRedCount();
                    case RED:
                        return board.getRedCount() - board.getBlackCount();
                }
        }

        if ( maximizingPlayer )
        {
            int maxEval = -1000000;
            list<Move> moves = board.getValidMoves( turn );
            for ( list<Move>::iterator it = moves.begin(); it != moves.end(); it++ )
            {
                OthelloBoard newBoard = board;
                newBoard.makeMove( turn, *it );
                maxEval = max( maxEval, minimax( newBoard, depth - 1, false ) );
            }
            return maxEval;
        }
        else
        {
            int minEval = 1000000;
            list<Move> moves = board.getValidMoves(turn);
            for (list<Move>::iterator it = moves.begin(); it != moves.end(); it++ )
            {
                OthelloBoard newBoard = board;
                newBoard.makeMove( turn, *it );
                minEval = min(minEval, minimax( newBoard, depth - 1, true));
            }
            return minEval;
        }
    };

Move MyBot::play( const OthelloBoard& board )
{
//    board.print();
//
//    int minimax( const OthelloBoard& board, int depth, bool maximizingPlayer );
//
//    // Default function below
//    list<Move> moves = board.getValidMoves( turn );
//    int randNo = rand() % moves.size();
//    list<Move>::iterator it = moves.begin();
//    // for(int i=0; i < randNo; it++, i++);
//    return *it;
    board.print();
    list<Move> moves = board.getValidMoves( turn );
    int maxEval = -1000000;
    Move& bestMove = moves.front();
    for (list<Move>::iterator it = moves.begin(); it != moves.end(); it++ )
    {
        OthelloBoard newBoard = board;
        newBoard.makeMove( turn, *it );
        int eval = minimax( newBoard, 4, false );
        if ( eval > maxEval )
        {
            maxEval = eval;
            bestMove = *it;
        }
    }
    return bestMove;
}

// The following lines are _very_ important to create a bot module for Desdemona

extern "C" {
    OthelloPlayer* createBot( Turn turn )
    {
        return new MyBot( turn );
    }

    void destroyBot( OthelloPlayer* bot )
    {
        delete bot;
    }
}


