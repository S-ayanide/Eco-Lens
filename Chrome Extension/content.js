var images = document.getElementsByTagName('img');
var prices = document.getElementsByClassName('hl-item__displayPrice secondary-text');
var products = document.getElementsByClassName('hl-carousel__item hl-standard-carousel__item');

if (products.length == 0) {
    products = document.getElementsByClassName('s-item__price');
    if (products.length == 0) {
      products = document.getElementsByClassName('u-flL w29 vi-price');
    }
}

var color = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "ten"];

var userData
function getUserData(){
	const Url = "http://127.0.0.1:8000/userData/";
  const Sdata = '{"user_email":"david"}';
	$.post(Url, Sdata, function(data){
    userData = data
  })
};
getUserData();

//console.log('images', images[0].src)
for (var i = 0, l = products.length; i < l; i++) {
    var r = Math.floor(Math.random()*100)
    var c = Math.round(r/10)
	//products[i].insertAdjacentHTML("beforeend", '<button id="myecoBtn" onclick="myFunction"><img src="https://thumbs.dreamstime.com/b/eco-friendly-percent-green-sticker-wavy-edge-design-element-packaging-design-promotional-material-eco-friendly-170367361.jpg" alt="eco_friendly" height="100" width="100"></img></button');
	var button = document.createElement("button");
	button.innerHTML = ` <span class=${color[c]}>${r}</span>`;
    button.id ='ecoscore'; 
	var product= products[i];
	product.appendChild(button);

	button.addEventListener("click", function(event){
		modal.style.display = "block";
	});

}

var countries = ["China", "USA", "Canada", "Spain", "France", "Italy", "Switzerland"]
var r = Math.abs(Math.random()*7)
document.getElementById('mainContent').insertAdjacentHTML("beforebegin", `<div id="myModal" class="ecomodal"><div class="ecomodal-content"><span class="close">&times;</span><h2>Product footprint:</h2><p>Origin: China</p><p>Distance to you: 3500km</p><p>Emitted CO2: 0.4t CO2 </p><p> Cruelty-Free: YES<br> </p></div></div>`);

// Get the modal
var modal = document.getElementById("myModal");


// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];


// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

function postUserBuy(){
	const Url = "http://127.0.0.1:8000/user_buy/";
  const data = '{"user_email":"david","user_country":"USA", "product_name":"product","product_rate":50,"product_price":"10","product_country":"USA","product_dimensions":"3x3x3","product_weight":"48lbs","product_material":"aluminium"}';
	$.post(Url, data, function(data, status){
		console.log("post", data);
	})
}

var button = document.getElementById("isCartBtn_btn");
if(button != null){
button.addEventListener("click", function(){
    postUserBuy();
});
}

window.onclick = function(event) {
    if ($(event.target.closest('a')).attr('class') == 'hl-item__link') {
        var product_url = $(event.target.closest('a')).attr('href')
        console.log("url", product_url)
        // const Url = "http://127.0.0.1:8000/productData/";
        // const data = {"url":"test"};
        // $.post(Url, data, function(data, status){
        //   alert("data",data)
        // })
    }
}