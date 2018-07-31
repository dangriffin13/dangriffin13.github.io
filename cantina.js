
var click_ctr = 0

document.addEventListener('click', function(event){
		click_ctr++;
		menu_tools()
	})

var menu_tools = function(){

	// document.addEventListener('click', function(event){
	// 	var elements = document.getElementsByClassName('Dish');
	// 	console.log("elements:", elements);
	// 	console.log("style:", elements[0].style);
		
	// 	for (var i = 0; i < elements.length; i++){
	// 		elements[i].style.visibility = 'hidden';
	// 	}
	// });

	// document.addEventListener('click', function(event){
	// 	var cantwin = new Audio('cantwin.mp3');
	// 	cantwin.play();
	// });
	
	// if (click_ctr === 1){
	// 	var cantwin = new Audio('cantwin.mp3');
	// 	cantwin.play();
	// };

	if (click_ctr === 1){
		var music = new Audio('cantinaslice.mp3');
		music.play();
	};

	// if (click_ctr === 2){
	// 	var 
	// }

}

// menu_tools()


