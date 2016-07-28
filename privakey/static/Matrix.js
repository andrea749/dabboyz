function MatrixAnimation ()
{
var c = document.getElementById("c");
var ctx = c.getContext("2d");

//making the canvas full screen
c.height = window.innerHeight;
c.width = window.innerWidth;

//binary code//
var binary = ["01010000","01010010", "01001001", "01010110", "01000001","01001011", "01000101","01011001"];

var font_size = 20;
var columns = c.width/font_size; //number of columns for the rain
//an array of drops - one per column
var drops = [];
//x below is the x coordinate
//1 = y co-ordinate of the drop(same for every drop initially)
for(var x = 0; x < columns; x++)
	drops[x] = 1;

//drawing the characters
function draw()
{
	//Black BG for the canvas
	//translucent BG to show trail
	ctx.fillStyle = "rgba(0, 0, 0, 0.02)";
	ctx.fillRect(0, 0, c.width, c.height);
	ctx.font = font_size + "px monospace";
	//looping over drops
	for(var i = 0; i < drops.length; i++)
	{
		//a binary code to print
		var text = binary[Math.floor(Math.random()*binary.length)];

		if (text == "01010000" || text == "01010010" ){
			ctx.fillStyle = "#0000FF"
		}

		else if (text == "01001001" || text == "01000001" ){
			ctx.fillStyle = "#FF0000"
		}
		else {
			ctx.fillStyle = "#00FF00"
		}

		//x = i*font_size, y = value of drops[i]*font_size
		ctx.fillText(text, i*font_size, drops[i]*font_size);

		//sending the drop back to the top randomly after it has crossed the screen
		//adding a randomness to the reset to make the drops scattered on the Y axis
		if(drops[i]*font_size > c.height && Math.random() > 0.989)
			drops[i] = 0;

		//incrementing Y coordinate
		drops[i]++;
	}
}

setInterval(draw, 33);
}


$(function(){
		$("button").hover(function(){
				$(this).css("text-shadow", "0 0 20px #ff0000, 0 0 20px #0F0, 0 0 20px #0000ff, 0 0 20px #0F0, 0 0 20px #0F0, 0 0 20px #0F0, 0 0 20px");
			}, function(){
				$(this).css("text-shadow", "0 0 20px #0000ff, 0 0 20px #0000ff, 0 0 20px #0000ff, 0 0 20px #0000ff, 0 0 20px #0000ff, 0 0 20px #0F0, 0 0 20px");
		});
	});
