// マイページアップデート
const updateMyPageBtn = document.getElementById("update-mypage-btn");
const updateMyPageModal = document.getElementById("update-mypage-modal");
const updateMyPageButtonClose = document.getElementById("update-mypage-close-btn");

// モーダルを開く
function modalOpen(mode) {
  if (mode === "update") {
    if (uid !== channel.uid) {
      return;
    } else {
      updateMyPagelModal.style.display = "block";
    } 
}


updateMyPageBtn.addEventListener("click", () => {
  modalOpen("update-mypage");
});



// モーダルを閉じる
function modalClose(mode) {
  if (mode === "update-mypage") {
    updateMyPageModal.style.display = "none";
  }
}

updateMyPageButtonClose.addEventListener("click", () => {
  modalClose("update-mypage");
}

// モーダルコンテンツ以外がクリックされた時
addEventListener("click", (e) => {
  if (e.target == updateMyPageModal) {
    updateMyPageModal.style.display = "none";
});
}
