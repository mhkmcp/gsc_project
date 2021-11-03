const checkbox = document.getElementById("id_is_agreed");
const submitBtn = document.getElementById("submitBtn");

const toggleDisble = () => {
	if (!checkbox.checked === true) {
		submitBtn.setAttribute("disabled", "true");
	} else {
		submitBtn.removeAttribute("disabled", "false");
	}
};
toggleDisble();

checkbox.addEventListener("change", () => toggleDisble());
