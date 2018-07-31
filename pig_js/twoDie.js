/*
GAME RULES:

- The game has 2 players, playing in rounds
- In each turn, a player rolls a dice as many times as he whishes. Each result get added to his ROUND score
- BUT, if the player rolls a 1, all his ROUND score gets lost. After that, it's the next player's turn
- The player can choose to 'Hold', which means that his ROUND score gets added to his GLBAL score. After that, it's the next player's turn
- The first player to reach 100 points on GLOBAL score wins the game

*/
var scores, roundScore, activePlayer, dice, gamePlaying, winningScore;

document.querySelector('.btn-new').addEventListener('click', initGame);

initGame();


//document.querySelector('.dice').style.display = 'none';

//anonymous function
//roll button functionality
document.querySelector('.btn-roll').addEventListener('click', function () {
    if (gamePlaying) {
        //generate number
        var dice = Math.floor(Math.random() * 6) + 1;

        var diceDOM = document.querySelector('.dice');
        diceDOM.style.display = 'block';
        diceDOM.src = 'dice-' + dice + '.png';

        if (dice == 6 && lastRoll == 6) {
            scores[activePlayer] = 0;
            document.querySelector('#score-' + activePlayer).textContent = scores[activePlayer];
            endTurn();
        } else if (dice == 1) {
            endTurn();
        } else {
            lastRoll = dice
            roundScore += dice;
            document.querySelector('#current-' + activePlayer).textContent = roundScore;
            };
    };

});

//hold button functionality
document.querySelector('.btn-hold').addEventListener('click', function() {
    if (gamePlaying) {
        //add round score to player's global score
        scores[activePlayer] += roundScore;

        //update display value
        document.querySelector('#score-' + activePlayer).textContent = scores[activePlayer];

        //check if player won
        if (scores[activePlayer] >= winningScore) {
            document.querySelector('#name-' + activePlayer).textContent = 'Winner!';
            document.querySelector('.player-' + activePlayer + '-panel').classList.add('winner');
            document.querySelector('.player-' + activePlayer + '-panel').classList.remove('active');
            gamePlaying = false;
        } else {
            endTurn();
        };
        document.querySelector('.dice').style.display = 'none';
    };
});

//submit winning score functionality
document.querySelector('.winning-score-submit').addEventListener('click', function () {
        console.log('clicked on submit');
        var input = document.querySelector('.winning-score').value;
        console.log('input: ', input, typeof input);
        if (input == parseInt(input, 10)) {
            document.querySelector('.winning-score').style.backgroundColor = '#778899';
            winningScore = parseInt(input, 10);
            document.querySelector('.winning-score-warning').style.visibility = 'hidden';
            document.querySelector('.winning-score-submit').style.visibility = 'hidden';
            document.querySelector('.winning-score').readOnly = 'true';
            document.querySelector('.btn-hold').style.visibility = 'visible'
            document.querySelector('.btn-roll').style.visibility = 'visible'
        } else {
            console.log('Input else actions');
            document.querySelector('.winning-score-warning').textContent = 'You must enter a round number.';
            document.querySelector('.winning-score-warning').style.visibility = 'visible';
        };
    });


function initGame() {
    scores = [0,0];
    roundScore = 0;
    activePlayer = 0;
    gamePlaying = true;

    document.querySelector('.dice').style.display = 'none';
    document.querySelector('.winning-score').readOnly = false;
    document.querySelector('.winning-score').value = "";
    document.querySelector('.winning-score').style.backgroundColor = 'white';
    document.querySelector('.winning-score-submit').style.visibility = 'visible';
    document.querySelector('.btn-hold').style.visibility = 'hidden'
    document.querySelector('.btn-roll').style.visibility = 'hidden'

    document.getElementById('score-0').textContent = '0';
    document.getElementById('score-1').textContent = '0';
    document.getElementById('current-0').textContent = '0';
    document.getElementById('current-1').textContent = '0';
    document.getElementById('name-0').textContent = 'Player 1';
    document.getElementById('name-1').textContent = 'Player 2';
    document.querySelector('.player-0-panel').classList.remove('winner');
    document.querySelector('.player-1-panel').classList.remove('winner');
    document.querySelector('.player-0-panel').classList.remove('active');
    document.querySelector('.player-1-panel').classList.remove('active');

    document.querySelector('.player-0-panel').classList.add('active');
};




function endTurn() {
        roundScore = 0;
        lastRoll = 0;
        document.querySelector('#current-' + activePlayer).textContent = roundScore;

        activePlayer === 0 ? activePlayer = 1 : activePlayer = 0;

        document.querySelector('.player-0-panel').classList.toggle('active');
        document.querySelector('.player-1-panel').classList.toggle('active');
};
