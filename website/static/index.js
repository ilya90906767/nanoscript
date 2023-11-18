function deleteNote(uploadId) {
  fetch("/delete-upload", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}
