// "use strict";

// $(function () {
// 	$(".toggle-menu").click(function () {
// 		$(".exo-menu").toggleClass("display");
// 	});
// });

// toggle mobile menu
const mobileMenu = document.getElementById("mobileMenu");
const showBtn = document.getElementById("showMenu");
const hideBtn = document.getElementById("hideMenu");

function showMenu() {
	showBtn.classList.add("d-none");
	mobileMenu.classList.remove("d-none");
}

function hideMenu() {
	showBtn.classList.remove("d-none");
	mobileMenu.classList.add("d-none");
}

// toggle dropdown
const dropBtns = document.querySelectorAll(".dropdown");
console.log("dropBtns", dropBtns);

// close all opened menus
function closeOpenItems() {
	openMenus = document.querySelectorAll(".drop-menu");
	openMenus.forEach(function (menus) {
		console.log(menus);
		menus.style.display = "none";
		const angleDown = menus.parentNode.querySelector(".angleDown");
		angleDown.classList.add("d-none");
		const angleRight = menus.parentNode.querySelector(".angleRight");
		angleRight.classList.remove("d-none");
	});
}

dropBtns.forEach(function (btn) {
	btn.addEventListener("click", function (e) {
		console.log("clicked");
		const dropContent = btn.querySelector(".drop-menu");
		console.log("dropContent1", dropContent);
		const display = dropContent.style.display;
		console.log("display", display);
		e.preventDefault();

		// First close all open items.
		closeOpenItems();
		// Check if the clicked item should be opened.
		if (display == "none") {
			// Open the clicked item.
			dropContent.style.display = "block";
			console.log("btn", btn);
			btn.querySelector(".angleRight").classList.add("d-none");
			btn.querySelector(".angleDown").classList.remove("d-none");
		}
		e.stopPropagation();
	});
});

// event listeners
showBtn.addEventListener("click", showMenu);
hideBtn.addEventListener("click", hideMenu);
