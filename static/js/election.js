const addCandidateBtn = document.getElementById("addCandidateBtn");
const candidateFormset = document.getElementById("candidateFormset");

const emptyForm = document.getElementById("emptyForm");

// const totalNewForms = document.getElementById("id_form-TOTAL_FORMS");
console.log("totalFormSetCount", totalFormSetCount);
addCandidateBtn.addEventListener("click", () => {
	// console.log("totalNewForms", totalNewForms);
	console.log("clicked");
	const currentCandidateForm =
		document.getElementsByClassName("candidate-form");
	let currentCandidateFormCount = currentCandidateForm.length;
	const copyEmptyFormEl = emptyForm.cloneNode(true);
	copyEmptyFormEl.setAttribute("class", "candidate-form");
	// copyEmptyFormEl.setAttribute(
	// 	"id",
	// 	`id_candidate_set-${currentCandidateFormCount}-user`
	// );
	const regex = new RegExp("__prefix__", "g");
	copyEmptyFormEl.innerHTML = copyEmptyFormEl.innerHTML.replace(
		regex,
		currentCandidateFormCount
	);
	candidateFormset.append(copyEmptyFormEl);
});
