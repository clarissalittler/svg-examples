window.onload = function () {
    var xmlns = "http://www.w3.org/2000/svg";
    var canvas = document.getElementById("canvas");
    canvas.addEventListener("click", function (e) {
	var xpos = e.clientX;
	var ypos = e.clientY;
	var newCirc = document.createElementNS(xmlns, "circle");
	newCirc.setAttributeNS(null,"cx",xpos);
	newCirc.setAttributeNS(null,"cy",ypos);
	newCirc.setAttributeNS(null,"r",Math.floor(Math.random() * 100));
	canvas.appendChild(newCirc);
    });
}
