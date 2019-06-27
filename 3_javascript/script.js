var imgs = document.getElementsByClassName("GalleryImg");

var close = document.getElementById("close");
var popup = document.getElementById("popup");
var popup_img = document.getElementById("popup_img");

var current_index;


function open(img) {
	popup_img.src = img;
	popup.style.display = 'block';	
}

for (var i=0;i<imgs.length;i++) {
	imgs[i].index = i;
	imgs[i].onclick = function() {
		open(this.src);
		current_index = this.index;
	};
}

close.onclick = function() {
	popup.style.display = 'none';
}
