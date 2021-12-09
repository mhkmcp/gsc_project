document.addEventListener("DOMContentLoaded", (e) => {
	let sc = document.createElement("script");

	sc.setAttribute(
		"src",
		"https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js"
	);
	document.head.append(sc);

	sc.onload = () => {
		// tinymce.init({
		// 	selector: "#",
		// });

		tinymce.init({
			selector: "#id_content",
			height: 500,
			menubar: false,
			plugins: [
				"advlist autolink lists link image charmap print preview anchor",
				"searchreplace visualblocks code fullscreen",
				"insertdatetime media table paste code help wordcount",
			],
			toolbar:
				"undo redo | formatselect | " +
				"bold italic backcolor | alignleft aligncenter " +
				"alignright alignjustify | bullist numlist outdent indent | " +
				"removeformat | help",
			content_style:
				"body { font-family:Helvetica,Arial,sans-serif; font-size:14px }",
		});
	};
});
