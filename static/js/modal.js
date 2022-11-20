// モーダルを表示させる

const addChannelBtn = document.getElementById("add-channel-btn");
const addChannelModal = document.getElementById("add-channel-modal");
const addPageButtonClose = document.getElementById("add-page-close-btn");

const deleteChannelModal = document.getElementById("delete-channel-modal");
const deletePageButtonClose = document.getElementById("delete-page-close-btn");

const logoutBtn = document.getElementById("logout-btn");
const logoutModal = document.getElementById("logout-modal");
const logoutPageButtonClose = document.getElementById("logout-page-close-btn");

// モーダルを開く
// <button id="add-channel-btn">新規チャンネル作成</button>ボタンがクリックされた時
addChannelBtn.addEventListener("click", () => {
  modalOpen("add");
});
logoutBtn.addEventListener("click", () => {
  modalOpen("logout");
});

function modalOpen(mode) {
  if (mode === "add") {
    addChannelModal.style.display = "block";
  } else if (mode === "delete") {
    deleteChannelModal.style.display = "block";
  } else if (mode === "logout") {
    logoutModal.style.display = "block";
  }
}

// モーダル内のキャンセルがクリックされた時
addPageButtonClose.addEventListener("click", () => {
  modalClose("add");
});
deletePageButtonClose.addEventListener("click", () => {
  modalClose("delete");
});
logoutPageButtonClose.addEventListener("click", () => {
  modalClose("logout");
});

function modalClose(mode) {
  if (mode === "add") {
    addChannelModal.style.display = "none";
  } else if (mode === "delete") {
    deleteChannelModal.style.display = "none";
  } else if (mode === "logout") {
    logoutModal.style.display = "none";
  }
}

// モーダルコンテンツ以外がクリックされた時
addEventListener("click", outsideClose);
function outsideClose(e) {
  if (e.target == addChannelModal) {
    addChannelModal.style.display = "none";
  } else if (e.target == deleteChannelModal) {
    deleteChannelModal.style.display = "none";
  } else if (e.target == logoutModal) {
    logoutModal.style.display = "none";
  }
}
