document.addEventListener("DOMContentLoaded", (e) => {
	let sc = document.createElement("script");

	sc.setAttribute(
		"src",
		"https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js"
	);
	document.head.append(sc);

	sc.onload = () => {
		// tinymce.init({
		// 	selector: "#id_content",
		// 	height: 500,
		// 	menubar: false,
		// 	plugins: [
		// 		"advlist autolink lists link image charmap print preview anchor",
		// 		"searchreplace visualblocks code fullscreen",
		// 		"insertdatetime media table paste code help wordcount",
		// 	],
		// 	toolbar:
		// 		"undo redo | formatselect | " +
		// 		"bold italic backcolor | alignleft aligncenter " +
		// 		"alignright alignjustify | bullist numlist outdent indent | " +
		// 		"removeformat | help",
		// 	content_style:
		// 		"body { font-family:Helvetica,Arial,sans-serif; font-size:14px }",
		// });

		tinymce.init({
			selector: "#id_content",
			plugins:
				"print preview powerpaste casechange importcss tinydrive searchreplace autolink autosave save directionality advcode visualblocks visualchars fullscreen image link media mediaembed template codesample table charmap hr pagebreak nonbreaking anchor toc insertdatetime advlist lists checklist wordcount tinymcespellchecker a11ychecker imagetools textpattern noneditable help formatpainter permanentpen pageembed charmap tinycomments mentions quickbars linkchecker emoticons advtable export",
			tinydrive_token_provider: "URL_TO_YOUR_TOKEN_PROVIDER",
			tinydrive_dropbox_app_key: "YOUR_DROPBOX_APP_KEY",
			tinydrive_google_drive_key: "YOUR_GOOGLE_DRIVE_KEY",
			tinydrive_google_drive_client_id: "YOUR_GOOGLE_DRIVE_CLIENT_ID",
			mobile: {
				plugins:
					"print preview powerpaste casechange importcss tinydrive searchreplace autolink autosave save directionality advcode visualblocks visualchars fullscreen image link media mediaembed template codesample table charmap hr pagebreak nonbreaking anchor toc insertdatetime advlist lists checklist wordcount tinymcespellchecker a11ychecker textpattern noneditable help formatpainter pageembed charmap mentions quickbars linkchecker emoticons advtable",
			},
			menu: {
				tc: {
					title: "Comments",
					items: "addcomment showcomments deleteallconversations",
				},
			},
			menubar: "file edit view insert format tools table tc help",
			toolbar:
				"undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | a11ycheck ltr rtl | showcomments addcomment",
			autosave_ask_before_unload: true,
			autosave_interval: "30s",
			autosave_prefix: "{path}{query}-{id}-",
			autosave_restore_when_empty: false,
			autosave_retention: "2m",
			image_advtab: true,
			importcss_append: true,
			template_cdate_format:
				"[Date Created (CDATE): %m/%d/%Y : %H:%M:%S]",
			template_mdate_format:
				"[Date Modified (MDATE): %m/%d/%Y : %H:%M:%S]",
			height: 500,
			image_caption: true,
			quickbars_selection_toolbar:
				"bold italic | quicklink h2 h3 blockquote quickimage quicktable",
			noneditable_noneditable_class: "mceNonEditable",
			toolbar_mode: "sliding",
			spellchecker_ignore_list: ["Ephox", "Moxiecode"],
			tinycomments_mode: "embedded",
			content_style: ".mymention{ color: gray; }",
			contextmenu: "link image imagetools table configurepermanentpen",
			a11y_advanced_options: true,
		});
	};
});
