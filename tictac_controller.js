
var grid = [
		["upperleft", "uppercenter", "upperright"],
		["centerleft", "centercenter", "centerright"],
		["lowerleft", "lowercenter", "lowerright"]
		]

var player = "O"
var turnCount = 0

function checkWin(){

	console.log("checking for win");

	listsOfThree = [
	[grid[0][0], grid[0][1], grid[0][2]],
	[grid[1][0], grid[1][1], grid[1][2]],
	[grid[2][0], grid[2][1], grid[2][2]],

	[grid[0][0], grid[1][0], grid[2][0]],
	[grid[0][1], grid[1][1], grid[2][1]],
	[grid[0][2], grid[1][2], grid[2][2]],

	[grid[0][0], grid[1][1], grid[2][2]],
	[grid[2][0], grid[1][1], grid[0][2]]
	]

	for (var i = 0; i < listsOfThree.length; i++){
		console.log("checking list "+i);
		if (listsOfThree[i][0] === listsOfThree[i][1] && listsOfThree[i][1] === listsOfThree[i][2]){
			console.log("found a winner")
			return true
		}
	}
}


function gridUpdate(gridLocation){

	for (var i = 0; i < grid.length; i++){
		for (var j = 0; j < grid[i].length; j++){
			if (gridLocation === grid[i][j]){
				grid[i][j] = player;
			}
		}
	}
}

function endGame(player){
	console.log("player received by endGame", player);
	console.log("player = O", player === "O")
	if (player === "X" || player === "O") {
		alert("Player "+player+" wins!");
	} else {
		alert("This game ends in a draw.  Click OK to play again.")
	}
	
	$(".col-md-4").empty();
	turnCount = 0;

	grid = [
		["upperleft", "uppercenter", "upperright"],
		["centerleft", "centercenter", "centerright"],
		["lowerleft", "lowercenter", "lowerright"]
		]
}

function tictacController(){
	$(".col-md-4").on('click',function(event){
		console.log("contents after click", $(this).text())
		console.log(event.target.id);

		// check if the square has already been used
		if ($(this).text() === ("X" || "O")){
			alert("That square has already been played.  Click on a blank square.");
		} else {
			gridUpdate(event.target.id);
			$(this).html("<p>"+player+"</p>");
			turnCount = turnCount + 1;
			console.log("contents after insertion of player name",$(this).text());
		
			//check for win or draw (board is full)
			if (checkWin() === true) {
				console.log("player passed to endGame", player)
				endGame(player);
			} else if (turnCount === 9) {
				player = "Draw";
				endGame(player);
			}

			// switch the player for the next turn
			if (player === "O") {
				player = "X";
			} else {
				player = "O";
			}
		}
	})
}



$(document).ready( function (){
	console.log("document ready");

	tictacController()
});