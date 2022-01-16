const addCandidateBtn = document.getElementById("addCandidateBtn");
const removeCandidateBtn = document.getElementById("removeCandidateBtn");
const candidateFormset = document.getElementById("candidateFormset");
const totalNewForms = document.getElementById("id_candidate_set-TOTAL_FORMS");
const emptyForm = document.getElementById("emptyForm");

console.log("emptyForm", emptyForm);
console.log("totalNewForms", totalNewForms);

// add new field
addCandidateBtn.addEventListener("click", () => {
	const currentCandidateForm =
		document.getElementsByClassName("candidate-form");
	let currentCandidateFormCount = currentCandidateForm.length;
	const copyEmptyFormEl = emptyForm.cloneNode(true);
	copyEmptyFormEl.setAttribute("class", "candidate-form");
	// copyEmptyFormEl.setAttribute(
	// 	"id",
	// 	`formset-candidate-${currentCandidateFormCount}`
	// );
	const regex = new RegExp("__prefix__", "g");
	copyEmptyFormEl.innerHTML = copyEmptyFormEl.innerHTML.replace(
		regex,
		currentCandidateFormCount
	);
	totalNewForms.setAttribute("value", currentCandidateFormCount + 1);
	candidateFormset.append(copyEmptyFormEl);

	// make newly added field required
	const selectField = document.getElementById(
		`id_candidate_set-${currentCandidateFormCount}-user`
	);
	selectField.setAttribute("required", "true");
});

// remove last added field
removeCandidateBtn.addEventListener("click", () => {
	document
		.querySelectorAll(".candidate-form:last-child")
		.forEach((e) => e.remove());
	totalNewForms.setAttribute("value", currentCandidateFormCount + 1);
});
